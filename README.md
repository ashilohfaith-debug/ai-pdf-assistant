# AI PDF Companion
A lightweight AI-powered web application built with Python and Streamlit that enables users to interact with PDF documents through natural language conversations.

The application extracts text from uploaded PDFs and uses Google Gemini 2.5 Flash to provide context-aware answers, summaries, explanations, and semantic analysis based on document content.

<br/>

Live demo: https://ai-pdf-assistant-8hymgebtssqcbtr46bxqtw.streamlit.app/

*Built to gain hands-on experience with APIs, PDF processing, prompt engineering, and deploying web applications, after learning Python Programming in my second semester at college.*

<br/>

https://github.com/user-attachments/assets/02ce20a6-2566-41ec-acaf-1dd0d82d9925

## Tech Stack

- **Language:** Python v3.14.2
- **Application Framework:** [Streamlit](https://streamlit.io/) v1.57.0
- **LLM API:** [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
- **PDF Processing:** [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/) 

---

## Local Installation

### Prerequisites
- Ensure you have Python 3.10 or higher installed on your local machine 
- Obtain a valid Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ashilohfaith-debug/ai-pdf-assistant.git
cd ai-pdf-assistant
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run ai_website.py
```

### Additional Information
Check the available Gemini models for your API by using the code from 'test_models.py' file.

---

## Future Improvements
- Multi-PDF support
- Chat memory
- OCR support for scanned PDFs
- Citation-based responses

---

## License
This project is open-source and available under the MIT License.
