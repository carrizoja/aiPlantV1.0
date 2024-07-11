from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
 #set the OpenAI API key from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


#Get the botanical response

def get_botanical_response(prompt):
    try:
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200)
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

