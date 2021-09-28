#Movie ratings
import requests
#first letter must be capital
name=input("enter movie name")
parameters = {'t':name,'apikey':'805640d7'}
res = requests.get('http://omdbapi.com/',params=parameters)
result=res.json()
title=result['Title']
rating=result['Ratings'][0]['Value']
print("The rating of {} Movie is {}".format(title,rating))
