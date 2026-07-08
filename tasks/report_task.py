from crewai import Task
from agents.report_agent import report_agent

report_task = Task(
    description="Generate a final audit report from verified chunks.",
    expected_output="Final audit report document.",
    agent=report_agent
)
