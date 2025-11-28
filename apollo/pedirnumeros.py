# -------------------------------
# CRUD de Productos
# Cada producto tiene: id, nombre, precio y stock
# -------------------------------

productos = []
id_prod = 1

while True:
    op = int(input(" 1. Crear producto\n 2. Ver Productos\n 3. Actualizar producto\n 4. Eliminar producto\n 0. Salir"))






"""



# CREATE
def crear_producto(nombre, precio, stock):
    global id_prod
    producto = {
        "id": id_prod,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos.append(producto)
    id_prod += 1
    return producto


# READ
def listar_productos():
    return productos


# UPDATE
def actualizar_producto(id_buscar, nombre=None, precio=None, stock=None):
    for p in productos:
        if p["id"] == id_buscar:
            if nombre:
                p["nombre"] = nombre
            if precio is not None:
                p["precio"] = precio
            if stock is not None:
                p["stock"] = stock
            return p
    return None


# DELETE
def eliminar_producto(id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            productos.remove(p)
            return True
    return False
    """


""""
CRUD CON MATCH-CASE
tareas = []

def agregar_tarea():
    tarea = input("Escribe la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente.\n")

def listar_tareas():
    if not tareas:
        print("No hay tareas.\n")
        return
    
    print("\n--- Lista de tareas ---")
    for i, t in enumerate(tareas, start=1):
        print(f"{i}. {t}")
    print()

def actualizar_tarea():
    listar_tareas()
    try:
        indice = int(input("Número de tarea a actualizar: ")) - 1
        nueva = input("Escribe la nueva descripción: ")
        tareas[indice] = nueva
        print("Tarea actualizada.\n")
    except:
        print("Índice inválido.\n")

def eliminar_tarea():
    listar_tareas()
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        tareas.pop(indice)
        print("Tarea eliminada.\n")
    except:
        print("Índice inválido.\n")

# ---------- MENÚ CON match-case ----------
while True:
    print("=== MENÚ ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")
    
    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1":
            agregar_tarea()
        case "2":
            listar_tareas()
        case "3":
            actualizar_tarea()
        case "4":
            eliminar_tarea()
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida.\n")

"""

"""
CRUD DE TAREA

# -------------------------------
# CRUD de Tareas usando una simple lista
# -------------------------------

tareas = []


# CREATE
def agregar_tarea(tarea):
    tareas.append(tarea)
    return tarea


# READ
def listar_tareas():
    return tareas


# UPDATE
def actualizar_tarea(indice, nueva_tarea):
    if 0 <= indice < len(tareas):
        tareas[indice] = nueva_tarea
        return True
    return False


# DELETE
def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        return True
    return False
"""

"""
CRUD PRODUCTOS

# -------------------------------
# CRUD de Productos
# Cada producto tiene: id, nombre, precio y stock
# -------------------------------

productos = []
id_prod = 1


# CREATE
def crear_producto(nombre, precio, stock):
    global id_prod
    producto = {
        "id": id_prod,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos.append(producto)
    id_prod += 1
    return producto


# READ
def listar_productos():
    return productos


# UPDATE
def actualizar_producto(id_buscar, nombre=None, precio=None, stock=None):
    for p in productos:
        if p["id"] == id_buscar:
            if nombre:
                p["nombre"] = nombre
            if precio is not None:
                p["precio"] = precio
            if stock is not None:
                p["stock"] = stock
            return p
    return None


# DELETE
def eliminar_producto(id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            productos.remove(p)
            return True
    return False
"""

"""
crud de usuarios

# -------------------------------
# CRUD de Usuarios usando una lista
# Cada usuario será un diccionario con: id, nombre y email
# -------------------------------

usuarios = []  # Lista principal donde se guardarán los usuarios
id_actual = 1  # Para generar IDs automáticamente


# CREATE - Crear un usuario
def crear_usuario(nombre, email):
    global id_actual
    usuario = {
        "id": id_actual,
        "nombre": nombre,
        "email": email
    }
    usuarios.append(usuario)
    id_actual += 1
    return usuario


# READ - Leer todos los usuarios
def listar_usuarios():
    return usuarios


# UPDATE - Editar un usuario por ID
def actualizar_usuario(id_buscar, nuevo_nombre=None, nuevo_email=None):
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            if nuevo_nombre:
                usuario["nombre"] = nuevo_nombre
            if nuevo_email:
                usuario["email"] = nuevo_email
            return usuario
    return None  # Si no se encontró el usuario


# DELETE - Eliminar un usuario por ID
def eliminar_usuario(id_buscar):
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            usuarios.remove(usuario)
            return True
    return False
"""