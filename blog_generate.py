# %%
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# %%
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

# %%
llm = GoogleGenerativeAI(model = 'gemini-pro', google_api_key= google_api_key)

# %%
#llm.invoke("Hi")

# %%
template = ''''Generate a deatialed blog on this topic: {topic}'''

prompt = PromptTemplate.from_template(template)
chain = prompt | llm | StrOutputParser()

def generate_blog(text):
    response = chain.invoke({'topic':text})

    return response


# %%
#generate_blog("CNN")


