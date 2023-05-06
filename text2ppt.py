from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
#Create a new PowerPoint presentation
prs = Presentation()

def add_slide(prs, layout, title, subtitle):
    slide = prs.slides.add_slide(layout)
    slide.shapes.title.text = title
    slide.placeholders[1].text =subtitle
    font = slide.shapes.title.text_frame.paragraphs[0].font
    font.name = 'Arial'
    font.size = Pt(36)
    font.bold = True
    font.italic = False
    font1= slide.placeholders[1].text_frame.paragraphs[0].font
    font1.name = 'Arial'
    font1.size = Pt(24)
    font1.bold = False
    font1.italic = False
    return slide



capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
m=list(capital_city.keys())
n=list(capital_city.values())
#print(m[1])


#Choose the layout as desired

title_slide_layout = prs.slide_layouts[1]

for i in range (0,len(m)):     
    slide = add_slide(prs, title_slide_layout, m[i],n[i] )


# Save the presentation
prs.save("PPT.pptx")

