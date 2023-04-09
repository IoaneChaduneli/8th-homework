from fpdf import FPDF

class shirtificate(FPDF):

    def make_header(self):
        self.add_page()

        self.set_font('Arial', 'B', 12)

        self.cell(0, 30, "This Shirtificate goes to", 0, 0, 'C', 0)

        self.ln(20)


    def make_image(self):
        self.image('shirtificate.png', x=50, y=50, w=100)
        self.set_font('Arial', 'B', 20)
        name = input("Enter Student name:")
        self.cell(0,120, name, 0, 0, 'C', 0)
        self.set_text_color(51,51,255)
        self.ln(15)


pdf = shirtificate('portrait', 'mm', 'A4')

header = pdf.make_header()
image = pdf.make_image()

pdf.output('graduation.pdf')

# pdf = shirtificate("portrait", 'mm', 'A4')

# pdf.add_page()

# pdf.image('shirtificate.png', x=50, y=50, w=100)

# pdf.set_font('Arial', 'B', 20)

# name = input('Enter Student name: ')

# pdf.cell(0, 150, name, 0, 0, 'C', 0 )

# pdf.set_text_color(51,51,255)

# pdf.ln(15)

# pdf.output("pdf-shirtificate.pdf", 'F')