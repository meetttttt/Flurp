import os
import streamlit as st

from config import GEMINI_MODEL_NAME
from utils import call_gemini, extract_text

st.title("Con Call Summarizer")

uploaded_file = st.file_uploader("Upload Con call in PDF format", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing PDF..."):
        save_path = os.path.join("docs", uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Get the text extracted from the PDF
        text = extract_text(file_path=f"docs/{uploaded_file.name}",
                            save_to_txt=False)

        final_query = f"""
        Think like a Financial Analyst. You will provided with the Earning's Concall Transcipt.
        You have to deep dive in the transcript and collect the most important pieces and summarize it.
        Your summary should be extensive and cover all the aspects. And always provide output in Markdown format. 
    
        Note: Look out when management is trying to sugar coat any issue or is trying to cover up. 
        Do not fall for those traps. Stay neutral in those cases and do point it out.
    
        Earning's Concall Transcript:
        {text} 
        """
        # Get response from Gemini
        response = call_gemini(query=final_query, model=GEMINI_MODEL_NAME)

        st.markdown(response)
