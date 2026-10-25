'''
leia os numeros inteiros, informe se o 
primeiro é maior, se o segundo é maior ou se os dois
 são iguais . use uma cadeia if / elif / else para resolver o problema.
   teste com numeros iguais, o primeiro maior e o segundo maior.
'''

nun = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if nun > num2:
    print(f"O primeiro número ({nun}) é maior que o segundo número ({num2}).")

elif nun < num2:
    print(f"O segundo número ({num2}) é maior que o primeiro número ({nun}).")

else:
    print(f"Os dois números são iguais: {nun} = {num2}.")

print("Fim do programa.")    