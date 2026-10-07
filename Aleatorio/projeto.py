class AtributosPessoas(object):

#essa coisa é uma classificação dentro de uma instancia, por isso __init__
#o parametro self é essencial para se ter a noção de uma varieavel com atributos
    
    def __init__(self, altura, mbti, raça, idade):
        self.altura= altura
        self.mbti= mbti
        self.raça= raça
        self.idade= idade

#é para organizar um retorno em altura e idade     
    def altura_idade(self):
        return "{} cm, {} anos".format(self.altura, self.idade)

class Universidade(object):
    pass
class Exatas(Universidade):
    def pressao(self):
        SocialLife=[]
        if self == "burro":
            SocialLife.append("depressão")
            return SocialLife
class Engenharia(Exatas):
    def energia(self):
        return "Sou viciado em cafeina"
class Civil(Engenharia):
    pass
        





pessoa1= AtributosPessoas("176","infp","amarelo","17")
pessoa2= Civil()
print(pessoa2.energia())