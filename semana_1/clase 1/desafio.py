# Facturación del Servicio de Agua Potable
# El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y
#  establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
# Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido.
#  Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
# A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.
# Tarifa base:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.
# Bonificaciones y Recargos según tipo de cliente:
# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.


# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.


# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.


# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.
# Requerimientos del programa:
# Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
# Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
# Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.

cargo_fijo = 7000
costo_metro = 200
iva = 21

metro_cubico = int(input("Ingrese el consumo (en m³): "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): ")


costo_final_metro = metro_cubico * costo_metro
calculo = cargo_fijo + costo_final_metro
calculo_iva = calculo * iva / 100
precio_iva = calculo_iva + calculo

recargo = 0
descuento = 0 

match tipo_cliente:
    case "Residencial":
        if metro_cubico < 30:
            descuento = calculo * 0.10
            precio_final = precio_iva - descuento
            print(f"Felicidades! Te ganaste un descuento del 10%!\n En total es ${precio_final}")
        elif metro_cubico > 80:
            recargo = calculo * 0.15
            precio_final = precio_iva + recargo
            print(f"Se te aplico un recargo del 15%\n El precio final es: ${precio_final}")
            if calculo <= 35000:
                descuento = precio_final * 0.05
                precio_final_caso = precio_iva - descuento
                print(f"Felicidades! Te ganaste un descuento adicional del 5%!\n En total es ${precio_final_caso}")
            # print(f"El precio final es de ${precio_iva} ")
    case "Comercial":
        if metro_cubico >= 150:
            descuento = calculo * 0.08
            precio_final = precio_iva - descuento
            print(f"Felicidades! Te ganaste un descuento del 8%!\n En total es ${precio_final}")
        elif metro_cubico >= 300:
            descuento = calculo * 0.12
            precio_final = precio_iva - descuento
            print(f"Felicidades! Te ganaste un descuento del 12%!\n En total es ${precio_final}")
        elif metro_cubico <= 50:
            recargo = calculo * 0.05
            precio_final = precio_iva + recargo
            print(f"Se te aplico un recargo del 5%\n El precio final es: ${precio_final}")
        else:
            print(f"El precio final es de ${precio_iva} ")
    case "Industrial":
        if metro_cubico >= 500:
            descuento = calculo * 0.20
            precio_final = precio_iva - descuento
            print(f"Felicidades! Te ganaste un descuento del 20%!\n En total es ${precio_final}")
        elif metro_cubico >= 1000:
            descuento = calculo * 0.30
            precio_final = precio_iva - descuento
            print(f"Felicidades! Te ganaste un descuento del 30%!\n En total es ${precio_final}")
        elif metro_cubico <= 200:
            recargo = calculo * 0.10
            precio_final = precio_iva + recargo
            print(f"Se te aplico un recargo del 10%\n El precio final es: ${precio_final}")
        else:
            print(f"El precio final es de ${precio_iva} ")


print("---Factura---")
print(f"El consumo: {calculo}")
print(f"Precio total (con IVA): {precio_iva} ")