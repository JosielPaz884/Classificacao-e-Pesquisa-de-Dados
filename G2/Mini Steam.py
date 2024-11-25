class Game:
    def __init__(self, jogoId, titulo, desenvolvedor, preco, generos):
        self.jogoId = jogoId
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  

class NodeGame:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None

class TreeGame:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        if self.raiz is None:
            self.raiz = NodeGame(jogo)
        else:
            no_atual = self.raiz
            while True:
                if jogo.preco < no_atual.jogo.preco:
                    if no_atual.esquerda is None:
                        no_atual.esquerda = NodeGame(jogo)
                        break
                    else:
                        no_atual = no_atual.esquerda
                else:
                    if no_atual.direita is None:
                        no_atual.direita = NodeGame(jogo)
                        break
                    else:
                        no_atual = no_atual.direita       

    def buscaPorPreco(self, preco):
        no_atual = self.raiz  
        while no_atual is not None:
            if no_atual.jogo.preco == preco:
                return no_atual.jogo  
            elif preco < no_atual.jogo.preco:
                no_atual = no_atual.esquerda  
            else:
                no_atual = no_atual.direita  
        return None  
    
    def buscaPorFaixaPreco(self, precoMinimo, precoMaximo):
        resultados = []
        self._buscaPorFaixaPreco(self.raiz, precoMinimo, precoMaximo, resultados)
        return resultados

    def _buscaPorFaixaPreco(self, no_atual, precoMinimo, precoMaximo, resultados):
        if no_atual is None:
            return
        
        if precoMinimo <= no_atual.jogo.preco <= precoMaximo:
            resultados.append(no_atual.jogo)

        if no_atual.jogo.preco > precoMinimo:
            self._buscaPorFaixaPreco(no_atual.esquerda, precoMinimo, precoMaximo, resultados)

        if no_atual.jogo.preco < precoMaximo:
            self._buscaPorFaixaPreco(no_atual.direita, precoMinimo, precoMaximo, resultados)

    def listarJogos(self):
        jogos = []
        self._listarJogosLoop(self.raiz, jogos)
        return jogos
    
    def _listarJogosLoop(self, nodeAtual, jogos):
        if nodeAtual is not None:
            self._listarJogosLoop(nodeAtual.esquerda, jogos)
            jogos.append(nodeAtual.jogo)
            self._listarJogosLoop(nodeAtual.direita, jogos)

class HashGenero:
    def __init__(self):
        self.generoParaJogos = {}

    def adicionarJogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.generoParaJogos:
                self.generoParaJogos[genero] = []
            self.generoParaJogos[genero].append(jogo)  # Armazenar o objeto de jogo, não só o ID

    def obterJogo(self, genero):
        return self.generoParaJogos.get(genero, [])

    # Ajuste na função buscarJogoPorGenero
    def buscarJogoPorGenero(self, genero):
        jogos_encontrados = self.generos.obterJogo(genero)
        jogos_info = []

        for jogo in jogos_encontrados:
            jogos_info.append({
                'id': jogo.jogoId,
                'nome': jogo.titulo,
                'genero': genero
            })
        
        return jogos_info

class MotorSearchGame:
    def __init__(self):
        self.catalogoJogos = TreeGame()
        self.generos = HashGenero()

    def adicionarJogo(self, jogo):
        self.catalogoJogos.inserir(jogo)
        self.generos.adicionarJogo(jogo)

    def buscarJogoPorPreco(self, preco):
        return self.catalogoJogos.buscaPorPreco(preco)

    def buscarJogoPorFaixaPreco(self, precoMinimo, precoMaximo):
        return self.catalogoJogos.buscaPorFaixaPreco(precoMinimo, precoMaximo)
    
    def buscarJogoPorId(self, jogoId):
        return self._buscarJogoPorId(self.catalogoJogos.raiz, jogoId)

    def _buscarJogoPorId(self, no_atual, jogoId):
        if no_atual is None:
            return None
        
        if no_atual.jogo.jogoId == jogoId:
            return no_atual.jogo
        elif jogoId < no_atual.jogo.jogoId:
            return self._buscarJogoPorId(no_atual.esquerda, jogoId)
        else:
            return self._buscarJogoPorId(no_atual.direita, jogoId)

    def buscarJogoPorGenero(self, genero):
        jogos_encontrados = self.generos.obterJogo(genero)
        jogos_info = []

        for jogo in jogos_encontrados:
            jogos_info.append({
                'id': jogo.jogoId,
                'nome': jogo.titulo,
                'genero': genero
            })
        
        return jogos_info

    def listarJogos(self):
        jogos = self.catalogoJogos.listarJogos()
        if jogos:
            print("Lista de todos os jogos:")
            for jogo in jogos:
                print(f"ID: {jogo.jogoId}, Título: {jogo.titulo}, Desenvolvedor: {jogo.desenvolvedor}, Preço: R$ {jogo.preco}, Gêneros: {', '.join(jogo.generos)}")
        else:
            print("Não há jogos no catálogo.")

