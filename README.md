# Flurp

## Overview
Flurp is an AI-powered bot designed for summarizing conference calls using Gemini. It allows users to upload a PDF file containing meeting transcripts, extracts text from it, does the summarization using the pre defined prompts and then displays the summarized output in a structured Markdown format.

## Features
- Upload a single PDF file
- Save the uploaded file locally
- Extract text from the PDF
- Summraize the text and display the output
- Uses Streamlit for an interactive UI

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/flurp.git
   cd flurp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the Streamlit web interface.
2. Upload a PDF containing the meeting transcript.
3. The summarized text will be displayed in Markdown format.

## Technologies Used
- **Python**
- **Streamlit**
- **pdfplumber** (for text extraction)
- **Gemini AI** (for summarization)

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

