from projeto import AtributosPessoas

x= AtributosPessoas("190","Enfp","Negro","23")
ErroP=[x/x for x in range(1,10)]
ErroT=[x/(2*x) for x in range(1,11)]
print(ErroT)