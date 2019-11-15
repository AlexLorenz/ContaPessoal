from flask import Flask, render_template, request, redirect   #Importa a biblioteca do microframework Flask do diretório "flask"
from CreditoNu import Boleto                                  #Imposta a classe "Boleto" do diretório "CreditoNu"

boleto = 'nubank-2019-04.csv'                                 #Especifíca o título do arquivo que será extraído
data = '2019-03-09'                                           #Especifíca a data que será pesquisada

categoria1 = 'restaurante'                                    #Especifíca a categoria 1
categoria2 = 'servicos'                                       #   //      //  //      2
categoria3 = 'transporte'                                     #   //      //  //      3

app = Flask(__name__)

data = 0
teste = 0

@app.route('/')
def index():
    return render_template('inicio.html', titulo = 'Pesquisa')

@app.route('/pesquisar', methods=['POST',])
def pesquisar():
    extrato = request.form['extrato']
    data = request.form['data']
    teste = Boleto(extrato)                                                          # Variável recebe a classe "Boleto" com a variável "boleto" passada como parâmentro
    return render_template('painel.html',
                           data = '2019-07',
                           quantidade= teste.quantidadeTransacoes(),
                           extrato = teste.lista,
                           maiorGasto = teste.maiorGasto(),
                           valorGastoTotal = teste.valorGastoTotal(),
                           valorPagoTotal = teste.valorPagoTotal(),
                           categoria=categoria3.capitalize(),
                           valorCategoria=teste.valorTransacoesPorCategoria(categoria3),
                           Data=data,
                           transacoesData= teste.mostraTransacoesPorData(data))
    #return redirect('/')


app.run(debug=True)


#################### Teste ########################