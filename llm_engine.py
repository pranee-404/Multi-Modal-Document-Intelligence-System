import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= ""
)

def analyze_document(text, fields):

    prompt = f"""
You are analyzing an OCR extracted document.

OCR TEXT:
{text}

EXTRACTED FIELDS:
{fields}

Return ONLY valid JSON with this structure:

{{
  "document_type": "...",
  "summary": "...",
  "validation": "...",
  "confidence_score": 0.0
}}

Do not include explanations or markdown.
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {"role": "system", "content": "You analyze documents and return structured JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content