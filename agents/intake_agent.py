# agents/intake_agent.py
from tools.document_loader import DocumentLoaderTool

def intake_agent_process(filepath: str):
    loader = DocumentLoaderTool()
    return loader.run(filepath)
