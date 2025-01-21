1. Rédaction de la notice d’utilisation



A. Titre et Introduction

# Usage Guide for Network Traffic Analysis Tool
This tool processes network traffic logs, extracts key information, and generates detailed reports for analysis. It is designed to help identify anomalies in network activity efficiently.

B. Étapes pour exécuter les scripts

## 1. How to Use
### A. Running the Python Script
1. Place the network log file (.txt) in the same directory as the Python script.
2. Run the following command in a terminal:
   bash
   python analyze_network.py

	3.	The script will generate:
	•	A CSV file: analyzed_traffic.csv.
	•	An Excel file: analyzed_traffic.xlsx (includes data and a chart).
	•	A Markdown report: network_analysis_report.md.

#### C. **Analyse des résultats dans Excel**
markdown
### B. Exploring the Excel Report
1. Open the analyzed_traffic.xlsx file in Excel.
2. Go to the "Data" sheet to see raw extracted data.
3. Look at the chart to visualize packet length distribution over time.

D. Prérequis

## 2. Requirements
- Python 3.x installed.
- Required Python libraries: pandas, xlsxwriter, re.
- Excel (or equivalent software) for .xlsx files.

E. Remarques et Contact

## 3. Notes
- Input files must follow the tcpdump log format.
- For customization, modify the script to extract more fields.

## 4. Contact
For issues, visit the project repository on GitHub or contact the developer.