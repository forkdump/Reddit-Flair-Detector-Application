# Reddit-Flair-Detector-Application <a href="https://reddit-realtime-analysis.herokuapp.com/"><img src="static/46.png" align="left" height="55" width="55" ></a>

Reddit-Flair-Detector-Application

1. **Web-Application** is live at https://reddit-realtime-analysis.herokuapp.com/

2. **Automated Testing** URL at https://reddit-realtime-analysis.herokuapp.com/automated_testing

3. **Jupyter Notebook** at https://github.com/abhisheksaxena1998/Reddit-Flair-Detector-Application/tree/master/Jupyter%20Notebooks

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

    ![How to install](/Images/5.png)
    
2.  Link for automated testing is: https://reddit-realtime-analysis.herokuapp.com/automated_testing

3.  Upload a text file which contains a link of a r/india post in every line and click on GET PREDICTIONS.

    ![How to install](/Images/6.png)
    
    ![How to install](/Images/7.png)

4.  The result is a JSON file as depicted here.

    ![How to install](/Images/8.png)
    
    ![How to install](/Images/9.png)    
## Approach Followed

1.  Fetch data from r/india subreddit.
2.  Clean the data for bogus symbols like ",!()?", combine features, remove stopwords using Spacy.
3.  Train using combined features through SGDClassifier.
4.  Save the classifier for using it in the Web-Application.
5.  Predict the flair, through subreddit URL.

    
