class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __repr__(self):
        return f"Arquivo(nome='{self.nome}', caminho='{self.caminho}', tamanho={self.tamanho} KB)"


class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, nome):
        return hash(nome) % self.tamanho

    def adicionar(self, arquivo):
        indice = self._hash(arquivo.nome)
        for arq in self.tabela[indice]:
            if arq.nome == arquivo.nome:
                print(f"O arquivo '{arquivo.nome}' já existe na tabela.")
                return
        self.tabela[indice].append(arquivo)
        print(f"Arquivo '{arquivo.nome}' adicionado com sucesso.")

    def buscar(self, nome):
        indice = self._hash(nome)
        for arq in self.tabela[indice]:
            if arq.nome == nome:
                return arq
        return None

    def remover(self, nome):
        indice = self._hash(nome)
        for i, arq in enumerate(self.tabela[indice]):
            if arq.nome == nome:
                del self.tabela[indice][i]
                print(f"Arquivo '{nome}' removido com sucesso.")
                return
        print(f"Arquivo '{nome}' não encontrado.")

    def listar(self):
        arquivos = []
        for lista in self.tabela:
            arquivos.extend(lista)
        return arquivos

    def atualizar(self, nome, novo_caminho=None, novo_tamanho=None):
        arquivo = self.buscar(nome)
        if arquivo:
            if novoCaminho:
                arquivo.caminho = novoCaminho
            if novoTamanho is not None:
                arquivo.tamanho = novoTamanho
            print(f"Arquivo '{nome}' atualizado com sucesso.")
        else:
            print(f"Arquivo '{nome}' não encontrado para atualização.")

    def estaVazia(self):
        return all(len(lista) == 0 for lista in self.tabela)


def main():
    tabela = TabelaHash()
    tabela.adicionar(Arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 1024))
    tabela.adicionar(Arquivo("foto.jpg", "/imagens/foto.jpg", 2048))
    tabela.adicionar(Arquivo("dados.csv", "/planilhas/dados.csv", 512))
    tabela.adicionar(Arquivo("backup.zip", "/backup/backup.zip", 4096))
    arquivoBusca = tabela.buscar("dados.csv")
    print(f"Arquivo encontrado: {arquivo_busca}")
    tabela.atualizar("dados.csv", novoCaminho="/planilhas/dados_atualizados.csv", novoTamanho=600)
    tabela.remover("foto.jpg")
    arquivosRestantes = tabela.listar()
    print("Arquivos restantes na tabela:")
    for arq in arquivosRestantes:
        print(arq)

    if tabela.estaVazia():
        print("A tabela hash está vazia.")
    else:
        print("A tabela hash não está vazia.")


if __name__ == "__main__":
    main()
