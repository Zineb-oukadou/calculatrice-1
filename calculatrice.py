import tkinter as tk
import math

# Fonction pour ajouter les chiffres et les opérateurs à l'écran
def append_value(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

# Fonction pour effacer l'écran
def clear_display():
    display.delete(0, tk.END)

# Fonction pour calculer le résultat
def calculate_result():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour calculer la racine carrée
def sqrt():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, math.sqrt(current))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour calculer la puissance
def power():
    try:
        display.delete(0, tk.END)
        display.insert(tk.END, '**')
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour calculer le sinus
def sin():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, math.sin(math.radians(current)))  # En radians
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour calculer le cosinus
def cos():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, math.cos(math.radians(current)))  # En radians
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour calculer la tangente
def tan():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, math.tan(math.radians(current)))  # En radians
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour le logarithme
def log():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, math.log10(current))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Fonction pour pi
def pi():
    display.delete(0, tk.END)
    display.insert(tk.END, math.pi)

# Fonction pour exponentielle
def exp():
    try:
        current = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, math.exp(current))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Erreur')

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")
root.geometry("400x500")  # Taille de la fenêtre

# Création de l'écran d'affichage
display = tk.Entry(root, width=20, borderwidth=5, font=('Arial', 18), justify='right', bg='#f1f1f1')
display.grid(row=0, column=0, columnspan=5, pady=20)

# Liste des boutons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('pow', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sin', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3), ('cos', 4, 4),
    ('=', 5, 0), ('tan', 5, 1), ('log', 5, 2), ('pi', 5, 3), ('exp', 5, 4),
]

# Ajout des boutons à la fenêtre avec couleurs et tailles personnalisées
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculate_result, bg='#4CAF50', fg='white')
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear_display, bg='#FF5733', fg='white')
    elif text == 'sqrt':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=sqrt, bg='#FF9F00', fg='white')
    elif text == 'pow':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=power, bg='#FF9F00', fg='white')
    elif text == 'sin':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=sin, bg='#FF9F00', fg='white')
    elif text == 'cos':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=cos, bg='#FF9F00', fg='white')
    elif text == 'tan':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=tan, bg='#FF9F00', fg='white')
    elif text == 'log':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=log, bg='#FF9F00', fg='white')
    elif text == 'pi':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=pi, bg='#FF9F00', fg='white')
    elif text == 'exp':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=exp, bg='#FF9F00', fg='white')
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda value=text: append_value(value), bg='#4CAF50', fg='white')

    button.grid(row=row, column=col, padx=5, pady=5)

# Lancer l'application
root.mainloop()

