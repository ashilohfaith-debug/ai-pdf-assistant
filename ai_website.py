import streamlit as st
import google.generativeai as genai
import PyPDF2

# Set up the web page interface
st.title("Your AI PDF Companion")
st.caption("Upload a PDF and get quick summaries from Gemini")

st.markdown("""
### How to use
1. Enter your Gemini API key in the sidebar  
2. Upload a PDF document (Up to 200 MB supported)
3. Ask questions about the document
""")

st.sidebar.subheader("API Configuration")

api_key = st.sidebar.text_input(
    "Enter your Gemini API Key",
    type="password"
)

# Upload the PDF file
uploaded_file = st.file_uploader(
    "",
    type="pdf"
)

if uploaded_file and api_key:

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Read the PDF content
    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    # Ask a question
    user_question = st.text_input(
        "Ask a question about this document:"
    )

    if user_question:

        # Gemini model
        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        # Prompt with PDF context
        prompt = f"""
        You are a helpful AI assistant.

        Use the following PDF content to answer the question.

        PDF Content:
        {text}

        Question:
        {user_question}
        """

        # Generate response
        with st.spinner("Analyzing document and generating response..."):
            response = model.generate_content(prompt)

        # Display answer
        st.write(response.text)