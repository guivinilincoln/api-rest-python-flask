from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' # configuração do tipo e caminho e nome do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Desativa os rastreamentos de notificações
api = Api(app)

@app.before_first_request #decorador que so existe nas v abaixo de 2.2.5, ela faz os flask rodar a função assim que inicia o flask
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis') #(EndPoint)aqui é a URI que usamos para chamar a API
api.add_resource(Hotel, '/hoteis/<string:hotel_id>') #(EndPoint)aqui a URI que usamos para chamar a API + arguentos

if __name__ == '__main__':
    from sql_alchemy import banco #import da class sql_alchemy e da instancia banco, esta fazendo aqui, pois so queremos que ele inici junto da aplcação
    banco.init_app(app) #usando uma função do alchemy ele inicia o banco junto com aplicação
    app.run(debug=True)
