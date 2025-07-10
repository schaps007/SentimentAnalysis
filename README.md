# Sentiment & Summary Analyzer for News Articles and Blogs

This tool allows you to upload `.pdf` or `.docx` news/blog files, and analyze the **sentiment** (Positive / Negative / Neutral) and generate a **summary** using GroqCloud's LLMs.

---

## Features

- Upload `.pdf` or `.docx` files
- Extracts text using `pdfplumber`, `PyMuPDF`, or `python-docx`
- Sends text to **GroqCloud** LLM 
- Returns both:
  -  Sentiment (Positive / Negative / Neutral)
  -  2–3 sentence summary

## How to Run
- Clone the repository using git clone
- Navigate to the backend folder and download the requirements given in requirements.txt
- Run the backend by typing this command: `uvicorn main:app --reload`
- While the backend is running, run the frontend by double clicking on the **index.html** file
You can now upload any news article and analyse its sentiment!



