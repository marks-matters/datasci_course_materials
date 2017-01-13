# C:\Users\Mark\Documents\GitHub\datasci_course_materials\assignment1

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
print response
type_resp = json.load(response)
#print type(type_resp)

resp_results = type_resp["results"]

resp_res_text = type(resp_results)

#print type_resp.keys()
#print resp_results[0]
#print type(resp_results[0])
result1 = resp_results[0]

#print result1.keys()
text1 = result1["text"]

print text1