# declaracion de variables

nombre_red = "Red_EdificioL"
dispositivos_activos = 0
total_dispositivos = 0


# lista de dispositivos

dispositivos = [
    "Router R1",
    "Switch SW1",
    "PC-01",
    "PC-02",
    "Servidor S1"
]

print(dispositivos[0])
print(dispositivos[1])
print(dispositivos[2])
print(dispositivos[3])
print(dispositivos[4])

# len para saber cuantos objetos hay en la lista

total_dispositivos = len(dispositivos)

print("Total de dispositivos:", total_dispositivos)


# diccionario

router = {
    "hostname": "Router1",
    "ip_address": "192.168.10.1",
    "model": "Cisco 2900",
    "activo": True
}


# mostrar información del router

print(router["hostname"])
print(router["ip_address"])
print(router["model"])


#conversion de datos

cantidad = input("Ingresa la cantidad de dispositivos activos: ")

dispositivos_activos = int(cantidad)

print("Dispositivos activos:", dispositivos_activos)


#calcular porcentaje

porcentaje = (dispositivos_activos / total_dispositivos) * 100

print("Porcentaje de dispositivos activos:", porcentaje, "%")


#estructura condicional

if dispositivos_activos == total_dispositivos:
    print("La red esta operativa")

elif dispositivos_activos >= total_dispositivos / 2:
    print("La red tiene disponibilidad parcial")

else:
    print("La red tiene problemas")

#ciclo for

print("Lista de dispositivos:")

for dispositivo in dispositivos:
    print(dispositivo)


#manejo de archivos

with open("reporte_red.txt", "w") as archivo:

    archivo.write("REPORTE DE MONITOREO DE RED\n")
    archivo.write(f"Nombre de la red: {nombre_red}\n")
    archivo.write(f"Total de dispositivos: {total_dispositivos}\n")
    archivo.write(f"Dispositivos activos: {dispositivos_activos}\n")
    archivo.write(f"Porcentaje de disponibilidad: {porcentaje}%\n")
    
    archivo.write("\nLISTA DE DISPOSITIVOS\n")

    for dispositivo in dispositivos:
        archivo.write(f"- {dispositivo}\n")

    archivo.write("\nINFORMACION DEL ROUTER\n")
    archivo.write(f"Hostname: {router['hostname']}\n")
    archivo.write(f"Direccion IP: {router['ip_address']}\n")
    archivo.write(f"Modelo: {router['model']}\n")
    archivo.write(f"Activo: {router['activo']}\n")


print("El reporte se guardo correctamente en reporte_red.txt")