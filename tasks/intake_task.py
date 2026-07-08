from crewai import Task
from agents.intake_agent import intake_agent

intake_task = Task(
    description="Load and split documents into chunks.",
    expected_output="List of text chunks.",
    agent=intake_agent
)
