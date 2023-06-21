# PolarLowIdentifier
This hack is an ML model that can identify a polar low storm. Recognizing them and alerting potentially affected communities can aid in their preparedness and response to these storm events.

# What it is
A Machine Learning Model that can identify a polar low storm

# Inspiration
This project is based on a research project I did with my team - Ryan, Riya, and Katie - in one of my classes here at UMD. Riya mentioned to me that the dataset we had used had some invalid entry points, so I thought it would be a good idea to clean up the dataset and try to improve our previous model.

# What it does
This model uses a pre-trained CNN called AlexNet combined with a decision tree to identify whether an image contains a polar low or not.

# How I built it
After removing the invalid data points from the original dataset, I added some new data because I was suspicious that our original model was overfitting our small dataset. After this, I tried to manipulate the hyperparameters of our model (such as the number of epochs and learning rate) to find an optimal combination that led to improved accuracy.

The working model is located in this folder:
https://drive.google.com/drive/folders/1L-yxUVKnaQYqoldtnwlqqsZ4rVuDJXVY?usp=share_link
