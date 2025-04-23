from pathlib import Path
from tkinter import Tk, Canvas, Button, Entry
from PIL import Image, ImageTk
from modules.print_report import print_report
from windows.customer_register_window import register_customer_window
from windows.product_register_window import product_register_window
from windows.delete_product_window import delete_product_window
from windows.view_products_window import view_products_window
from windows.update_stock_window import update_stock_window
from windows.sell_window import sell_window
from windows.view_sales_window import view_sales_window
from windows.edit_sale_window import edit_sale_window
from windows.delete_sale_window import delete_sale_window
from windows.edit_customer_window import edit_customer_window
from windows.view_customers_window import view_customers_window

OUTPUT_PATH = Path(__file__).resolve().parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main_window():
    
    window = Tk() # Cria a janela

    window.title ("Sistema Cali Surf Skate Shop")

    window.iconbitmap("images/logo ícone.ico")

    window.geometry("1600x900")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas( # Cria o canvas onde os widgets da janela serão colocados
            window,
            bg = "#FFFFFF",
            height = 900,
            width = 1600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

    canvas.place(x = 0, y = 0) # Põe o canvas na tela

    canvas.create_rectangle( # Retângulo principal
            0.0,
            0.0,
            1600.0,
            900.0,
            fill="#FFFFFF",
            outline="")

    canvas.create_rectangle( # Retângulo azul
            500.0,
            0.0,
            1600.0,
            900.0,
            fill="#278ee3",
            outline="")
    
    sale_id_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 20)
    )

    product_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    customer_name_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    cpf_entry = Entry (
        bd=2,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Arial", 18)
    )

    cali_logo = Image.open(relative_to_assets("Logo.png")) # Coloca o logo da empresa na tela
    logo_resized = cali_logo.resize((300, 300), Image.Resampling.LANCZOS) # Redimensiona a logo
    window.logo_tk = ImageTk.PhotoImage(logo_resized)
    canvas.create_image(220, 170, image=window.logo_tk)

    button_register_customer = Button(text= "Registrar Cliente", command=lambda: register_customer_window(window)) # Adiciona o botão de cadastro de clientes

    button_register_customer.place(x=50, y=350, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Editar Cliente", command=lambda: edit_customer_window(window)) # Adiciona o botão de edição de clientes

    button_register_customer.place(x=250, y=350, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Pesquisar Cliente", command=lambda: view_customers_window(window)) # Adiciona o botão de cadastro de clientes

    button_register_customer.place(x=50, y=400, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Cadastrar Produto", command=lambda: product_register_window(window)) # Adiciona o botão de cadastrar produto

    button_register_customer.place(x=250, y=400, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Deletar Produto", command=lambda: delete_product_window(window)) # Adiciona o botão de deletar produto

    button_register_customer.place(x=50, y=450, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Pesquisar Produtos", command=lambda: view_products_window(window)) # Adiciona o botão de visualizar produtos

    button_register_customer.place(x=250, y=450, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Atualizar Estoque", command=lambda: update_stock_window(window)) # Adiciona o botão de atualizar estoque de produtos

    button_register_customer.place(x=50, y=500, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Efetuar Venda", command=lambda: sell_window(window)) # Adiciona o botão para ir para a página de Vendas

    button_register_customer.place(x=250, y=500, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Pesquisar Vendas", command=lambda: view_sales_window(window)) # Adiciona o botão para ir para a página de visualização de vendas

    button_register_customer.place(x=50, y=550, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Editar Venda", command=lambda: edit_sale_window(window)) # Adiciona o botão para ir para a página de edição de vendas

    button_register_customer.place(x=250, y=550, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Cancelar Venda", command=lambda: delete_sale_window(window)) # Adiciona o botão para ir para a página de cancelamento de vendas

    button_register_customer.place(x=50, y=600, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Imprimir Relatório", command=lambda: print_report()) # Adiciona o botão de imprimir relatório para o lojista

    button_register_customer.place(x=250, y=600, width=157, height=29) # Coloca o botão no canvas

    button_register_customer = Button(text= "Sair do Sistema", command=lambda: window.destroy()) # Adiciona o botão de sair do programa

    button_register_customer.place(x=150, y=700, width=157, height=29) # Coloca o botão no canvas

    window.mainloop()