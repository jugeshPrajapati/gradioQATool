# Web Content Q&A Tool

This project is a web-based tool that allows you to ingest text content from one or more URLs and then ask questions based solely on that ingested content. The tool uses Selenium and BeautifulSoup to scrape webpage content and a pre-trained NLP model from Hugging Face's Transformers to answer questions. The user interface is built with Gradio, providing a two-step process:

1. **Ingest URLs:** Submit URLs to scrape and store their content.
2. **Ask a Question:** Use the stored content as context to answer your question.

## Prerequisites

- Python 3.8 (or compatible)
- Anaconda (recommended)
- Chrome browser (for Selenium scraping)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (if not using `webdriver-manager`)

## Setup Instructions

### 1. Clone the Repository

Clone this repository or download the source code:

```bash
git clone <repository_url>
cd <repository_directory>

### 2. Create and Activate the Conda Environment
An environment.yml file is provided to simplify dependency management. Create and activate the environment with:
conda env create -f environment.yml
conda activate webqa

3. Run the Application
The main application file is main.py. Run the project using:
python app.py

This will launch the Gradio interface in your web browser where you can perform the following steps:
Ingest URLs: Enter one or more URLs (one per line) and click "Ingest URLs".
Ask a Question: Enter your question and click "Get Answer" to see the response based on the ingested content.

Project Structure
main.py: Main Python script containing the Gradio interface and application logic.
environment.yml: Conda environment file with all required dependencies.
README.md: This file with setup and usage instructions.

Usage
Step 1: Ingest URLs

Enter one or more URLs in the textbox.
Click the "Ingest URLs" button.
The application will scrape the content from each URL and store the combined text.
Step 2: Ask a Question

Enter your question in the question textbox.
Click the "Get Answer" button.
The tool will use the stored content as context and display an answer.

Troubleshooting
Selenium Errors:
Ensure that your ChromeDriver is compatible with your Chrome browser version. If you encounter issues, consider using webdriver-manager to manage the ChromeDriver automatically.

Model Backend Errors:
The Transformers pipeline requires either PyTorch or TensorFlow. Verify that one of these is installed (PyTorch is installed by default in this setup).

Dependency Issues:
If you encounter issues with package versions (e.g., typing_extensions), try upgrading the problematic package:
pip install --upgrade typing_extensions
```
