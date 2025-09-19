from Bus import Bus
from Cliente import Cliente
from Billete import Billete

capacidades_buses = [50,20,35,30]
destinos_buses = ["Barcelona-Madrid","Barcelona-Valencia","Barcelona-Sevilla","Barcelona-Zaragoza"]
buses = []
accion_usuario = 1
accion_bus = 0
bus_seleccionado = ""

def mostrar_menu_acciones():
    menu = "1.- Venta de billetes.\n" \
    + "2.- Devolución de billetes.\n" \
    + "3.- Estado de la venta.\n" \
    + "0.- Salir."
    return menu

def mostrar_menu_buses(buses):
    menu = ""
    for bus in buses:
        menu += f"{bus.GetBusID()}- {bus.GetDestino()}\n"
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

def creacion_billete(bus, cliente):
    billete = Billete(bus, cliente, bus.GetBusID())
    return billete

creacion_buses(4, capacidades_buses, destinos_buses)

print("Bienvind@ a viajes terretres F&G\n ¿Que desea hacer?")

while accion_usuario != 0:
    print(mostrar_menu_acciones())
    accion_usuario = int(input("Elige una opción: "))

    if accion_usuario == 1: 
        print(mostrar_menu_buses(buses))
        accion_bus = int(input("Elige un bus: "))

        while accion_bus > len(buses) or accion_bus <= 0:
            accion_bus = int(input("Ese bus no esta en sistema, Elige uno nuevo: "))
        
        bus_seleccionado = buses[accion_bus - 1]

        #Revisar
        print("Introduzca su nombre y apellido")
        cliente = creacion_cliente((input("Nombre: ")), (input("Apellido: ")))
        billete_nuevo =  creacion_billete(bus_seleccionado, cliente)
        print(bus_seleccionado.VenderBillete(billete_nuevo))

        

            


   

