'''
Nome: Caio Mendes Coutinho e Garcia
Matricula: 2024007305
Data: 26/03/2025
'''
import numpy as np
import sys

# Cria a matriz a partir da leitura dos dados do dataset (utiliza a funcao loadtxt da biblioteca numpy)
# Em caso de sucesso, a funcao retorna uma ndarray, a depender das caracteristicas dos dados
# Caso algum erro aconteça, None sera retornado 
def criaMatriz(filename):
    try:
        return np.loadtxt(f"{filename}.txt")
    except FileNotFoundError:
        print("Arquivo nao encontrado")
        return None
    except ValueError as e:
        print(f"Erro encontrado: {e}")
        return None

# Salva o resultado da criaçao da matriz em um arquivo .txt, indicando qual foi o dataset e as dimensoes da ndarray criada
# Em caso de sucesso, a funcao cria/modifica o arquivo corretamente
# Caso algum erro aconteça, o usuario sera notificado  
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

# Verifica se o script esta sendo executado diretamente como script ou como modulo em um externo
if __name__ == '__main__':
    main(sys.argv[1])
