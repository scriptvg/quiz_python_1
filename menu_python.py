import random
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def mostrar_menu():
    print(f"\n{Style.BRIGHT}{Fore.CYAN}Menú Interactivo:")
    print(f"{Fore.YELLOW}1. Mostrar un mensaje")
    print(f"{Fore.YELLOW}2. Mostrar una lista de nombres")
    print(f"{Fore.YELLOW}3. Salir del programa")

def mostrar_mensaje():
    mensajes = [
        f"{Fore.GREEN}A veces, la persona a la que nadie imagina capaz de nada es la que hace cosas que nadie imagina. -Alan Turing.",
        f"{Fore.GREEN}La vida es como montar en bicicleta. Para mantener el equilibrio, debes seguir adelante. -Albert Einstein.",
        f"{Fore.GREEN}El éxito es la suma de pequeños esfuerzos repetidos día tras día. -Robert Collier.",
        f"{Fore.GREEN}La creatividad es la inteligencia divirtiéndose. -Albert Einstein.",
        f"{Fore.GREEN}El único modo de hacer un gran trabajo es amar lo que haces. -Steve Jobs."
    ]
    mensaje_aleatorio = random.choice(mensajes)
    print(f"\n{Style.BRIGHT}{mensaje_aleatorio}")

def mostrar_nombres():
    nombres = ["Adriana", "Allan José", "Audrey", "Bairon", "Caleb Martin", "Darien", "Fer Alexey", "Isaac David", "Jaqueline", "Jocksan", "Josebeth", "Jostin Gabriel", "María José", "Marieza Coraima", "Steven"]
    print(f"\n{Style.BRIGHT}{Fore.MAGENTA}Lista de nombres:")
    for nombre in nombres:
        print(f"{Fore.LIGHTBLUE_EX}- {nombre}")

def main():
    while True:
        mostrar_menu()
        opcion = input(f"\n{Fore.CYAN}Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_mensaje()
        elif opcion == "2":
            mostrar_nombres()
        elif opcion == "3":
            print(f"\n{Style.BRIGHT}{Fore.RED}Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print(f"\n{Fore.RED}Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()

