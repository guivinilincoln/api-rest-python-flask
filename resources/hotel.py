from flask_restful import Resource, reqparse #reqparse auxilia no recebimento dos elementos de request
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.3,
        'diaria': 320.34,
        'cidade': 'São Paulo'
    }
]

class Hoteis(Resource): #(Referente ao end point url/hoteis )Retorna uma lista de hoteis padrão
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource): #(Referente ao end point url/hoteis/id )Retorna uma lista de hoteis padrão
    atributos = reqparse.RequestParser() #usando o reqparse como atribulos de uma class
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def find_hotel(hotel_id): #metodo para localizar hotel por ID
        for hotel in hoteis: #percorre a lista de hoteis
            if hotel['hotel_id'] == hotel_id: #verifica se hotel desejado existe na lista
                return hotel #retonar o hotel desejado
        return None #caso não devolve None

    def get(self, hotel_id): #faz um get por id
        hotel = Hotel.find_hotel(hotel_id) #chama o metodo find_hotel, passando o id recebido pelo EndPoint
        if hotel: #Verifica se o existe
            return hotel #Retorna o hotel
        return {'message': 'Hotel not found.'}, 404 # not fund, se não existe o hotel buscado

    def post(self, hotel_id):

        ''' novo_hotel = { #exemplo pouco usual
             'hotel_id': hotel_id,
             'nome': dados['nome'],
             'estrelas': dados['estrelas'],
             'diaria': dados['diaria'],
             'cidade': dados['cidade']
         } # criando "dicionario"
         '''
        dados = Hotel.atributos.parse_args() # Instanciando um classe e criando um objeito do tipo Hotel
        # E utilizando seu atribulo (argumentos) e a função (parse_args) de dependencia reqparse

        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        hoteis.append(novo_hotel) #adicionando o novo elemento a lista já existente
        return novo_hotel, 201 # e retorna o codigo 201 criado

    def put(self, hotel_id):

        dados = Hotel.atributos.parse_args()# Instanciando um classe e criando um objeito do tipo Hotel
        # E utilizando seu atribulo (argumentos) e o função (parse_args) de dependencia reqparse

        hotel_objeto = HotelModel(hotel_id, **dados)# Instanciando um classe e criando um objeito do tipo HotelModel
        #passando dois argumentos, id do hotel e dados como um **kwargs

        novo_hotel = hotel_objeto.json() #ultilizando a função .json da classe HotelModel

        hotel = Hotel.find_hotel(hotel_id) #utilizando a função se existe hotel da classe Hotel

        if hotel: #verifica se o hotel que foi retornado existe
            hotel.update(novo_hotel) #se existe ele faz um update na lista
            return novo_hotel, 200 # OK retorna o item criado
        hoteis.append(novo_hotel) # caso o hotel não seja encontrado na lista pela funcção fin.hotel o append cria um nv
        return novo_hotel, 201 # retorna status code 201 criado

    def delete(self, hotel_id):
        global hoteis; #mostra que queremos usar a variavel global
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id] #list comparing (quero que retorne hotel para cada hotel
        # dentro de hoteis se o hotel com id não for igual id recebido
        return {'message': 'Hotel deleted.'}