#!/bin/bash

echo "    CALCULADORA      "

read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

echo ""
echo "1 - Soma"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"

read -p "Escolha uma opção: " opcao

case $opcao in
    1)
        resultado=$((num1 + num2))
        echo "Resultado: $resultado"
        ;;
    2)
        resultado=$((num1 - num2))
        echo "Resultado: $resultado"
        ;;
    3)
        resultado=$((num1 * num2))
        echo "Resultado: $resultado"
        ;;
    4)
        if [ "$num2" -ne 0 ]; then
            resultado=$((num1 / num2))
            echo "Resultado: $resultado"
        else
            echo "Erro: divisão por zero!"
        fi
        ;;
    *)
        echo "opção inválida!"
        ;;
esac
