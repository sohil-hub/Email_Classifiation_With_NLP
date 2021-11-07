# Email_Classifiation_With_NLP


This is a Natural alnguage processing based project, in which I tried to train a model that can predict whether an email is a spam or not.

## Dataset
The dataset is having around 5500 examples.
This dataset is imbalanced dataset since it has around 46-47k examples belong to one class and remaining belongs to another class. I used downsampling to avoid this problem. 

## Classification Using BERT
BERT is a strong and pretrained model available on tensorflow-hub. We can preprocess the text can get the word embedding for each word in the text.
I have added a custom model on top of BERT to make it usefull for email classification problem.
Got accuracy of 92% on test dataset.

## Classification From Scratch
I have used pandas for working with a csv file, nltk for text preprocessing, GaussianNB and Artificial Neural Networks for classification.
Got accuracy of 95.32% using GaussianNB and around 94% using ANN on test set.

## Deployment
Used stearmlit library and streamlit cloud for deployment.
link to the app:- https://share.streamlit.io/sohil-hub/email_classifiation_with_nlp/main/main.py
