import tweepy

auth = tweepy.OAuthHandler("bLsisgRN4QoBYQRqj5Z6qEb2T", "x0y8Cj8Ft6Qqlba9iZXUMpkIqi2ZHfrEUlS6xXWjuH1mMRXSVf")
auth.set_access_token("909984739301326848-DsZHUr8ZTONeQgoasNBH7kqrB1vT2bN", "yqiFB2ZtCap5i55VNIwtQtR3VzJqrHOUOGpwK8QsDQgTO")

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


# user = api.me()
# print(user.name)

# print(user.screen_name)

# print(user.followers_count)



# genrous bot
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)


# he he we can not proceed any forther because twitter yet not give us the permition to use their api