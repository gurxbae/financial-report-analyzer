import os
import sys
from agent.extractor import extract_financial_pages
from agent.analyzer import analyze_report
from agent.reporter import generate_report

def main():
    print("=" * 50)
    print("   Financial Report Analyzer Agent")
    print("=" * 50)
    
    # Get PDF path from user
    pdf_path = input("\nEnter the path to the annual report PDF: ").strip()
    
    if not os.path.exists(pdf_path):
        print("Error: File not found. Please check the path.")
        sys.exit(1)
    
    company_name = input("Enter the company name: ").strip()
    
    print("\n[1/3] Extracting financial data from PDF...")
    text = extract_financial_pages(pdf_path)
    
    if not text:
        print("Error: Could not extract financial data from PDF.")
        sys.exit(1)
    
    print(f"      Extracted {len(text)} characters of financial data successfully.")
    
    print("\n[2/3] Analyzing report with AI...")
    analysis = analyze_report(text)
    print("      Analysis complete.")
    
    print("\n[3/3] Generating PDF report...")
    report_path = generate_report(analysis, company_name)
    print(f"      Report saved to: {report_path}")
    
    print("\n" + "=" * 50)
    print("   Analysis Complete!")
    print("=" * 50)
    print("\n--- ANALYSIS SUMMARY ---\n")
    print(analysis)

if __name__ == "__main__":
    main()