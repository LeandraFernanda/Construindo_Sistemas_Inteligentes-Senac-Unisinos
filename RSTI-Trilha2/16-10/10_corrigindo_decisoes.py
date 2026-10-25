'''
O programa deveria permitir 
a participação de pessoas a partir de 16 anos que tenham
autorização, mas contém erros:
        idade = input("Idade: ")
        autorizacao = input("Possui autorização? (Sim/Não): ")

        if idade >= 16 and autorizacao = "Sim" or "sim" or "s"
        print("Participação permitida!")
          
        else:
            print("Participação não permitida!")

Reescreva o código corrigindo
a conversão da idade , o operador de comparação  os dois pontos e a indentação
Explique cada correção em um comentário.
Considere uma idade não negativa e as respostas sim ou não.   
'''
idade = int(input("Idade: "))  # Corrigido para converter a entrada em inteiro, pois input retorna uma string.
autorizacao = input("Possui autorização? (Sim/Não): ")
print(autorizacao)  # Adicionado para depuração, para verificar a entrada do usuário.  
 

