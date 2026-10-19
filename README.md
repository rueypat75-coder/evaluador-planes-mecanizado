\# Evaluador automático de planes de mecanizado



Script en Python que evalúa un plan de pasadas de mecanizado contra una rúbrica de reglas, calcula una calificación por pieza y genera un reporte en archivo de texto.



\## Reglas de evaluación



| Regla | Criterio |

|---|---|

| Avance válido | El avance debe estar entre 100 y 800 mm/min |

| Longitud máxima | La longitud no puede superar 500 mm |

| Nombre presente | El nombre no puede estar vacío ni tener solo espacios |

| Tiempo correcto | El tiempo registrado debe coincidir con longitud ÷ avance, con tolerancia de 0.0001 |



Cada regla es una función que devuelve `True` o `False`.



\## Funcionamiento



1\. El plan es una lista de diccionarios, uno por pieza, con nombre, longitud, avance y tiempo.

2\. `evaluar\_pieza` aplica las cuatro reglas a cada pieza y cuenta cuántas se cumplen.

3\. El script imprime el resultado por pieza y genera `reporte\_evaluacion.txt` con la calificación general en porcentaje.



\## Ejecución



Requiere Python 3.8 o superior.



```bash

python evaluador\_planes.py

```



\## Ejemplo de salida



```

eje A: 4 de 4 reglas cumplidas

eje B: 3 de 4 reglas cumplidas

eje C: 3 de 4 reglas cumplidas

&#x20;    : 3 de 4 reglas cumplidas

Calificación general: 81.25%

```



\## Estructura



\- `evaluador\_planes.py`: reglas, evaluación y generación del reporte.

\- `reporte\_evaluacion.txt`: se genera al ejecutar el script.

