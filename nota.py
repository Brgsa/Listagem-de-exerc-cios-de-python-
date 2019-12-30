
nota1 = float(input("Digita a nota do Primeiro bimestre: "))
nota2 = float(input("Digita a nota do Segundo bimestre: "))
nota3 = float(input("Digita a nota do Terceiro bimestre: "))
nota4 = float(input("Digita a nota do Quatro bimestre: "))
soma = nota1 + nota2 + nota3 + nota4
divisao = 4
media = soma / divisao
print("Nota 1° {}\nNota 2° {}\nNota 3° {}\nNota 4° {}\nSoma {}".format(nota1,nota2,nota3,nota4,soma))
if media > 5:
  print("<<<<<<Aprovado>>>>>>>")
elif media == 5:
  print("<<<<<Recuperação>>>>>>>>>")
else:
    print("<<<<<<Reprovado>>>>>>>>")

fecha = input('Clique na tecla ENTER PARA SAIR')