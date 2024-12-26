import tkinter as tk
from tkinter import ttk

# Função para criar a interface gráfica
def criar_interface():
    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Alfabeto e Números")
    janela.geometry("800x650")
    janela.configure(bg="#f0f8ff")

    # Título da aplicação
    titulo = tk.Label(janela, text="Alfabeto e Números", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#333")
    titulo.pack(pady=20)

    # Frame para organizar a grade
    frame_grade = tk.Frame(janela, bg="#f0f8ff")
    frame_grade.pack(pady=10)

    # Cores para alternar entre as células
    cores = ["#ff9999", "#99ccff", "#99ff99", "#ffff99"]

    # Letras do alfabeto e números
    elementos = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]  # Letras A-Z e números 0-9
    linhas, colunas = 6, 6  # Quantidade de linhas e colunas
    index = 0

    # Criação da grade
    for linha in range(linhas):
        for coluna in range(colunas):
            if index < len(elementos):
                bg_cor = cores[(linha + coluna) % len(cores)]
                label = tk.Label(frame_grade, text=elementos[index], font=("Arial", 24, "bold"), bg=bg_cor, width=5, height=2)
                label.grid(row=linha, column=coluna, padx=5, pady=5)
                index += 1

    # Execução da interface
    janela.mainloop()

# Executa a interface
if __name__ == "__main__":
    criar_interface()
