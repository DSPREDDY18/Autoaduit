from crewai import Task
from agents.classify_agent import classify_agent

classify_task = Task(
    description="Classify document chunks by type or category.",
    expected_output="List of chunk categories.",
    agent=classify_agent
)
