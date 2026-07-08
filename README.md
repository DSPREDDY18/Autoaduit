# AutoAudit Pro

An AI-powered document auditing pipeline built with [CrewAI](https://github.com/crewAIInc/crewAI) and Google Gemini. AutoAudit Pro automatically ingests documents, classifies them, runs compliance checks, verifies findings, and generates structured audit reports.

## Architecture

The pipeline uses a **sequential multi-agent** architecture with five specialized stages:

```
Document → Intake → Classify → Analyze → Verify → Report
```

| Stage | Agent | Description |
|---|---|---|
| **Intake** | `intake_agent` | Loads and reads the document from the filesystem |
| **Classify** | `classify_agent` | Categorizes the document by type (short/long) |
| **Analyze** | `analysis_agent` | Runs rule-based compliance checks for sensitive content |
| **Verify** | `verification_agent` | Validates analysis results and flags discrepancies |
| **Report** | `report_agent` | Generates a structured final audit report |

## Project Structure

```
Autoaudit_pro/
├── main.py                        # CLI entry point
├── crew.py                        # Pipeline orchestration
├── gemini_llm.py                  # Gemini LLM configuration
├── agents/
│   ├── intake_agent.py            # Document ingestion agent
│   ├── classify_agent.py          # Document classification agent
│   ├── analysis_agent.py          # Compliance analysis agent
│   ├── verification_agent.py      # Result verification agent
│   └── report_agent.py            # Report generation agent
├── tasks/
│   ├── intake_task.py             # CrewAI task definition for intake
│   ├── classify_task.py           # CrewAI task definition for classification
│   ├── analysis_task.py           # CrewAI task definition for analysis
│   ├── verification_task.py       # CrewAI task definition for verification
│   └── report_task.py             # CrewAI task definition for reporting
├── tools/
│   ├── document_loader.py         # File reading utility
│   └── rule_checker.py            # Compliance rule engine
├── requirements.txt
├── .env.example
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.10+
- A [Google Gemini API key](https://aistudio.google.com/apikey)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DSPREDDY18/Autoaduit.git
   cd Autoaduit
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

### Usage

```bash
# Audit a specific document
python main.py path/to/document.txt

# Run with the default test document
python main.py
```

### Example Output

```
--- AutoAudit Report ---

Document Type: short
Verified: False
Issues Found:
- Contains confidential info
- Contains password
```

## Compliance Rules

The current rule engine (`tools/rule_checker.py`) checks for:

| Rule | Trigger |
|---|---|
| Confidential information | Text contains "confidential" |
| Password exposure | Text contains "password" |

> **Extending rules:** Add new keyword checks or integrate regex patterns in `RuleCheckerTool.run()`.

## Configuration

| Environment Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-rule`)
3. Commit your changes (`git commit -m "Add new compliance rule"`)
4. Push to the branch (`git push origin feature/new-rule`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
