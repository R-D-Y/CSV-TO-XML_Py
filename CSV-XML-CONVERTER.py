import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file, xml_file):
    # Ouvrir le fichier CSV
    with open(csv_file, 'r') as file:
        # Utiliser DictReader pour lire les données CSV
        reader = csv.DictReader(file)

        # Configurer l'arbre XML
        root = ET.Element('root')
        for row in reader:
            # Ajouter une nouvelle entrée pour chaque ligne du fichier CSV
            entry = ET.SubElement(root, 'entry')
            for key, value in row.items():
                # Ajouter un élément pour chaque colonne dans la ligne CSV
                ET.SubElement(entry, key).text = value

        # Écrire l'arbre XML dans un fichier
        tree = ET.ElementTree(root)
        tree.write(xml_file)

# Exemple d'utilisation


csv_file = r'C:\Folder_Of_Your_CSV_FILE\export.csv'

xml_file = r'C:\Folder_Of_Your_FUTUR_XML_FILE\example.xml'


csv_to_xml(csv_file, xml_file)
