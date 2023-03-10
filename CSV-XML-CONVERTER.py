import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file, xml_file):
    # Open CSV File
    with open(csv_file, 'r') as file:
        # Utiliser DictReader pour lire les données CSV
        reader = csv.DictReader(file)

        # Configure XML 
        root = ET.Element('root')
        for row in reader:
            # Add new entry for every lines of the CSV file
            entry = ET.SubElement(root, 'entry')
            for key, value in row.items():
                # Add element for every column one the CSV lines 
                ET.SubElement(entry, key).text = value

        # Write in XML on the output file
        tree = ET.ElementTree(root)
        tree.write(xml_file)

# Exemple d'utilisation


csv_file = r'C:\Folder_Of_Your_CSV_FILE\export.csv'

xml_file = r'C:\Folder_Of_Your_FUTUR_XML_FILE\example.xml'


csv_to_xml(csv_file, xml_file)
