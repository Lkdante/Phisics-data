class LivrosManeiro(object):
    
    #Analise que possui 3 parametros, o primeiro é para simplesmente reconhecer a string que tu usou
    
    # o segundo e o terceiro são parametos da função, lembre se do conceito de função :D
    def __init__(self, nome, data):
        self.data= data
        self.nome= nome 
    
    
    
    #Essa uma função que pega a string que vc classificou nessa classe e lança um retorno q depende da função de cima, e claramente de seus parametros
        
    def __str__(self):
        return "Esse livro se chama " + self.nome + " e foi lançado em " + self.data


#Aqui definimos a string "livro1" como a classe LivrosManeiro, e colocamos os paramentros para ser usada na função da classe em si
    
livro1=LivrosManeiro("O inferno de Dante","1478")
print(livro1)