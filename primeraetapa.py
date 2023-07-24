import re

def validar_numero_nomina(numero_nomina):
    if re.match("^[a-zA-Z0-9]+$", numero_nomina):
        return True
    else:
        return False

def validar_nombre_usuario(nombre_usuario):
    if re.match("^[a-zA-Z]+$", nombre_usuario):
        return True
    else:
        return False

def validar_cantidad_videos(cantidad_videos):
    if cantidad_videos.isdigit():
        return True
    else:
        return False

def validar_titulo_video(titulo_video):
    if re.match("^[a-zA-Z0-9]+$", titulo_video):
        return True
    else:
        return False

def validar_nombre_video(nombre_video):
    if re.match("^[a-zA-Z0-9]+$", nombre_video):
        return True
    else:
        return False

def validar_extension_video(extension_video):
    if re.match("^[a-zA-Z0-9]+$", extension_video):
        return True
    else:
        return False

def validar_tamano_video(tamano_video):
    try:
        tamano = float(tamano_video)
        if 0 <= tamano <= 3:
            return True
        else:
            return False
    except ValueError:
        return False

def pedir_datos_usuario():
    while True:
        numero_nomina = input("Ingrese su número de nómina: ")
        if validar_numero_nomina(numero_nomina):
            break
        else:
            print("Nómina en formato incorrecto. Debe capturar solo números y letras.")

    while True:
        nombre_usuario = input("Ingrese su nombre: ")
        if validar_nombre_usuario(nombre_usuario):
            break
        else:
            print("Nombre de usuario en formato incorrecto. Debe capturar solo letras.")

    while True:
        cantidad_videos = input("Ingrese la cantidad de videos que subirá: ")
        if validar_cantidad_videos(cantidad_videos):
            break
        else:
            print("Cantidad de videos en formato incorrecto. Debe capturar solo números.")

    return numero_nomina, nombre_usuario, int(cantidad_videos)

def pedir_datos_video(numero_video):
    while True:
        titulo_video = input(f"Ingrese el título del video {numero_video}: ")
        if validar_titulo_video(titulo_video):
            break
        else:
            print("Título del video en formato incorrecto. Debe capturar solo números y letras.")

    while True:
        nombre_video = input(f"Ingrese el nombre del video {numero_video}: ")
        if validar_nombre_video(nombre_video):
            break
        else:
            print("Nombre del video en formato incorrecto. Debe capturar solo números y letras.")

    while True:
        extension_video = input(f"Ingrese la extensión del video {numero_video} (.mpg, .mov, etc): ")
        if validar_extension_video(extension_video):
            break
        else:
            print("Extensión del video en formato incorrecto. Debe capturar solo números y letras.")

    while True:
        tamano_video = input(f"Ingrese el tamaño del video {numero_video} en megas (no mayor a 3 megas): ")
        if validar_tamano_video(tamano_video):
            break
        else:
            print("Tamaño del video en formato incorrecto. Debe capturar un valor numérico entre 0 y 3.")

    print("Información del video registrada correctamente.")

    return titulo_video, nombre_video, extension_video, tamano_video

def generar_archivo(numero_nomina, nombre_usuario, cantidad_videos, videos):
    nombre_archivo = f"{numero_nomina}_{nombre_usuario}.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Número de nómina: {numero_nomina}\n")
        archivo.write(f"Nombre del usuario: {nombre_usuario}\n")
        archivo.write(f"Cantidad de videos: {cantidad_videos}\n\n")

        for i, video in enumerate(videos, start=1):
            titulo_video, nombre_video, extension_video, tamano_video = video
            archivo.write(f"Título del video {i}: {titulo_video}\n")
            archivo.write(f"Nombre del video {i}: {nombre_video}\n")
            archivo.write(f"Extensión del video {i}: {extension_video}\n")
            archivo.write(f"Tamaño del video {i}: {tamano_video}\n\n")

    print(f"Archivo {nombre_archivo} generado exitosamente.")

def ejecutar_sistema():
    while True:
        numero_nomina, nombre_usuario, cantidad_videos = pedir_datos_usuario()

        print(f"Bienvenido {nombre_usuario}, tu número de nómina es {numero_nomina} y estás intentando subir {cantidad_videos} videos.")

        confirmacion = input("¿Es correcta la información? (Si/No): ")

        if confirmacion.lower() == "si":
            videos = []
            for i in range(cantidad_videos):
                datos_video = pedir_datos_video(i + 1)
                videos.append(datos_video)

            generar_archivo(numero_nomina, nombre_usuario, cantidad_videos, videos)

            break
        elif confirmacion.lower() == "no":
            salir = input("¿Deseas salir del sistema? (Si/No): ")
            if salir.lower() == "si":
                print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                break
            elif salir.lower() == "no":
                continue
            else:
                print("Opción inválida. Por favor, ingresa 'Si' o 'No'.")
        else:
            print("Opción inválida. Por favor, ingresa 'Si' o 'No'.")





ejecutar_sistema()
