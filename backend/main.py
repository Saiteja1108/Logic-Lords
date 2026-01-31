from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from groq import Groq
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env [cite: 152]
load_dotenv()
app = FastAPI()

# Enable CORS for frontend communication to avoid browser blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client with API key from .env [cite: 157-159]
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class CodeReviewRequest(BaseModel):
    code: str
    language: str
    focus_areas: list

@app.get("/", response_class=HTMLResponse)
async def serve_login():
    """Serves the initial login page at the root URL """
    try:
        # Matches your project structure: backend and frontend are siblings [cite: 94-106]
        with open("../frontend/login.html", "r", encoding='utf-8') as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>login.html not found. Check project structure.</h1>")

@app.get("/app", response_class=HTMLResponse)
async def serve_tool():
    """Serve the tool page after login [cite: 198-201, 252]"""
    try:
        with open("../frontend/index.html", "r", encoding='utf-8') as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>index.html not found. Check project structure.</h1>")

@app.post("/api/review")
async def review_code(request: CodeReviewRequest):
    """Review code using Groq API and Llama 3.3 70B [cite: 206-208]"""
    if not request.code.strip():
        # Validate that the code input is not empty [cite: 210, 216]
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    # Format user-selected focus areas for the prompt [cite: 211, 217]
    focus_str = ", ".join(request.focus_areas)
    
    # Construct the expert persona prompt [cite: 213]
    prompt = (
        f"You are an expert code reviewer with 15+ years of experience. "
        f"Analyze this {request.language} code focusing on {focus_str}. "
        f"Provide a structured review with these exact sections: "
        f"### Critical Issues, ### High Priority, ### Medium Priority, and ### Low Priority. "
        f"\n\nCode:\n{request.code}"
    )

    # Execute ultra-fast LLM inference via Groq [cite: 8, 73, 154]
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile", # Defined model [cite: 161]
        temperature=0.3, # Generation settings [cite: 162, 166]
        max_tokens=2000, # Generation settings [cite: 163, 166]
        top_p=0.9 # Generation settings [cite: 164, 166]
    )
    
    # Return structured review content for frontend rendering [cite: 218]
    return {"review": response.choices[0].message.content}

if __name__ == "__main__":
    import uvicorn
    # Start server process on localhost port 8000 [cite: 254-259]
    uvicorn.run(app, host="127.0.0.1", port=8000)