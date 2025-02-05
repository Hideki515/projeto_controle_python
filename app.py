# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import os
import csv
from datetime import datetime

arquivo_csv = "./gastos.csv"

# Se o arquivo não existir, cria com cabeçalho
if not os.path.isfile(arquivo_csv):
    with open(arquivo_csv, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Data", "Categoria", "Descrição", "Valor"])


def adicionar_gasto():
    data = datetime.now().strftime("%d/%m/%Y")
    categoria = input("Digite a categoria: ")
    descricao = input("Digite a descrição: ")
    valor = input("Digite o valor gasto: ")

    # Converter valor para float, substituindo "," por "."
    try:
        valor = float(valor.replace(",", "."))
    except ValueError:
        print("❌ Valor inválido! Use apenas números e ',' ou '.'.")
        return

    # Abrindo o arquivo no modo "a" para adicionar sem sobrescrever
    with open(arquivo_csv, mode="a", newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow([data, categoria, descricao, valor])

    print("👌 Gasto adicionado com sucesso!")


def listar_gastos():
    try:
        with open(arquivo_csv, mode="r", newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Pular cabeçalho
            total = 0
            # Converte para lista para verificar se há dados
            gastos = list(reader)

            if not gastos:
                print("📭 Nenhum gasto cadastrado.")
                return

            print("\n📜 Lista de Gastos:")
            print("-" * 50)
            for linha in gastos:
                print(f"{linha[0]} | {linha[1]} | {linha[2]} | R$ {linha[3]}")
                total += float(linha[3])
            print("-" * 50)
            print(f"💰 Total Gasto: R$ {total:.2f}\n")
    except FileNotFoundError:
        print("🚨 Arquivo não encontrado. Nenhum gasto cadastrado ainda.")


def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            print("👋 Saindo do programa...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


menu()
