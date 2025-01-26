from utils import call_gemini, extract_text
from config import GEMINI_MODEL_NAME

# Get the text extracted from the PDF
text = extract_text(file_path="docs/2369ea6b-467a-434d-8d66-fcf82f3bdfda.pdf",
                    save_to_txt=False)

final_query = f"""
Think like a Financial Analyst. You will provided with the Earning's Concall Transcipt.
You have do deep dive in the transcript and collect the most important pieces and summarize it.
Your summary should be extensive and cover all the aspects. And always provide output in Markdown format. 

Note: Look out when management is trying to sugar coat any issue or is trying to cover up. 
Do not fall for those traps. Stay neutral in those cases and do point it out.

Earning's Concall Transcript:
{text} 
"""
# Get response from Gemini
response = call_gemini(query=final_query, model=GEMINI_MODEL_NAME)
print("Response from Gemini: ", response)