def main():
    jogo1 = Game(1, "The Legend of Zelda: Tears of the Kingdom", "Nintendo", 349.90, ["Ação", "Aventura", "RPG"])
    jogo2 = Game(2, "God of War: Ragnarök", "Santa Monica Studio", 150, ["Ação", "Aventura"])
    jogo3 = Game(3, "Hogwarts Legacy", "Avalanche Software", 299.90, ["RPG", "Mundo Aberto", "Aventura"])
    jogo4 = Game(4, "Elden Ring", "FromSoftware", 249.90, ["RPG", "Ação", "Fantasia"])
    jogo5 = Game(5, "Grand Theft Auto V", "Rockstar Games", 99.90, ["Ação","Mundo Aberto", "Aventura"])
    jogo6 = Game(6, "Minecraft", "Mojang Studios", 149.90, ["SandBox", "Sobrevivência"])
    jogo7 = Game(7, "Fortnite","Epic Games", 0.00, ["Ação", "Aventura", "Battle Royale"])
    jogo8 = Game(8, "The Witcher 3: Wild Hunt", "CD Projekt", 299.90, ["RPG", "Mundo Aberto", "Aventura", "Fantasia", "Ação"])
    jogo9 = Game(9, "Cyberpunk 2077", "CD Projekt",249.90, ["RPG","Mundo Aberto", "Ação", "Futuristic"])
    jogo10 = Game(10, "Stardew Valley", "RConcernedApe", 37.99, ["Simulação","RPG", "Indie"])


    motorBusca = MotorSearchGame()

    motorBusca.adicionarJogo(jogo1)
    motorBusca.adicionarJogo(jogo2)
    motorBusca.adicionarJogo(jogo3)
    motorBusca.adicionarJogo(jogo4)
    motorBusca.adicionarJogo(jogo5)
    motorBusca.adicionarJogo(jogo6)
    motorBusca.adicionarJogo(jogo7)
    motorBusca.adicionarJogo(jogo8)
    motorBusca.adicionarJogo(jogo9)
    motorBusca.adicionarJogo(jogo10)

    while True:
        print("\n--- Menu ---")
        print("1. Listar todos os jogos")
        print("2. Buscar jogo por preço")
        print("3. Buscar jogos por faixa de preço")
        print("4. Buscar jogos por gênero")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            motorBusca.listarJogos() 

        elif opcao == '2':
            preco = float(input("Digite o preço do jogo que deseja buscar: "))
            jogo = motorBusca.buscarJogoPorPreco(preco)
            if jogo is not None:  # Check if jogo is not None
                print(f"Jogo encontrado: ID {jogo.jogoId}, Título {jogo.titulo}, Preço: R$ {jogo.preco}")
            else: 
                print("Jogo não encontrado!")

        elif opcao == '3':
            precoMinimo = float(input("Digite o preço mínimo: "))
            precoMaximo = float(input("Digite o preço máximo: "))
            jogos = motorBusca.buscarJogoPorFaixaPreco(precoMinimo, precoMaximo)
            if jogos:
                print("Lista de jogos encontrados:")
                for jogo in jogos:
                    print(f"ID: {jogo.jogoId}, Título: {jogo.titulo}, Preço: R$ {jogo.preco}")
            else:
                print("Não há jogos na faixa de preço selecionada.")

        elif opcao == '4':
            genero = input("Digite o gênero do jogo: ")
            jogos = motorBusca.buscarJogoPorGenero(genero)
            if jogos: 
                print("Lista de jogos encontrados:")
                for jogo in jogos:
                    print(f"ID: {jogo['id']}, Nome: {jogo['nome']}, Gênero: {jogo['genero']}")
            else: 
                print("Não há jogos com o gênero selecionado.")
        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
