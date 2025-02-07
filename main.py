# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import customtkinter as ctk
import os
from PIL import Image  # pip install pillow


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title('Gerenciador de Gastos')  # Title of the window
        self.geometry('900x700')  # width x height

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

        self.apparence_mode_menu = ctk.CTkOptionMenu(self.navegation_frame,
                                                     values=[
                                                         'Light', 'Dark', 'System'],
                                                     command=self.change_apparence_mode)
        self.apparence_mode_menu.grid(
            row=7, column=0, pady=20, padx=20, sticky="s")

        # Frames
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
                                           text='Expenses Page',
                                           font=('Arial Bold', 36))

        self.title_list = ctk.CTkLabel(self.list_frame,
                                       text='List Page',
                                       font=('Arial Bold', 36))

        self.title_list_category = ctk.CTkLabel(self.list_category_frame,
                                                text='List Category Page',
                                                font=('Arial Bold', 36))

        self.title_list_month = ctk.CTkLabel(self.list_month_frame,
                                             text='List Month Page',
                                             font=('Arial Bold', 36))

        self.title_export = ctk.CTkLabel(self.export_frame,
                                         text='Export Page',
                                         font=('Arial Bold', 36))

        self.select_frame_by_name("Home")

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
            self.title_home.grid(row=0, column=0, pady=20, padx=20)
        else:
            self.home_frame.grid_forget()

        if name == "Adicionar Gasto":
            self.expenses_frame.grid(row=0, column=1, sticky="nsew")
            self.title_expenses.grid(row=0, column=0, pady=20, padx=20)
        else:
            self.expenses_frame.grid_forget()

        if name == "Listar Gastos":
            self.list_frame.grid(row=0, column=1, sticky="nsew")
            self.title_list.grid(row=0, column=0, pady=20, padx=20)
        else:
            self.list_frame.grid_forget()

        if name == "Listar Gastos Categoria":
            self.list_category_frame.grid(row=0, column=1, sticky="nsew")
            self.title_list_category.grid(row=0, column=0, pady=20, padx=20)
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
