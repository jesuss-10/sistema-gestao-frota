class Veiculo:
    """Classe base dos veículos da frota."""

    def __init__(self, modelo, placa, valor_diaria):
        # O construtor usa os setters para validar os dados.
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    # Getters: permitem consultar os atributos privados.
    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    # Setters: validam os dados antes de guardá-los.
    def set_modelo(self, modelo):
        if isinstance(modelo, str) and len(modelo.strip()) >= 3:
            self.__modelo = modelo.strip()
        else:
            raise ValueError("O modelo deve ter pelo menos 3 caracteres.")

    def set_placa(self, placa):
        if isinstance(placa, str) and len(placa.strip()) >= 7:
            self.__placa = placa.strip().upper()
        else:
            raise ValueError("A placa deve ter pelo menos 7 caracteres.")

    def set_valor_diaria(self, valor):
        if (
            isinstance(valor, (int, float))
            and not isinstance(valor, bool)
            and valor > 0
        ):
            self.__valor_diaria = float(valor)
        else:
            raise ValueError("O valor da diária deve ser maior que zero.")

    def calcular_aluguel(self, dias):
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("A quantidade de dias deve ser um inteiro maior que zero.")
        return self.__valor_diaria * dias


# Testes da classe base (executados somente ao abrir este arquivo diretamente).
if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    objeto_valido = Veiculo("Toyota Corolla", "ABC1234", 180.00)
    print(
        f"Objeto criado: {objeto_valido.get_modelo()} - "
        f"R$ {objeto_valido.get_valor_diaria():.2f}"
    )

    print("\n--- Teste 1: tentativa de diária negativa ---")
    try:
        Veiculo("Honda Civic", "DEF5678", -150.00)
    except ValueError as erro:
        print(f"Validação funcionando: {erro}")

    print("\n--- Teste 2: tentativa de modelo muito curto ---")
    try:
        objeto_valido.set_modelo("AB")
    except ValueError as erro:
        print(f"Validação funcionando: {erro}")
    print(f"Modelo continua protegido: {objeto_valido.get_modelo()}")
