import random
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def mostrar_menu():
    print(f"\n{Style.BRIGHT}{Fore.BLUE}{'='*50}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{' MENÚ INTERACTIVO ':^50}")
    print(f"{Fore.BLUE}{'='*50}")
    print(f"{Fore.YELLOW}1. {Fore.WHITE}Mostrar un mensaje")
    print(f"{Fore.YELLOW}2. {Fore.WHITE}Mostrar una lista de nombres")
    print(f"{Fore.YELLOW}3. {Fore.WHITE}Salir del programa")
    print(f"{Fore.BLUE}{'='*50}")

def formatear_mensaje(mensaje, ancho=50):
    palabras = mensaje.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= ancho:
            linea_actual += (palabra + " ")
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    if linea_actual:
        lineas.append(linea_actual.strip())

    return "\n".join(lineas)

def mostrar_mensaje():
    mensajes = [
        f"A veces, la persona a la que nadie imagina capaz de nada es la que hace cosas que nadie imagina. -Alan Turing.",
        f"La vida es como montar en bicicleta. Para mantener el equilibrio, debes seguir adelante. -Albert Einstein.",
        f"El éxito es la suma de pequeños esfuerzos repetidos día tras día. -Robert Collier.",
        f"La creatividad es la inteligencia divirtiéndose. -Albert Einstein.",
        f"El único modo de hacer un gran trabajo es amar lo que haces. -Steve Jobs."
    ]
    mensaje_aleatorio = random.choice(mensajes)
    mensaje_formateado = formatear_mensaje(mensaje_aleatorio, ancho=48)

    print(f"\n{Style.BRIGHT}{Fore.BLUE}{'='*50}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{' MENSAJE ALEATORIO ':^50}")
    print(f"{Fore.BLUE}{'='*50}")
    print(f"\n{Style.BRIGHT}{Fore.GREEN}{mensaje_formateado}")
    print(f"{Fore.BLUE}{'='*50}")

def mostrar_nombres():
    nombres = ["Adriana", "Allan José", "Audrey", "Bairon", "Caleb Martin", "Darien", "Fer Alexey", "Isaac David", "Jaqueline", "Jocksan", "Josebeth", "Jostin Gabriel", "María José", "Marieza Coraima", "Steven"]
    print(f"\n{Style.BRIGHT}{Fore.BLUE}{'='*50}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{' LISTA DE NOMBRES ':^50}")
    print(f"{Fore.BLUE}{'='*50}")
    for nombre in nombres:
        print(f"{Fore.LIGHTCYAN_EX}- {nombre}")
    print(f"{Fore.BLUE}{'='*50}")

def main():
    while True:
        mostrar_menu()
        opcion = input(f"\n{Fore.CYAN}Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_mensaje()
        elif opcion == "2":
            mostrar_nombres()
        elif opcion == "3":
            print(f"\n{Style.BRIGHT}{Fore.RED}{'='*50}")
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{' GRACIAS ':^50}")
            print(f"{Fore.RED}{'='*50}")
            print(f"{Fore.WHITE}Gracias por usar el programa. ¡Hasta luego!")
            print(f"{Fore.RED}{'='*50}")
            break
        else:
            print(f"\n{Fore.RED}{'='*50}")
            print(f"{Fore.YELLOW}{Style.BRIGHT}{' OPCIÓN NO VÁLIDA ':^50}")
            print(f"{Fore.RED}{'='*50}")
            print(f"{Fore.WHITE}Por favor, intenta de nuevo.")
            print(f"{Fore.RED}{'='*50}")

if __name__ == "__main__":
    main()
