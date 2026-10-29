num1 = float(input('Digíte o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
while True:
 print("\n Escolha uma opção: ")
 print("1 - Soma")
 print("2 - Multiplicação")
 print("3 - Subtração")
 print("4 - Divisão")
 print("5 - Potenciação")
 print("6 - Encerrar")
 opcao = input("Escolha uma opção: ")

 if opcao == "1":
   resultado = num1 + num2
   print("A soma é:", resultado)

 elif opcao == "2":
   resultado = num1 * num2
   print("A multiplicação é:", resultado)

 elif opcao == "3":
    resultado = num1 - num2
    print("A subtração é:", resultado)

 elif opcao == "4":
  if num2 != 0:
   resultado = num1 / num2
   print("A divisão é:", resultado)

 elif opcao == "5":
    resultado = num1 ** num2
    print("A potenciação é:", resultado)

 elif opcao == "6":
   print("Programa encerrado!")
   break

 else:
   print("Opção inválida!")
