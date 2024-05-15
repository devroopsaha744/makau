import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore

def load_data(json_path):
    loader = JSONLoader(json_path)
    return loader.load()

def split_data(docs, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True
    )
    return text_splitter.split_documents(docs)

def create_pinecone_index(texts, index_name, embeddings):
    vectorstore = PineconeVectorStore.from_documents(texts, index_name=index_name, embedding=embeddings)
    return vectorstore

def initialize_embeddings(google_api_key):
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)

def main():
    # Load environment variables
    load_dotenv()
    
    # Get API keys from environment variables
    google_api_key = os.getenv('GOOGLE_API_KEY')
    pinecone_key = os.getenv("PINECONE_API_KEY")
    
    # Initialize Google Generative AI embeddings
    embeddings = initialize_embeddings(google_api_key)
    
    # Load data
    data_dir = r"C:\Users\devro\OneDrive\Desktop\Projects\Chikitsak\data\medical.txt.txt"
    docs = load_data(data_dir)
    
    # Split data
    texts = split_data(docs)
    
    # Create Pinecone index
    index_name = "chikitsak"
    vectorstore = create_pinecone_index(texts, index_name, embeddings)
    
    # Retrieve
    retriever = vectorstore.as_retriever()

if __name__ == "__main__":
    main()


