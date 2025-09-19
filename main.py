from Bus import Bus
from Cliente import Cliente
from Billete import Billete

capacidades_buses = [50,20,35,30]
destinos_buses = ["Barcelona-Madrid","Barcelona-Valencia","Barcelona-Sevilla","Barcelona-Zaragoza"]
buses = []
accion_usuario = 0

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

creacion_buses(4,capacidades_buses,destinos_buses)

print("Bienvind@ a viajes terretres F&G\n ¿Que desea hacer?")
print(mostrar_menu_acciones())

