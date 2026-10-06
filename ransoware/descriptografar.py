from cryptography.fernet import Fernet
import os

#1 - Carregar a chave salva

def carregarChave():
    return open("chave.key", "rb").read()

#2 - Descriptografar um único arquivo

def descriptografarArquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dadosDescriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dadosDescriptografados)

#3 - Encontrar arquivos para descriptografar

def encontrarArquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#4 - Execução principal

def main():
    chave = carregarChave()
    arquivos = encontrarArquivos("testFiles")
    for arquivo in arquivos:
        descriptografarArquivo(arquivo, chave)
    print("Arquivos restaurados com sucesso!")

if __name__=="__main__":
    main()    