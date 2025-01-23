from utils import call_gemini

input_query = input("Enter query to ask gemini...")
response = call_gemini(input_query)
print("Response from Gemini: ", response)
