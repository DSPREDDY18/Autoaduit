# tools/rule_checker.py
class RuleCheckerTool:
    def run(self, text: str):
        # Simple placeholder for compliance rules
        issues = []
        if "confidential" in text.lower():
            issues.append("Contains confidential info")
        if "password" in text.lower():
            issues.append("Contains password")
        return issues
