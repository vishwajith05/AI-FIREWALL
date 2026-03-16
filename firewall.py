import json
from datetime import datetime


# Load attack patterns from JSON
def load_patterns():
    with open("data/attack_patterns.json", "r") as file:
        return json.load(file)


# Log attack attempts
def log_attack(prompt, attack_type, ip):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{timestamp} | {ip} | {attack_type} | {prompt}\n"

    with open("logs/attacks.log", "a") as file:
        file.write(log_entry)


# Detect malicious prompts
def detect_attack(prompt, ip):

    patterns = load_patterns()
    prompt_lower = prompt.lower()

    for attack_type in patterns:
        for keyword in patterns[attack_type]:

            if keyword in prompt_lower:
                log_attack(prompt, attack_type, ip)
                return True, attack_type

    return False, None


# Remove malicious phrases
def sanitize_prompt(prompt):

    patterns = load_patterns()
    clean_prompt = prompt.lower()

    for attack_type in patterns:
        for keyword in patterns[attack_type]:
            clean_prompt = clean_prompt.replace(keyword, "")

    return clean_prompt.strip()