from utilities.configurations import *


def buildPayloadFromDB(query):
    addBody={}
    tp=getQuery(query)
    addBody['name']=tp[0]
    addBody['isbn']=tp[1]
    addBody['aisle']=tp[2]
    addBody['author']=tp[3]
    return addBody

def addBookPayLoad(isbn,aisle):
    body={
        "name" : "Learn just learn",
        "isbn" : isbn,
        "aisle": aisle,
        "author" : "kps"


    }
    return body
