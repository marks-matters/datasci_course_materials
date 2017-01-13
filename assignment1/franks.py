import urllib
import json


list_of_tweets = []
index = 0
number_pages = 10

search_url = "http://search.twitter.com/search.json?q=microsoft"

for result_page_num in range(1,number_pages+1): #range goes from first number and stops before last number
        
    print "RESULTS PAGE NUMBER: "+str(result_page_num)
    new_search_url = search_url+"&page="+str(result_page_num) #note this will start from &page=2,  SECOND PAGE OF RESULTS &page=1 
    
    response = urllib.urlopen(new_search_url)
    dict_results = json.load(response)
    
    # capture just the tweet data
    for item in dict_results['results']:
        list_of_tweets.append(item['text'].encode('utf-8'))
        print "INDEX:" + str(index) + "TWEET: " + list_of_tweets[index]
        index += 1