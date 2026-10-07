def transpor_vetor(vetor):
    vetor = vetor.replace(',','.')
    vetor= vetor.split()
    vetor=[float(x) for x in vetor]
    return vetor

def main():
    Excelinput= input("manda a coluna do excel para nois:")
    print(transpor_vetor(Excelinput))
if __name__ == "__main__":
    main()