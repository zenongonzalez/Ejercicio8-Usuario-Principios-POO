"""
Desafio N° 3 - Grupo N°5 - Comision N°4

Integrantes:

- Alvarez Bisordi Lucas Martin
- Zenón González
- Yanina Jacqueline Serpa
- Tomas Lautaro Rodriguez
- Guillermo Andrés Torres
- Melisa Larroza
- Daniel Victor Diaz

"""

from datetime import datetime

# Clase Usuario.
class Usuario:
    es_colaborador = False
    es_publico = False

    # Constructor.
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
    
    def login(self):
        username = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            print("Inicio de sesion exitoso.")
        else:
            print("Ingreso mal los datos.")
            self.login()
    
    def registrar(self):
        self.id = input("Ingrese su ID: ")
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.telefono = input("Ingrese su telefono: ")
        self.username = input("Ingrese su nombre de usuario: ")
        self.email = input("Ingrese su correo electronico: ")
        self.contraseña = input("Ingrese su contraseña: ")
        self.fecha_registro = datetime.now()
        self.avatar = input("Ingrese el enlace de su avatar: ")
        self.estado = input("Ingrese su estado: ")
        self.online = False
        
        tipo_usuario = input("¿Desea registrarse como Colaborador (C) o Público (P)? ").lower()
        if tipo_usuario == "c":
            usuario = Colaborador(self.id, self.nombre, self.apellido, self.telefono, self.username, self.email, self.contraseña, self.fecha_registro, self.avatar, self.estado, self.online, True)
            print("Registro exitoso.")
            self.es_colaborador = True
            return usuario
        elif tipo_usuario == "p":
            usuario = Publico(self.id, self.nombre, self.apellido, self.telefono, self.username, self.email, self.contraseña, self.fecha_registro, self.avatar, self.estado, self.online, True)
            print("Registro exitoso.")
            self.es_publico = True
            return usuario
        else:
            print("Ingreso mal los datos.")
            self.registrar()
    
    def esColaborador(self):
        if self.es_colaborador:
            return True
        else:
            return False
    
    def esPublico(self):
        if self.es_publico:
            return True
        else:
            return False

# Clase Publico que hereda de Usuario.
class Publico(Usuario):
    # Constructor.
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = es_publico
    
    def comentar(self, articulo):
        if self.online:
            id_articulo = articulo.id
            id_usuario = self.id
            contenido = input("Ingrese su comentario: ")
            estado = "Publicado"
            nuevo_comentario = Comentario(None, id_articulo, id_usuario, contenido, datetime.now(), estado)
            articulo.agregar_comentario(nuevo_comentario)
            print("Comentario publicado:", contenido)
            return nuevo_comentario
        else:
            print("Debe iniciar sesion para comentar.")

# Clase Colaborador que hereda de Usuario.
class Colaborador(Usuario):
    # Constructor.
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador
    
    def comentar(self, articulo):
        if self.online:
            id_articulo = articulo.id
            id_usuario = self.id
            contenido = input("Ingrese su comentario: ")
            estado = "Publicado"
            nuevo_comentario = Comentario(None, id_articulo, id_usuario, contenido, datetime.now(), estado)
            articulo.agregar_comentario(nuevo_comentario)
            print("Comentario publicado:", contenido)
            return nuevo_comentario
        else:
            print("Debe iniciar sesion para comentar.")
    
    def publicar(self):
        if self.online:
            titulo = input("Ingrese el titulo del articulo: ")
            resumen = input("Ingrese el resumen del articulo: ")
            contenido = input("Ingrese el contenido del articulo: ")
            fecha_publicacion = datetime.now()
            imagen = input("Ingrese el enlace de la imagen del articulo: ")
            estado = "Publicado"
            
            articulo = Articulo(None, self.id, titulo, resumen, contenido, fecha_publicacion, imagen, estado)
            print("Articulo publicado con ID:", articulo.id)
            return articulo
        else:
            print("Debe iniciar sesion para publicar un articulo.")

# Clase Articulo.
class Articulo:
    contadorDeID = 1
    
    # Constructor.
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id if id else Articulo.contadorDeID
        Articulo.contadorDeID += 1
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado
        self.comentarios = []
    
    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

# Clase Comentario.
class Comentario:
    contadorDeID = 1
    
    # Constructor.
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id if id else Comentario.contadorDeID
        Comentario.contadorDeID += 1
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado

# Funcion para printear al usuario Colaborador.
def printear_colaborador(colaborador):
    print("ID:", colaborador.id)
    print("Nombre:", colaborador.nombre)
    print("Apellido:", colaborador.apellido)
    print("Telefono:", colaborador.telefono)
    print("Nombre de usuario:", colaborador.username)
    print("Correo electronico:", colaborador.email)
    print("Contraseña:", colaborador.contraseña)
    print("Fecha de registro:", colaborador.fecha_registro)
    print("Avatar:", colaborador.avatar)
    print("Estado:", colaborador.estado)
    print("En linea:", colaborador.online)
    print("Es colaborador:", colaborador.es_colaborador)

