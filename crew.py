# crew.py
from agents.intake_agent import intake_agent_process
from agents.classify_agent import classify_agent_process
from agents.analysis_agent import analysis_agent_process
from agents.verification_agent import verification_agent_process
from agents.report_agent import report_agent_process

def run_autoaudit(filepath: str):
    # Step 1: Load document
    intake_result = intake_agent_process(filepath)
    
    # Step 2: Classify
    classify_result = classify_agent_process(intake_result)
    
    # Step 3: Analysis
    analysis_result = analysis_agent_process(classify_result)
    
    # Step 4: Verification
    verification_result = verification_agent_process(analysis_result)
    
    # Step 5: Report
    report_result = report_agent_process(verification_result)
    
    return report_result
