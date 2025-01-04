# sistema simples de um banco para o desafio de codigo do bootcamp python AI Backend VIVO
def banco():
    print('''
    **************bem vindo a nossa startapp ****************    
    digite uma opcao para realizar :
      
      ( 1 ) extrato
      ( 2 ) depositar
      ( 3 ) sacar
      ( 4 ) sair
    ''')
    saldo =int(0)
    LIMITE = 500
    N_operacoes = 1
    l = []
    def depositar (LIMITE):
      global sd_a
      deposito = int(input("digite a quantidade q deseja depositar  : "))
      sd_a = deposito
      if deposito < LIMITE:
        dp_r =f"deposito realizado com sucesso no valor de {deposito}"
        l.append(dp_r)
        print(dp_r)  
      else:
         dp_n = f"deposito nao realizado pq o valor \n do deposito nao pode exceder  {LIMITE} "
         l.append(dp_n)
         print(dp_n)   
    def saque (LIMITE):
      global sd_a
      saque = int(input("digite a quantia q deseja sacar   : "))
      if saque > sd_a:
          sq_n =f"saque invalido pq vc nao tem saldo vc tem : {sd_a}\n ou tenha ecedido o limite de {LIMITE}"
          print(sq_n)
          l.append(sq_n)
      else :
          sd_a -= saque
          sq_r = f"saque realizado com sucesso no valor de {saque}"
          l.append(sq_r)
    def op_invalida ():
        if opcao != "1" or "2" or "3" or "4" or "" :
           print("operacao invalida")
        elif opcao == "":
           print("operacao invalida")
        else:
            pass
    def extrato ():
      saldo_atual =f"seu saldo atual e {sd_a}"
      l.append("consulta de extrato")
      l.append(saldo_atual)
      print("""
      **************extrato****************
          operacoes realizadas :
      """)
      for lista in enumerate(l):
         print("_"*50)
         print(f"    {lista}\n ")     
    while N_operacoes <= 3:     
        opcao = input("qual operacao vc deseja realizar ?  : ")
        if opcao == "1":
           extrato()
           N_operacoes+=1  
        elif opcao == "2" :
           depositar(LIMITE)
           N_operacoes+=1
        elif opcao == "3":
           saque(LIMITE)
           N_operacoes+=1
        elif opcao == "4":
           print("       obrigado por escolher o nosso banco\n"+"_"*50)
           break
        else :
           op_invalida()
           N_operacoes+=1
banco()