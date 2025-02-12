# Gerenciador de Gastos

Este é um aplicativo de desktop construído com Python e as bibliotecas CustomTkinter e Tkinter para gerenciar gastos pessoais. Ele permite adicionar, listar e exportar gastos em formato CSV.

## Funcionalidades

- **Adicionar Gasto:**
  - Registra novos gastos com data, categoria, descrição e valor.
  - Formata a data (DD.MM.AAAA) e o valor (R$ 0.00) automaticamente.
  - Valida se todos os campos foram preenchidos.
  - Salva os gastos em um arquivo CSV (`gastos.csv`).
- **Listar Gastos:**
  - Exibe os gastos em uma tabela.
  - Filtra os gastos por categoria e mês.
  - Calcula e exibe o total de gastos com base nos filtros aplicados.
  - Lida com a ausência do arquivo CSV, mostrando um aviso.
- **Exportar Gastos:**
  - Permite exportar todos os gastos registrados para um novo arquivo CSV, escolhido pelo usuário.
  - Informa o usuário sobre o sucesso da exportação ou exibe um erro, se ocorrer.
- **Interface Gráfica:**
  - Interface Moderna utilizando CustomTkinter.
  - Menu de navegação lateral com ícones.
  - Botões para Home, Adicionar Gasto, Listar Gastos e Exportar Gastos.
  - Usa imagens/ícones (localizados na pasta `img`).
  - Layout responsivo com uso de grid.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `customtkinter`
  - `tkinter`
  - `Pillow (PIL)`
  - `datetime`
  - `csv`
  - `os`
  - `sys`

## Instalação das dependências

```bash
pip install customtkinter Pillow
```

A biblioteca Tkinter, bem como as demais bibliotecas, já são built-in, nativas do python.

## Estrutura do Projeto

```
gerenciador-de-gastos/
├── main.py
├── img/
│   ├── dollar.png
│   ├── icon_gasto.png
│   ├── icon_home.png
│   ├── icon_lista.png
│   ├── icon_categoria.png
│   ├── icon_calendar.png
│   └── icon_csv.png
└── gastos.csv  (criado automaticamente na primeira adição de gasto)
```

- **`main.py`**: Código principal do aplicativo.
- **`img/`**: Pasta contendo as imagens usadas na interface.
- **`gastos.csv`**: Arquivo CSV onde os gastos são armazenados (será criado automaticamente ao adicionar o primeiro gasto).

## Como Executar

1.  Clone o repositório:

    ```bash
    git clone https://github.com/<seu-usuario>/gerenciador-de-gastos.git
    ```

    (Substitua `<seu-usuario>` pelo seu nome de usuário do GitHub).

2.  Navegue até a pasta do projeto:

    ```bash
    cd gerenciador-de-gastos
    ```

3.  Execute o aplicativo:

    ```bash
    python main.py
    ```

## Classes Principais

- **`AddExpenseFrame`**: Frame para adicionar novos gastos. Contém a lógica de formatação de data, valor e adição ao CSV.
- **`ListExpenseFrame`**: Frame para listar os gastos. Implementa a filtragem, exibição em tabela (Treeview) e cálculo do total.
- **`ExportFileFrame`**: Frame para exportar os gastos para um arquivo CSV.
- **`App`**: Classe principal do aplicativo. Gerencia a janela principal, o menu de navegação, a criação e exibição dos frames, além do tratamento de eventos dos botões.

## Melhorias Futuras (Sugestões)

- **Gráficos:** Adicionar gráficos para visualizar os gastos por categoria e ao longo do tempo.
- **Edição/Exclusão:** Permitir editar e excluir gastos existentes.
- **Configurações:** Adicionar opções de configuração, como o caminho do arquivo CSV padrão.
- **Importação de Dados:** Implementar a importação de gastos de outros formatos (ex: extratos bancários).
- **Persistência de Configurações:** Salvar o estado da aplicação (último frame aberto, etc.)
- **Testes:** Adicionar testes unitários para garantir a qualidade do código.
- **Interface:**
  - Melhorar a responsividade para diferentes tamanhos de tela.
  - Adicionar um tema claro/escuro.
- **Funcionalidades:**
  - Incluir orçamentos, e alertas para quando os gastos estiverem próximos dos limites.
  - Possibilitar a criação de múltiplas categorias customizáveis.
  - Adicionar funcionalidade de backup automático do arquivo CSV.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões de melhorias, abra uma issue ou envie um pull request.
