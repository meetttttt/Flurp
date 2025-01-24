import os
import fitz
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def call_gemini(query: str, stream: bool = False, model: str = os.getenv("GEMINI_MODEL_NAME")) -> str:
    """
    This function will call gemini based on the query passed and then generate the response and send back.
    :param query: The query to be sent to gemini model.
    :param stream: Stream the response based on the value provided.
    :param model: Gemini Model Name.
    :return: Response generated from the gemini model else empty string.
    """
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(query, stream=stream)
        return response.text

    except Exception as e:
        print(f"Error has occurred: {e}")
        return ""


def extract_text(file_path: str, save_to_txt: bool = False) -> str:
    """
    This function will extract the text from pdf file and return the back the text.
    :param file_path: Path were pdf file is stored.
    :param save_to_txt: Save the text extracted from pdf to txt file.
    :return: Text extracted from the pdf.
    """
    try:
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
                if save_to_txt:
                    f = open("docs/extracted_text.txt", "a")
                    f.write(text)
            return text
    except Exception as e:
        print(f"Error has occurred: {e}")
        return ""
