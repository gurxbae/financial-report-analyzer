import pdfplumber

FINANCIAL_KEYWORDS = [
    "revenue", "net profit", "total income", "ebitda", "earnings per share",
    "eps", "return on equity", "roe", "debt", "equity", "operating profit",
    "cash flow", "balance sheet", "income statement", "financial highlights",
    "profit after tax", "pat", "gross profit", "net income", "total assets",
    "liabilities", "dividend", "results of operations", "dollars in millions",
    "compounded annual", "operating and financial review"
]

ANCHOR_PHRASES = [
    "results of operations",
    "operating and financial review",
    "management's discussion and analysis",
    "financial condition and results"
]

def extract_financial_pages(pdf_path):
    """
    Extracts financial pages by finding the MD&A / Results of Operations
    section, skipping the table of contents area at the start.
    """
    financial_text = ""
    matched_pages = []

    print("      Scanning pages for financial data...")

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"      Total pages in document: {total_pages}")

        # Skip first 15% of doc to avoid table of contents
        skip_pages = int(total_pages * 0.15)
        print(f"      Skipping first {skip_pages} pages (table of contents area)...")

        # Find anchor page
        anchor_page = None
        for i in range(skip_pages, total_pages):
            text = pdf.pages[i].extract_text()
            if not text:
                continue
            text_lower = text.lower()
            for phrase in ANCHOR_PHRASES:
                if phrase in text_lower:
                    anchor_page = i
                    print(f"      Found financial section at page {i+1}")
                    break
            if anchor_page is not None:
                break

        if anchor_page is not None:
            # Extract anchor page + next 18 pages
            for i in range(anchor_page, min(anchor_page + 18, total_pages)):
                text = pdf.pages[i].extract_text()
                if text:
                    financial_text += f"\n--- Page {i+1} ---\n"
                    financial_text += text + "\n"
                    matched_pages.append(i + 1)
        else:
            # Fallback: keyword density scan skipping first 15%
            print("      Anchor not found, using keyword scan...")
            for i in range(skip_pages, total_pages):
                text = pdf.pages[i].extract_text()
                if not text:
                    continue
                matches = [kw for kw in FINANCIAL_KEYWORDS if kw in text.lower()]
                if len(matches) >= 4:
                    financial_text += f"\n--- Page {i+1} ---\n"
                    financial_text += text + "\n"
                    matched_pages.append(i + 1)
                if len(financial_text) > 40000:
                    break

    print(f"      Extracted data from pages: {matched_pages}")
    return financial_text