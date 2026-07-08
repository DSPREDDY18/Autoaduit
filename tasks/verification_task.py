from crewai import Task
from agents.verification_agent import verification_agent

verification_task = Task(
    description="Verify analyzed chunks for accuracy and consistency.",
    expected_output="Verification report with discrepancies.",
    agent=verification_agent
)
