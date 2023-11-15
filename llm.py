# tag::llm[]
import streamlit as st
from langchain.chat_models import ChatOpenAI, ChatOllama

llm = ChatOllama(
    model="llama2"
)
# end::llm[]

# tag::embedding[]
from langchain.embeddings import OpenAIEmbeddings, OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="llama2"
)
# end::embedding[]
