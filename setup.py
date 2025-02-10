import sys
from cx_Freeze import setup, Executable
from cx_Freeze.command.bdist_msi import bdist_msi

# Dependências do seu projeto
packages = ["customtkinter", "tkinter", "os", "csv", "PIL",
            "datetime", "tkinter.messagebox", "tkinter.filedialog"]

# Arquivos adicionais (imagens, ícones, etc.) - **IMPORTANTE!**
include_files = ["img/dollar.png", "img/icon_gasto.png",  "img/icon_home.png", "img/icon_lista.png", "img/icon_categoria.png",
                 # Substitua pelos seus arquivos. Inclua a pasta 'img'
                 "img/icon_calendar.png", "img/icon_csv.png", "gastos_teste.csv"]

# Módulos a serem excluídos (opcional)
excludes = []

# Base do executável (GUI no Windows)
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_options = {
    "packages": packages,
    "include_files": include_files,
    "excludes": excludes,
    "include_msvcr": True  # Inclui as bibliotecas de runtime do Visual C++
}


setup(
    name="Gerenciador de Gastos",
    version="0.1",
    description="Aplicativo para gerenciar gastos",
    options={"build_exe": build_options},
    # Substitua 'seu_arquivo.py' pelo nome do seu script principal. Defina o ícone, se desejar.
    executables=[Executable("main.py", base=base,
                            icon="img/dollar.png")]
)
