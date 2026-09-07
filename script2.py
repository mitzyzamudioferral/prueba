#clase 03/09/26

#ips_servidores = ["192.168.1.10","192.168.1.11","192.168.1.12"]

#print(ips_servidores[0])
#print(ips_servidores[1])
#print(ips_servidores[2])

#ips_servidores.append("10.0.0.14")
#print(ips_servidores[3])
#print(len(ips_servidores))

#append para agregar cosas a la lista sin  modificarla 
#len para ver cuantos objetos se encuentran en nuestra lista 
#diccionario
router = {
    "hostname": "Router1",
    "ip_address": "192.168.1.1",
    "model": "Cisco 2900",
    "activo": True
}
#diccionario

#ALT,SHIFT Y FLECHAS PARA DUPLICAR

#print(router["hostname"])
#print(router["model"])
#print(router["ip_address"])
#print (router["puertos"])

#router["model"] = "Cisco 2911"  #modificar en el diccionario
#router["puertos"] = "24"  
#print(router ["model"])

estado = "down"
vlan =- 99

if estado == "up":
    print("El router esta activo")
else:
    print("El router esta inactivo")   

    vlans_permitidas = [10, 20, 30, 40, 50] 
if vlan in vlans_permitidas:
    print("La VLAN esta permitida")
else: 
     print("La VLAN  no esta permitida") 

with open("config.txt","w")  as archivo:
    archivo.write(f"Modelo del router :{router['model']}")     