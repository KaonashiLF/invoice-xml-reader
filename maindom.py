import xml.etree.ElementTree as ET
from xmlreader import xmlfile




xmlfile = r"I:\\Documentos\\Programacao\\Repos\\GitHub\\invoice-xml-reader\\xmlfile.xml"

tree = ET.parse(xmlfile)
root = tree.getroot()

for child in root.findall('nfeProc'):
    second_node = child.find('NFe')
    third_node = second_node.find('infNFe')
    
    total_node = third_node.find('total')
    icms_values = total_node.find('ICMSTot')
    
    total_product_price = icms_values.find('vNF').text
    print(total_product_price)