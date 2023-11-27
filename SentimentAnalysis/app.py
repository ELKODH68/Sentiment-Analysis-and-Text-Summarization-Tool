# Import necessary modules from Flask and Flask Bootstrap
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# Import TextBlob for natural language processing
from textblob import TextBlob, Word
import random
import time

# Create a Flask web application
app = Flask(__name__)

# Initialize Bootstrap for the Flask app
Bootstrap(app)

# Define the root route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for analyzing the input text
@app.route('/analyse', methods=['POST'])
def analyse():
    # Record the start time to measure the processing time
    start = time.time()

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the raw text from the form
        rawtext = request.form['rawtext']

        # Perform natural language processing using TextBlob
        blob = TextBlob(rawtext)
        received_text = blob

        # Extract sentiment and subjectivity from the text
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity

        # Count the number of tokens (words) in the text
        number_of_tokens = len(list(blob.words))

        # Extracting main points (nouns) from the text
        nouns = [word.lemmatize() for word, tag in blob.tags if tag == 'NN']
        len_of_words = len(nouns)

        # Randomly select and pluralize some nouns
        rand_words = random.sample(nouns, len(nouns))
        final_word = [Word(item).pluralize() for item in rand_words]

        # The summary is the final set of words obtained
        summary = final_word

        # Calculate the processing time
        end = time.time()
        final_time = end - start

    # Render the template with the results
    return render_template('index.html', received_text=received_text, number_of_tokens=number_of_tokens,
                           blob_sentiment=blob_sentiment, blob_subjectivity=blob_subjectivity,
                           summary=summary, final_time=final_time)

# Run the Flask app if this script is the main module
if __name__ == '__main__':
    app.run(debug=True)
