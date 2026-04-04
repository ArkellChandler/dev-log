from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# Configura a chave da API a partir da variável de ambiente
genai.configure(api_key=os.getenv("AIzaSyBgLA8RUK9d6nR8eY-DTi3GwYG-OIRHpIc"))

@app.post("/chat")
async def chat(prompt: str):
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
