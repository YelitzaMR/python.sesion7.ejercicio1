import Calculadora

def main():
    numSuma=Calculadora.suma(6, 2)
    print('La suma es', numSuma)

    numResta=Calculadora.resta(6,2)
    print('La resta es',numResta)

    numMulti=Calculadora.multiplica(6, 2)
    print('La multiplicación', numMulti)

    numDivi=Calculadora.dividir(6, 2)
    print('La división es', numDivi)
    
if __name__== '__main__':
        main()