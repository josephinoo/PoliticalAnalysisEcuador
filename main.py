from  recursive_twets import *



print("Welcome..............")
stop=False
while(stop!=True):
    query_search= input("Ingrese el query a buscar: ")
    since=input("Desde: ")
    util=input("Hasta:")
    numberTweets=input("Numero de Tweets:")
    tweets_old(query_search,since,util,int(numberTweets))
    stop=True

