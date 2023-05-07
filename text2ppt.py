from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
#Create a new PowerPoint presentation

def presentate(defined_list):
    prs = Presentation()

    def add_slide(prs, layout, title, subtitle):
        slide = prs.slides.add_slide(layout)
        slide.shapes.title.text = title
        textbox = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(6), Inches(2))
        # Add text to the text box
        tf = textbox.text_frame
        tf.text = subtitle
        textbox.left = Inches(1)
        textbox.top = Inches(2)
        textbox.width = Inches(10)
        textbox.height = Inches(2)
        font = slide.shapes.title.text_frame.paragraphs[0].font
        font.name = 'Arial'
        font.size = Pt(30)
        font.bold = True
        font.italic = False
        for x in tf.paragraphs:
            font1= x.font
            font1.name = 'Arial'
            font1.size = Pt(16)
            font1.bold = False
            font1.italic = False
        return slide

    title_slide_layout = prs.slide_layouts[5]

    for i in range (0,len(defined_list)):     
        slide = add_slide(prs, title_slide_layout, defined_list[i]["Topic"],"\n".join(defined_list[i]["Summary"]))

    # Save the presentation
    prs.save("PPT.pptx")