# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
#### Estudiante: Carla Juliana Giraldo Camacho

### Instrucciones para reproducir el experimento:

### Parte 1
#### La Secretaría está por firmar la compra de un servidor del doble de velocidad para que el proceso de Tamiza quepa en la ventana de cuatro horas. 
#### ¿Por qué debe analizarse primero el algoritmo, si el que está en producción lleva ocho años entregando el resultado correcto?

La Secretaría de Salud utilizando el software actual Tamiza, cumplen con la corrección: un algoritmo que ordene los casos de mayor a menor riesgo, pero, no cumple con la eficiencia temporal requerida de 4 horas. Es decir, la corrección garantiza el resultado, pero es totalmente aparte de los recursos computacionales y del tiempo necesarios para llegar a este.

La restricción que se incumple es la latencia máxima de ejecución de cuatro horas que nos mencionan tiene el sistema para cumplir su tarea. Y el duplicar la velocidad del servidor no resuelve el problema de fondo debido a que el crecimiento del tiempo de ejecución según la cantidad de datos es cuadrático. Por lo que, a pesar de que sea posible que aliviane (así sea mínimo) el problema, no es una solución que se mantenga a largo plazo. 

Para entenderlo mejor, si se duplica la velocidad es un factor de 2X, lo cual es un comportamiento lineal y es mucho menor al crecimiento cuadrático. 

Por ejemplo, un banco que adquiere los clientes de su competencia por compra de la misma (Banco de Bogotá e Itaú). La cantidad de clientes aumenta debido a la migración en aproximadamente 267.000 usuarios, con un promedio de depósitos totales de COP$4,1 billones.

Durante el cierre bancario nocturno, el sistema ejecuta un proceso para validar que no existan transacciones duplicadas o fraudulentas. Entonces, compara cada transacción contra el resto mediante un algoritmo de búsqueda y la restricción del sistema es una ventana de tiempo de 1:00am a 4:00am (3 horas) antes de reabrir las consultas.

Aunque se cumpla la identificación de duplicados y fraudes, comparar un promedio de 1'335.000 de registros más que en el pasado resulta en un incumplimiento de la ventana de tiempo que anteriormente servía. Lo que podría dejar la aplicación del banco fuera de servicio por más horas.
