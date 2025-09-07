# main.py - THE MONEY MAKER

import io
import tiktoken
from pypdf import PdfReader
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# --- CONFIGURATION ---
# This is the price for gpt-4-turbo-preview input tokens.
# Always check the latest OpenAI pricing page. This is just an example.
PRICE_PER_MILLION_TOKENS_USD = 10.00
# --- END CONFIGURATION ---

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class TextPayload(BaseModel):
    text_to_tokenize: str

def process_text_and_tokenize(text: str):
    """
    This is the heart of our service. It does three things:
    1. Counts tokens.
    2. Decodes tokens.
    3. Calculates the cost.
    """
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
        token_ids = encoding.encode(text)
        token_count = len(token_ids)
        
        # The new, critical part: calculate the cost.
        cost = (token_count / 1_000_000) * PRICE_PER_MILLION_TOKENS_USD
        
        decoded_tokens = [encoding.decode([token_id]) for token_id in token_ids]
        
        return {
            "token_count": token_count,
            "estimated_cost_usd": cost,
            "decoded_tokens": decoded_tokens
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_text")
async def process_text_endpoint(payload: TextPayload):
    text = payload.text_to_tokenize
    return process_text_and_tokenize(text)

@app.post("/process_pdf")
async def process_pdf_endpoint(file: UploadFile = File(...)):
    full_text = ""
    try:
        pdf_bytes = await file.read()
        pdf_stream = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_stream)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n" # Add a newline between pages
        
        return process_text_and_tokenize(full_text)

    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}
    