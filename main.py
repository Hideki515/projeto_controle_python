# encoding: utf-8

import customtkinter as ctk
import tkinter as tk
import os
import csv
from tkinter import ttk
from PIL import Image  # pip install pillow
from datetime import datetime
from tkinter import messagebox

arquivo_csv = './gastos_teste.csv'


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title('Gerenciador de Gastos')  # Title of the window
        self.geometry('1060x700')  # width x height
        self._apply_appearance_mode('dark')

        # Configuração do grid 1x2
        self.grid_rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Pegando imagens
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'img')

        self.logo_image = ctk.CTkImage(Image.open(
            os.path.join(image_path, "dollar.png")), size=(26, 26))

        self.icon_gasto = ctk.CTkImage(Image.open(
            os.path.join(image_path, "icon_gasto.png")), size=(26, 26))

        self.icon_home = ctk.CTkImage(Image.open(
            os.path.join(image_path, "icon_home.png")), size=(26, 26))

        self.icon_list = ctk.CTkImage(Image.open(
            os.path.join(image_path, "icon_lista.png")), size=(26, 26))

        self.icon_categoria = ctk.CTkImage(Image.open(
            os.path.join(image_path, "icon_categoria.png")), size=(26, 26))

        self.icon_calendar = ctk.CTkImage(Image.open(
            os.path.join(image_path, "icon_calendar.png")), size=(26, 26))

        self.icon_csv = ctk.CTkImage(Image.open(
            os.path.join(image_path, "icon_csv.png")), size=(26, 26))

        # Frame de botões de navegação
        self.navegation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navegation_frame.grid(row=0, column=0, sticky="nsew")
        self.navegation_frame.grid_rowconfigure(7, weight=1)

        self.nav_frame_label = ctk.CTkLabel(self.navegation_frame,
                                            text=" Gerenciador de Gastos",
                                            image=self.logo_image,
                                            compound='left',
                                            fg_color='transparent',
                                            font=ctk.CTkFont(size=15, weight='bold'))
        self.nav_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botão Home
        self.home_button = ctk.CTkButton(self.navegation_frame,
                                         corner_radius=6,
                                         height=40,
                                         border_spacing=10,
                                         text="Home",
                                         image=self.icon_home,
                                         fg_color="transparent",
                                         text_color="White",
                                         hover_color="gray",
                                         anchor="w",
                                         command=self.home_button_click)
        self.home_button.grid(row=1, column=0, sticky="ew")

        # Botão Gastos
        self.expenses_button = ctk.CTkButton(self.navegation_frame,
                                             corner_radius=6,
                                             height=40,
                                             border_spacing=10,
                                             text="Adicionar Gasto",
                                             image=self.icon_gasto,
                                             fg_color="transparent",
                                             text_color="White",
                                             hover_color="gray",
                                             anchor="w",
                                             command=self.expenses_button_click)
        self.expenses_button.grid(row=2, column=0, sticky="ew")

        # Botão Listar Gastos
        self.list_button = ctk.CTkButton(self.navegation_frame,
                                         corner_radius=6,
                                         height=40,
                                         border_spacing=10,
                                         text="Listar Gastos",
                                         image=self.icon_list,
                                         fg_color="transparent",
                                         text_color="White",
                                         hover_color="gray",
                                         anchor="w",
                                         command=self.list_button_click)
        self.list_button.grid(row=3, column=0, sticky="ew")

        # Botão Listar Gastos Categoria
        self.category_button = ctk.CTkButton(self.navegation_frame,
                                             corner_radius=6,
                                             height=40,
                                             border_spacing=10,
                                             text="Listar Gastos Categoria",
                                             image=self.icon_categoria,
                                             fg_color="transparent",
                                             text_color="White",
                                             hover_color="gray",
                                             anchor="w",
                                             command=self.list_category_button_click)
        self.category_button.grid(row=4, column=0, sticky="ew")

        # Botão Listar Gastos Mês
        self.month_button = ctk.CTkButton(self.navegation_frame,
                                          corner_radius=6,
                                          height=40,
                                          border_spacing=10,
                                          text="Listar Gastos Mês",
                                          image=self.icon_calendar,
                                          fg_color="transparent",
                                          text_color="White",
                                          hover_color="gray",
                                          anchor="w",
                                          command=self.list_month_button_click)
        self.month_button.grid(row=5, column=0, sticky="ew")

        # Botão Exportar Gastos
        self.export_button = ctk.CTkButton(self.navegation_frame,
                                           corner_radius=6,
                                           height=40,
                                           border_spacing=10,
                                           text="Exportar Gastos",
                                           image=self.icon_csv,
                                           fg_color="transparent",
                                           text_color="White",
                                           hover_color="gray",
                                           anchor="w",
                                           command=self.export_button_click)
        self.export_button.grid(row=6, column=0, sticky="ew")

        # self.apparence_mode_menu = ctk.CTkOptionMenu(self.navegation_frame,
        #                                              values=[
        #                                                  'Light', 'Dark', 'System'],
        #                                              command=self.change_apparence_mode)
        # self.apparence_mode_menu.grid(
        #     row=7, column=0, pady=20, padx=20, sticky="s")

        self.home_frame = ctk.CTkFrame(self,
                                       corner_radius=0,
                                       fg_color='transparent')

        self.expenses_frame = ctk.CTkFrame(self,
                                           corner_radius=0,
                                           fg_color='transparent')

        self.list_frame = ctk.CTkFrame(self,
                                       corner_radius=0,
                                       fg_color='transparent')

        self.list_category_frame = ctk.CTkFrame(self,
                                                corner_radius=0,
                                                fg_color='transparent')

        self.list_month_frame = ctk.CTkFrame(self,
                                             corner_radius=0,
                                             fg_color='transparent')

        self.export_frame = ctk.CTkFrame(self,
                                         corner_radius=0,
                                         fg_color='transparent')

        # Widgets em frames
        self.title_home = ctk.CTkLabel(self.home_frame,
                                       text='Home Page',
                                       font=('Arial Bold', 36))

        self.title_expenses = ctk.CTkLabel(self.expenses_frame,
                                           text='Adicionar Gasto',
                                           font=('Arial Bold', 36),)

        self.title_list = ctk.CTkLabel(self.list_frame,
                                       text='Lista de Gastos',
                                       font=('Arial Bold', 36))

        self.title_list_category = ctk.CTkLabel(self.list_category_frame,
                                                text='Lista de gastos por categoria',
                                                font=('Arial Bold', 36))

        self.title_list_month = ctk.CTkLabel(self.list_month_frame,
                                             text='List Month Page',
                                             font=('Arial Bold', 36))

        self.title_export = ctk.CTkLabel(self.export_frame,
                                         text='Export Page',
                                         font=('Arial Bold', 36))

        self.select_frame_by_name("Home")

    def fields_expenses(self):
        # Campos Adcionar Gastos
        # Campo Data
        self.label_date = ctk.CTkLabel(self.expenses_frame,
                                       text='Data: ',
                                       font=('Arial', 13))

        self.input_date = ctk.CTkEntry(self.expenses_frame,
                                       width=250,
                                       corner_radius=6)

        # Dropdown Categoria
        self.label_categoy = ctk.CTkLabel(self.expenses_frame,
                                          text='Categoria: ',
                                          font=('Arial', 12))
        self.dropdown_categoria = ctk.CTkOptionMenu(self.expenses_frame,
                                                    values=[
                                                        'Alimentação', 'Transporte', 'Saúde', 'Educação', 'Lazer', 'Outros'],
                                                    fg_color='black',
                                                    width=250,
                                                    button_hover_color='purple',
                                                    button_color='gray',
                                                    corner_radius=6)
        self.dropdown_categoria.set("Selecione uma categoria")

        # Campo de Descrição
        self.label_description = ctk.CTkLabel(self.expenses_frame,
                                              text='Descrição do gasto: ',
                                              font=('Arial', 12))

        self.input_description = ctk.CTkEntry(self.expenses_frame,
                                              placeholder_text='Descrição do gasto',
                                              width=250,
                                              corner_radius=6)

        # Campo de Valor
        self.label_value = ctk.CTkLabel(self.expenses_frame,
                                        text='Valor gastado: ',
                                        font=('Arial', 12))
        self.input_currency = ctk.CTkEntry(self.expenses_frame,
                                           placeholder_text='Valor do gasto: ',
                                           width=250,
                                           corner_radius=6)

        # Botão Adicionar Gasto
        self.button_add_expense = ctk.CTkButton(self.expenses_frame,
                                                text='Adicionar Gasto',
                                                font=('Arial', 12),
                                                fg_color='green',
                                                hover_color='darkgreen',
                                                border_width=0,
                                                corner_radius=7,
                                                command=self.add_expense)

    def table_expenses(self):
        self.style_tree = ttk.Style()
        self.style_tree.theme_use("clam")
        self.style_tree.configure("Treeview",
                                  background="#2A2A2A",
                                  foreground="white",
                                  rowheight=25,
                                  fieldbackground="#2A2A2A",
                                  borderwidth=0,
                                  padding=5)

        self.style_tree.map("Treeview", background=[("selected", "#1F6AA5")])

        self.style_tree.configure("Treeview.Heading",
                                  background="#1F1F1F",
                                  foreground="white",
                                  font=("Arial", 10, "bold"))

        self.table_frame = ctk.CTkFrame(self.list_frame,
                                        corner_radius=6)
        self.table_frame.grid(row=2, column=0, pady=10, sticky="nsew")

        columns = ("Data", "Categoria", "Descrição", "Valor")
        self.tree = ttk.Treeview(self.table_frame,
                                 columns=columns,
                                 show="headings")

        self.tree.heading("Data", text="Data")
        self.tree.column("Data", anchor="center")

        self.tree.heading("Categoria", text="Categoria")
        self.tree.column("Categoria", anchor="w")

        self.tree.heading("Descrição", text="Descrição")
        self.tree.column("Descrição", anchor="w")

        self.tree.heading("Valor", text="Valor")
        self.tree.column("Valor", anchor="w")

        self.tree.grid(row=1, column=0, sticky="nsew")

        self.lbl_total = ctk.CTkLabel(self.list_frame,
                                      text="Total de gastos: R$ 0.00",
                                      font=("Arial", 12, "bold"))
        self.lbl_total.grid(row=2, column=0, pady=10)

    def table_category_list(self):
        # Dropdown Categoria
        self.categoria_filter_var = tk.StringVar()
        self.dropdown_categoria_filter = ctk.CTkOptionMenu(self.list_category_frame,
                                                           values=[
                                                               'Alimentação', 'Transporte', 'Saúde', 'Educação', 'Lazer', 'Outros'],
                                                           fg_color='black',
                                                           width=250,
                                                           button_hover_color='purple',
                                                           button_color='gray',
                                                           variable=self.categoria_filter_var,
                                                           corner_radius=6)
        self.dropdown_categoria_filter.set("Selecione uma categoria")

        self.style_tree_category = ttk.Style()
        self.style_tree_category.theme_use("clam")
        self.style_tree_category.configure("Treeview",
                                           background="#2A2A2A",
                                           foreground="white",
                                           rowheight=25,
                                           fieldbackground="#2A2A2A",
                                           borderwidth=0,
                                           padding=5)

        self.style_tree_category.map("Treeview", background=[
                                     ("selected", "#1F6AA5")])

        self.style_tree_category.configure("Treeview.Heading",
                                           background="#1F1F1F",
                                           foreground="white",
                                           font=("Arial", 10, "bold"))

        self.table_frame_catagory = ctk.CTkFrame(self.list_category_frame,
                                                 corner_radius=6)
        self.table_frame_catagory.grid(row=2, column=0, pady=10, sticky="nsew")

        columns = ("Data", "Categoria", "Descrição", "Valor")
        self.tree_catagory = ttk.Treeview(self.table_frame_catagory,
                                          columns=columns,
                                          show="headings")

        self.tree_catagory.heading("Data", text="Data")
        self.tree_catagory.column("Data", anchor="center")

        self.tree_catagory.heading("Categoria", text="Categoria")
        self.tree_catagory.column("Categoria", anchor="w")

        self.tree_catagory.heading("Descrição", text="Descrição")
        self.tree_catagory.column("Descrição", anchor="w")

        self.tree_catagory.heading("Valor", text="Valor")
        self.tree_catagory.column("Valor", anchor="w")

        self.tree_catagory.grid(row=1, column=0, sticky="nsew")

        self.lbl_total_catagory = ctk.CTkLabel(self.list_category_frame,
                                               text="Total de gastos: R$ 0.00",
                                               font=("Arial", 12, "bold"))

    def add_expense(self):
        data = self.input_date.get()
        categoria = self.dropdown_categoria.get().lower()
        descricao = self.input_description.get()
        valor = self.input_currency.get()

        if categoria == "Selecione uma categoria" or not descricao or not valor:
            print(data, categoria, descricao, valor)
            messagebox.showwarning(
                "Aviso", "Todos os campos devem ser preenchidos!")
            return

        if not os.path.isfile(arquivo_csv):

            print("Arquivo CSV não encontrado. Nenhum gasto cadastrado ainda.")

            with open(arquivo_csv, mode="w", newline='') as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(["Data", "Categoria", "Descrição", "Valor"])

        with open(arquivo_csv, mode="a", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow([data, categoria, descricao, valor])

        messagebox.showinfo(
            "Sucesso", "Gasto adicionado com sucesso!")
        self.input_date.delete(0, "end")
        self.input_description.delete(0, "end")
        self.dropdown_categoria.set("Selecione uma categoria")
        self.input_currency.delete(0, "end")
        self.input_currency.insert(0, "R$ 0.00")

    def format_currency(self, event):
        texto = self.input_currency.get()

        # Remove caracteres não numéricos
        texto = ''.join(filter(str.isdigit, texto))

        if texto == "":
            self.input_currency.delete(0, "end")
            self.input_currency.insert(0, "R$ 0.00")
            return

        # Converte para fornmato monetário
        self.valor = int(texto) / 100
        self.texto_formatado = f"R$ {self.valor:,.2f}".replace(
            ",", "X").replace(".", ",").replace("X", ".")

        self.input_currency.delete(0, "end")
        self.input_currency.insert(0, self.texto_formatado)

    def list_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        with open(arquivo_csv, mode="r", newline='') as file:
            reader = csv.reader(file)
            next(reader)
            total = 0
            for linha in reader:
                self.tree.insert("", "end", values=linha)
                self.convert_currency = linha[3].replace(
                    "R$", "").replace(",", ".").strip()
                self.converted_currency = float(self.convert_currency)
                total += self.converted_currency

        self.lbl_total.configure(
            text=f"Total de gastos: R$ {total:.2f}")

    def list_category_expenses(self, *args):
        categoria_selecionada = self.categoria_filter_var.get().lower()

        for row in self.tree_catagory.get_children():  # Use tree_catagory aqui
            self.tree_catagory.delete(row)

        total = 0

        try:  # Lidar com FileNotFoundError
            with open(arquivo_csv, mode="r", newline='') as csv_file:
                reader_csv = csv.reader(csv_file)
                next(reader_csv)  # Pular o cabeçalho

                for linha_csv in reader_csv:
                    if categoria_selecionada == "selecione uma categoria" or linha_csv[1].lower() == categoria_selecionada:
                        self.tree_catagory.insert("", "end", values=linha_csv)
                        self.valor = linha_csv[3].replace(
                            "R$", "").replace(",", ".").strip()
                        self.valor_float = float(self.valor)
                        total = total + self.valor_float

        except FileNotFoundError:
            total = 0
            messagebox.showwarning(
                "Aviso", f"Arquivo {arquivo_csv} não encontrado.")
            return

        self.lbl_total_catagory.configure(
            text=f'Total de gastos: R$ {total:.2f}')

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color="gray"
                                   if name == "Home" else "transparent")

        self.expenses_button.configure(fg_color="gray"
                                       if name == "Adicionar Gasto" else "transparent")

        self.list_button.configure(fg_color="gray"
                                   if name == "Listar Gastos" else "transparent")

        self.category_button.configure(fg_color="gray"
                                       if name == "Listar Gastos Categoria" else "transparent")

        self.month_button.configure(fg_color="gray"
                                    if name == "Listar Gastos Mês" else "transparent")

        self.export_button.configure(fg_color="gray"
                                     if name == "Exportar Gastos" else "transparent")

        if name == "Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.title_home.grid(
                row=0, column=0, columnspan=1, pady=20, padx=20)
        else:
            self.home_frame.grid_forget()

        if name == "Adicionar Gasto":
            self.expenses_frame.grid(row=0, column=1, sticky="nsew")
            self.title_expenses.grid(
                row=0, column=0, columnspan=4, pady=20, padx=20, sticky="s")

            self.fields_expenses()

            self.input_date.configure(state='normal')
            self.input_date.delete(0, "end")
            self.input_date.configure(state='readonly')
            self.input_description.delete(0, "end")
            self.dropdown_categoria.set("Selecione uma categoria")
            self.input_currency.delete(0, "end")

            self.label_date.grid(row=1, column=0, pady=10, padx=10, sticky="w")
            self.input_date.grid(row=1, column=1, pady=10, padx=10)
            self.input_date.configure(state='normal')
            self.input_date.insert(0, datetime.now().strftime("%d.%m.%Y"))
            self.input_date.configure(state='readonly')

            self.label_categoy.grid(
                row=2, column=0, pady=10, padx=10, sticky="w")
            self.dropdown_categoria.grid(row=2, column=1, pady=10, padx=10)

            self.label_description.grid(
                row=3, column=0, pady=10, padx=10, sticky="w")
            self.input_description.grid(row=3, column=1, pady=10, padx=10)

            self.label_value.grid(
                row=4, column=0, pady=10, padx=10, sticky="w")
            self.input_currency.grid(
                row=4, column=1, pady=10, padx=10)

            self.input_currency.insert(0, "R$ 0.00")
            self.input_currency.bind("<KeyRelease>", self.format_currency)

            self.button_add_expense.grid(row=5, column=1, pady=10, padx=10)
        else:
            self.expenses_frame.grid_forget()

        if name == "Listar Gastos":
            self.list_frame.grid(row=0, column=1, sticky="nsew")
            self.title_list.grid(row=0, column=0, pady=20, padx=20)

            self.table_expenses()

            self.list_expenses()
            self.lbl_total.grid(row=7, column=0, pady=10)

        else:
            self.list_frame.grid_forget()

        if name == "Listar Gastos Categoria":
            self.list_category_frame.grid(row=0, column=1, sticky="nsew")
            self.title_list_category.grid(row=0, column=0, pady=20, padx=20)

            self.table_category_list()

            self.dropdown_categoria_filter.grid(
                row=1, column=0, pady=10, padx=10)

            self.categoria_filter_var.trace("w", self.list_category_expenses)

            # print(
            #     f'Categoria selecionada: {self.dropdown_categoria_filter.get()}')

            self.list_category_expenses()
            self.lbl_total_catagory.grid(row=7, column=0, pady=10)

        else:
            self.list_category_frame.grid_forget()

        if name == "Listar Gastos Mês":
            self.list_month_frame.grid(row=0, column=1, sticky="nsew")
            self.title_list_month.grid(row=0, column=0, pady=20, padx=20)
        else:
            self.list_month_frame.grid_forget()

        if name == "Exportar Gastos":
            self.export_frame.grid(row=0, column=1, sticky="nsew")
            self.title_export.grid(row=0, column=0, pady=20, padx=20)
        else:
            self.export_frame.grid_forget()

    def home_button_click(self):
        self.select_frame_by_name('Home')

    def expenses_button_click(self):
        self.select_frame_by_name('Adicionar Gasto')

    def list_button_click(self):
        self.select_frame_by_name('Listar Gastos')

    def list_category_button_click(self):
        self.select_frame_by_name('Listar Gastos Categoria')

    def list_month_button_click(self):
        self.select_frame_by_name('Listar Gastos Mês')

    def export_button_click(self):
        self.select_frame_by_name('Exportar Gastos')

    def change_apparence_mode(self, mode):
        print(f'Apparence mode changed to {mode}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
