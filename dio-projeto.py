# sistema simples de um banco para o desafio de codigo do bootcamp python AI Backend VIVO
print('''
    **************bem vindo a nossa startapp ****************    
    digite uma opcao para realizar :
      
      ( 1 ) extrato
      ( 2 ) depositar
      ( 3 ) sacar
      ( 4 ) sair
''')
# aqui nao vou usar funcoes pq isso sera um projeto de  melhoria dese sistema em um proximo 
#desafio de codigo

saldo = 0
LIMITE = 500
N_operacoes = 1
l = []
ext =( "operacoes realizadas : ")
l.append(ext)

# demorei para ajustar a lista de extrato 

while N_operacoes <= 3 :
    opcao = int(input("qual operacao vc deseja realizar ?  : "))

    if opcao == 1 :
        sd_a =f"seu saldo atual e {saldo}"
        l.append("consulta de extrato")
        l.append(sd_a)
        print("""
    **************extrato****************
              operacoes realizadas :
""")
        print(l)
        N_operacoes+=1

    elif opcao == 2 :
      deposito = int(input("digite a quantidade q deseja depositar  : "))
      if deposito > LIMITE :
               print(f"a operacao nao pode exceder o limite de {LIMITE}")
               dp_n = f"deposito nao realizado pq o valor do deposito nao pode exceder  {LIMITE} "
               l.append(dp_n)
               N_operacoes+=1

      else :
         saldo += deposito
         dp_r =f"deposito realizado com sucesso no valor de {deposito}"
         l.append(dp_r)
         print(f"deposito realizado com sucesso no valor de {deposito}")
         N_operacoes+=1

    elif opcao == 3 :
        saque = int(input("digite a quantia q deseja sacar   : "))
        if saque > saldo :
              print(f"saque invalido pq vc nao tem saldo vc tem : {saldo}")
              sq_n ="saque nao realizado"
              l.append(sq_n)
              N_operacoes+=1

        elif saque > LIMITE:
          print(f"a operacao nao pode exceder o limite de {LIMITE}")
          sq_n ="saque nao realizado"
          l.append(sq_n)
          N_operacoes+=1

        else :
              saldo -= saque
              sq_r = "saque realizado com sucesso "
              l.append(sq_r)
              N_operacoes+=1

    elif opcao == 4 :
        print("obrigado por escolher o nosso banco")
        break
    
    else :
        print("operacao invalida")
N_operacoes+=1