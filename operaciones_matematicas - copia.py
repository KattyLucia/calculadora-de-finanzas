#Operaciones matematicas 
salario = 925.83   #ingreso
alquiler = 110     #gasto1
comida= 350      #gasto2
transporte = 40 #gasto3
servicios_ba= 47
ropa= 15
entretenimiento =10
Porcentaje_ahorro = 0.20
aportecapsmec=30
gastos_mes_anterior= 500
copias =float(input("Ingrese dinero por copias :" ))
aseo=  float(input("Ingrese dinero por labores de aseo :"))
Total_ingresos= salario + copias + aseo
t_gastosvariables= ropa + entretenimiento
t_gastosfijos= alquiler + comida + transporte + servicios_ba + aportecapsmec
dinero_disponible= salario - t_gastosfijos
porcentaje_gasto=((t_gastosfijos+ t_gastosvariables) * 100 )/ salario
porcentaje_al=(alquiler * 100)/ salario
ahorro= salario * Porcentaje_ahorro
dinero_a_gastar= salario - ahorro    #
balance= dinero_a_gastar - t_gastosfijos - t_gastosvariables
gasto_mensual_actual= t_gastosfijos + t_gastosvariables   #comparar gastos
diferencia= gasto_mensual_actual - gastos_mes_anterior
gasto_diario= gasto_mensual_actual / 30
meta = 5000
Meta_ahorro= meta / ahorro
anual_gastosf= t_gastosfijos * 12
anual_gastosv= t_gastosvariables * 12
print("Sueldo:", salario)
print("Total de gasto: ", t_gastosfijos)
print("Dinero disponible: ", dinero_disponible)
print(f"Porcentaje de alquiler {porcentaje_al:.2f} % de tu ingreso")
print(f"Gastas el porcentaje de {porcentaje_gasto:.2f} % de tu ingreso")  #solo salga con dos decimales :.2f
print("Ahorro mensual:", ahorro)
print("Dinero para gastar:", dinero_a_gastar)
print("Balance de dinero sobrante:", balance)
print("Gastos actuales", gasto_mensual_actual)
if diferencia > 0: 
    print(f"Gastaste {diferencia } mas este mes")
else:
    print (f"Ahorraste {diferencia} este mes")
print("Gastas a diario: ", gasto_diario)
print(f"En {Meta_ahorro:.1f} meses alcanzaras la meta")
print(f"Se gasta un total de {anual_gastosf} en gastos fijos al año")
print(f"Se gasta un total de {anual_gastosv} en gastos variables al año")
print("Costo copias", copias)
print("Costo labores de aseo", aseo)
print("Total de ingresos :", Total_ingresos)