import streamlit as st

log_file = "logs/attacks.log"

st.title("AI Firewall Security Dashboard")

attacks = []

try:
    with open(log_file, "r") as file:
        attacks = file.readlines()
except:
    attacks = []

total_attacks = len(attacks)

attack_types = {}

for attack in attacks:
    parts = attack.split("|")
    if len(parts) >= 2:
        attack_type = parts[1].strip()
        attack_types[attack_type] = attack_types.get(attack_type, 0) + 1

st.metric("Total Attack Attempts", total_attacks)

st.subheader("Attack Type Distribution")

for attack_type, count in attack_types.items():
    st.write(f"{attack_type}: {count}")

st.subheader("Recent Attacks")

for attack in attacks[-10:]:
    st.text(attack)