import numpy as np
import sys

def criaMatriz(filename):
    try:
        return np.loadtxt(f"{filename}.txt")
    except FileNotFoundError:
        print("Arquivo nao encontrado")
        return None
    except ValueError as e:
        print(f"Erro encontrado: {e}")
        return None
    
def salvarResultado(filename, lin, col):
    try:
        arq = open('resultado.txt', 'a+')
        resultado = f"{filename}.txt {lin} {col}\n"
        arq.writelines(resultado)
        arq.close()
    except:
        print("Erro ao ler o arquivo")

def main(filename):
    m = criaMatriz(filename)
    print(m)
    print(type(m))
    if m is None:
        return
    l, c = m.shape
    salvarResultado(filename, l, c)

if __name__ == '__main__':
    main(sys.argv[1])