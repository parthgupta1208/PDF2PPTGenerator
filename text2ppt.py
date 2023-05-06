from pptx import Presentation
from pptx.util import Inches

# Create a new PowerPoint presentation
prs = Presentation()

# Add a new slide with a title and subtitle

slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
subtitle = slide.placeholders[1]

# Add text to the slide
title.text = "MEOW "
subtitle.text = '''YKEHTE HAI MEOW MEOW MEOW . 
MEOW MEOW MEOW MEOWMEOQ WO
mWOQ EHEHVRJFJHGHF '''

# Save the presentation
prs.save("meow.pptx")
