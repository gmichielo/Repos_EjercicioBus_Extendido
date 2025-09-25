from Bus import Bus
from Cliente import Cliente
from Billete import Billete

capacidades_buses = [50,20,35,30]
destinos_buses = ["Barcelona-Madrid","Barcelona-Valencia","Barcelona-Sevilla","Barcelona-Zaragoza"]
buses = []
accion_usuario = 1
accion_bus = 0
bus_seleccionado = ""
billetes_vendidos = 1

def mostrar_menu_acciones():
    menu = "\033[33m1.- Venta de billetes.\n" \
    + "2.- Devolución de billetes.\n" \
    + "3.- Estado de la venta.\n" \
    + "4.- Añadir bus.\n" \
    + "0.- Salir.\033[0m\n"
    return menu

def mostrar_menu_buses(buses):
    menu = ""
    for bus in buses:
        menu += f"{bus.GetBusID()}-{bus.GetDestino()}\n"
    return menu

def creacion_buses(cantidad, capacidades, destinos):
    contador = 1
    indice = 0
    while contador <= cantidad:
        bus = Bus(contador,capacidades[indice],destinos[indice])
        buses.append(bus)
        contador += 1
        indice += 1
    
def creacion_cliente(nombre, apellido):
    cliente = Cliente(nombre,apellido)
    return cliente

def creacion_billete(num_billete, bus, cliente):
    billete = Billete(bus, cliente,num_billete)
    return billete

def creacion_nuevo_bus(buses, capacidad, destino):
    bus = Bus(len(buses) + 1, int(capacidad), f"Barcelona-{destino}")
    buses.append(bus)
    


creacion_buses(4, capacidades_buses, destinos_buses)

print("\033[36mBienvenid@ a viajes terrestres F&G\n ¿Que desea hacer?\033[0m\n")

while accion_usuario != 0:
    print(mostrar_menu_acciones())
    try:
        accion_usuario = int(input(" Elige una opción: ").strip())
    except ValueError:
        print("\033[31mOpción inválida, escribe un número.\033[0m")
        continue
    if accion_usuario > 4 or accion_usuario < 0:
        print("\033[31mOpción inválida, seleccione un numero del menu.\033[0m")
        continue

    if accion_usuario == 1: 
        print("\033[33m"+ mostrar_menu_buses(buses) + "\033[0m")
        accion_bus = input(" Elige un bus: ")

        while (accion_bus.isdigit() == False) or (int(accion_bus) > len(buses)) or (int(accion_bus) <= 0) :
            accion_bus = input("\033[31mEse bus no esta en sistema, Elige uno nuevo: \033[0m")
        
        bus_seleccionado = buses[int(accion_bus) - 1]

        print("\nIntroduzca su nombre y apellido")
        cliente = creacion_cliente((input("Nombre: ")), (input("Apellido: ")))
        billete_nuevo =  creacion_billete(billetes_vendidos, bus_seleccionado, cliente)
        print(bus_seleccionado.VenderBilletes(billete_nuevo))

        billetes_vendidos += 1
        bus_seleccionado = None

    elif accion_usuario == 2:
        print("\033[33m" + mostrar_menu_buses(buses) + "\033[0m")
        
        accion_bus = input(" Elige el bus donde quieres devolver: ")

        while (accion_bus.isdigit() == False) or (int(accion_bus) > len(buses)) or (int(accion_bus) <= 0):
            accion_bus = input("\033[31mEse bus no esta en sistema, Elige otro: \033[0m")

        bus_seleccionado = buses[int(accion_bus) - 1]

        if bus_seleccionado.GetVendidos() == 0:
            print("\033[31mNo hay billetes vendidos en este bus.\033[0m\n")
            bus_seleccionado = None
            continue

        print("\nIntroduzca el nombre y apellido del titular del billete a devolver")
        cliente_tmp = creacion_cliente((input("Nombre: ")), (input("Apellido: ")))
        cliente_num_billete = int(input("Introduzca el numero de tu billete: "))

        print(bus_seleccionado.DevolverBilletes(cliente_tmp, cliente_num_billete))

        bus_seleccionado = None

    elif accion_usuario == 3:
        print(mostrar_menu_buses(buses))
        accion_bus = input(" Elige el bus que deseas revisar: ")

        while (accion_bus.isdigit() == False) or (int(accion_bus) > len(buses)) or (int(accion_bus) <= 0):
            accion_bus = input("\033[31mEse bus no esta en sistema, Elige otro: \033[0m")
        
        bus_seleccionado = buses[int(accion_bus) - 1]

        print(bus_seleccionado.Estado())

    elif accion_usuario == 4:

        destino_bus = input("\nIntroduce el destino del bus: ")
        capacidad_bus = input("Introduce la capacidad del bus: ")
        
        while destino_bus == "" or capacidad_bus.isdigit() == False or int(capacidad_bus) <= 0:
            print("\033[31mVuelve a introducir los datos, hay un problema \033[0m")
            destino_bus = input("\nIntroduce el destino del bus: ")
            capacidad_bus = input("Introduce la capacidad del bus: ")
            
        if capacidad_bus.isdigit() == True and destinos_buses != "": 
            creacion_nuevo_bus(buses, capacidad_bus, destino_bus)
            print("\033[32mSe creo el bus correctamente \033[0m")


print("\033[36mHasta luego muchas gracias por escogernos\033[0m")

        

            


   

