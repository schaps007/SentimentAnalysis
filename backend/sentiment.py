from utils import extract_text
import requests

# Replace with your actual Groq API key
GROQ_API_KEY = "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"

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

async def analyze_sentiment(file):
    extracted_text = extract_text(file)

    if not extracted_text or extracted_text.strip() == "":
        return {"error": "No readable text found in the uploaded document."}

    trimmed_text = extracted_text[:3000]  

   
    prompt = (
        "Analyze the following news article or blog. "
        "First, provide a 2-3 sentence **summary** of the content. "
        "Then clearly state the **sentiment** as one of: Positive, Negative, or Neutral.\n\n"
        + trimmed_text
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=body)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"].strip()

        # Optional: Try to extract both fields from the output
        return {
            "result": content
        }

    except Exception as e:
        return {"error": "Failed to analyze sentiment and summary.", "details": str(e)}
