from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
def get_gemini():
    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)
    return model

def get_huggingface():
    model=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
    return model

