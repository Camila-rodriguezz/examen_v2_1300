print("Camila Rodriguez Ruiz 1300")
class Peluqueria1300:
    def diccionario_sucursal_datos1300(self):
        sucursal1300={
            "Id de Sucursal:": "2605",
            "Nombre de Sucursal:": "Sucursal Las Torres",
            "direccion de Sucursal:": "Las torres #2124",
            "Telefono de Sucursal:": "656 646 1278",
            "Horario de Sucursal:": "12:00 p.m - 9:00 p.m",
            "Encargado de Sucursal:": "Juan Rodriguez",
            "Codigo postal de Sucursal:": "36534"
        }
        for s,u in sucursal1300.items():
            print(s,u)

    def diccionario_empleado_datos1300(self):
        empleado1300={
            "Id de empleado:": "144",
            "Nombre de empleado:": "Abril Cisneros",
            "Cargo de empleado:": "Peluquera",
            "Email de empleado:": "abrilcc@gmail.com",
            "Telefono de empleado:": "656 198 5426",
            "salario de empleado:": "$4000",
            "Id de la sucursal del empleado:": "2605"
        }
        for e,m in empleado1300.items():
            print(e,m)
    
    def diccionario_cliente_datos1300(self):
        cliente1300={
            "Id de cliente:": "186",
            "Nombre de cliente:": "Sofia Ruiz",
            "Telefono de cliente:": "656 239 7627",
            "Email de cliente:": "sofiaaarr@gmail.com",
            "Direccion de cliente:": "Calle flor #2409",
            "Fecha de registro de cliente:": "12/12/2023",
            "Comentarios de cliente:": "Ninguno"
        }
        for c,l in cliente1300.items():
            print(c,l)

    def diccionario_cita_datos1300(self):
        cita1300={
            "Id de cita:": "489",
            "Fecha de cita:": "28/09/2024",
            "Hora de cita:": "3:00 p.m",
            "Id del cliente de la cita:": "186",
            "Id del empleado de la cita:": "144",
            "Servicio de la cita:": "Corte de pelo para mujer",
            "Estado de la cita:": "Pendiente"
        }
        for t,a in cita1300.items():
            print(t,a)

#creacion de objet0
objeto1300=Peluqueria1300()

# uso de objeto y llamada a funciones
print("\nDiccionario de la tabla sucursal")
objeto1300.diccionario_sucursal_datos1300()
print("\nDiccionario de la tabla empleado")
objeto1300.diccionario_empleado_datos1300()
print("\nDiccionario de la tabla cliente")
objeto1300.diccionario_cliente_datos1300()
print("\nDiccionario de la tabla cita")
objeto1300.diccionario_cita_datos1300()