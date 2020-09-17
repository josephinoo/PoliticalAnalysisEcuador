import GetOldTweets3 as got 



def tweets_old(query, since , until,numberTweets,filename="output.csv"):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(since).setUntil(until).setMaxTweets(numberTweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    fileTweet=open(filename,"a")
    for tweet in tweets:
        filename.write(tweet.text+"\n")
        print(tweet.text)
    return tweets   
    