class Pagamento:                               #Cria a Classe "Pagamento"
    def __init__(self, data, nome, valor):     #Cria o método construtor passando como parâmetro a data, nome e valor
        self._data = data                      #
        self._categoria = nome                      #
        self._referencia = 'fatura'
        self._valor = valor                    #

    @property                                  #
    def data(self):                            #Cria o método "data"
        return self._data                      #Retorna a variável "data"

    @property                                  #
    def categoria(self):                            #Cria o método "nome"
        return self._categoria                      #Retorna a variável "nome"

    @property
    def referencia(self):
        return self._referencia

    @property                                  #
    def valor(self):                           #Cria o método "valor"
        return self._valor                     #Retorna a variável "valor"

    def __str__(self):
        return self._data + ' | ' + self._categoria + ' | ' + self._referencia + ' | ' + str(self._valor)

###################### Teste ########################
'''
data = '2019-06-02'
nome = 'null'
valor = '100.00'

teste = Pagamento(data, nome, valor)

print(teste.data)
print(teste.nome)
print(teste.valor)
'''
