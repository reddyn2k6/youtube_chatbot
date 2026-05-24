from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant for answering questions about a YouTube video.

Use the retrieved context below to answer the user's question.

If the answer is not present in the context, say "I don't know."

Context:
{context}

Question:
{question}
""")