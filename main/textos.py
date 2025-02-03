guia = """📌 GUÍA DE USO - CALCULADORA GRÁFICA

----------------------------------------

🔹 ¿CÓMO USAR EL PROGRAMA?
1. Ingresar una ecuación en el campo de texto.
   - Usa la variable 'x' para representar la incógnita.
2. Presionar "Definir Ecuación" para graficar la función.
3. Explorar el historial haciendo doble clic en una ecuación guardada para reutilizarla.
4. Hacer zoom o mover la gráfica con el mouse.
5. Presionar "Ayuda" para ver esta guía en cualquier momento.

----------------------------------------

🔹 REGLAS PARA ESCRIBIR ECUACIONES
- Usa 'x' como la variable de la función.
- Usa 'np.' para funciones matemáticas avanzadas.
- Usa '**' para exponentes (en vez de '^').

✅ EJEMPLOS DE FUNCIONES BÁSICAS
----------------------------------------
| Tipo de función     | Ejemplo de entrada      | Interpretación    |
|---------------------|------------------------|-------------------|
| Polinómica         | x**2 + 3*x - 5          | f(x) = x² + 3x - 5 |
| Exponencial        | np.exp(x)               | f(x) = e^x        |
| Logarítmica        | np.log(x)               | f(x) = ln(x)      |
| Trigonométrica     | np.sin(x) + np.cos(x)   | f(x) = sin(x) + cos(x) |
| Valor absoluto     | np.abs(x - 2)           | f(x) = |x - 2|    |
| Raíz cuadrada      | np.sqrt(x)              | f(x) = √x         |

----------------------------------------

🔹 EJEMPLOS AVANZADOS CON NUMPY
1. **Función Sigmoide** (Usada en redes neuronales):
   1 / (1 + np.exp(-x))

2. **Función Gaussiana**:
   np.exp(-x**2)

3. **Función Tangente Hiperbólica**:
   np.tanh(x)

4. **Función Escalón de Heaviside**:
   np.heaviside(x, 1)

5. **Función seno normalizada**:
   np.sin(2 * np.pi * x)

----------------------------------------

📌 ¡Listo! Ahora puedes graficar cualquier función matemática fácilmente. 🎯
"""