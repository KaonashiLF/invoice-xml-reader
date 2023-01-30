# Testing code in internet

import xml.etree.ElementTree as ET
tree = ET.parse('I:\Documentos\Programacao\Repos\GitHub\invoice-xml-reader\country_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)