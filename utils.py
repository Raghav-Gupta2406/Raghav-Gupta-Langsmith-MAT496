# utils.py
# This helper file is required by all notebooks to simulate a Retrieval-Augmented Generation (RAG) process.

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def get_vector_db_retriever():
    """
    Creates a simple in-memory vector database retriever for demonstration purposes.
    The dummy documents explain concepts used in this assignment.
    """
    # Documents related to Langsmith features
    docs = [
        Document(page_content="The @traceable decorator is a simple way to log traces. You can add it to any function to automatically track its inputs, outputs, and errors in LangSmith."),
        Document(page_content="LangSmith supports adding metadata to traces. This is done by passing a 'metadata' dictionary to the @traceable decorator. You can also add metadata at runtime using the 'langsmith_extra' parameter."),
        Document(page_content="A run tree is a nested structure of runs. The @traceable decorator handles the creation and management of this tree for you automatically.")
    ]
    
    # Using a standard embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Creating the vector store
    vector_db = FAISS.from_documents(docs, embedding_model)
    
    # Return a retriever that will find the relevant documents
    return vector_db.as_retriever(search_kwargs={"k": 2})

# Common system prompt used across several notebooks
RAG_SYSTEM_PROMPT = """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the latest question in the conversation. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.
"""