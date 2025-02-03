import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def update_history(equation, history_listbox):
    """Añade una ecuación al historial."""
    history_listbox.insert(tk.END, equation)

def select_equation(history_listbox, entry):
    """Selecciona una ecuación del historial y la pone en el campo de entrada."""
    selected_equation = history_listbox.get(tk.ACTIVE)
    entry.delete(0, tk.END)
    entry.insert(0, selected_equation)

def f(x, equation):
    """Evalúa la ecuación con valor x."""
    return eval(equation)

def grafica(equation, canvas_frame, canvas_widget):
    """Genera la gráfica de la ecuación y la muestra en la ventana principal."""
    # Limpiar la gráfica anterior
    if canvas_widget:
        canvas_widget.get_tk_widget().destroy()

    x = np.linspace(-10, 10, 400)
    y = f(x, equation)

    # Crear la figura de matplotlib
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label=f'f(x) = {equation}')
    ax.set_title('Gráfica de f(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()
    ax.grid(True)

    # Dibujar los ejes en cruz
    ax.axhline(0, color='black',linewidth=2)  # Eje horizontal (y = 0)
    ax.axvline(0, color='black',linewidth=2)  # Eje vertical (x = 0)

    # Convertir la figura a un objeto que Tkinter pueda mostrar
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)  # Crear un canvas de Tkinter
    canvas.draw()  # Dibujar la gráfica
    canvas_widget = canvas  # Guardar el objeto canvas para eliminarlo en la próxima llamada
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Mostrar el canvas en la ventana

    return canvas_widget

def get_equation(root, history_listbox, canvas_frame, canvas_widget):
    """Obtiene la ecuación desde el input con historial."""
    
    # Crear campo de entrada para la ecuación
    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=10)

    # Crear el botón de actualizar
    equation_var = tk.StringVar()

    def on_submit():
        equation_var.set(entry.get())
        update_history(entry.get(), history_listbox)
        # Llamar a la función de gráfica al definir la ecuación
        nonlocal canvas_widget
        canvas_widget = grafica(entry.get(), canvas_frame, canvas_widget)

    submit_button = tk.Button(root, text="Definir Ecuación", command=on_submit)
    submit_button.pack(pady=5, side=tk.LEFT)

    # Crear el botón de Ayuda
    def show_help():
        help_window = tk.Toplevel(root)
        help_window.title("Ayuda")

        # Crear un campo de texto donde puedes escribir la descripción
        help_text = tk.Text(help_window, wrap=tk.WORD, width=50, height=10)
        help_text.pack(padx=10, pady=10)
        help_text.insert(tk.END, "Aquí va la guía o descripción sobre cómo ingresar ecuaciones. "
                                "Ejemplo: Ingrese 'x**2' para graficar f(x) = x^2.")
        help_text.config(state=tk.DISABLED)  # Deshabilitar la edición para que solo se vea el texto

    help_button = tk.Button(root, text="Ayuda", command=show_help)
    help_button.pack(pady=5, side=tk.LEFT)

    # Crear el historial de ecuaciones
    history_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # Agregar opción para seleccionar ecuación del historial
    history_listbox.bind("<Double-1>", lambda event: select_equation(history_listbox, entry))

    return equation_var.get()

def main():
    root = tk.Tk()
    root.title("Calculadora Gráfica")

    # Crear un frame para contener la gráfica
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el historial de ecuaciones
    history_listbox = tk.Listbox(root, width=50, height=10)
    
    # Inicializamos el widget del canvas como None
    canvas_widget = None
    
    # Obtener la ecuación y mostrar la gráfica
    get_equation(root, history_listbox, canvas_frame, canvas_widget)

    root.mainloop()

    def on_closing():
        root.quit()   # Detiene el loop de Tkinter
        root.destroy()  # Cierra la ventana
        exit(0)  # Asegura que el proceso termina completamente

    root.protocol("WM_DELETE_WINDOW", on_closing)

main()