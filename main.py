# main.py
from crew import run_autoaudit
import sys

if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = "test_doc.txt"
    print("No file path provided. Using default 'test_doc.txt'")

output = run_autoaudit(filepath)
print("\n--- AutoAudit Report ---\n")
print(output)
