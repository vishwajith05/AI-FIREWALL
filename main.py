from fastapi import FastAPI
from pydantic import BaseModel
from firewall import detect_attack

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.post("/chat")
def chat(request: PromptRequest):

    prompt = request.prompt

    attack_detected, attack_type = detect_attack(prompt)

    if attack_detected:
        return {
            "status": "blocked",
            "reason": attack_type,
            "message": "Prompt blocked by AI Firewall"
        }

    # If no attack detected
    return {
        "status": "allowed",
        "message": "Prompt is safe",
        "prompt": prompt
    }