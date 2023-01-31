# Invoice reader with Python

import xml.etree.ElementTree as ET
import pandas as pd




xmlfile = r"I:\\Documentos\\Programacao\\Repos\\GitHub\\invoice-xml-reader\\xmlfile.xml"


# This block of is working correctly
with open(xmlfile, mode='r') as file:
    for row in file:
        # print(row)
        if 'vNF' in row:
            row = row.replace(' ', '')
            row = row.replace('\n', '')
            row = row.replace("<vNF>","")
            row = row.replace("</vNF>","")
            row = float(row)


model_dataframe = {
    "Product":[],
    "Price":[],
    "InvoiceNumber":[],
    "TotalTax":[],
    "Date": []
}


df = pd.DataFrame(model_dataframe)

def insert_new_value( product,price, invoicenumber,totaltax, date):
    
    # The idea is this function insert new value into df 
    df.insert(product,price, invoicenumber,totaltax, date)
    print(df)

insert_new_value('product','price', 'invoicenumber','totaltax', 'date')

# Made by: Lucas Francisco
# GitHub: https://github.com/KaonashiLF













# =============================================================================
#                           Not working code yet
# =============================================================================




# This probabily works but I will try it again later
# Problem: I can't iterate child nodes of each tag. Probabily the problem is tag name

tree = ET.parse(xmlfile)
root = tree.getroot()
option = 0
what = None
for child in root:
    tag = child.findall('NFe')
    attrs = child.attrib
    
    
    while option == 1:
        what = str(input('Press "T" for Tag and "A" for attributes:\n'))
        if what.lower() == 't':
            print(f'Tag:\n{child.tag}')
        elif what.lower() == 'a':
            print(f'Attributes: \n{child.attrib}')
        else:
            print('Wrong answer, execute it again.')
            what = None
            option = 0
            
            
