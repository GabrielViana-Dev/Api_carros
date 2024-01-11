from flask import Flask, jsonify, abort, request, json
from carros import Carros

argo= Carros('Fiat',2016)
cronos = Carros('Fiat',2017)
kwid = Carros('Renault',2018)
kwid.carro_negociando()
onix = Carros('Chevrolet',2019)
onix.carro_vendido()

lista_carros = [argo, cronos, kwid, onix]

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>SERVIDOR FLASK FUNCIONANDO!</h1>"

@app.route('/api/carros/')
def listar_carros():
    dict_carros = []
    for carro in lista_carros:
        dict_carros.append(vars(carro))
    return jsonify(dict_carros)


@app.errorhandler(404)
def nao_encontrado(erro):
    data = {"erro":str(erro)}
    return (jsonify(data), 404)

def get_carro_or_404(id):
    for carro in lista_carros:
        if carro.id == id:
            return carro
    abort(400,'Carro não encontrado.')

@app.route('/api/carros/<int:id>/')
def detalhar_carros(id):
    carro = get_carro_or_404(id)
    return jsonify(vars(carro))


@app.route('/api/carros/<int:id>/', methods=['DELETE'])
def deletar_carros(id):
    carro = get_carro_or_404(id)
    lista_carros.remove(carro)
    return jsonify(vars(carro))
    
    
@app.route('/api/carros/', methods=['POST'])
def criar_carros():
    #Parciar informações:
    data = request.get_json()
    marca = data.get('marca')
    ano = data.get('ano')
    status = data.get('status')

    if not status:
        novo_carro = Carros(marca=marca,ano=ano)

    elif status == 'VENDIDO':
        novo_carro = Carros(marca=marca,ano=ano)
        novo_carro.carro_vendido()

    else:
        novo_carro = Carros(marca=marca,ano=ano)
        novo_carro.carro_negociando()

    lista_carros.append(novo_carro)    
    return data

@app.route('/api/carros/<int:id>/', methods =['PUT'])
def editar_carro(id):
    data = request.get_json()
    marca = data.get('marca')
    ano = data.get('ano')
    status = data.get('status')

    if not marca:
        abort(400,'Precisa inserir marca.')

    if not ano:
        abort(400,'Precisa inserir ano.')

    if not status:
        abort(400,'Precisa inserir status.')

    carro = get_carro_or_404(id)
    carro.ano = ano 
    carro.marca = marca
    carro.status = status

    return jsonify(vars(carro))
    
@app.route('/api/carros/<int:id>/', methods =['PATCH'])
def editar_parcial(id):
    data = request.get_json()   
    carro = get_carro_or_404(id)

    if 'marca' in data.keys():
        marca = data.get('marca')
        if not marca:
            abort(400,'Precisa inserir marca.')
        carro.marca = marca

    if 'ano' in data.keys():
        ano = data.get('ano')
        if not ano:
            abort(400,'Precisa inserir ano.')
        carro.ano = ano

    if 'status' in data.keys():
        status = data.get('status')
        if not status:
            abort(400,'Precisa inserir status.')
        carro.status = status

    return jsonify(vars(carro))