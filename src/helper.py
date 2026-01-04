import fitz
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file.
    Args:
        pdf_file: The PDF file.

    Returns:
        The text extracted from the PDF file.
    """
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")  
    for page in doc:
        text += page.get_text()
    return text

def ask_openai(prompt, max_tokens=500):
    """
    Send a prompt to the OpenAI API and return the response.
    Args:
        prompt: The prompt to send to the OpenAI API.
        max_tokens: The maximum number of tokens to return.

    Returns:
        The response from the OpenAI API.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                },
            ],
            temperature=0.5,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error sending prompt to OpenAI: {e}")
        return None

