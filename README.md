# PDF2PPT Generator

PDF2PPT Generator is a Python tool that converts PDF files to PowerPoint presentations. For each page of the PDF, it uses Spacy's sentence rank algorithm to summarize the page and generates bullet points and a topic name using the GPT-3.5-turbo model. It then extracts related images using the Google Image Search API and creates slides in the PowerPoint presentation. The resulting PowerPoint presentation contains two slides for each page of the PDF: one containing the topic name and bullet points, and the other containing a related image.

# Demo Video

https://user-images.githubusercontent.com/114602309/236706605-ef1720c7-7f11-4cef-825e-b5f44b84a1fd.mp4

## Requirements

To use PDF2PPT Generator, you will need the following:

- Python 3.6 or later
- Spacy
- GPT-3.5-turbo
- Google Cloud SDK
- Google Image Search API
- Python Imaging Library (PIL)
- Tkinter
- OBVIOUSLY, a PDF to test !

## Installation

1. Clone the repository:

   - git clone https://github.com/parthgupta1208/PDF2PPTGenerator.git
   - cd PDF2PPTGenerator

2. Install the required dependencies:

   - pip install spacy
   - pip install gpt-3.5-turbo
   - pip install google_images_search
   - pip install pillow
   - pip install openai
   - pip install PyPDF2
   - pip install python-pptx
   - pip install tkinter


3. Set up your Google Cloud project and obtain your API credentials for the Google Image Search API and the Google Cloud Vision API. Add your credentials to the `.env` file. Similarly obtain a OpenAI API Secret Key and append in `.env` file.

4. Run the GUI by executing the following command:

   - `python gui.py`

## Usage

1. Launch the GUI by running the `gui.py` script.

2. Select the PDF file that you want to convert to a PowerPoint presentation by pressing the button.

3. Wait for the process to complete till you get a `Job Completed` Alert.

4. Choose the file location where you want to save the generated file and provide a filename.

## License

PDF2PPT Generator is licensed under the MIT License. See the `LICENSE` file for more information.

## Credits

PDF2PPT Generator was created by Parth Gupta, Abhijeet Shankar and Sounak Chakraborty. It uses Spacy, GPT-3.5-turbo, Google Cloud SDK, Google Image Search API, PPTX API, Tkinter, PyPDF2 Library and Python Imaging Library (PIL).

## Additional Notes

For the free OpenAI key, the program is limited to the first 3 pages, however changing the same is possible by modifying the `pdf2final_list.py` file.
