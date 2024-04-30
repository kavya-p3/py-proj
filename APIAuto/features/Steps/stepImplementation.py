import requests
from behave import *

from payLoad import *
from utilities.configurations import *
from utilities.recources import *


@given('Book details which needs to be added to library')
def step_impl(context):
    context.query = 'Select * from Books'
    config = getconfig()
    context.url = config['API']['endpoint'] + ApiResources.addbook
    context.payload = buildPayloadFromDB(context.query)


@when(u'we execute the AddBook POSTAPI method')
def step_impl(context):
    context.resp = requests.post(context.url, json=context.payload)


@then(u'book is successfully added')
def step_impl(context):
    print(context.resp.text)
    context.id = context.resp.json()['ID']
    print(context.id)

@given('the book details with {isbn} and  {aisle}')
def step_impl(context,isbn,aisle):
    config = getconfig()
    context.url = config['API']['endpoint'] + ApiResources.addbook
    context.payload = addBookPayLoad(isbn,aisle)

@given(u'I have github cred')
def step_impl(context):
    context.se=requests.session()
    context.se.auth=auth=('kavya-p3','Git@1234')

@when(u'I hit getRepo API of github')
def step_impl(context):
    context.resp=context.se.get(ApiResources.github)



@then(u'Status code of response should be {code:d}')
def step_impl(context,code):
    print(context.resp.status_code)
    assert context.resp.status_code == code



