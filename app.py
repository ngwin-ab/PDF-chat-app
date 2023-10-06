import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Sidebar contents
with st.sidebar:
    st.title('PDF Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')

    add_vertical_space(5)
    st.write(
        'Tutorial by [Prompt Engineer](https://youtube.com/@engineerprompt)')


def main():
    st.header("Chat with any PDF 💬")

    # upload a PDF file
    new_pdf = st.file_uploader("Upload your PDF:", type = 'pdf')

    if new_pdf is not None:
        pdf_reader = PdfReader(new_pdf)

        input_text = ""

        for page in pdf_reader.pages: 
            input_text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        
        chunks = text_splitter.split_text(text=input_text)

        st.write(chunks)




if __name__ == '__main__':
    main()