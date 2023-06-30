import requests
import PyPDF2

# Prompt the user to enter their OpenAI API key
api_key = input("Please enter your OpenAI API key: ")

# Prompt the user to enter the PDF file path
pdf_file = input("Please enter the path to your PDF file: ")

# Read the PDF file
pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, "rb"))
num_pages = pdf_reader.numPages

# Extract text from each page
text = ""
for page_num in range(num_pages):
    page = pdf_reader.getPage(page_num)
    text += page.extractText()

# Remove unwanted characters
text = text.replace("\n", " ")

# OpenAI API endpoint
endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

# OpenAI API parameters
parameters = {
    "prompt": text,
    "max_tokens": 200,
    "temperature": 0.7
}

# Make an API call to OpenAI API
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(endpoint, json=parameters, headers=headers)
response.raise_for_status()

# Get the completed text from the API response
completed_text = response.json()["choices"][0]["text"]

# Print the completed text
print(completed_text)

