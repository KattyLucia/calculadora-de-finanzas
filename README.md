 Calculadora de Finanzas Personales
Sistema de gestión y análisis de finanzas personales que permite calcular gastos, ingresos, ahorros y proyecciones financieras mensuales.
📋 Descripción
Este programa en Python ayuda a gestionar las finanzas personales mediante el cálculo automático de:

Gastos fijos y variables
Porcentaje de ingresos destinado a gastos
Ahorro mensual
Balance disponible
Comparación con el mes anterior
Proyección de metas de ahorro
Gastos anuales estimados

✨ Características

Cálculo de gastos fijos: alquiler, comida, transporte, servicios básicos, aportes
Cálculo de gastos variables: ropa, entretenimiento
Ingresos adicionales: permite ingresar ingresos por copias y labores de aseo
Análisis de porcentajes: calcula qué porcentaje del ingreso representa cada categoría
Sistema de ahorro: calcula ahorro automático del 20% del salario
Comparación temporal: compara gastos con el mes anterior
Proyección de metas: estima cuántos meses tomará alcanzar una meta de ahorro
Proyección anual: calcula gastos totales anuales

🛠️ Requisitos

Python 3.x

No se requieren bibliotecas externas, solo la instalación básica de Python.
📥 Instalación

Clona o descarga este repositorio
Asegúrate de tener Python 3 instalado en tu sistema
Navega al directorio donde guardaste el archivo

🚀 Uso
Ejecuta el script desde la terminal o línea de comandos:
bashpython finanzas_personales.py
El programa te solicitará ingresar dos valores:

Dinero por copias: Ingreso adicional por servicios de copias
Dinero por labores de aseo: Ingreso adicional por servicios de limpieza

Ejemplo de ejecución
Ingrese dinero por copias: 50
Ingrese dinero por labores de aseo: 100
Salida esperada
El programa mostrará:

Sueldo base
Total de gastos fijos
Dinero disponible después de gastos fijos
Porcentaje del ingreso destinado a alquiler
Porcentaje total gastado
Ahorro mensual
Dinero disponible para gastar
Balance sobrante
Comparación con mes anterior
Gasto diario promedio
Meses necesarios para alcanzar meta de ahorro
Proyección de gastos anuales
Total de ingresos del mes

📊 Configuración
Puedes modificar los valores predeterminados en el código según tus necesidades:
pythonsalario = 925.83              # Tu salario base
alquiler = 110                # Costo de alquiler
comida = 350                  # Presupuesto de comida
transporte = 40               # Gasto en transporte
servicios_ba = 47             # Servicios básicos
ropa = 15                     # Presupuesto de ropa
entretenimiento = 10          # Presupuesto de entretenimiento
Porcentaje_ahorro = 0.20      # Porcentaje de ahorro (20%)
aportecapsmec = 30            # Aporte a caja/seguro
gastos_mes_anterior = 500     # Gastos del mes anterior
meta = 5000                   # Meta de ahorro
📈 Funcionalidades Detalladas
Cálculos Principales

Total de ingresos: Suma salario + ingresos adicionales
Gastos fijos: Suma de alquiler, comida, transporte, servicios y aportes
Gastos variables: Suma de ropa y entretenimiento
Ahorro automático: 20% del salario base
Balance mensual: Dinero restante después de gastos y ahorro
Proyección de meta: Tiempo estimado para alcanzar meta de $5000

Análisis Comparativo
El programa compara los gastos del mes actual con el mes anterior y te indica si:

Gastaste más dinero este mes
Ahorraste en comparación al mes anterior

🔧 Posibles Mejoras Futuras

Guardar histórico de gastos en archivo
Interfaz gráfica (GUI)
Gráficos de gastos por categoría
Alertas cuando se excede el presupuesto
Exportación de reportes a PDF o Excel
Múltiples perfiles de usuario
Categorías de gastos personalizables

📝 Notas

El porcentaje de ahorro está fijado en 20% del salario base
La meta de ahorro predeterminada es de $5000
Los cálculos anuales asumen gastos constantes cada mes

👤 Autor
Proyecto de gestión financiera personal
📄 Licencia
Este proyecto es de código abierto y está disponible para uso personal y educativo.

Consejo: Revisa y ajusta tus gastos mensualmente para mantener un control efectivo de tus finanzas. ¡El ahorro constante es la clave! 💪
