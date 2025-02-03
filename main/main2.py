import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from sympy import symbols, diff, lambdify, solveset, S
from textos import guia as texto_guia

# Variables globales para la configuración de la gráfica
x_min, x_max, resolution = -10, 10, 400

def update_history(equation, history_listbox):
    history_listbox.insert(tk.END, equation)

def select_equation(history_listbox, entry):
    selected_equation = history_listbox.get(tk.ACTIVE)
    entry.delete(0, tk.END)
    entry.insert(0, selected_equation)

def f(x, equation):
    return eval(equation, {"x": x, "np": np})

def calcular_info(equation, info_label):
    x = symbols('x')
    expr = eval(equation, {"x": x, "np": np})
    
    derivada_1 = diff(expr, x)
    derivada_2 = diff(derivada_1, x)
    
    criticos = solveset(derivada_1, x, domain=S.Reals)
    puntos_criticos = [p.evalf() for p in criticos]
    
    info_text = f"Expresión: {expr}\n" \
                f"1ª Derivada: {derivada_1}\n" \
                f"2ª Derivada: {derivada_2}\n" \
                f"Puntos críticos: {puntos_criticos}"
    
    info_label.config(text=info_text)

def grafica(equation, canvas_frame, canvas_widget):
    global x_min, x_max, resolution

    if canvas_widget:
        canvas_widget.get_tk_widget().destroy()
    
    x = np.linspace(x_min, x_max, resolution)
    y = f(x, equation)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label=f'f(x) = {equation}')
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()
    ax.grid(True)
    
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas_widget = canvas
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    return canvas_widget

def get_equation(root, history_listbox, canvas_frame, canvas_widget, info_label):
    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=10)
    
    equation_var = tk.StringVar()
    
    def on_submit():
        equation_var.set(entry.get())
        update_history(entry.get(), history_listbox)
        nonlocal canvas_widget
        canvas_widget = grafica(entry.get(), canvas_frame, canvas_widget)
        calcular_info(entry.get(), info_label)
    
    submit_button = tk.Button(root, text="Definir Ecuación", command=on_submit)
    submit_button.pack(pady=5, side=tk.LEFT)
    
    def show_help():
        help_window = tk.Toplevel(root)
        help_window.title("Ayuda")
        help_text = tk.Text(help_window, wrap=tk.WORD, width=50, height=10)
        help_text.pack(padx=10, pady=10)
        help_text.insert(tk.END, texto_guia)
        help_text.config(state=tk.DISABLED)
    
    help_button = tk.Button(root, text="Ayuda", command=show_help)
    help_button.pack(pady=5, side=tk.LEFT)
    
    history_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    history_listbox.bind("<Double-1>", lambda event: select_equation(history_listbox, entry))
    
    return equation_var.get()

def configurar_grafica(canvas_frame, canvas_widget, equation):
    global x_min, x_max, resolution

    config_window = tk.Toplevel()
    config_window.title("Configuración de Gráfica")
    
    tk.Label(config_window, text="Límite inferior de x:").pack()
    x_min_entry = tk.Entry(config_window)
    x_min_entry.pack()
    x_min_entry.insert(0, str(x_min))
    
    tk.Label(config_window, text="Límite superior de x:").pack()
    x_max_entry = tk.Entry(config_window)
    x_max_entry.pack()
    x_max_entry.insert(0, str(x_max))
    
    tk.Label(config_window, text="Resolución:").pack()
    resolution_entry = tk.Entry(config_window)
    resolution_entry.pack()
    resolution_entry.insert(0, str(resolution))
    
    def apply_changes():
        global x_min, x_max, resolution
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        resolution = int(resolution_entry.get())
        config_window.destroy()
        
        nonlocal canvas_widget
        canvas_widget = grafica(equation, canvas_frame, canvas_widget)

    tk.Button(config_window, text="Aplicar", command=apply_changes).pack()

def main():
    root = tk.Tk()
    root.title("Calculadora Gráfica")
    
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    history_listbox = tk.Listbox(root, width=50, height=10)
    
    canvas_widget = None
    
    info_label = tk.Label(root, text="Información de la función", justify=tk.LEFT, anchor="w")
    info_label.pack(padx=10, pady=10, fill=tk.BOTH)
    
    equation = get_equation(root, history_listbox, canvas_frame, canvas_widget, info_label)
    
    config_button = tk.Button(root, text="Configurar Gráfica", command=lambda: configurar_grafica(canvas_frame, canvas_widget, equation))
    config_button.pack(pady=5)
    
    def on_closing():
        root.quit()
        root.destroy()
        exit(0)
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

main()