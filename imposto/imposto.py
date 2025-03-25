def calcular_impostos(preco_produto, taxa_iva, taxa_ir):
    # Cálculo do Imposto IVA
    imposto_iva = (preco_produto * taxa_iva) / 100

    # Cálculo do Imposto de Renda (IR)
    imposto_ir = (preco_produto * taxa_ir) / 100

    # Cálculo do valor final após impostos
    total_com_impostos = preco_produto + imposto_iva + imposto_ir

    return imposto_iva, imposto_ir, total_com_impostos

def obter_entrada(prompt):
    while True:
        try:
            # Tenta converter a entrada para um número flutuante
            return float(input(prompt))
        except ValueError:
            # Se não for possível, exibe uma mensagem de erro
            print("Erro: Por favor, insira um número válido.")

def main():
    while True:  # Loop para permitir cálculos contínuos
        print("Bem-vindo ao sistema de cálculo de impostos!")

        # Solicitar os dados ao usuário com validação de preço
        while True:
            preco_produto = obter_entrada("Digite o preço do produto/serviço (R$): ")
            if preco_produto <= 0:
                print("Erro: O preço do produto deve ser um valor positivo. Tente novamente.")
            else:
                break

        # Solicitar a taxa de IVA com validação
        while True:
            taxa_iva = obter_entrada("Digite a taxa de IVA (%): ")
            if taxa_iva < 0:
                print("Erro: A taxa de IVA não pode ser negativa. Tente novamente.")
            else:
                break

        # Solicitar a taxa de Imposto de Renda com validação
        while True:
            taxa_ir = obter_entrada("Digite a taxa de Imposto de Renda (%): ")
            if taxa_ir < 0:
                print("Erro: A taxa de Imposto de Renda não pode ser negativa. Tente novamente.")
            else:
                break

        # Calcular os impostos
        imposto_iva, imposto_ir, total_com_impostos = calcular_impostos(preco_produto, taxa_iva, taxa_ir)
        
        # Exibir os resultados
        print("\nResultado do cálculo:")
        print(f"Imposto IVA: R$ {imposto_iva:.2f}")
        print(f"Imposto de Renda: R$ {imposto_ir:.2f}")
        print(f"Total após impostos: R$ {total_com_impostos:.2f}")

        # Perguntar se o usuário quer realizar outro cálculo
        continuar = input("\nVocê deseja calcular novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por usar o sistema de cálculos de impostos!")
            break  # Sai do loop e encerra o programa

if __name__ == "__main__":
    main()
