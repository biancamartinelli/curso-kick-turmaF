try:
    
    maca = int(input("Digite quantas maçãs compradas: "))

    if maca < 12:
        valor_total = maca * 0.30
    else:
        valor_total = maca * 0.25
    
    print(f"O valor total da compra é R${valor_total:.2f}")
except:
    print(f"O valor incorreto, digite um valor inteiro")
    
    
    
    # =======================================
    
    from datetime import datetime
    
    hora_atual = datatime.now().hour
    
    if hora_atual >= 18 or hora_atual < 5:
        print("Boa noite")
    elif hora_atual >= 4 and hora_atual < 12:
        print("Bom dia")
    else:
        print("Boa tarde")
