from langchain_community.llms import Ollama
import streamlit as st
from langchain.llms import HuggingFaceHub
from decouple import config
import os


llm = Ollama(model="llama3")
st.title("Q&A app using Llama 3")

hf_api_key = config('HUGGINGFACEHUB_API_TOKEN')
llm=HuggingFaceHub(repo_id = "meta-llama/Meta-Llama-3-8B")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(llm.invoke(prompt, stop=['<|eot_id|>']))
