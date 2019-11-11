from flask import Flask, render_template                      #Importa a biblioteca do microframework Flask do diretório "flask"
from CreditoNu import Boleto                                  #Imposta a classe "Boleto" do diretório "CreditoNu"

boleto = 'nubank-2019-03.csv'                                 #Especifíca o título do arquivo que será extraído
data = '2019-02-11'                                           #Especifíca a data que será pesquisada

categoria1 = 'restaurante'                                    #Especifíca a categoria 1
categoria2 = 'servicos'                                       #   //      //  //      2
categoria3 = 'transporte'                                     #   //      //  //      3

extrato = Boleto(boleto)                                      #Variável recebe a classe "Boleto" com a variável "boleto" passada como parâmentro

lista = extrato.lista                                         #Variável "lista" recebe o return do método "lista" da classe "Boleto"
#for item in lista:
#    print(item)

app = Flask(__name__)

'''
for transacao in transacoes:
    if type(transacao) is Gasto:
        print('gasto')

    else:
        print('pagamento')
'''
teste = extrato.mostraTransacoesPorData(data)
#print(type(teste[1]))

@app.route('/inicio')
def ola():
    return render_template('painel.html',
                           data = '2019-07',
                           quantidade= extrato.quantidadeTransacoes(),
                           extrato = lista,
                           categoria=categoria3,
                           valorCategoria=extrato.valorTransacoesPorCategoria(categoria1),
                           Data=data,
                           transacoesData= extrato.mostraTransacoesPorData(data))

app.run()


#################### Teste ########################

#print(lista[0])