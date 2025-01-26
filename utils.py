import fitz
import google.generativeai as genai

from config import (GEMINI_API_KEY, GEMINI_DEFAULT_MODEL_NAME, GEMINI_TEMPERATURE,
                    GEMINI_OUTPUT_TOKEN, GEMINI_SYSTEM_INSTRUCTION)

genai.configure(api_key=GEMINI_API_KEY)


def call_gemini(query: str, stream: bool = False, model: str = GEMINI_DEFAULT_MODEL_NAME) -> str:
    """
    This function will call gemini based on the query passed and then generate the response and send back.
    :param query: The query to be sent to gemini model.
    :param stream: Stream the response based on the value provided.
    :param model: Gemini Model Name.
    :return: Response generated from the gemini model else empty string.
    """
    try:
        model = genai.GenerativeModel(model, system_instruction=GEMINI_SYSTEM_INSTRUCTION)
        response = model.generate_content(query,
                                          generation_config=genai.GenerationConfig(
                                              max_output_tokens=GEMINI_OUTPUT_TOKEN,
                                              temperature=GEMINI_TEMPERATURE,
                                          ),
                                          stream=stream)
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
