from crewai import Task
from agents.analysis_agent import analysis_agent

analysis_task = Task(
    description="Run compliance analysis on document chunks.",
    expected_output="List of rule-check results for each chunk.",
    agent=analysis_agent
)
