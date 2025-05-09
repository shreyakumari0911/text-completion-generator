import streamlit as st
from transformers import pipeline, set_seed

st.title("Text Completion Generator")
st.subheader("By Shreya Kumari")


@st.cache_resource
def load_generator():
    generator = pipeline('text-generation', model='gpt2')
    return generator

generator = load_generator()
set_seed(42)


prompt = st.text_input("Enter the beginning of a sentence:")

if prompt:
    with st.spinner("Generating text..."):
        output = generator(prompt, max_length=50, num_return_sequences=1)
        completed = output[0]['generated_text']
    st.markdown("### Completed Sentence:")
    st.success(completed)
