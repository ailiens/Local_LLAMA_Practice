import streamlit as st
from langchain.llms import CTransformers
import time

llm = CTransformers(
    model = 'llama-2-7b-chat.ggmlv3.q3_K_L.bin',
    model_type = 'llama'
)

st.title('Local LLama')

content = st.text_input('Send a message')

if st.button('button'):
    with st.spinner('wait'):
        result = llm.predict('explain about' + content + ": ")
        st.write(result)


# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
#
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1, text=progress_text)