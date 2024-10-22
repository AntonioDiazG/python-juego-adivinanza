

def mostar_menu():
    print("\n Agenda de Contactos:")
    print("1. Agregar Nuevo Contacto")
    print("2. Eliminar Contacto Existente")
    print("3. Buscar Contactos")
    print("4. Lista de Contacto")
    print("5. Salir del programa")

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")
    agenda[nombre] = {"telefono": telefono, "correo": correo}
    print("Contacto agregado con exito")
  
def eliminar_contacto(agenda):
    nombre = input(" Ingrese el nombre de la agenda que desea eliminar")
    if agenda in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado correctamente")
    else:
        print(f"El contacto {nombre} no existe en la agenda")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f" Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]["telefono"]}")
        print(f"Correo: {agenda[nombre]["correo"]}")
    else:
        print(f"El contacto {nombre} no existe en la agenda")

def lista_contactos(agenda):
    if agenda:
        print("\n Lista de Copntactos: ")
        for nombre, info in  agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Telefono: {info["correo"]}")
            print("-" * 20)
    else:
        print("No hay contactos en la agenda")
    
def agenda_contactos():
    agenda = {}
    
    while True:
        mostar_menu()
        opcion = input("Ingrese la opción que desee: ")
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2": 
             eliminar_contacto(agenda)
        elif opcion == "3": 
            buscar_contacto(agenda) 
        elif opcion == "4": 
            lista_contactos(agenda )
        elif opcion == "5": 
            print(" Saliendo de la Agenda, ¡Hasta luego!")
            break
        else:
            print(" Opción no válida, por favor intente de nuevo.")
            
agenda_contactos()
        
        