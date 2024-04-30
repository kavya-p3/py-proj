from flask import Flask, request

app = Flask(__name__)

stores= [
    {
        "name": 'Dmart',
        'items': [
            {'name': 'chocolates',
             'price': 10
             },
            {'name': 'Rice',
             'price': 100
             },
            {'name': 'Lays',
             'price': 5}
        ]
    }
]
#get all
@app.get('/stores')
def get_all():
    return {'stores_all' : stores}

#get particular store details
@app.get('/stores/<string:name>')
def get_stores(name):
    for store in stores:
        if store['name']==name:

            return  {'store_items' : store['items']}
    return {"message": 'store not found'}, 404

#post store
@app.post('/store')
def post_store():
    request_data=request.get_json()
    new_store={'name':request_data["name"],"items":request_data['items']}
    stores.append(new_store)
    return new_store,201


#post items in the particular store
@app.post('/store/<string:store_name>/item')
def create_item(store_name):
    for store in stores:
        if store['name']==store_name:
            request_data=request.get_json()
            for item in request_data['items']:

                store['items'].append(item)
            return store['items'], 201
    return {"message":'store not found'},404