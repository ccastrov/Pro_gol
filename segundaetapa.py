from primeraetapa import*

class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def capturar_nombre(self):
        while True:
            nombre = input("Ingrese su nombre: ")
            if validar_nombre_usuario(nombre):
                self.nombre = nombre
                break
            else:
                print("Nombre inválido. Debe capturar solo letras.")

    def capturar_id(self):
        while True:
            id = input("Ingrese su número de nómina: ")
            if validar_numero_nomina(id):
                self.id = id
                break
            else:
                print("Número de nómina en formato incorrecto. Debe capturar sólo números.")

    def guardar_datos_persona(self):
        datos_persona = f"Número de nómina: {self.id}\nNombre del usuario: {self.nombre}\n"
        return datos_persona


class Videos:
    def __init__(self):
        self.lista_videos = []

    def capturar_nombre_video(self):
        while True:
            nombre_video = input("Ingrese el nombre del video: ")
            if validar_nombre_video(nombre_video):
                self.lista_videos.append(nombre_video)
                break
            else:
                print("Nombre del video en formato incorrecto. Debe capturar solo números y letras.")

    def capturar_extension_video(self):
        while True:
            extension_video = input("Ingrese la extensión del video (.mpg, .mov, etc): ")
            if validar_extension_video(extension_video):
                self.lista_videos.append(extension_video)
                break
            else:
                print("Extensión del video en formato incorrecto. Debe capturar solo números y letras.")

    def capturar_tamano_video(self):
        while True:
            tamano_video = input("Ingrese el tamaño del video en megas (no mayor a 3): ")
            if validar_tamano_video(tamano_video):
                self.lista_videos.append(tamano_video)
                break
            else:
                print("Tamaño del video en formato incorrecto. Debe capturar un valor numérico entre 0 y 3.")

    def guardar_datos_videos(self):
        datos_videos = ""
        for i, video in enumerate(self.lista_videos):
            datos_videos += f"Título del video {i+1}: {video}\n"

        return datos_videos


def imprimir_datos_en_txt(datos_persona, datos_videos):
    nombre_archivo = f"{datos_persona['id']}_{datos_persona['nombre']}.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write(datos_persona)
        archivo.write(datos_videos)


def menu_principal():
    while True:
        nombre = input("Ingrese su nombre: ")
        id = input("Ingrese su número de nómina: ")

        if validar_nombre_usuario(nombre) and validar_numero_nomina(id):
            persona = Usuario(nombre, id)

            cantidad_videos = input("Ingrese la cantidad de videos que subirá: ")

            if validar_cantidad_videos(cantidad_videos):
                videos = Videos()
                confirmacion = input(f"Bienvenido {persona.nombre}, tu número de nómina es {persona.id} y estás intentando subir {cantidad_videos} videos. ¿Es correcta la información? (Si/No): ")

                if confirmacion.lower() == "si":
                    for _ in range(int(cantidad_videos)):
                        print("Ingrese los datos del video:")
                        videos.capturar_nombre_video()
                        videos.capturar_extension_video()
                        videos.capturar_tamano_video()

                    datos_persona = persona.guardar_datos_persona()
                    datos_videos = videos.guardar_datos_videos()
                    imprimir_datos_en_txt(datos_persona, datos_videos)

                    break
                elif confirmacion.lower() == "no":
                    salir_sistema = input("¿Deseas salir del sistema? (Si/No): ")
                    if salir_sistema.lower() == "si":
                        print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                        break
                else:
                    print("Respuesta inválida. Por favor, responde 'Si' o 'No'.")
        else:
            print("Datos inválidos. Por favor, verifique que ha ingresado un nombre válido y un número de nómina válido.")

