# Sentiment Analysis and Text Summarization Tool

This project is a web application built using Flask, a Python web framework, for performing sentiment analysis and text summarization using natural language processing (NLP) techniques. The application allows users to input text, analyze its sentiment, extract main points, and view a summary of the text.

## Installation

To run this project locally, follow these steps:

1/ Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/sentiment-analysis-tool.git
cd sentiment-analysis-tool
```

2/ Run the Flask application:

```bash
python app.py

```
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

## Usage

```python
# Import necessary modules from Flask and Flask Bootstrap
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# Import TextBlob for natural language processing
from textblob import TextBlob, Word
import random
import time
```

1.Visit the application URL.

2.Enter the text you want to analyze in the provided text area.

3.Click the "Submit" button to initiate the analysis.

4.Explore the sentiment analysis results, main points, and other details.


## Contributors

@ELKODH68

## License

[MIT](https://choosealicense.com/licenses/mit/)
