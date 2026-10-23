from modelos_base import Veiculo


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)

        if not isinstance(portas, int) or isinstance(portas, bool) or portas <= 0:
            raise ValueError("A quantidade de portas deve ser um inteiro maior que zero.")

        self.portas = portas

    # Carro possui taxa fixa de limpeza de R$ 50.
    def calcular_aluguel(self, dias):
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("A quantidade de dias deve ser um inteiro maior que zero.")
        return self.get_valor_diaria() * dias + 50


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)

        if (
            not isinstance(cilindradas, int)
            or isinstance(cilindradas, bool)
            or cilindradas <= 0
        ):
            raise ValueError("As cilindradas devem ser um inteiro maior que zero.")

        self.cilindradas = cilindradas

    # Moto possui desconto de 10%.
    def calcular_aluguel(self, dias):
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("A quantidade de dias deve ser um inteiro maior que zero.")
        return self.get_valor_diaria() * dias * 0.90


# Lista centralizada com objetos Carro e Moto.
frota = []


def main():
    while True:
        try:
            print("\n===== SISTEMA DE GESTÃO DE FROTA =====")
            print("1 - Cadastrar carro")
            print("2 - Cadastrar moto")
            print("3 - Listar veículos")
            print("4 - Calcular aluguel")
            print("0 - Sair")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                print("\n--- CADASTRO DE CARRO ---")
                modelo = input("Modelo do carro: ")
                placa = input("Placa: ")
                valor = float(input("Valor da diária: R$ "))
                portas = int(input("Quantidade de portas: "))

                carro = Carro(modelo, placa, valor, portas)
                frota.append(carro)
                print("\nCarro cadastrado com sucesso!")

            elif opcao == 2:
                print("\n--- CADASTRO DE MOTO ---")
                modelo = input("Modelo da moto: ")
                placa = input("Placa: ")
                valor = float(input("Valor da diária: R$ "))
                cilindradas = int(input("Cilindradas: "))

                moto = Moto(modelo, placa, valor, cilindradas)
                frota.append(moto)
                print("\nMoto cadastrada com sucesso!")

            elif opcao == 3:
                print("\n===== VEÍCULOS CADASTRADOS =====")
                if not frota:
                    print("Nenhum veículo cadastrado.")
                else:
                    for i, veiculo in enumerate(frota, start=1):
                        print("\n-------------------------")
                        print(f"Veículo: {i}")
                        print(f"Tipo: {type(veiculo).__name__}")
                        print(f"Modelo: {veiculo.get_modelo()}")
                        print(f"Placa: {veiculo.get_placa()}")
                        print(f"Valor da diária: R$ {veiculo.get_valor_diaria():.2f}")

                        if isinstance(veiculo, Carro):
                            print(f"Portas: {veiculo.portas}")
                        elif isinstance(veiculo, Moto):
                            print(f"Cilindradas: {veiculo.cilindradas} cc")

            elif opcao == 4:
                if not frota:
                    print("\nNenhum veículo cadastrado. Cadastre um veículo primeiro.")
                    continue

                dias = int(input("Digite a quantidade de dias do aluguel: "))
                if dias <= 0:
                    raise ValueError("A quantidade de dias deve ser maior que zero.")

                print("\n===== VALORES DOS ALUGUÉIS =====")
                for veiculo in frota:
                    valor_total = veiculo.calcular_aluguel(dias)
                    print("\n-------------------------")
                    print(f"Tipo: {type(veiculo).__name__}")
                    print(f"Modelo: {veiculo.get_modelo()}")
                    print(f"Placa: {veiculo.get_placa()}")
                    print(f"Dias: {dias}")
                    print(f"Valor total: R$ {valor_total:.2f}")

            elif opcao == 0:
                print("\nSistema encerrado.")
                break

            else:
                print("\nOpção inexistente. Escolha uma opção válida.")

        except ValueError as erro:
            print("\nERRO:", erro)
            print("Confira os dados digitados e tente novamente.")

        except Exception as erro:
            print("\nOcorreu um erro inesperado:", erro)

        finally:
            print("--------------------------------")


if __name__ == "__main__":
    main()
