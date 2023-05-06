from pptx import Presentation
from pptx.util import Inches

# Create a new PowerPoint presentation
prs = Presentation()

def add_slide(prs, layout, title, subtitle):
    slide = prs.slides.add_slide(layout)
    slide.shapes.title.text = title
    slide.placeholders[1].text =subtitle
    return slide



title_slide_layout = prs.slide_layouts[1]

slide = add_slide(prs, title_slide_layout, "Yooooo", "IF you smelllllllllllllllllllllllllllll")
slide2 = add_slide(prs, title_slide_layout, "Meow","What the rock is cooking ")
slide3 = add_slide(prs, title_slide_layout, "Meow1"," Then offfffffffffffffff")

# Save the presentation
prs.save("PPT.pptx")
