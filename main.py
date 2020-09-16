import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama whitehouse")\
                                           .setMaxTweets(2)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)