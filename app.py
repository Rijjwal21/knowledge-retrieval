import streamlit as st
from gemini import extract_text, answer_query, summarize

st.set_page_config(page_title="Knowledge Retrieval")

st.header(":blue[Knowledge Retrieval]")
st.markdown("##### Welcome! Upload a PDF to make it act as a knowledge base and ask any questions from it!")

user_file = st.file_uploader("Upload your document (PDF only)", type="pdf")

# With Gemini
if user_file:
    file_text = extract_text(user_file)

    if st.button("Summarize"):
        result = summarize(file_text)
        st.write(result)
    
    
    user_input = st.chat_input("Enter your question:")
        
    if user_input:
        st.markdown("#### Query:")
        st.write(user_input)

        result = answer_query(user_input, file_text)
        st.markdown("#### Answer:")
        st.write(result)