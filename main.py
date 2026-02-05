class OrcamentoAluguel:
    def __init__(self, aluguel, agua, luz, internet):
        self.aluguel = aluguel
        self.agua = agua
        self.luz = luz
        self.internet = internet

    def calcular_total(self):
        return self.aluguel + self.agua + self.luz + self.internet


def main():
    print("=== Cálculo de Orçamento de Aluguel Mensal ===")

    aluguel = float(input("Informe o valor do aluguel: "))
    agua = float(input("Informe o valor da água: "))
    luz = float(input("Informe o valor da luz: "))
    internet = float(input("Informe o valor da internet: "))

    orcamento = OrcamentoAluguel(aluguel, agua, luz, internet)
    total = orcamento.calcular_total()

    print(f"Valor total do orçamento mensal: R$ {total:.2f}")


if __name__ == "__main__":
    main()
