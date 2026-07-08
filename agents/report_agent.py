# agents/report_agent.py

def report_agent_process(verification_result: dict):
    report = f"Document Type: {verification_result['type']}\n"
    report += f"Verified: {verification_result['verified']}\n"
    if verification_result["issues"]:
        report += "Issues Found:\n"
        for issue in verification_result["issues"]:
            report += f"- {issue}\n"
    else:
        report += "No issues found."
    return report
