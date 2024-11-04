from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
	# print(row["Topic"])
	pdf.add_page()
	pdf.set_font('Times', 'B', 24)
	pdf.set_text_color(255,0,0)
	pdf.cell(w=0, h=12, text = f'{row["Topic"]}', align = "L",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
	pdf.line(10, 23, 200, 23)
	for _ in range(row["Pages"] - 1):
		pdf.add_page()

pdf.output("output.pdf")
# pdf.

