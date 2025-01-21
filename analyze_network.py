import re
import csv
import pandas as pd

# 1. Lecture et extraction des données du fichier texte
def extract_data(input_file):
    pattern = re.compile(
        r'(?P<timestamp>\d{2}:\d{2}:\d{2}\.\d+)\s+'
        r'IP\s+(?P<src_ip>[\w\.-]+)\s*>\s*(?P<dst_ip>[\w\.-]+):\s*'
        r'.*length\s+(?P<length>\d+)'  # Extrait la longueur du paquet
    )
    extracted_data = []

    with open(input_file, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                extracted_data.append(match.groupdict())
    return extracted_data

# 2. Génération d'un fichier CSV
def generate_csv(data, output_file):
    csv_headers = ["timestamp", "src_ip", "dst_ip", "length"]
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        writer.writerows(data)

# 3. Génération d'un fichier Excel avec un graphique
def generate_excel(data, output_file):
    df = pd.DataFrame(data)
    df['length'] = df['length'].astype(int)  # Convertir 'length' en entier

    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Data', index=False)
        workbook = writer.book
        worksheet = writer.sheets['Data']

        # Ajouter un graphique
        chart = workbook.add_chart({'type': 'column'})
        chart.add_series({
            'name': 'Packet Length',
            'categories': ['Data', 1, 0, len(df), 0],  # Utiliser les timestamps comme catégories
            'values': ['Data', 1, 3, len(df), 3],  # Utiliser les longueurs comme valeurs
        })
        chart.set_title({'name': 'Distribution of Packet Lengths'})
        chart.set_x_axis({'name': 'Timestamp'})
        chart.set_y_axis({'name': 'Length'})
        worksheet.insert_chart('F2', chart)

# 4. Génération d'un rapport Markdown
def generate_markdown_report(data, output_file):
    df = pd.DataFrame(data)
    most_common_src_ip = df['src_ip'].value_counts().idxmax()
    most_common_dst_ip = df['dst_ip'].value_counts().idxmax()
    average_packet_length = df['length'].astype(int).mean()

    report_content = f"""
# Network Analysis Report

## Summary
- *Total Packets Analyzed:* {len(df)}
- *Most Frequent Source IP:* {most_common_src_ip}
- *Most Frequent Destination IP:* {most_common_dst_ip}
- *Average Packet Length:* {average_packet_length:.2f} bytes

## Data Insights
This report provides insights into the network traffic and highlights the most active IPs and average packet sizes.
"""
    with open(output_file, 'w') as file:
        file.write(report_content)

# 5. Fonction principale
def main():
    input_file = "logs.txt"  # Le fichier contenant les logs Wireshark
    csv_output_file = "analyzed_traffic.csv"
    excel_output_file = "analyzed_traffic.xlsx"
    markdown_output_file = "network_analysis_report.md"

    # Extraction des données
    data = extract_data(input_file)

    # Vérifier si des données ont été extraites
    if not data:
        print("Aucune donnée valide n'a été trouvée dans le fichier.")
        return

    # Génération des fichiers
    generate_csv(data, csv_output_file)
    generate_excel(data, excel_output_file)
    generate_markdown_report(data, markdown_output_file)

    print(f"Fichiers générés :\n- {csv_output_file}\n- {excel_output_file}\n- {markdown_output_file}")

if _name_ == '_main_'
    main()