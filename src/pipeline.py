from src.tools.yt_transcript import get_transcript_from_url
from src.tools.chunks import chunk_text, create_vectorstore
from src.tools.get_model import get_gemini, get_huggingface
from src.tools.retriver import get_retriever, retrive_docs, pre_process_docs
from src.prompt import prompt

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda


def final_pipeline(url, question):

    transcript = get_transcript_from_url(url)

    chunks = chunk_text(transcript)

    embedding_model = get_huggingface()
   
    retriever=get_retriever(chunks, embedding_model)



    model = get_gemini()

    parser = StrOutputParser()

    chain = (
        {
            "context": retriever | RunnableLambda(pre_process_docs),
            "question": RunnablePassthrough()
        }
        | prompt
        | model
        | parser
    )

    return chain.invoke(question)