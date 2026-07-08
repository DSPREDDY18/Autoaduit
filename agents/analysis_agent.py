# agents/analysis_agent.py
from tools.rule_checker import RuleCheckerTool

def analysis_agent_process(classified_data: dict):
    text = classified_data["text"]
    checker = RuleCheckerTool()
    issues = checker.run(text)
    return {"text": text, "issues": issues, "type": classified_data["type"]}
