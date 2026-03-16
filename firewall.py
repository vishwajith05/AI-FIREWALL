import json
from datetime import datetime

# Load attack patterns
def load_patterns():
    with open("data/attack_patterns.json", "r") as file:
        patterns = json.load(file)
    return patterns


# Log attack attempts
def log_attack(prompt, attack_type):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{timestamp} | {attack_type} | {prompt}\n"

    with open("logs/attacks.log", "a") as log_file:
        log_file.write(log_entry)


# Detect attacks
def detect_attack(prompt):

    patterns = load_patterns()
    prompt_lower = prompt.lower()

    for attack_type in patterns:
        for keyword in patterns[attack_type]:

            if keyword in prompt_lower:
                log_attack(prompt, attack_type)
                return True, attack_type

    return False, None