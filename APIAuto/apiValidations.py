import requests
from utilities.configurations import *
from utilities.recources import *
from payLoad import *
import json
import re

# response= requests.get('http://216.10.245.166/Library/GetBook.php',params='AuthorName=Rahul Shetty')
#
# json_resp=response.json()
# for book in json_resp:
#     if re.match(r'ab\w' , book['isbn']):
#         print (book['book_name'])
# config=getconfig()
#
# response= requests.post(config['API']['endpoint']+ApiResources.addbook,json={
#
# "name":"kavyaas555",
# "isbn":"070233559",
# "aisle":"991830",
# "author":"kavya555"
# },headers={'Content-Type': 'applicatio/json'})
# print(response.status_code)
# #response_json=response.json()
# id=response.json()['ID']
# print(id)
# print(response.json())
#
# resp=requests.post(config['API']['endpoint']+ApiResources.deletebook,json={
#     "ID":id
# },headers={'Content-Type': 'applicatio/json'})
# # print(resp.json())
# se=requests.session()
# se.cookies.update({'A':'200'})
# cookie={'k':'100'}
# resp=se.get('http://httpbin.org/cookies',cookies=cookie)
# # print(resp.text)
# files = {'file': open('C:\\Users\\kp\\Pictures\\Sketchpad.png', 'rb')}
# url='https://petstore.swagger.io/v2/pet/9843217/uploadImage'
# resp=requests.post(url,files=files)
# print(resp.status_code)
# print(resp.text)
query='Select * from Books'
config=getconfig()
url=config['API']['endpoint']+ApiResources.addbook
resp=requests.post(url,json=buildPayloadFromDB(query))
print(resp.text)
id=resp.json()['ID']
resp=requests.post(config['API']['endpoint']+ApiResources.deletebook,json={
     "ID":id})
print(resp.text)