# Funcion para printear al usuario Publico.
def printear_publico(publico):
    print("ID:", publico.id)
    print("Nombre:", publico.nombre)
    print("Apellido:", publico.apellido)
    print("Telefono:", publico.telefono)
    print("Nombre de usuario:", publico.username)
    print("Correo electronico:", publico.email)
    print("Contraseña:", publico.contraseña)
    print("Fecha de registro:", publico.fecha_registro)
    print("Avatar:", publico.avatar)
    print("Estado:", publico.estado)
    print("En linea:", publico.online)
    print("Es público:", publico.es_publico)

# Funcion para imprimir un articulo y sus comentarios.
def imprimir_articulo(articulo):
    print(f"\n*************** ARTICULO N°{articulo.id} ***************")
    print("ID:", articulo.id)
    print("Titulo:", articulo.titulo)
    print("Resumen:", articulo.resumen)
    print("Contenido:", articulo.contenido)
    print("Fecha de publicacion:", articulo.fecha_publicacion)
    print("Imagen:", articulo.imagen)
    print("Estado:", articulo.estado)

    if len(articulo.comentarios) > 0:
        for comentario in articulo.comentarios:
            print(f"\n************ COMENTARIO N°{comentario.id} ************")
            imprimir_comentario(comentario)
    else:
        print("No hay comentarios.")

# Funcion para imprimir un comentario.
def imprimir_comentario(comentario):
    print("ID:", comentario.id)
    print("ID del articulo:", comentario.id_articulo)
    print("ID del usuario:", comentario.id_usuario)
    print("Contenido:", comentario.contenido)
    print("Fecha y hora:", comentario.fecha_hora)
    print("Estado:", comentario.estado)

# Main.
usuario_precargado = Colaborador(
    1,
    "Lucas",
    "Prueba",
    "12345678",
    "usuario",
    "lucas@hotmail.com",
    "usuario",
    "2023-06-22 18:00:00",
    "../Images/UserAvatar1.png",
    "Activo",
    False,
    True
)

usuario = Usuario(None, None, None, None, None, None, None, None, None, None, None)

articulo_precargado = Articulo(
    None,
    1,
    "Titulo del articulo",
    "Resumen del articulo",
    "Contenido del articulo",
    "2023-06-22 20:00:00",
    "../Images/Articulo1.png",
    "Publicado"
)

print("\n**************** USUARIO COLABORADOR PRECARGADO ****************\n")

printear_colaborador(usuario_precargado)

opcion = input("\nIngrese 'R' para crear un nuevo usuario o 'L' para iniciar sesion: ")

if opcion.upper() == 'R':
    nuevo_usuario = usuario.registrar()
    saludo = nuevo_usuario.username
    nuevo_usuario.login()
    if nuevo_usuario.esColaborador():
        opcion = input(f"\nHola Colaborador: {nuevo_usuario.username}.\nIngrese 'P' para publicar un articulo o 'C' para comentar: ")
        if opcion.upper() == 'P':
            articulo = nuevo_usuario.publicar()
            imprimir_articulo(articulo)
        elif opcion.upper() == 'C':
            nuevo_usuario.comentar(articulo_precargado)
            imprimir_articulo(articulo_precargado)
        else:
            print("Opcion incorrecta.")
    
    if nuevo_usuario.esPublico():
        opcion = input(f"\nHola Usuario: {nuevo_usuario.username}.\nIngrese 'C' para comentar un articulo: ")
        if opcion.upper() == 'C':
            nuevo_usuario.comentar(articulo_precargado)
            imprimir_articulo(articulo_precargado)
        else:
            print("Opcion incorrecta.")

elif opcion.upper() == 'L':
    saludo = usuario_precargado.username
    usuario_precargado.login()
    if usuario_precargado.esColaborador():
        opcion = input(f"\nHola Colaborador: {usuario_precargado.username}.\nIngrese 'P' para publicar un articulo o 'C' para comentar: ")
        if opcion.upper() == 'P':
            articulo = usuario_precargado.publicar()
            imprimir_articulo(articulo)
        elif opcion.upper() == 'C':
            usuario_precargado.comentar(articulo_precargado)
            imprimir_articulo(articulo_precargado)
        else:
            print("Opcion incorrecta.")
    
    if usuario_precargado.esPublico():
        opcion = input(f"\nHola Usuario: {usuario_precargado.username}.\nIngrese 'C' para comentar un articulo: ")
        if opcion.upper() == 'C':
            usuario_precargado.comentar(articulo_precargado)
            imprimir_articulo(articulo_precargado)
        else:
            print("Opcion incorrecta.")

else:
    print("Opcion incorrecta.")

print(f"\n********************* HASTA LUEGO {saludo.upper()} *********************\n")