# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
##### Estudiante: Carla Juliana Giraldo Camacho
#
### Instrucciones para reproducir el experimento:
#
### Parte 1
#### La Secretaría está por firmar la compra de un servidor del doble de velocidad para que el proceso de Tamiza quepa en la ventana de cuatro horas. 
#### ¿Por qué debe analizarse primero el algoritmo, si el que está en producción lleva ocho años entregando el resultado correcto?

La Secretaría de Salud utilizando el software actual Tamiza, cumplen con la corrección: un algoritmo que ordene los casos de mayor a menor riesgo, pero, no cumple con la eficiencia temporal requerida de 4 horas. Es decir, la corrección garantiza el resultado, pero es totalmente aparte de los recursos computacionales y del tiempo necesarios para llegar a este.

La restricción que se incumple es la latencia máxima de ejecución de cuatro horas que nos mencionan tiene el sistema para cumplir su tarea. Y el duplicar la velocidad del servidor no resuelve el problema de fondo debido a que el crecimiento del tiempo de ejecución según la cantidad de datos es cuadrático. Por lo que, a pesar de que sea posible que aliviane (así sea mínimo) el problema, no es una solución que se mantenga a largo plazo. 

Para entenderlo mejor, si se duplica la velocidad es un factor de 2X, lo cual es un comportamiento lineal y es mucho menor al crecimiento cuadrático. 

Por ejemplo, un banco que adquiere los clientes de su competencia por compra de la misma (Banco de Bogotá e Itaú). La cantidad de clientes aumenta debido a la migración en aproximadamente 267.000 usuarios, con un promedio de depósitos totales de COP$4,1 billones.

Durante el cierre bancario nocturno, el sistema ejecuta un proceso para validar que no existan transacciones duplicadas o fraudulentas. Entonces, compara cada transacción contra el resto mediante un algoritmo de búsqueda y la restricción del sistema es una ventana de tiempo de 1:00am a 4:00am (3 horas) antes de reabrir las consultas.

Aunque se cumpla la identificación de duplicados y fraudes, comparar un promedio de 1'335.000 de registros más que en el pasado resulta en un incumplimiento de la ventana de tiempo que anteriormente servía. Lo que podría dejar la aplicación del banco fuera de servicio por más horas.
#
### Parte 2
#### Como responsable técnico de Tamiza, ¿qué responsabilidad ambiental y ética asume al decidir qué algoritmo de ordenamiento se ejecuta cada madrugada sobre los datos de 1.200.000 pacientes?

##### Ambiental:

El tiempo de ejecución del algoritmo se traduce en consumo de energía eléctrica y huella de carbono. En el caso del Insertion Sort (que tiene un Big O(n^2)) procesando 1'200.000 registros, el procesador opera al 100 % de su capacidad durante horas, manteniendo la CPU, los sistemas de refrigeración del centro de datos y la memoria RAM en su mayor demanda energética. Lo que significa que puede mantener un servidor encendido y a máxima carga durante 4 a 8 horas todas las madrugadas del año.

A largo plazo la diferencia entre ejecutarlo contra un algoritmo eficiente representa miles de kilovatios-hora desperdiciados. Y el comprar un servidor del doble de potencia para correrlo empeora la situación, ya que duplica el consumo eléctrico y la demanda de refrigeración, incrementando la huella ecológica de la Secretaría de Salud.

##### Ética:

Si el proceso nocturno no concluye a las 6:00am y el centro de contacto recibe una lista incompleta o desordenada, un paciente con un índice de riesgo alto podría quedar fuera o incluso al final de la lista y ser contactado días después. Un retraso de 24 a 48 horas en un tamizaje cardiovascular puede significar la diferencia entre una atención preventiva a tiempo y un evento grave (como un infarto).

Las consecuencias las asume el paciente, su familia, y el sistema de salud público. El paciente debido al riesgo de deterioro de su salud o muerte, y el sistema de salud costeando una atención a futuro mucho más compleja y costosa.

Si el algoritmo falla en la ordenación, no solo incumple en el tiempo, sino que en la equidad del programa. Un ordenamiento incorrecto perjudica el principio médico de atender primero a quien tiene mayor probabilidad de complicarse. Por esto el equipo técnico tiene la obligación ética de garantizar que el código se ejecute dentro de las 4 horas, y a su vez de verificar que la lógica de ordenamiento respete la prioridad del índice de riesgo.

