class Teatro:
    def _init_(self, linhas, colunas, valor_ingresso):
        self.linhas = linhas
        self.colunas = colunas
        self.valor_ingresso = valor_ingresso
        self.total_cadeiras = linhas * colunas
        self.cadeiras = [['Livre' for _ in range(colunas)] for _ in range(linhas)]
        self.vendas = 0
        self.reservas = 0

    def iniciar_teatro(self):
        if self.vendas == 0 and self.reservas == 0:
            print("Teatro iniciado.")
        else:
            print("Não é possível iniciar o teatro enquanto houver espetáculo em andamento.")

    def reservar_lugar(self, linha, coluna):
        if self.cadeiras[linha][coluna] == 'Livre':
            self.cadeiras[linha][coluna] = 'Reservado'
            self.reservas += 1
            print("Lugar reservado com sucesso!")
        else:
            print("Este lugar já está reservado. Por favor, escolha outro.")

    def comprar_lugar(self, linha, coluna):
        if self.cadeiras[linha][coluna] == 'Livre':
            self.cadeiras[linha][coluna] = 'Vendido'
            self.vendas += 1
            print("Lugar comprado com sucesso!")
        elif self.cadeiras[linha][coluna] == 'Reservado':
            self.cadeiras[linha][coluna] = 'Vendido'
            self.reservas -= 1
            self.vendas += 1
            print("Lugar comprado com sucesso!")
        else:
            print("Este lugar já está ocupado.")

    def liberar_lugar(self, linha, coluna):
        if self.cadeiras[linha][coluna] == 'Reservado':
            self.cadeiras[linha][coluna] = 'Livre'
            self.reservas -= 1
            print("Reserva liberada com sucesso!")
        elif self.cadeiras[linha][coluna] == 'Vendido':
            self.cadeiras[linha][coluna] = 'Livre'
            self.vendas -= 1
            print("Venda liberada com sucesso!")
        else:
            print("Este lugar já está livre.")

    def listar_poltronas(self):
        total_livres = sum(row.count('Livre') for row in self.cadeiras)
        total_reservadas = sum(row.count('Reservado') for row in self.cadeiras)
        total_vendidas = sum(row.count('Vendido') for row in self.cadeiras)
        print(f"Total Geral de Cadeiras: {self.total_cadeiras}")
        print(f"Total de Cadeiras Vazias: {total_livres}")
        print(f"Total de Cadeiras Reservadas: {total_reservadas}")
        print(f"Total de Cadeiras Vendidas: {total_vendidas}")
        print(f"Total do Espetáculo em R$: {self.vendas * self.valor_ingresso:.2f}")
        print(f"Total não recebido em R$: {self.reservas * self.valor_ingresso * 0.3:.2f}")
        print(f"Total em reservas R$: {self.reservas * self.valor_ingresso * 0.7:.2f}")

    def encerrar_espetaculo(self):
        ocupacao_total = self.vendas + self.reservas
        if ocupacao_total >= 0.6 * self.total_cadeiras:
            print("Espetáculo encerrado.")
            self.listar_poltronas()
            self.reiniciar_espetaculo()
        else:
            print("Não é possível encerrar o espetáculo, ocupação mínima não atingida.")

    def reiniciar_espetaculo(self):
        self.cadeiras = [['Livre' for _ in range(self.colunas)] for _ in range(self.linhas)]
        self.vendas = 0
        self.reservas = 0
        print("Espetáculo reiniciado.")


def menu():
    print("=== Menu ===")
    print("[1] - Iniciar o teatro")
    print("[2] - Reservar lugar")
    print("[3] - Comprar lugar")
    print("[4] - Liberar lugar")
    print("[5] - Listar poltronas")
    print("[6] - Encerrar o espetáculo")
    print("[7] - Reiniciar o espetáculo")
    print("[0] - Sair")


def main():
    linhas = int(input("Informe o número de linhas do teatro: "))
    colunas = int(input("Informe o número de colunas do teatro: "))
    valor_ingresso = float(input("Informe o valor do ingresso: "))

    teatro = Teatro(linhas, colunas, valor_ingresso)

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            teatro.iniciar_teatro()
        elif opcao == 2:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            teatro.reservar_lugar(linha, coluna)
        elif opcao == 3:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            teatro.comprar_lugar(linha, coluna)
        elif opcao == 4:
            linha = int(input("Informe a linha: "))
            coluna = int(input("Informe a coluna: "))
            teatro.liberar_lugar(linha, coluna)
        elif opcao == 5:
            teatro.listar_poltronas()
        elif opcao == 6:
            teatro.encerrar_espetaculo()
        elif opcao == 7:
            teatro.reiniciar_espetaculo()
        elif opcao == 0:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if _name_ == "_main_":
    main()