# Financial Report Analyzer Agent

An agentic AI system that automates financial analysis of annual report PDFs. 
It extracts key financial metrics, identifies risks, and generates a structured 
PDF analysis report — reducing manual analysis time from hours to seconds.

## What it does
- Smartly scans annual report PDFs to locate financial sections
- Extracts key metrics: Revenue, Net Profit, EPS, Margins, CAGR
- Analyzes risks and business highlights using Claude AI
- Generates a formatted PDF report

## Tech Stack
Python, Anthropic Claude API, pdfplumber, FPDF2, pandas, python-dotenv

## How to run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Anthropic API key to `.env`
4. Run: `python main.py`

## Sample Output
Tested on Infosys FY2025 Annual Report (Form 20-F)
- Revenue: $19,277 million | Net Profit: $3,162 million
- 4-Year Revenue CAGR: 9.2% | Gross Margin: 30.5%