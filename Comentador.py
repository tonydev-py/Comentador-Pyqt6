import re
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

def adicionar_comentarios_pyqt(caminho_arquivo):
    try:
        # Lê o arquivo original
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas:
            messagebox.showerror("Erro", "O arquivo está vazio ou não pôde ser lido.")
            return
        
        novas_linhas = []
        componentes = {
    "QPushButton": "Botão clicável",
    "QToolButton": "Botão de ferramenta",
    "QCheckBox": "Caixa de seleção",
    "QRadioButton": "Botão de opção",
    "QLineEdit": "Campo de entrada de texto (linha única)",
    "QTextEdit": "Área de texto multi-linhas",
    "QPlainTextEdit": "Área de texto simples (multi-linhas)",
    "QComboBox": "Caixa de seleção suspensa",
    "QSpinBox": "Campo numérico (inteiro)",
    "QDoubleSpinBox": "Campo numérico (decimal)",
    "QSlider": "Controle deslizante",
    "QDial": "Controle giratório",
    "QTabWidget": "Widget de abas",
    "QTabBar": "Barra de abas",
    "QMenu": "Menu suspenso",
    "QAction": "Ação de menu ou atalho",
    "QLabel": "Rótulo de texto ou imagem",
    "QStatusBar": "Barra de status",
    "QProgressBar": "Barra de progresso",
    "QToolBar": "Barra de ferramentas",
    "QListWidget": "Lista de itens",
    "QTreeWidget": "Árvore de itens",
    "QTableWidget": "Tabela interativa",
    "QCalendarWidget": "Calendário interativo",
    "QGroupBox": "Caixa de grupo",
    "QFrame": "Frame de agrupamento ou separação",
    "QStackedWidget": "Widget com múltiplos layouts empilhados",
    "QSplitter": "Divisor ajustável entre widgets",
    "QScrollArea": "Área com barra de rolagem",
    "QToolBox": "Caixa de ferramentas com abas",
    "QFormLayout": "Layout de formulário",
    "QVBoxLayout": "Layout vertical",
    "QHBoxLayout": "Layout horizontal",
    "QGridLayout": "Layout em grade",
    "QBoxLayout": "Layout base para caixas",
    "QMessageBox": "Caixa de mensagem padrão",
    "QInputDialog": "Caixa de diálogo para entrada de dados",
    "QFileDialog": "Caixa de diálogo para seleção de arquivos",
    "QFontDialog": "Caixa de diálogo para seleção de fontes",
    "QColorDialog": "Caixa de diálogo para seleção de cores",
    "QGraphicsView": "Visualização de uma cena gráfica",
    "QGraphicsScene": "Cena gráfica",
    "QGraphicsItem": "Item gráfico dentro de uma cena",
    "QChartView": "Visualização de gráficos",
    "QWebEngineView": "Visualização de páginas web",
    "QVideoWidget": "Widget para exibição de vídeos",
    "QMediaPlayer": "Player de mídia",
    "QSystemTrayIcon": "Ícone na bandeja do sistema",
    "QDockWidget": "Widget encaixável",
    "QPixmap": "Imagem (gráfico rasterizado)",
    "QImage": "Imagem para manipulação gráfica",
    "QIcon": "Ícone de ação ou janela",
    "QFont": "Fonte de texto",
    "QColor": "Cor para elementos gráficos",
    "QSizePolicy": "Política de redimensionamento de widgets"
}


        # Processa cada linha do arquivo
        for linha in linhas:
            if linha.strip().startswith("#"):  # Ignora linhas de comentário
                novas_linhas.append(linha)
                continue
            
            comentario_adicionado = False
            
            # Modifica a expressão regular para capturar componentes mesmo quando são passados como parâmetros
            for componente, descricao in componentes.items():
                # Verifica se o nome do componente aparece na linha
                if re.search(r'(\w+)\s*=\s*QtWidgets?\.' + re.escape(componente), linha):
                    comentario = f"# {descricao} encontrado na linha.\n"
                    novas_linhas.append(comentario)
                    comentario_adicionado = True

            # Detectando modificações no retranslateUi
            if "setText" in linha or "setItemText" in linha:  # Detecta mudanças de texto
                if re.search(r'setText\("([^"]+)"\)', linha):
                    novas_linhas.append("# Modificando o texto do componente\n")
                elif re.search(r'setItemText\(\d+, _translate\("([^"]+)"\)', linha):
                    novas_linhas.append("# Modificando o item de texto do componente\n")

            novas_linhas.append(linha)
        
        # Permite ao usuário escolher onde salvar o arquivo final
        caminho_arquivo_salvo = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Arquivos Python", "*.py")],
            title="Salvar Arquivo Comentado"
        )
        
        if caminho_arquivo_salvo:
            # Salva o arquivo modificado no local escolhido
            with open(caminho_arquivo_salvo, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novas_linhas)
            messagebox.showinfo("Sucesso", f"Arquivo salvo como: {caminho_arquivo_salvo}")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o arquivo: {e}")

def iniciar_processamento():
    arquivo_selecionado = filedialog.askopenfilename(
        title="Selecione um arquivo Python",
        filetypes=[("Arquivos Python", "*.py")]
    )
    if arquivo_selecionado:
        adicionar_comentarios_pyqt(arquivo_selecionado)

# Configuração da janela principal
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.title("Comentador de Arquivos PyQt")
janela.geometry("500x500")
janela.resizable(False, False)  # Desabilitar redimensionamento

# Carregar imagem e ajustá-la ao tamanho da janela
imagem = ctk.CTkImage(
    Image.open("C:/Users/tonyc/Desktop/Comentador de Códigos/Comentador-Pyqt6/Comentador.jpg"),
    size=(500, 500)  # Define tamanho fixo igual ao da janela
)

# Widget de exibição da imagem
label_imagem = ctk.CTkLabel(janela, text="", image=imagem)
label_imagem.place(relx=0, rely=0, relwidth=1, relheight=1)  # Ajusta para ocupar toda a janela

# Botão de iniciar
botao_iniciar = ctk.CTkButton(
    janela, text="Iniciar", command=iniciar_processamento, width=200, height=50
)
botao_iniciar.place(relx=0.5, rely=0.9, anchor="center")

janela.mainloop()
