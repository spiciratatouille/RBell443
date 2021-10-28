#Program 4
#Due: 4/21/2021
#CIS 443-75
#Grading ID: P5279
#This program parses a csv file and calculates the statistics of sentiment, 
#polarity, cumulative agreement, disagreement, and number of reviews 


import pandas as pd
from textblob import TextBlob

#import csv and set number of reviews
file = 'yelp.csv'
reviews = pd.read_csv(file)
columns = 10000

#determine positive, neutral, or negative based on star rating
def star_rating(row):
    if row['stars'] == 1:
        rate = 'negative'
    elif row['stars'] == 2:
        rate = 'negative'
    elif row['stars'] == 3:
        rate = 'neutral'
    else:
        rate = 'positive'
    return rate

#determine value of polarity
def polarity(x):
    return TextBlob(x).sentiment.polarity

#assign positive, negative, or neutral based on polarity
def analyze_polarity(row):
    if row['Polarity'] > 0.05:
        rate = 'positive'
    elif row['Polarity'] < -0.05:
        rate = 'negative'
    else:
        rate = 'neutral'
    return rate

#determine whether or not the sentiments and polarities match
def compare(row):
    if row['Sentiment'] == row['Polarity Analysis']:
        value = True
    else:
        value = False
    return value

#add data to csv
reviews['Sentiment'] = reviews.apply(star_rating, axis = 1)
reviews['Polarity'] = reviews['text'].apply(polarity)
reviews['Polarity Analysis'] = reviews.apply(analyze_polarity, axis = 1)
reviews['Comparison'] = reviews.apply(compare, axis = 1)

#cumulative stats for data
count_false = reviews['Comparison'].value_counts()[0]
count_true = reviews['Comparison'].value_counts()[1]
agreement = (count_true / columns)*100
disagreement = (count_false / columns)*100

#number of reviews for each star rating
a1 = reviews.groupby(by='stars')['Comparison'].count()[1]
a2 = reviews.groupby(by='stars')['Comparison'].count()[2]
a3 = reviews.groupby(by='stars')['Comparison'].count()[3]
a4 = reviews.groupby(by='stars')['Comparison'].count()[4]
a5 = reviews.groupby(by='stars')['Comparison'].count()[5]
reviews.groupby(by='stars')['Comparison']

#number of agreements for each star rating
agree5 = len(reviews[(reviews['stars'] == 5) & (reviews['Sentiment'] =='positive') & (reviews['Polarity Analysis'] == 'positive')])
agree4 = len(reviews[(reviews['stars'] == 4) & (reviews['Sentiment'] =='positive') & (reviews['Polarity Analysis'] == 'positive')])
agree3 = len(reviews[(reviews['stars'] == 3) & (reviews['Sentiment'] =='neutral') & (reviews['Polarity Analysis'] == 'neutral')])
agree2 = len(reviews[(reviews['stars'] == 2) & (reviews['Sentiment'] =='negative') & (reviews['Polarity Analysis'] == 'negative')])
agree1 = len(reviews[(reviews['stars'] == 1) & (reviews['Sentiment'] =='negative') & (reviews['Polarity Analysis'] == 'negative')])

#calculate percentage of agreements for each star rating
aper5 = (agree5/a5) * 100
aper4 = (agree4/a4) * 100
aper3 = (agree3/a3) * 100
aper2 = (agree2/a2) * 100
aper1 = (agree1/a1) * 100

#number of disagreements for each star rating
d5 = a5 - agree5
d4 = a4 - agree4
d3 = a3 - agree3
d2 = a2 - agree2
d1 = a1 - agree1

#calculate percentage of disagreements for each star rating
dper5 = (d5/a5) * 100
dper4 = (d4/a4) * 100
dper3 = (d3/a3) * 100
dper2 = (d2/a2) * 100
dper1 = (d1/a1) * 100

#print out the data
print(f'Total Agree: {count_true}')
print(f'Total Disagree: {count_false}')
print(f'Agreement %: {agreement:.2f}')
print(f'Disagreement %: {disagreement:.2f}')
print('Stars|Total Reviews|Num. Agree|% Agree|Num. Disagree|% Disagree')
print(f"  5  |      {a5}   |    {agree5}  | {aper5:.2f}%|     {d5}     |  {dper5:.2f}%")
print(f"  4  |      {a4}   |    {agree4}  | {aper4:.2f}%|     {d4}     |  {dper4:.2f}%")
print(f"  3  |      {a3}   |    {agree3}   | {aper3:.2f}%|     {d3}    |  {dper3:.2f}%")
print(f"  2  |      {a2}    |    {agree2}   | {aper2:.2f}%|     {d2}     |  {dper2:.2f}%")
print(f"  1  |      {a1}    |    {agree1}   | {aper1:.2f}%|     {d1}     |  {dper1:.2f}%")