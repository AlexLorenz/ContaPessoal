from gasto import Gasto                                         #Importa a classe "Gasto" do diretório "gasto"
from pagamento import Pagamento                                 #Importa a classe "Pagamento" do diretório "pagamento"

class Boleto:                                                  #Cria a classe "Boleto"
    def __init__(self, extrato):                                #Cria o método construtor solicitando o parâmetro 'extrato'
        self._extrato = extrato
        data = open(extrato, 'r')                               #A variável "data" recebe o arquivo em mode de leitura(read)
        #print(type(data))
        boleto = data.read()                                    #Variável boleto recebe a
        data.close()


        boleto = boleto.replace(',,', ',')                      #Troca ",," por ","
        boleto = boleto.replace('educaÃ§Ã£o', 'educacao')       #Troca "educaÃ§Ã£o" por "educacao"
        boleto = boleto.replace('serviÃ§os', 'servicos')        #Troca "serviÃ§os" por "servicos"


        listaBoleto = boleto.split('\n')                        #Variável "listaBoleto" recebe "boleto" separado por "\n", o que torna "listaBoleto" uma Lista
        #print(listaBoleto)

        del(listaBoleto[0])

        lista = []                                              #Cria a variável "lista" que recebe uma Lista vazia
        #print(listaBoleto)

        for line in listaBoleto:                                #Para cada "line"(item) em "listaBoleto" faça isso:
            transacao = line.split(',')                         #Variável "transacao" recebe line(cada item de "listaBoleto") separado por ",", criando Listas dentro da
                                                                # Lista "listaBoleto"

            lista.append(transacao)                             #Adiciona "transacao" a Lista "lista"

        #print(lista)

        n = 0
        self._transacoes = []                                   #Cria a varíavel "transacoes" de forma que todas os métodos tenham acesso a ela(self.) e de maneita que só
                                                                # possa ser acessado pela propria classe e suas 'filhas'(_)

        for item in lista:                                                           #Para cada 'item' na "lista"
            # print(item)
            if len(item) == 3:                                                       #Se a quantidade de itens(len()) de 'item' for igual a 3 faça isso:
                pagamento = Pagamento(lista[n][0], lista[n][1], lista[n][2])         #Variável "pagamento" recebe a classe "Pagamento" com o primeiro, segundo e terceiro itens
                                                                                     # de cada Lista(item) passados como parâmetro
                self._transacoes.append(pagamento)                                   #Adiciona "pagamento" a Lista "transacoes"
                # print(n)
                n = n + 1

            else:                                                                    #Se não, faça isso:
                gasto = Gasto(lista[n][0], lista[n][1], lista[n][2], lista[n][3])    #Variável "gasto" recebe a classe "Gasto" com primeiro, segundo, terceiro e quarto itens
                                                                                     # de cada Lista(item) passados como parâmetro
                self._transacoes.append(gasto)                                       #Adiciona "gasto" a Lista "transacoes"
                # print(n)
                n = n + 1

    @property                                                  #
    def lista(self):                                           #Cria o método "lista"
        return self._transacoes                                #Retorna a Lista "transacoes"

    @property
    def extrato(self):
        return self._extrato

    def mostraTransacoesPorData(self, data):                   #Cria o método "mostraTransacoesPorData" e recebe "data" como parâmetro
        linha = 0
        existe = 0
        transacoesPorData = []                                 #Variável "transacoesPorData" recebe uma Lista vazia

        for line in self._transacoes:                          #Para cada "line"(cada item) em "transacoes"
            if line.data == data:                              #Se
                transacoesPorData.append(line)                 #
                linha = linha + 1
                existe = 1

            else:                                              #Se não faça isso:
                linha = linha + 1

        if existe == 0:                                        #Se a variável "existe" for igual a 0, faça isso:
            return 'data inválida'                             #Retorna a String("data inválida")

        else:                                                  #Se não, faça isso:
            return transacoesPorData                           #Retorna a variável "transacoesPorData"

    def mostraExtrato(self):                                   #Cria o método "MostraExtrato"
        for line in self._transacoes:                          #Para cada line(cada item)
            print(line)                                        #

    def valorTransacoesTotal(self):                            #Cria o método "valorTransacoesTotal"
        soma = 0
        for line in self._transacoes:
            soma = soma + float(line.valor)

        return round(soma, 2)

    def valorTransacoesPorCategoria(self, categoria):         #Cria o método "valorTransacoesPorCategoria" e recebe "categoria" como parâmetro
        soma = 0

        for line in self._transacoes:                         #Para cada line(cada item) na Lista "transacoes"
            #print(type(line))
            if type(line) is Gasto:
                #print('true')
                if line.categoria == categoria:                   #Se .................
                    soma = soma + float(line.valor)               #..................

        return round(soma, 2)                                 #Retorna "soma" com dois dígitos depois da vírgula

    def quantidadeTransacoes(self):                           #Cria o método "quantidadaTransacoes"
        return len(self._transacoes)                          #Retorna a quatidade de itens(len()) em "transacoes"

    def __str__(self):
        return self._extrato

############################ Teste ################################

boleto = 'nubank-2019-07.csv'
teste = Boleto(boleto)
print(teste)

for item in teste.lista:
    print(item)

#data = '2019-07-02'
#print(teste.mostraTransacoesPorData(data))

#teste.mostraExtrato()

#print(teste.valorTransacoesTotal())

#categoria = 'restaurante'
#print(teste.valorTransacoesPorCategoria(categoria))

#print(teste.quantidadeTransacoes())

