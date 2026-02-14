
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
vader_sentiment = SentimentIntensityAnalyzer()
#be sure to use pip install vaderSentiment for this to work.

sentence_1 = "The movie was spectacular! I loved the visual effects!"
sentence_2 = "Did you see those shoes? Awful!"

print(sentence_1)
print(vader_sentiment.polarity_scores(sentence_1))
print(sentence_2)
print(vader_sentiment.polarity_scores(sentence_2))

#Using the compound part of the sentiment sore
com = vader_sentiment.polarity_scores(sentence_2)
#vader sentiment returns a dictionary so you need to retrieve the compound score from there.
print(type(com))
sen2_compound = com.get("compound")

#Assigning results based on the compound score
def get_result(score):
    if(score > 1):
        print("statement is positive")
    elif(score < 0):
        print("statement is negative")
    elif(score == 0):
        print("statement is zero")


#running results on sentence 2.
get_result(sen2_compound)