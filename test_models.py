import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

for model in genai.list_models():
    print(model.name)