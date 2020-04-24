# Reddit-Flair-Detector-Application <a href="https://reddit-realtime-analysis.herokuapp.com/"><img src="static/46.png" align="left" height="55" width="55" ></a>

Reddit-Flair-Detector-Application

1. **Web-Application** is live at https://reddit-realtime-analysis.herokuapp.com/

2. **Automated Testing** URL at https://reddit-realtime-analysis.herokuapp.com/automated_testing

3. **Jupyter Notebook** at https://github.com/abhisheksaxena1998/Reddit-Flair-Detector-Application/tree/master/Jupyter%20Notebooks

## To use automated_testing

**Automated Testing** URL at https://reddit-realtime-analysis.herokuapp.com/automated_testing

**Python Code for automated_testing :** 

```
import requests

r = requests.post("https://reddit-realtime-analysis.herokuapp.com/automated_testing", files = {'upload_file': open('s.txt', 'rb')})
print (r.text)    
```

## Terms used in collected Dataset

1. Preprocessed Text=Text with bogus symbols " ! ? / , @ : " removed.
2. Combined Text = Preprocessed Text of URL + Title + Comments.
3. Cleaned Text = Preprocessed text with STOPWORDS like " the,I,was,were " removed using "en_core_web_sm" module of [Spacy Library](https://spacy.io/).

## Classifiers used :

SVM, MLP, MultinomialNB, SGDClassifier, Logistic Regression, RandomForest

## Accuracy of various Classifiers :

Classifier | Cleaned Text | Combined Features | Processed URL | Processed Title
------------ | ------------- | ------------ | ------------- | ------------- 
SVM | 0.79 | 0.72 | 0.47 | 0.65
MLP |0.61	| 0.61 | 0.42 | 0.54
MultinomialNB | 0.61 | 0.57 | 0.40 | 0.58
SGDClassifier | 0.80 | 0.79 | 0.49 | 0.66
Logistic Regression | 0.76 | 0.74 | 0.47 | 0.65
RandomForest | 0.75 | 0.71 | 0.44 | 0.63



## Installation Guide

1.  Extract Reddit-Flair-Detector-Application zip file.
2.  In Reddit-Flair-Detector-Application folder there is a file requirements.txt
3.  Open Command Prompt in Reddit-Flair-Detector-Application folder.
  
    ![How to install](/Images/1.png)  

4.  Type following command in cmd.

    ![How to install](/Images/2.png)

5.  To run the code, write following command in terminal.

    python manage.py runserver
    
    ![How to install](/Images/3.png)

6.  Type http://127.0.0.1:8000/ in URL bar of browser and press Enter. Machine Learning powered Web-Application will start.  

    ![How to install](/Images/4.png)

## Usage : 

1.  Type URL in text bar and click on GET REALTIME ANALYSIS.

    ![Usage](/Images/5.png)
    
2.  Link for automated testing is: https://reddit-realtime-analysis.herokuapp.com/automated_testing

3.  Upload a text file which contains a link of a r/india post in every line and click on GET PREDICTIONS.

    ![Usage](/Images/6.png)
    
    ![Usage](/Images/7.png)

4.  The result is a JSON file as depicted here.

    ![Usage](/Images/8.png)
    
    ![Usage](/Images/9.png)    
## Approach Followed

1.  Fetch data from r/india subreddit.
2.  Clean the data for bogus symbols like " , ! ( ) ? " combine features, remove stopwords using Spacy.
3.  Train using combined features through SGDClassifier.
4.  Save the classifier for using it in the Web-Application.
5.  Predict the flair, through subreddit URL.

## About Application

1. Data Analysis section at : https://reddit-realtime-analysis.herokuapp.com/dataanalysis

    ![Usage](/Images/dataanalysis.png)

2. Data that is searched through this application is stored in a database : https://reddit-realtime-analysis.herokuapp.com/geturlhistory

    ![Usage](/Images/database.png)
    
3. Themes discussed in each flair are depicted at : https://reddit-realtime-analysis.herokuapp.com/themes

    ![Usage](/Images/themes.png)
