from fpdf import FPDF
from PIL import Image
from datetime import datetime

DATE, TIME = datetime.now().strftime("%d/%m/%Y, %H:%M:%S").split(', ')

WIDTH = 210
HEIGHT = 297

img = Image.new('RGB', (WIDTH, HEIGHT),'#fcf9e6')
img.save('bg.png')

def create_title(day, pdf):
	pdf.set_font('Arial', '', 24)
	pdf.write(100, f'{DATE} {TIME}')


def create_report(filename='report.pdf'):
	pdf = FPDF()
	pdf.add_page()
	pdf.image('bg.png',x=0, y=0, w=WIDTH, h=HEIGHT)
	pdf.image('EA.jpg', 10, 8, 33)



	pdf.output(filename)

create_report()

