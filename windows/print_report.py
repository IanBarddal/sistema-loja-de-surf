import sqlite3
from contextlib import closing
import pandas as pd
from tkinter import messagebox, filedialog
import os

def print_report(): # Imprime um relatório para o lojista
        
    directory = filedialog.askdirectory()

    if not directory:
        messagebox.showinfo(title="Erro", message="Nenhum diretório selecionado")
        return

    try:
        # Primeiro, faz uma requisição de vendas

        with sqlite3.connect("surfstore.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute ("select * from Vendas")

                resultado = cursor.fetchall()

                if not resultado:  # Se não houver vendas registradas
                    messagebox.showinfo(title="Notificação", message="Nenhuma venda registrada no banco de dados.")
                    return

                colunas = [desc[0] for desc in cursor.description]

            data_sheet = pd.DataFrame(resultado, columns=colunas)

            data_sheet = data_sheet.groupby("Produto", as_index=False)[["Quantidade Vendida", "Valor Total", "Data da Venda"]].sum()

            file_path = os.path.join(directory, "Relatório.xlsx")

            data_sheet.to_excel(file_path, index=False)

            messagebox.showinfo(title="Notificação", message=f"Arquivo 'Relatório.xlsx' criado com sucesso na pasta {directory}")
                
    except Exception as e:
            
        messagebox.showinfo(title="Notificação", message=f"Erro ao gerar relatório: {e}.")