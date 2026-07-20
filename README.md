A Flask-based web application that analyzes Etsy product reviews to calculate a Customer Satisfaction Index (CSI) using sentiment analysis (RoBERTa) and weighted scoring.

https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/Flask-2.0+-green.svg
https://img.shields.io/badge/RoBERTa-NLP-red.svg
https://img.shields.io/badge/License-MIT-yellow.svg

📋 Table of Contents
Overview

How to Use

How It Works

Screenshots

Tech Stack

Installation

Project Structure

Dependencies

Contributing

License

🎯 Overview
Sales Sheet Scanner is an intelligent web application designed to help sellers, buyers, and platform owners make data-driven decisions about product viability. By analyzing customer reviews and rating data from Etsy listings, the application computes a Customer Satisfaction Index (CSI) that indicates whether a product is worth selling.

The application leverages:

Advanced Natural Language Processing (RoBERTa) for sentiment analysis

Weighted scoring algorithms for balanced evaluation

Interactive Flask web interface for seamless user experience

🚀 How to Use
1. Prepare Your CSV File
Ensure your CSV file contains the following columns exactly as named:

Column Name	Description	Example
Reviews	Customer review text	"This product is amazing!"
ItemRating	Product rating (1-5 scale)	4.5
ShippingRating	Shipping experience rating (1-5 scale)	4.0
Note: The file must be in CSV format with these exact column headers.

2. Upload and Analyze
Launch the application locally

Navigate to http://127.0.0.3:5002/

📸 Upload Interface
Select and upload your CSV file for analysis

https://Artifacts/Screenshots/sales.png

Click "Choose File" and select your CSV file

Click "Submit" to begin analysis

Wait for processing (typically 2-5 seconds per 100 reviews)

3. Interpret Results
The application will display:

CSI Score — A value between 0 and 1 representing overall customer satisfaction

Product Status — "Fit to Sell" (CSI ≥ 0.6) or "Needs Improvement" (CSI < 0.6)

Detailed Breakdown — Individual component scores for transparency

⚙️ How It Works
The application follows a four-stage pipeline to transform raw data into actionable insights.

Stage 1: Data Refining & Cleaning
Raw Etsy data is scraped and processed to ensure quality and completeness:

Data Collection: Web scraping extracts product information, reviews, and ratings

Missing Value Handling: A linear regression model predicts and fills missing data points with 95% accuracy

Data Organization: Pandas structures and normalizes the dataset

Data Validation: Column presence, data types, and value ranges are verified

Visualization: Matplotlib generates exploratory plots to identify patterns and outliers

Stage 2: Sentiment Analysis with RoBERTa
RoBERTa (Robustly Optimized BERT Approach) performs state-of-the-art sentiment analysis:

Model Selection: RoBERTa is chosen for its superior performance on emotion detection tasks

Fine-tuning: The model is trained on diverse emotion datasets for accurate sentiment classification

Inference: Each review is analyzed to determine sentiment polarity:

Positive: Indicates customer satisfaction (score: 0.5 to 1.0)

Neutral: Indicates mixed or indifferent sentiment (score: -0.5 to 0.5)

Negative: Indicates dissatisfaction (score: -1.0 to -0.5)

Compound Score: A continuous value between -1 and 1 is generated for each review

Stage 3: Customer Satisfaction Index (CSI) Calculation
The CSI is a weighted average of three key satisfaction factors:

Factor	Weight	Rationale
ItemRating	40%	Direct measure of product quality satisfaction
ShippingRating	20%	Reflects delivery experience satisfaction
RoBERTa Compound	40%	Captures nuanced sentiment from review text
Formula:

text
CSI = (0.4 × ItemRating/5) + (0.2 × ShippingRating/5) + (0.4 × Normalized(RoBERTa_Compound))
Normalization Process:

Ratings are normalized to a 0-1 scale (divide by 5)

RoBERTa compound scores are normalized using min-max scaling

Weighted sum is calculated and clamped to [0, 1] range

Final score interpreted:

≥ 0.6: Product is "Fit to Sell"

< 0.6: Product "Needs Improvement"

Stage 4: Flask Web Application
The entire pipeline is deployed as a user-friendly web application:

File Validation: Ensures correct CSV format and required columns

Asynchronous Processing: Handles large files without blocking the interface

Error Handling: Graceful error messages for invalid inputs

Result Presentation: Clear visualization of CSI scores and recommendations

📸 Results Dashboard
View your CSI score and product recommendation

https://Artifacts/Screenshots/sales2.png

🛠️ Tech Stack
Backend
Component	Technology	Purpose
Web Framework	Flask	Server-side routing and API
Data Processing	Pandas, NumPy	Data manipulation and analysis
NLP Model	RoBERTa (Hugging Face)	Sentiment analysis
Visualization	Matplotlib	Data exploration and plotting
Development	Jupyter Notebook	Prototyping and experimentation
Frontend
HTML5 for structure

CSS3 for styling

JavaScript for interactivity

Deployment
Local server (development)

Flask development server

📦 Installation
Prerequisites
Python 3.8 or higher

pip package manager

Step-by-Step Setup
Clone the Repository

bash
git clone https://github.com/yourusername/Sales-Sheet-Scanner.git
cd Sales-Sheet-Scanner
Create Virtual Environment (Optional but recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
pip install -r requirements.txt
Or install manually:

bash
pip install flask flask_cors pandas transformers re matplotlib numpy scikit-learn
Run the Application

bash
python check.py
Access the Application

Open your browser and navigate to: http://127.0.0.3:5002/

(Port may vary; check console output for exact URL)

📁 Project Structure
text
Sales-Sheet-Scanner/
│
├── Artifacts/
│   └── Screenshots/
│       ├── sales.png
│       └── sales2.png
│
├── templates/
│   ├── index.html
│   └── script.js
│
├── Assets/
│   ├── Etsy/                    # Raw scraped data
│   ├── Etsy_preprocessed/       # Cleaned dataset
│   ├── EtsyAnalyzing/          # Jupyter notebooks
│   └── roberta_model/          # Fine-tuned RoBERTa model
│
├── check.py                     # Flask application entry point
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
📚 Dependencies

Package	Version	Purpose
Flask	≥2.0.0	Web framework
flask_cors	≥3.0.0	Cross-Origin Resource Sharing
pandas	≥1.3.0	Data manipulation
transformers	≥4.20.0	RoBERTa model integration
torch	≥1.9.0	PyTorch backend for transformers
numpy	≥1.21.0	Numerical operations
matplotlib	≥3.4.0	Data visualization
scikit-learn	≥0.24.0	Machine learning utilities
re	Built-in	Regular expressions

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch: git checkout -b feature/AmazingFeature

Commit your changes: git commit -m 'Add some AmazingFeature'

Push to the branch: git push origin feature/AmazingFeature

Open a Pull Request

Contribution Guidelines
Follow PEP 8 style guide for Python code

Write clear, descriptive commit messages

Update documentation for any new features

Test your changes before submitting


📞 Contact
Project Maintainer: Saudha Hibathullah

Email: saudha.hibathullah@gmail.com

