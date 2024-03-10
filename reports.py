#!/usr/bin/env python3

import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

pdfdata=upload_descriptions(listtextfiles)
def pdfdata_func(pdfdata):
    for i in pdfdata:
        for j in i:
            print(j)
    print('\n')


##### This function generates report in pdf format########
def generate(filename, title, data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
#  report_info = Paragraph(additional_info, styles["BodyText"])
#  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
#report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1,20)
#    report.build([report_title, empty_line,  report_table])
def pdfdata_func(pdfdata):
    for i in pdfdata:
        for j in i:
            print(j)
    print('\n')
data=pdfdata_func(pdfdata)
x=datetime.date.today()
reports.generate("processed.pdf", f'Processed Update on {x.strftime("%b %d, %Y")}',data)
