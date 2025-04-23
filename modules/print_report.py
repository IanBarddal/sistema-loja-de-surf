import pandas as pd
from tkinter import messagebox, filedialog
import os
from modules.database import DataBase
import locale
from datetime import datetime
from logs.log_class import Log

def print_report(): # Imprime um relatório para o lojista

    date_now = datetime.now()
    date_formatted = date_now.strftime("%d-%m-%Y")

    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        
    directory = filedialog.askdirectory()

    if not directory:
        messagebox.showinfo(title="Erro", message="Nenhum diretório selecionado")
        return

    try:
        # Primeiro, faz uma requisição de vendas

        DataBase().connect()

        resultado = DataBase().read("SELECT * FROM Vendas")

        if not resultado:  # Se não houver vendas registradas, ele não grava o relatório
            messagebox.showinfo(title="Notificação", message="Nenhuma venda registrada no banco de dados.")
            Log("print_report_failure").log_warning(f"Tentativa de imprimir relatório falhou (Não há vendas registradas)")
            return
        
        colunas = ["ID", "Cliente", "CPF", "Produto", "Quantidade Vendida", "Valor Total", "Data da Venda"]

        data_sheet = pd.DataFrame(resultado, columns=colunas)

        data_sheet["Valor Total"] = pd.to_numeric(data_sheet["Valor Total"], errors='coerce')

        data_sheet = data_sheet.groupby("Produto", as_index=False)[["Quantidade Vendida", "Valor Total"]].sum()

        data_sheet["Valor Total"] = data_sheet["Valor Total"].apply(lambda x: locale.currency(x, grouping=True))

        file_path = os.path.join(directory, f"Relatório {date_formatted}.xlsx")

        data_sheet.to_excel(file_path, index=False)

        messagebox.showinfo(title="Notificação", message=f"Arquivo 'Relatório.xlsx' criado com sucesso na pasta {directory}")
        Log("print_report_success").log_info(f"Tentativa de imprimir relatório bem-sucedida.")
                
    except Exception as e:
            
        messagebox.showinfo(title="Erro", message=f"Erro ao gerar relatório: {e}.")
        Log("print_report_failure").log_warning(f"Tentativa de imprimir relatório falhou.")