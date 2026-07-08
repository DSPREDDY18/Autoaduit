# agents/classify_agent.py

def classify_agent_process(text: str):
    # Placeholder classification logic
    if len(text) < 100:
        return {"type": "short", "text": text}
    else:
        return {"type": "long", "text": text}
