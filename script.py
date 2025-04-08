import pyautogui
import time
import pandas as pd

# Configurações iniciais
pyautogui.PAUSE = 0.5  # Tempo mais adequado entre ações
pyautogui.FAILSAFE = True  # Permite abortar movendo o mouse para canto superior esquerdo

# Abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)  # Espera o Chrome abrir

# Acessar site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)  # Espera o site carregar

# Login
# ATENÇÃO: Coordenadas devem ser ajustadas com pegar_posicao.py para seu monitor
pyautogui.click(x=685, y=451)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua_senha_aqui")  # Substitua pela senha real
pyautogui.press("enter")  # Melhor que click em coordenadas para botão de login
time.sleep(3)

# Importar dados
tabela = pd.read_csv("produtos.csv")

# Cadastrar produtos
for linha in tabela.index:
    # ATENÇÃO: Coordenadas devem ser ajustadas com pegar_posicao.py para seu monitor
    pyautogui.click(x=653, y=294)
    
    # Preencher campos
    campos = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo"]
    for campo in campos:
        valor = str(tabela.loc[linha, campo])
        pyautogui.write(valor)
        pyautogui.press("tab")
    
    # Campo observação (opcional)
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    pyautogui.press("enter")  # Submeter formulário
    
    # Rolagem para ver próximo produto
    pyautogui.scroll(-500)  # Valor negativo para rolar para baixo
    time.sleep(0.5)  # Pequena pausa após cada cadastro