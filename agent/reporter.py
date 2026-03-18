from fpdf import FPDF
import os

def clean_text(text):
    """Remove characters that fpdf cannot handle."""
    replacements = {
        "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-", "\u2022": "*", "\u25cf": "*",
        "\u20b9": "Rs.", "\u00a0": " "
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text.encode("latin-1", errors="ignore").decode("latin-1")

def generate_report(analysis_text, company_name="Company"):
    """Generates a formatted PDF report from the analysis."""
    
    pdf = FPDF()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Financial Analysis Report", ln=True, align="C")
    pdf.set_font("Helvetica", "I", 11)
    pdf.cell(0, 8, clean_text(company_name), ln=True, align="C")
    pdf.ln(6)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(8)

    # Content
    for line in analysis_text.split("\n"):
        line = clean_text(line.strip())
        if not line:
            pdf.ln(2)
            continue
        if line.startswith("#") or line.endswith(":"):
            pdf.set_font("Helvetica", "B", 12)
        else:
            pdf.set_font("Helvetica", "", 10)
        try:
            pdf.multi_cell(0, 7, line)
        except Exception:
            # Skip any line that still causes issues
            continue

    # Save
    os.makedirs("reports", exist_ok=True)
    output_path = f"reports/{company_name.replace(' ', '_')}_analysis.pdf"
    pdf.output(output_path)
    return output_path