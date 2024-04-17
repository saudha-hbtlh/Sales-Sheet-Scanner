from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from transformers import pipeline
import re

app = Flask(__name__)
CORS(app)

# Initializing sentiment analysis pipeline
sentiment_analysis = pipeline('sentiment-analysis', model='roberta-base')

@app.route('/Hello')
def hello():
    print("Hello route accessed")  # Log message to console
    return "Hi"

@app.route('/index', methods=['GET'])
def serve_html():
    print("HTML page served")  # Log message to console
    return render_template('check.html')

@app.route('/index', methods=['POST'])
def handle_post():
    try:
        # Get the uploaded CSV file
        csv_file = request.files['csv_file']
        print("CSV file received:", csv_file.filename)  # Log filename to console

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Check if the CSV file has the correct columns
        expected_columns = {'Reviews', 'ItemRating', 'ShippingRating'}
        if not set(df.columns).issuperset(expected_columns):
            missing_columns = expected_columns - set(df.columns)
            error_message = f"Incorrect Input Data: Missing columns {missing_columns}. " \
                            f"The CSV file should have columns: Reviews, ItemRating, ShippingRating"
            print("Error:", error_message)  # Log error message to console
            return jsonify(error=error_message), 400

        print("Input data validated successfully")  # Log success message to console

        # Preprocess input data before passing to sentiment analysis
        reviews = preprocess_reviews(df['Reviews'].tolist())

        print("Input data preprocessed")  # Log success message to console

        # Perform sentiment analysis using RoBERTa
        sentiment_scores = sentiment_analysis(reviews)

        print("Sentiment analysis performed")  # Log success message to console

        # Extract the sentiment labels from the sentiment scores and convert to numerical values
        sentiment_labels = [float(score['label'].split('_')[1]) for score in sentiment_scores]

        # Calculate the CSI value
        avg_item_rating = df['ItemRating'].astype(float).mean()  # Convert to float
        avg_shipping_rating = df['ShippingRating'].astype(float).mean()  # Convert to float
        avg_sentiment_score = sum(sentiment_labels) / len(sentiment_labels)

        max_item_rating = 5
        max_shipping_rating = 5
        max_sentiment_score = 1

        satisfaction_scores = {
            'ItemRating': avg_item_rating / max_item_rating,
            'ShippingRating': avg_shipping_rating / max_shipping_rating,
            'roberta_compound': avg_sentiment_score / max_sentiment_score
        }

        importance_scores = {'ItemRating': 0.4, 'ShippingRating': 0.2, 'roberta_compound': 0.4}
        weighted_satisfaction_scores = {attribute: satisfaction_scores[attribute] * importance_scores[attribute]
                                        for attribute in importance_scores}
        CSI = sum(weighted_satisfaction_scores.values()) / sum(importance_scores.values())

        CSI = max(0, min(1, CSI))  # Ensure CSI is within the range [0, 1]

        print("CSI value:", CSI)  # Log the calculated CSI value to console

        return jsonify({'csi': CSI})

    except KeyError:
        print("Error: Missing 'csv_file' in the request")  # Log error message to console
        return jsonify(error="Missing 'csv_file' in the request"), 400

    except pd.errors.ParserError:
        print("Error: Invalid CSV file format")  # Log error message to console
        return jsonify(error="Invalid CSV file format"), 400  # Change the status code to 400 for bad request

    except Exception as e:
        print("An unexpected error occurred:", e)  # Log unexpected error message to console
        return jsonify(error="An unexpected error occurred"), 500


def preprocess_reviews(reviews):
    # Placeholder preprocessing logic
    preprocessed_reviews = []
    for review in reviews:
        if isinstance(review, str):
            # Remove special characters and punctuation
            review = re.sub(r'[^\w\s]', '', review)
            # Convert to lowercase
            review = review.lower()
            # Remove extra whitespace
            review = ' '.join(review.split())
            preprocessed_reviews.append(review)
    return preprocessed_reviews


if __name__ == "__main__":
    app.run(host='127.0.0.3', port=5002, debug=True)
