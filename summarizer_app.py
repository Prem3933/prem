import streamlit as st
from docx import Document
import PyPDF2
from transformers import pipeline
from googletrans import Translator

# Initialize the summarization pipeline
summarizer = pipeline("summarization")
translator = Translator()

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def summarize_text(text, language="en"):
    summary = summarizer(text[:1000], max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
    if language == "hi":
        return translator.translate(summary, dest="hi").text
    return summary

def main():
    st.title("File Summarizer App")
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])
    language = st.selectbox("Select Summary Language", ["English", "Hindi"])
    
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]
        if file_type == "txt":
            text = uploaded_file.read().decode("utf-8")
        elif file_type == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            text = extract_text_from_docx(uploaded_file)
        
        if st.button("Summarize"):
            summary = summarize_text(text, "hi" if language == "Hindi" else "en")
            st.write("### Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()
