import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Funciones de archivos ---
def cargar_usuarios():
    try:
        with open("usuarios.txt", "r") as f:
            return [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        return []

def guardar_usuario(id, nombre, puntos):
    with open("usuarios.txt", "a") as f:
        f.write(f"{id},{nombre},{puntos}\n")

def verificar_o_crear_usuario(id_usuario):
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u[0] == id_usuario:
            return  # Usuario ya existe
    nombre = f"Usuario{id_usuario}"  # Nombre por defecto
    guardar_usuario(id_usuario, nombre, 0)

def calcular_puntos(tipo, cantidad):
    valores = {"plastico": 10, "papel": 5, "vidrio": 8}
    return valores.get(tipo.lower(), 0) * int(cantidad)

def actualizar_puntos(id_usuario, puntos_ganados):
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u[0] == id_usuario:
            u[2] = str(int(u[2]) + puntos_ganados)
            break
    with open("usuarios.txt", "w") as f:
        for u in usuarios:
            f.write(",".join(u) + "\n")

def registrar_reciclaje(id_usuario, tipo, cantidad):
    verificar_o_crear_usuario(id_usuario)
    puntos = calcular_puntos(tipo, cantidad)
    with open("reciclaje.txt", "a") as f:
        f.write(f"{id_usuario},{tipo},{cantidad},{puntos}\n")
    actualizar_puntos(id_usuario, puntos)
    return puntos

# --- Recompensas disponibles ---
recompensas = {
    "Bolsa ecológica": 50,
    "Descuento en tienda": 100,
    "Entrada a evento": 150
}

def canjear_recompensa():
    id_usuario = entry_id.get().strip()
    if not id_usuario:
        messagebox.showerror("Error", "Debes ingresar el ID del usuario para canjear.")
        return

    usuarios = cargar_usuarios()
    usuario = next((u for u in usuarios if u[0] == id_usuario), None)
    if not usuario:
        messagebox.showerror("Error", "Usuario no encontrado.")
        return

    puntos_actuales = int(usuario[2])
    opciones = [f"{nombre} ({costo} pts)" for nombre, costo in recompensas.items()]
    opcion = simpledialog.askstring("Canjear Recompensa", "Selecciona una recompensa:\n" + "\n".join(opciones))

    if not opcion:
        return

    seleccion = opcion.split(" (")[0]
    if seleccion in recompensas:
        costo = recompensas[seleccion]
        if puntos_actuales >= costo:
            usuario[2] = str(puntos_actuales - costo)
            with open("usuarios.txt", "w") as f:
                for u in usuarios:
                    f.write(",".join(u) + "\n")
            messagebox.showinfo("Éxito", f"¡Canjeaste '{seleccion}' por {costo} puntos!")
        else:
            messagebox.showwarning("Sin puntos", "No tienes suficientes puntos para esta recompensa.")
    else:
        messagebox.showerror("Error", "Recompensa no válida.")

# --- Funciones de interfaz ---
def registrar():
    id_usuario = entry_id.get().strip()
    tipo = entry_tipo.get().strip()
    cantidad = entry_cantidad.get().strip()

    if not id_usuario or not tipo or not cantidad.isdigit():
        messagebox.showerror("Error", "Completa todos los campos correctamente.")
        return

    puntos = registrar_reciclaje(id_usuario, tipo, cantidad)
    messagebox.showinfo("Éxito", f"¡Registrado! Ganaste {puntos} puntos.")
    entry_id.delete(0, tk.END)
    entry_tipo.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

def mostrar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        messagebox.showinfo("Usuarios", "No hay usuarios registrados.")
        return
    resultado = "\n".join([f"{u[1]} (ID: {u[0]}): {u[2]} puntos" for u in usuarios])
    messagebox.showinfo("Usuarios", resultado)

def mostrar_historial():
    id_usuario = entry_id.get().strip()
    if not id_usuario:
        messagebox.showerror("Error", "Ingresa un ID de usuario.")
        return
    try:
        with open("reciclaje.txt", "r") as f:
            actividades = [line.strip().split(",") for line in f.readlines() if line.startswith(id_usuario + ",")]
        if not actividades:
            messagebox.showinfo("Historial", "No hay actividades para este usuario.")
            return
        resultado = "\n".join([f"{tipo}, {cantidad} unidades -> {puntos} pts" for _, tipo, cantidad, puntos in actividades])
        messagebox.showinfo("Historial de Actividades", resultado)
    except FileNotFoundError:
        messagebox.showinfo("Historial", "No hay historial registrado.")

def mostrar_ranking():
    usuarios = cargar_usuarios()
    if not usuarios:
        messagebox.showinfo("Ranking", "No hay usuarios registrados.")
        return
    usuarios.sort(key=lambda x: int(x[2]), reverse=True)
    ranking = "\n".join([f"{i+1}. {u[1]} (ID: {u[0]}) - {u[2]} pts" for i, u in enumerate(usuarios)])
    messagebox.showinfo("Ranking de Usuarios", ranking)

# --- Interfaz gráfica ---
app = tk.Tk()
app.title("Reciclaje Responsable")

tk.Label(app, text="ID Usuario").grid(row=0, column=0)
tk.Label(app, text="Tipo (papel, plastico, vidrio)").grid(row=1, column=0)
tk.Label(app, text="Cantidad").grid(row=2, column=0)

entry_id = tk.Entry(app)
entry_tipo = tk.Entry(app)
entry_cantidad = tk.Entry(app)

entry_id.grid(row=0, column=1)
entry_tipo.grid(row=1, column=1)
entry_cantidad.grid(row=2, column=1)

tk.Button(app, text="Registrar Reciclaje", command=registrar).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(app, text="Ver Usuarios", command=mostrar_usuarios).grid(row=4, column=0, columnspan=2)
tk.Button(app, text="Canjear Recompensas", command=canjear_recompensa).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(app, text="Ver Historial", command=mostrar_historial).grid(row=6, column=0, columnspan=2)
tk.Button(app, text="Ver Ranking", command=mostrar_ranking).grid(row=7, column=0, columnspan=2, pady=5)

app.mainloop()
