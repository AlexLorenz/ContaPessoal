class Gasto:                                                     #Cria a classe "Gasto"
    def __init__(self, data, categoria, referencia, valor):      #Cria o método construtor que recebe como parâmetro data, categoria, referencia, valor
        self._data = data                                        #Variável "data" recebe o parâmetro "data"
        self._categoria = categoria                              #Variável "categoria" recebe o parâmetro "categoria"
        self._referencia = referencia                            #Variável "referencia" recebe o parâmetro "referencia"
        self._valor = valor                                      #Variável "valor" recebe o parâmetro "valor"

    @property                                                    #
    def data(self):                                              #Cria o método "data"
        return self._data                                        #Retorna a variável "data"

    @property                                                    #
    def categoria(self):                                         #Cria o método "categoria"
        return (str(self._categoria)).capitalize()               #Retorna a variável "categoria" com a primeira letra maiuscula

    @property                                                    #
    def referencia(self):                                        #Cria o método "referencia"
        return self._referencia                                  #Retorna a variável "referencia"

    @property                                                    #
    def valor(self):                                             #Cria o método "valor"
        return self._valor

    def __str__(self):                                           #Chama o metodo builtin "__str__" que retorna algo quando a classe é chamada
        return self._data + ' | ' \
             + self._categoria + ' | ' \
             + self._referencia + ' | ' \
             + self._valor

################### Teste ########################

#data = '2019-07-02'
#categoria = 'restaurante'
#referencia = 'Letras&Sabores'
#valor = '15.00'

#teste = Gasto(data, categoria, referencia, valor)
#print(teste)

#print(teste.data)
#print(teste.categoria)
#print(teste.referencia)
#print(teste.valor)