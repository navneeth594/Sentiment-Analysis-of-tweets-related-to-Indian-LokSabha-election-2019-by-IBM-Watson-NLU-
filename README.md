# Sentiment-Analysis-of-tweets-related-to-Indian-LokSabha-election-2019-by-IBM-Watson-NLU-



About my project:


Tweets related to Indian LOkSabha elections 019 were collected from February 2nd 2019 to April 25th 2019 trough twitter's streaming api
The tweets were written into json format. From the json files the text part was taken into account and written into a csv file.
Sentiment was found out on each of the tweets . Emotions like joy, anger, disgust, sadness and fear values were taken for Narendra Modi and Rahul Gandhi who were the two prominent leaders during the elections 



How to run:

After taking the file which contains only the preprocessed text part from the json files, the code altered1.py is made to run to collect tweets regarding only Indian elections and to remove all unrelated tweets.

Then the code first2.py is made to run to seggrate the tweets to different parties based on keywords.

To use IBM watson NLU as a tool for sentiment analysis first requirement is to develop an IBM bloud account and to subscirbe to IBM watson NLU resource. You will be provided with your api key and url

Then the file bjp3.py is made to run to find out the sentiment related to the party BJP and collects emotions towards Narendra Modi

Next the file congress4.py is made to run to find out the sentiment related to the party Indian National Congress and collects emotions towards Rahul Gandhi

Later mixed_tweets5.py is made to run to find out the sentiment of tweets which contain terms of both parties

partiesplot6.py gives the positive and negative sentiement plot related to the parties BJP and Congress

namo_rahuplot7.py gives the emotions related to Narendra Modi and Rahul Gandhi
