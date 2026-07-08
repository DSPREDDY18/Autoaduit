# tools/document_loader.py
class DocumentLoaderTool:
    def run(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error loading file: {e}"
