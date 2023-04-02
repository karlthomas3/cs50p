from fpdf import FPDF


def main():
    name = input("Name:")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_font('helvetica', '', 40)
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_margin(0)
    pdf.add_page()
    pdf.cell(200, 70, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.oversized_images = "DOWNSCALE"
    pdf.image("shirtificate.png")
    pdf.set_page_background(None)
    pdf.set_font('helvetica', '', 25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200, -250, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align='C')

    
    


    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
