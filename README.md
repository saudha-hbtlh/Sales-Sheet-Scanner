# Sales-Sheet-Scanner
## SUMMARY

The Sales Sheet Scanner is a Flask web application designed to help users determine whether a product is good for selling or not based on provided sales data. Simply upload a preprocessed CSV file containing sales data, and the app will analyze it to provide insights.

*****
*****

## TABLE OF CONTENTS

📚 — [Dependencies](https://github.com/Zernach/Airline-Price-Predictions#-dependencies)

🗂 — [Files in This Repo](https://github.com/Zernach/Airline-Price-Predictions#-files-in-this-repo)

0️⃣ — [Data Refining & Cleaning](https://github.com/Zernach/Airline-Price-Predictions#0%EF%B8%8F%E2%83%A3--data-refining--cleaning)

1️⃣ — [Predictive Modeling](https://github.com/Zernach/Airline-Price-Predictions#2%EF%B8%8F%E2%83%A3--predictive-modeling)

*****
*****


## 📚 Dependencies
To auto-install the dependencies for this project in a subshell virtual environment, the only packages you'll have to have pre-installed are `python`,'flask','flask_cors', 'pandas','transformers','re'


## 💻 How to Locally Run this Repo
1. Download repo to local machine and `cd` into directory
2. pip install the above dependencies
4. Run `python check.py` to serve the web-app and host it on a local server on your machine — you'll probably get some warnings about unpickle-ing the machine learning estimator pipeline, but please disregard & open the server @ http://127.0.0.3:5002/ (instead of 8050, your computer might run it on a different port number.. if it happens make sure to change the port number in js)

## 🗂 Files in This Repo
File/Directory | Description
--- | ---
`📂 Assets` | `📂 Directory — Etsy (the webscrapped file is preprocessed), Etsy_preprocessed(has the preprocessed csv file to check whether the app is working),EtsyAnalyzing(The data is analyzed in jupyter notebook),roberta_model(model used for sentiment analysis)
`📂 templates` | `📂 Directory` — Has the html and js file for the app
`Check.py` | Python file which contains the flask app

*****
*****

### 0️⃣ — DATA REFINING & CLEANING

I collected information from an Etsy website by webscrapping. Then, I looked at the data closely using a program called Jupyter Notebook. I made sure the data was neat and accurate by fixing any mistakes or missing pieces.I made sure the missing pieces fit perfectly by creating a linear model to calculate the accuracy..

After that, I used another program called Pandas to organize and clean up the data, making it easier to work with. I also used NumPy to do some math stuff to make the data even better for analysis.

Finally, I used a tool called Matplotlib to turn the data into pictures that are easy to understand. These pictures helped me see patterns and important details in the data.

### 1️⃣ — PREDICTIVE MODELING

I used a fancy tool called RoBERTa to understand how people feel in text, like whether they're happy, sad, or angry. I taught RoBERTa about emotions using lots of examples in a program called Jupyter Notebook.

Once RoBERTa learned what to look for, I gave it some text to see how well it could guess people's feelings. I tried different sentences to see if RoBERTa could figure out if they were positive, negative, or neutral.

After making sure RoBERTa worked well in Jupyter Notebook, I decided to use it in a web app made with Flask. This way, people could type in text, and RoBERTa could tell them how the words made people feel.
