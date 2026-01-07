# Conversor XML para Excel (Automação Fiscal) 📊

> Ferramenta Desktop desenvolvida em Python para automatizar a extração de dados de notas fiscais/romaneios (XML) e gerar relatórios formatados em Excel (.xlsx).

## 💡 O Problema Solucionado
Processos fiscais e logísticos frequentemente envolvem a leitura manual de arquivos XML para conferência de pesos e volumes. Este script elimina o erro humano e reduz o tempo da tarefa de horas para segundos.

## 🚀 Funcionalidades
- **Interface Gráfica (GUI):** Seleção de arquivos via janelas nativas do Windows (Tkinter).
- **Processamento de Dados:** Utiliza `ElementTree` para varredura profunda de tags XML.
- **Tratamento de Erros:** Converte automaticamente formatações numéricas (ponto/vírgula) e trata campos vazios.
- **Exportação Automática:** Gera planilhas Excel prontas para uso com a biblioteca `Pandas`.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** (Manipulação de Dataframes e Exportação)
- **Tkinter** (Interface Gráfica do Usuário)
- **XML.etree** (Parsing de arquivos hierárquicos)

## 📦 Como usar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt

2. Execute o script:
   python conversor_xml_excel.py

3. Selecione o arquivo XML na janela que abrir e escolha onde salvar o Excel gerado.
   

Desenvolvido por Washington Santos
