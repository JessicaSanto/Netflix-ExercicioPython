class Cliente:
    def __init__(self, nome, email, plano):
        # função init -> vai iniciar a classe (TODAS AS CLASSES VÃO TER UMA FUNÇÃO INIT)
        # qualquer variavel que for criada utilizando o sel
        # self -> Referencia a própria classe, ao criarmos os objetos, chamaremos pelo self ao inves de chamar pelo nome da classe
        # self só será usando dentro da criação da CLASSE, não será usado no objeto
        self.nome = nome
        # self.nome e nome são diferentes. O self.raca se trata da característica que queremos e o raca trata da variavel em que será armazeado o valor inputado
        self.email = email
        # self.plano = plano #TIRAR APÓS CRIAR A LISTA
        #Limitar os planos para impedir que o usuário entre com dados aleatórios
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print("Plano Inválido") #TIRAR APÓS CRIAR A LISTA
            #Para evitar que ele crie mesmo com o plano estando invalido
            # raise Exception("Plano Invalido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido")

cliente1 = Cliente("Jéssica", "jessica@email.com", "basic")
print(cliente1.nome)

print(cliente1.plano)
#mudar de plano
cliente1.mudar_plano("premium")
print(cliente1.plano)