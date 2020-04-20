import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate,identity
from flask_jwt import JWT,jwt_required
from models.item import ItemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot left blank"
    )
    parser.add_argument('price',
        type=str,
        required=True,
        help="This field cannot left blank"
    )
    parser.add_argument('store_id',
        type=str,
        required=True,
        help="store id"
    )    
    

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"item not found"},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'Already Exist'}
        
        data=Item.parser.parse_args()
        item= ItemModel(name, data['price'], data['store_id'])
        try:
            item.insert()
        except:
            return {'message':'An error occured'},500

        return {"message":"Item Insert completed"}

    def delete(self,name):
        '''con=sqlite3.connect("data.db")
        cursor=con.cursor()
        query="DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))
        con.commit()
        con.close()'''
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"Item Deleted completed"}

    def put(self,name):
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
        #updated_item= ItemModel(name, data['price'])
        if item is None:
            item=ItemModel(name,data['price'], data['store_id'])
        else:
            item.price=data['price']
        
        item.insert()

        return item.json()

class ItemList(Resource):
    def get(self):
        '''con=sqlite3.connect("data.db")
        cursor=con.cursor()
        query="SELECT * FROM items"
        result=cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name':row[0], 'price':row[1]})
        con.close()
        return {'items':items}'''
        return {"items":[item.json() for item in ItemModel.query.all()]}