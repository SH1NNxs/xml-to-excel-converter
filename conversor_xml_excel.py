import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET
import pandas as pd

def extrair_dados_xml():
    # 1. Selecionar o arquivo de entrada (XML)
    root_tk = tk.Tk()
    root_tk.withdraw()
    
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo XML",
        filetypes=[("Arquivos XML", "*.xml"), ("Todos os arquivos", "*.*")]
    )
    
    if not caminho_arquivo:
        return

    try:
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        dados = {
            "Código": [],
            "Peso Líquido": [],
            "Peso Bruto": []
        }

        # Extraindo os dados usando iteradores para encontrar as tags em qualquer nível
        # Usamos namespaces vazios ou ignoramos para facilitar a busca
        vols = [t.text for t in root.iter() if 'nVol' in t.tag]
        pls = [t.text for t in root.iter() if 'pesoL' in t.tag]
        pbs = [t.text for t in root.iter() if 'pesoB' in t.tag]

        for nvol, pl, pb in zip(vols, pls, pbs):
            # Tratamento de conversão:
            # 1. Substitui o ponto por nada (se houver separador de milhar) ou trata direto
            # 2. Converte para float para o Excel entender como número
            try:
                peso_l_formatado = float(pl.replace(',', '.'))
                peso_b_formatado = float(pb.replace(',', '.'))
            except (ValueError, AttributeError):
                peso_l_formatado = pl
                peso_b_formatado = pb

            dados["Código"].append(nvol)
            dados["Peso Líquido"].append(peso_l_formatado)
            dados["Peso Bruto"].append(peso_b_formatado)

        if not dados["Código"]:
            messagebox.showwarning("Aviso", "Nenhuma tag correspondente foi encontrada.")
            return

        # 3. Escolher local para salvar
        caminho_salvar = filedialog.asksaveasfilename(
            title="Salvar arquivo Excel",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")]
        )

        if caminho_salvar:
            df = pd.DataFrame(dados)
            
            # O comando abaixo garante que o Excel trate as colunas como números
            # e a formatação de vírgula aparecerá conforme a configuração regional do seu Windows
            df.to_excel(caminho_salvar, index=False)
            messagebox.showinfo("Sucesso", f"Arquivo salvo com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    extrair_dados_xml()
