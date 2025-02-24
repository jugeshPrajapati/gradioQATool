from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import gradio as gr
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from transformers import pipeline
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Initialize the QA model from Hugging Face
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def scrape_text(url):
    # Set up headless Chrome using Selenium
    options = Options()
    options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        html = driver.page_source
    finally:
        driver.quit()
    # Use BeautifulSoup to extract and clean text content
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    return text

def answer_question(urls, question):
    combined_text = ""
    # Process each URL (assume one URL per line)
    for url in urls.splitlines():
        url = url.strip()
        if url:
            combined_text += scrape_text(url) + " "
    # Use the combined text as context for the QA model
    result = qa_pipeline(question=question, context=combined_text)
    return result.get("answer", "No answer found.")

# Build the Gradio interface
iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(lines=5, placeholder="Enter one URL per line...", label="URLs"),
        gr.Textbox(lines=2, placeholder="Type your question here...", label="Question")
    ],
    outputs="text",
    title="Web Content Q&A Tool",
    description="Enter one or more URLs and ask a question. The answer is generated strictly from the ingested webpage content."
)

if __name__ == "__main__":
    iface.launch()

print("All libraries imported successfully!")

