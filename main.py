from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto = False, margin=0 )
for index, row in df.iterrows():
	pdf.add_page()

	#Set the header
	pdf.set_font('Times', 'B', 24)
	pdf.set_text_color(255,0,0)
	pdf.cell(w=0, h=12, text = row["Topic"], align = "L",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
	pdf.line(10, 23, 200, 23)

	#Set the footer
	pdf.ln(265)
	pdf.set_font('Times', 'I', 8)
	pdf.set_text_color(180,180,180)
	pdf.cell(w=0, h=12, text = row["Topic"], align = "R")


	for _ in range(row["Pages"] - 1):
		pdf.add_page()
		# Set the footer
		pdf.ln(277)
		pdf.set_font('Times', 'I', 8)
		pdf.set_text_color(180, 180, 180)
		pdf.cell(w=0, h=12, text=row["Topic"], align="R")

pdf.output("output.pdf")
# pdf.

