# Ejercicio8-Usuario-Principios-POO
Prueba de ejercicios Programación Web. Programación Orientada a Objetos. Junio 2023. Principios de programación orientada a objetos Requisitos técnicos:  - Herencia - Encapsulamiento.  Clases con sus atributos y métodos.
Desafío 8: Principios de programación orientada a objetos
Requisitos técnicos: 
- Herencia
- Encapsulamiento
Crear las siguientes clases con sus atributos y métodos.
Clase Usuario
 atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de 
registro, avatar, estado, online
 métodos: login(), registrar()
Clase Publico(Usuario)
 atributo: es_publico
 métodos: registrar(), comentar()
clase Colaborador(Usuario)
 atributos: es_colaborador
 métodos: registrar(), comentar(), publicar()
clase Articulo
 id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
clase Comentario
 id, id_articulo, id_usuario, contenido, fecha_hora, estado
Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y 
logueado, código que permita comentar al Publico y además publicar al Colaborador
