import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_report(text):
    """Sends extracted PDF text to Claude for financial analysis."""
    
    prompt = f"""
You are a financial analyst. Analyze the following annual report text and extract:

1. Company name and fiscal year
2. Key financial metrics:
   - Revenue / Total Income
   - Net Profit / PAT
   - EBITDA (if available)
   - EPS (Earnings Per Share)
   - Debt-to-Equity Ratio
   - Return on Equity (ROE)
3. Year-on-year growth (revenue and profit)
4. Key business highlights (2-3 points)
5. Risks mentioned (2-3 points)
6. Overall financial health summary (3-4 sentences)

Format your response clearly with headers for each section.
If a metric is not found, write "Not available".

Annual Report Text:
{text[:15000]}
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text