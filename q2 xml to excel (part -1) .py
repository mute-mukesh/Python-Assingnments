from turtle import pd
import xml.etree.ElementTree as Etree
import pandas as pd

Tree = Etree.parse("C:/Users/mukes/Downloads/LogProcessing/SAMPLEWork/A2DP/tc_log.xml")
root = Tree.getroot()
A= []
for ele in root:
        B = {}
        for i in list(ele):
                B.update({i.tag:  i.text})
                A.append(B)
df = pd.DataFrame(A)
df.drop_duplicates(keep ='first', inplace=True)
df.reset_index(drop=True, inplace=True)
writer = pd.ExcelWriter("C:/Users/mukes/Downloads/Excel/OUTPUT.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
worksheet = writer.sheets['sheet1']
worksheet.set_column('B:Z', 30)
writer.save()
print("XML file converted into Excel file")

