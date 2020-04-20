import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class RegisterUser(Resource):

    parser= reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):
        data=RegisterUser.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message":"user for this username is already exist"}
        '''con=sqlite3.connect("data.db")
        cursor=con.cursor()
        query="INSERT INTO users VALUES(NULL,?,?)"
        cursor.execute(query,(data['username'],data['password']))
        con.commit()
        con.close()'''
        newuser=UserModel(**data)
        newuser.save_to_db()
        return {'message':'registration successful'},201