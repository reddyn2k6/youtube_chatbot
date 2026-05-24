from src.tools.chunks import create_vectorstore,chunk_text
from src.tools.yt_transcript import get_transcript_from_url
from src.tools.get_model import get_huggingface


def get_retriever(chunks, embedding_model):
    vectorstore = create_vectorstore(chunks, embedding_model)
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k":4}
    )

def retrive_docs(retriever, question):
    return retriever.invoke(question)

def pre_process_docs(docs):
    text = "\n\n".join(doc.page_content for doc in docs)
    return text