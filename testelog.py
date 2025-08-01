def main():
    # Entrada de dados do utilizador
    # A entrada 'true' ou 'false' é convertida para um booleano.
    # A idade é convertida para um número inteiro.
    has_permission = input().lower() == "true"
    age = int(input())

    # Verifique condições de acesso
    # A primeira condição verifica se o visitante tem permissão E tem 18 anos ou mais.
    if has_permission and age >= 18:
        print("Acesso permitido")
    # A segunda condição verifica se o visitante não tem permissão.
    elif not has_permission:
        print("Acesso negado")
    # A última condição é executada se as anteriores forem falsas,
    # ou seja, o visitante tem permissão, mas a idade é insuficiente.
    else:
        print("Idade insuficiente")


if __name__ == "__main__":
    main()
