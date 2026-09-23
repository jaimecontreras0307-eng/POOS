from paciente import Paciente 
pacientes: list[Paciente] = []

def agregar_paciente() -> None:
    rut = input("Ingrese el Rut del Paciente: ")
    nombre = input("Ingrese el Nombre del Paciernte: ")
    edad = int(input("Ingrese la Edad del Paciente: "))
    print("Previsiones disponibles: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    prevision = input("Seleccione la previsioin del Paciente: ")
    if prevision == "1":
        prevision = "Fonasa"
    else :
        prevision == "Isapre"

    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")

def leer_numero(mensaje:str) -> int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, Ingrese un numero valido.")

def menu() -> int:
    opcion = -1
    while opcion < 0 or opcion > 5:
        print("Menú de clinica")
        print("1.- Agregar paciente")
        print("2.- Editar Paciente")
        print("3.- Eliminar paciente")
        print("4.- Imprimir un paciente")
        print("5.- Imprimir todos los pacientes")
        print("0.- Salir")
        opcion = leer_numero("Seleccione una oipcion: ")
    return opcion 

def buscar_paciente() -> Paciente:
    rut = input("Ingrese el R.U.T. del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
        

def imprimir_paciente() -> None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("Paciente no encontrado.")

def editar_paciente() -> None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
        print("Menu de edición de paciente")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        opcion = leer_numero("Seleccione una opción: ")
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            paciente.nombre = nuevo_nombre
        elif opcion == 2:
            nueva_edad = leer_numero("Ingrese la nueva edad: ")
            paciente.edad = nueva_edad
        elif opcion == 3:
            print("Previsiones disponibles: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("0.- No hacer cambios")
            nueva_privision = input("Seleccione la nueva prevision: ")
            if nueva_privision == "1":
                paciente.prevision = "Fonasa"
            elif nueva_privision == "2":
                paciente.prevision = "Isapre"
            else: 
                print("No se realizaron cambios.")
    else:
        print("Paciente no encontrado")

def imprimir_pacientes() -> None:
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

def eliminar_paciente() -> None:
    paciente = buscar_paciente()
    if paciente:
        paciente.remove(paciente)
        print("Paciente eliminado exitosamente.")
    else:
        print("Paciente no encontrado.")

def main():
    op = -1
    while op !=0:
        op = menu()
        if op == 1:
            print("Agregando paciente")
            agregar_paciente()
        elif op == 2:
            print("Editando paciente")
            editar_paciente()
        elif op == 3:
            print("Eliminado paciente")
            eliminar_paciente()
        elif op == 4:
            print("Imprimiendo un paciente")
            imprimir_paciente()
        elif op == 5:
            print("Imprimiendo todos los pacientes")
            imprimir_pacientes()
        elif op == 0:
            print("Saliendo del programa")

if __name__ == "__main__":
    main()
