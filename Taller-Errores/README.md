\# Taller – Detección de Errores y Tecnologías RS232



Este repositorio contiene el desarrollo de los puntos del taller relacionados con detección de errores, patentes de tecnologías RS232 y ejemplos de algoritmos de detección de errores.



---



\## 1. Tipos de detectores de errores



Existen diferentes mecanismos para verificar la integridad de la información transmitida en un canal de comunicación:



| Método                  | Descripción                                                                 | Ventajas                                    | Desventajas |

|-------------------------|-----------------------------------------------------------------------------|---------------------------------------------|-------------|

| \*\*Bit de paridad\*\*      | Se agrega un bit adicional para que la cantidad de 1’s sea par o impar.     | Simplicidad, bajo costo computacional.      | Solo detecta errores de 1 bit, no corrige. |

| \*\*Checksum\*\*            | Se suman los datos transmitidos y se envía la suma como verificador.        | Útil en redes y almacenamiento.             | Baja fiabilidad ante errores complejos. |

| \*\*CRC (Cyclic Redundancy Check)\*\* | Usa divisiones polinomiales para detectar errores múltiples en bloques de datos. | Muy robusto y usado en Ethernet, USB.       | No corrige, solo detecta. |

| \*\*Código de Hamming\*\*   | Introduce redundancia que permite \*\*detectar y corregir\*\* ciertos errores.  | Capacidad de corrección de 1 bit.           | Aumenta la redundancia de datos. |



---



\## 2. Patentes y tecnologías con RS232



Aunque RS232 es un estándar antiguo, aún se utiliza en diversas áreas. Tras revisar documentación técnica y registros de patentes, se identifican aplicaciones actuales:



1\. \*\*Automatización industrial\*\*  

&nbsp;  - Uso en PLCs y máquinas heredadas que aún dependen de comunicación serie.  

&nbsp;  - Ejemplo: Patentes de controladores industriales con puertos RS232 para diagnóstico.  



2\. \*\*Instrumentación médica\*\*  

&nbsp;  - Monitores de signos vitales, bombas de infusión y otros dispositivos transmiten datos por RS232.  

&nbsp;  - Permite compatibilidad con sistemas antiguos de registro hospitalario.  



3\. \*\*Sistemas de puntos de venta (POS)\*\*  

&nbsp;  - Lectores de códigos de barras, balanzas electrónicas y datáfonos.  

&nbsp;  - Su fiabilidad y bajo costo mantienen su uso en la industria.  



👉 Esto demuestra que RS232, pese a ser una tecnología de los años 60, sigue teniendo relevancia en aplicaciones críticas y de bajo nivel.



---



\## 3. Algoritmo de detección de errores



Ejemplo en \*\*Python\*\* de detección simple con \*\*paridad\*\*:



```python

def calcular\_paridad(bits):

&nbsp;   """Devuelve 1 si el número de 1's es impar, 0 si es par"""

&nbsp;   return sum(bits) % 2



\# Ejemplo de envío

datos = \[1, 0, 1, 1]  # 4 bits de datos

bit\_paridad = calcular\_paridad(datos)

paquete = datos + \[bit\_paridad]

print("Paquete transmitido:", paquete)



\# Ejemplo de recepción

recepcion = paquete.copy()

\# Simulamos error en un bit

recepcion\[2] = 0

print("Paquete recibido:", recepcion)



\# Verificación

if calcular\_paridad(recepcion\[:-1]) == recepcion\[-1]:

&nbsp;   print("Datos correctos ✅")

else:

&nbsp;   print("Error detectado ❌")

Salida esperada:



Paquete transmitido: \[1, 0, 1, 1, 1]

Paquete recibido:    \[1, 0, 0, 1, 1]

Error detectado ❌





👉 Se puede ampliar el ejemplo con CRC o Hamming, según el nivel de complejidad requerido.



4\. Documentación



Overleaf: Se redactará un documento formal en formato IEEE explicando los puntos anteriores con mayor detalle, diagramas y referencias bibliográficas.



GitHub: Este README resume la teoría, ejemplos y código de apoyo.



Conclusiones



La detección de errores es fundamental para garantizar la integridad de los datos.



Aunque existen métodos sencillos como la paridad, algoritmos más robustos como CRC o Hamming son preferidos en sistemas críticos.



RS232, pese a ser una tecnología antigua, mantiene aplicaciones prácticas en la industria, salud y comercio.



El trabajo combina teoría, ejemplos prácticos en Python y documentación técnica.

