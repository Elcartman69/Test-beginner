def conversor():
    tabelas = {
        '1': ('Comprimento', {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001}),
        '2': ('Massa', {'kg': 1, 'g': 0.001, 'lb': 0.453592, 'oz': 0.0283495}),
        '3': ('Temperatura', None)
    }
    to_c = {'c': lambda x: x, 'f': lambda x: (x-32)*5/9, 'k': lambda x: x-273.15}
    from_c = {'c': lambda x: x, 'f': lambda x: x*9/5+32, 'k': lambda x: x+273.15}

    while True:
        print("\n1.Comprimento\n2.Massa\n3.Temperatura\n4.Sair")
        op = input("Escolha: ")
        if op == '4': break
        if op not in tabelas: print("Inválido."); continue

        nome, fatores = tabelas[op]
        print(f"\n{nome}:", ', '.join(fatores.keys()) if fatores else "c, f, k")
        de, para = input("De: ").lower(), input("Para: ").lower()
        try: val = float(input(f"Valor em {de}: "))
        except: print("Entrada inválida."); continue

        try:
            if fatores:  # conversão genérica
                res = val * fatores[de] / fatores[para]
            else:        # temperatura
                res = from_c[para](to_c[de](val))
            print(f"{val} {de} = {res} {para}")
        except: print("Unidade inválida.")

if __name__ == "__main__":
    conversor()