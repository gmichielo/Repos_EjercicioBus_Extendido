from Bus import Bus
from Cliente import Cliente
from Billete import Billete
from Registro import Registro

buses = []
registros = {}
accion_usuario = 1
accion_bus = 0
bus_seleccionado = ""
billetes_vendidos = 1

def mostrar_menu_registro():
    menu = "\033[33m1.- Registrarse.\n" \
    + "2.- Iniciar Sesion.\033[0m\n"
    return menu

def mostrar_menu_acciones():
    menu = "\033[33m1.- Venta de billetes.\n" \
    + "2.- Devolución de billetes.\n" \
    + "3.- Estado de la venta.\n" \
    + "4.- Añadir bus.\n" \
    + "5.- Cerrar sesion.\n" \    
    + "0.- Apagar programa.\033[0m\n"
    return menu

def nuevo_registro(usuario, contrasenya, correo):
    reg = Registro(usuario, contrasenya, correo)
    registros[reg.GetUsuario()] = {
        "contrasenya": reg.GetContrasenya(),
        "correo": reg.GetCorreo()
    }

def iniciar_sesion(usuario, contrasenya):
    if usuario in registros and registros[usuario]["contrasenya"] == contrasenya:
        print(f"Bienvenido, {usuario}")
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False

def mostrar_menu_buses(buses):
    menu = ""
    for bus in buses:
        menu += f"{bus.GetBusID()}-{bus.GetDestino()}\n"
    return menu
    
def creacion_cliente(nombre, apellido):
    cliente = Cliente(nombre,apellido)
    return cliente

def creacion_billete(num_billete, bus, cliente):
    billete = Billete(bus, cliente,num_billete)
    return billete

def creacion_nuevo_bus(buses, capacidad, destino):
    bus = Bus(len(buses) + 1, int(capacidad), f"Barcelona-{destino}")
    buses.append(bus)
    
print("\033[36mBienvenid@ a viajes terrestres F&G\n ¿Elige registrarse o iniciar sesion\033[0m\n")


programa_encendido = True

while programa_encendido:
    # REGISTRO O INICIO DE SESION
    logueado = False
    while not logueado:
        print("\nElige registrarse o iniciar sesión:")
        print(mostrar_menu_registro())
        try:
            op = int(input(" Opción: ").strip())
        except ValueError:
            print("\033[31mOpción inválida, escribe un número.\033[0m")
            continue

        if op == 1:
            # registrar
            usuario = input("Nuevo usuario: ").strip()
            contrasenya = input("Contraseña: ").strip()
            correo = input("Correo de empresa: ").strip()
            try:
                nuevo_registro(usuario, contrasenya, correo)
                print("\033[32mRegistro correcto. Ahora inicia sesión.\033[0m")
            except ValueError as e:
                print(f"\033[31m{e}\033[0m")
        elif op == 2:
            # login
            usuario = input("Usuario: ").strip()
            contrasenya = input("Contraseña: ").strip()
            logueado = iniciar_sesion(usuario, contrasenya)
        else:
            print("\033[31mOpción inválida.\033[0m")
    # ACCIONES
    accion_usuario = -1        
    while logueado and accion_usuario != 0:
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
            if len(buses) == 0:
                print('\033[31mNo hay buses en el sistema. Añade un bus.\033[0m')
                continue
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
            if len(buses) == 0:
                print('\033[31mNo hay buses en el sistema. Añade un bus.\033[0m')
                continue        
            
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
            cliente_num_billete = input("Introduzca el numero de tu billete: ")
            while cliente_num_billete.isdigit() == False:
                cliente_num_billete = input("\033[31mIntroduce un numero entero válido: \033[0m")
            cliente_num_billete = int(cliente_num_billete)          

            print(bus_seleccionado.DevolverBilletes(cliente_tmp, cliente_num_billete))

            bus_seleccionado = None

        elif accion_usuario == 3:
            print(mostrar_menu_buses(buses))
            if len(buses) == 0:
                print('\033[31mNo hay buses en el sistema. Añade un bus.\033[0m')
                continue
            accion_bus = input(" Elige el bus que deseas revisar: ")

            while (accion_bus.isdigit() == False) or (int(accion_bus) > len(buses)) or (int(accion_bus) <= 0):
                accion_bus = input("\033[31mEse bus no esta en sistema, Elige otro: \033[0m")
            
            bus_seleccionado = buses[int(accion_bus) - 1]

            print(bus_seleccionado.Estado())

        elif accion_usuario == 4:

            destino_bus = input("\nIntroduce el destino del bus: ")
            while destino_bus == "":
                print("\033[31mTienes que poner un destino \033[0m")
                destino_bus = input("\nIntroduce el destino del bus: ")
                
            capacidad_bus = input("Introduce la capacidad del bus: ")
            control = 0
            
            while control == 0:
                if capacidad_bus.isdigit() == False:
                    print('\033[31mTiene que ser un numero\033[0m')
                    capacidad_bus = input("Introduce la capacidad del bus: ")
                elif int(capacidad_bus) <= 0:
                    print('\033[31mTiene que ser mayor a zero.\033[0m')
                    capacidad_bus = input("Introduce la capacidad del bus: ")
                elif int(capacidad_bus) > 50:
                    print("\033[31mCapacidad demasiado grande.\033[0m")
                    capacidad_bus = input("Introduce la capacidad del bus: ")
                else:
                    control = 1
                
            if capacidad_bus.isdigit() == True and destino_bus != "": 
                creacion_nuevo_bus(buses, capacidad_bus, destino_bus)
                print("\033[32mSe creo el bus correctamente \033[0m\n")
        
            elif accion_usuario == 5:
                print("\033[33mSesión cerrada. Volviendo al inicio...\033[0m")
                logueado = False  # salgo de este bucle y vuelvo a registro/login

            elif accion_usuario == 0:
                print("\033[36mApagando programa... Gracias por escogernos!\033[0m")
                logueado = False
                programa_encendido = False