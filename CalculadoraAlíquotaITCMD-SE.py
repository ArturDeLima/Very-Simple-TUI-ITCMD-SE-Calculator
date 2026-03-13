def data_para_int(data_str):
    """Converte DD/MM/AAAA para um inteiro AAAAMMDD para comparação fácil."""
    partes = data_str.split('/')
    if len(partes) != 3:
        return None
    # Preenche com zeros à esquerda se necessário e inverte para AAAAMMDD
    dia = partes[0].zfill(2)
    mes = partes[1].zfill(2)
    ano = partes[2]
    return int(ano + mes + dia)

def calcular_itcmd():
    print("--- Calculadora de ITCMD Sergipe ---")
    
    # Entradas do usuário
    data_input = input("Qual a data do fato gerador (DD/MM/AAAA)? ")
    data_fato = data_para_int(data_input)
    
    if data_fato is None:
        print("Erro: Formato de data inválido. Use DD/MM/AAAA.")
        return

    valor_ufp = float(input("Qual o valor total do bem (em UFPs)? ").replace(',', '.'))
    
    print("\nEscolha a Razão:")
    print("1 - Causa Mortis")
    print("2 - Doação")
    razao_op = input("Opção: ")
    razao = "CAUSA MORTIS" if razao_op == "1" else "DOAÇÃO"

    print("\nEscolha o Tipo de Bem:")
    print("1 - Imóvel")
    print("2 - Móvel / Outros")
    print("3 - Cota de Sociedade")
    tipo_op = input("Opção: ")
    tipo_bem = "IMOVEL" if tipo_op == "1" else ("COTA" if tipo_op == "3" else "MOVEL")

    resultado = ""
    aliquota = 0.0
    base_legal = ""
    situacao = ""

    # Lógica CAUSA MORTIS
    if razao == "CAUSA MORTIS":
        if data_fato <= 19811231:
            if tipo_bem == "IMOVEL":
                aliquota = 0.02
                base_legal = "Art. 14, I, 'c' da Lei nº 2.070/ 1976"
            else:
                situacao = "Não incidência (apenas imóveis nesta época)"
        
        elif data_fato <= 19890331:
            if tipo_bem == "IMOVEL":
                aliquota = 0.04
                base_legal = "Art. 14, II, 'c' da Lei nº 2.070/ 1976"
            else:
                situacao = "Não incidência (apenas imóveis nesta época)"
        
        elif data_fato <= 20131110:
            aliquota = 0.04
            base_legal = "Art. 10 da Lei nº 2.704/ 1989"
            
        elif data_fato <= 20151231:
            aliquota = 0.04
            base_legal = "Art. 14, I da Lei nº 7.724/ 2013"

        elif data_fato <= 20190330:
            base_legal = "Caput do Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 8.498/2018"
            if valor_ufp <= 1000: situacao = "Isento (até 1000 UFP)"
            elif valor_ufp <= 3500: aliquota = 0.02
            elif valor_ufp <= 7000: aliquota = 0.04
            elif valor_ufp <= 14000: aliquota = 0.06
            else: aliquota = 0.08

        elif (data_fato >= 20190331 and data_fato <= 20190423) or \
             (data_fato >= 20190801 and data_fato <= 20191107) or \
             (data_fato >= 20191201 and data_fato <= 20231005):
            
            if data_fato <= 20200811:
                base_legal = "Caput do Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 8.498/2018"
            else:
                base_legal = "Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 8.729/2020"
                
            if valor_ufp <= 200: situacao = "Isento (até 200 UFP)"
            elif valor_ufp <= 2417: aliquota = 0.03
            elif valor_ufp <= 12086: aliquota = 0.06
            else: aliquota = 0.08

        elif data_fato >= 20190424 and data_fato <= 20190731:
            aliquota = 0.02
            base_legal = "Art. 14, §4º da Lei nº 7.724/2013, acrescentado pela Lei nº 8.520/ 2019"

        elif data_fato >= 20191108 and data_fato <= 20191130:
            aliquota = 0.03
            base_legal = "§4º do Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 8.594/ 2019"

        elif data_fato >= 20231006:
            base_legal = "Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 9.297/2023"
            if tipo_bem == "COTA":
                if valor_ufp <= 500: situacao = "Isento (até 500 UFP)"
                else: aliquota = 0.02
            else:
                if valor_ufp <= 500: situacao = "Isento (até 500 UFP)"
                elif valor_ufp <= 2417: aliquota = 0.03
                elif valor_ufp <= 12086: aliquota = 0.06
                else: aliquota = 0.08

    # Lógica DOAÇÃO
    else:
        if data_fato <= 19811231:
            if tipo_bem == "IMOVEL":
                aliquota = 0.02
                base_legal = "Art. 14, I, 'c' da Lei nº 2.070/ 1976"
            else: situacao = "Não incidência (apenas imóveis)"
        
        elif data_fato <= 19890331:
            if tipo_bem == "IMOVEL":
                aliquota = 0.04
                base_legal = "Art. 14, II, 'c' da Lei nº 2.070/ 1976"
            else: situacao = "Não incidência"
            
        elif data_fato <= 20131110:
            aliquota = 0.04
            base_legal = "Art. 10 da Lei nº 2.704/ 1989"
            
        elif data_fato <= 20190330:
            aliquota = 0.04
            base_legal = "Art. 14, II da Lei nº 7.724/ 2013"

        elif (data_fato >= 20190331 and data_fato <= 20190423) or \
             (data_fato >= 20190801 and data_fato <= 20191107) or \
             (data_fato >= 20191201 and data_fato <= 20200811):
            base_legal = "Caput do Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 8.498/2018"
            if valor_ufp <= 200: situacao = "Isento (até 200 UFP)"
            elif valor_ufp <= 2417: aliquota = 0.03
            elif valor_ufp <= 12086: aliquota = 0.06
            else: aliquota = 0.08

        elif data_fato >= 20190424 and data_fato <= 20190731:
            aliquota = 0.02
            base_legal = "§4º do art. 14 da Lei nº 7.724/2013, pela Lei nº 8.520/ 2019"

        elif data_fato >= 20191108 and data_fato <= 20191130:
            aliquota = 0.03
            base_legal = "§4º do Art. 14 da Lei nº 7.724/ 2013, pela Lei nº 8.594/ 2019"

        elif data_fato >= 20200812 and data_fato <= 20231005:
            base_legal = "Art. 14 da Lei nº 7.724/ 2013, alterado pela Lei nº 8.729/2020"
            if valor_ufp <= 200: situacao = "Isento"
            elif valor_ufp <= 6900: aliquota = 0.02
            elif valor_ufp <= 46019: aliquota = 0.04
            else: aliquota = 0.08

        elif data_fato >= 20231006:
            if tipo_bem == "IMOVEL":
                if data_fato <= 20231231:
                    base_legal = "Art. 14, inciso II da Lei nº 7.724/ 2013 (Lei 9297/23)"
                    if valor_ufp <= 500: situacao = "Isento"
                    elif valor_ufp <= 6900: aliquota = 0.02
                    elif valor_ufp <= 46019: aliquota = 0.04
                    else: aliquota = 0.08
                else:
                    base_legal = "Art. 14, inciso II da Lei nº 7.724/ 2013 (Lei 9297/23)"
                    if valor_ufp <= 500: situacao = "Isento"
                    elif valor_ufp <= 6900: aliquota = 0.02
                    elif valor_ufp <= 12086: aliquota = 0.04
                    elif valor_ufp <= 27248: aliquota = 0.06
                    else: aliquota = 0.08
            else: # Bens Móveis
                base_legal = "Art. 14, inciso III -A da Lei nº 7.724/ 2013 (Lei 9297/23)"
                if valor_ufp <= 500: situacao = "Isento"
                else: aliquota = 0.02

    # Exibição do Resultado
    print("\n" + "="*50)
    print(f"RESULTADO PARA {razao}")
    print("="*50)
    if situacao != "":
        print(f"SITUAÇÃO: {situacao}")
    else:
        imposto = valor_ufp * aliquota
        print(f"ALÍQUOTA APLICADA: {aliquota*100:.1f}%")
        print(f"BASE LEGAL: {base_legal}")
        print("-" * 30)
        print("DEMONSTRATIVO DO CÁLCULO:")
        print(f"Valor em UFP: {valor_ufp:.2f}")
        print(f"Operação: {valor_ufp:.2f} x {aliquota}")
        print(f"Total devido: {imposto:.4f} UFPs")
    print("="*50)


    print("\nOBS: Atente-se aos casos de isenção e imunidade. Tais situações")
    print("não foram consideradas para os fins da resposta deste programa.")

if __name__ == "__main__":
    calcular_itcmd()
