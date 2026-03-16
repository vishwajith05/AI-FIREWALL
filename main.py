from fastapi import FastAPI, Request
from pydantic import BaseModel
from firewall import detect_attack, sanitize_prompt

app = FastAPI()

# Input format
class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "AI Firewall is running"}


@app.post("/chat")
def chat(request: Request, body: PromptRequest):

    prompt = body.prompt
    ip = request.client.host

    attack_detected, attack_type = detect_attack(prompt, ip)

    if attack_detected:
        return {
            "status": "blocked",
            "reason": attack_type,
            "ip": ip,
            "message": "Prompt blocked by AI Firewall"
        }

    # Sanitize prompt
    clean_prompt = sanitize_prompt(prompt)

    return {
        "status": "allowed",
        "prompt": clean_prompt
    }