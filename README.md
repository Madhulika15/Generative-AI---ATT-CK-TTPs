# Generative-AI---ATT-CK-TTPs

project/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── setup.py
├── data/
│   ├── enterprise-attack-v16.1-relationships.xlsx
│   ├── enterprise-attack-v16.1-tactics.xlsx
│   └── enterprise-attack-v16.1-techniques.xlsx
├── src/
│   ├── __init__.py
│   ├── data_processing.py      # Loading and cleaning data (e.g., merging Excel files)
│   ├── extraction.py           # Functions to extract TTPs and IOCs, fuzzy matching, semantic search
│   ├── visualization.py        # Functions for creating visual graphs (NetworkX/Plotly)
│   └── web_app.py              # Gradio interface and deployment code
├── examples/
│   └── sample_report.txt       # Sample threat report for testing extraction functions
└── docs/
    └── usage.md                # Additional documentation, usage instructions, and guides

# ATT&CK TTP & IOC Extractor

This project extracts TTPs and IOCs from threat reports using rule‑based and machine‑learning techniques. Features include:
- Data processing from MITRE ATT&CK Excel files
- Extraction of TTPs and IOCs with fuzzy matching and semantic search
- A user-friendly Gradio web app interface
- Visualization of relationships using NetworkX/Plotly

## Installation

Install the required packages using:

pip install -r requirements.txt

# Usage

Run the web app:

python src/web_app.py


Process reports in bulk:

from src.extraction import bulk_analyze
results = bulk_analyze("path/to/reports", mapping_df)
