from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis') #(EndPoint)aqui é a URI que usamos para chamar a API
api.add_resource(Hotel, '/hoteis/<string:hotel_id>') #(EndPoint)aqui a URI que usamos para chamar a API + arguentos

if __name__ == '__main__':
        app.run(debug=True)