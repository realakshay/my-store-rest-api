# my-store-rest-api

Using Flask, Flask-RESTful, Flask-SQLAlchemy, SQLite3, JWT

This is the rest api for store. which has two models item and store and there is relationship between them.
which item is asscociated with which store is managed by this rest api.

example item id 1, item name mango, item price 10.5, store_id = 1

and store -> store_id=1, name=Fruite

then items-> fruite : [name=mango, price=10.5]
