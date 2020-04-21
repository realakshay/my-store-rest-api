from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"store not found"},404


    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message" : "Store with name {} is already there".format(name)}, 400
        
        store=StoreModel(name)
        store.insert()
        return store.json(), 201

    def delete(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"store deleted"}, 201

    def put(self):
        pass

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}
    