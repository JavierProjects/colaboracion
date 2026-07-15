# Sistema de Análisis Académico

Proyecto de práctica para el curso de Python básico aplicado a Probabilidad y Estadística.

El objetivo es construir un sistema pequeño a partir de funciones simples. Cada función se implementa por separado y tiene su propio archivo de prueba.

---

## Reglas del proyecto

- Usar Python puro.
- No usar `pandas`.
- No usar `numpy`.
- No usar `statistics`.
- No usar `collections.Counter`.
- No modificar archivos dentro de `tests`.
- Las funciones deben regresar valores, no imprimir resultados.
- Trabajar siempre en una rama personal, no en `main`.

---

## Estructura del proyecto

```text
sistema_analisis_academico/
│
├── notebooks/
│   ├── 01_calificaciones_basicas.ipynb
│   ├── 02_estadistica_calificaciones.ipynb
│   ├── 03_asistencias.ipynb
│   ├── 04_encuestas.ipynb
│   └── 05_reportes.ipynb
│
├── src/
│   ├── calificaciones.py
│   ├── asistencias.py
│   ├── encuestas.py
│   └── reportes.py
│
├── tests/
│   ├── test_01_contar_calificaciones.py
│   ├── test_02_sumar_calificaciones.py
│   └── ...
│
└── README.md
```

---

## Flujo de trabajo del estudiante

1. Abrir el notebook correspondiente al tema.
2. Leer la función asignada.
3. Ubicar el archivo `.py` donde debe implementarse.
4. Implementar únicamente la función solicitada.
5. Ejecutar su archivo de prueba.
6. Corregir hasta que el test pase.

---

## Cómo ejecutar un test específico

Ejemplo:

```bash
python -m unittest tests/test_01_contar_calificaciones.py
```

---

## Cómo ejecutar todos los tests

```bash
python -m unittest discover tests
```

---

## Trabajo con Git

Cada estudiante debe trabajar en su propia rama.

Ejemplo:

```bash
git checkout -b Juan-RP
```

Para guardar avances:

```bash
git add .
git commit -m "Implementa función asignada"
```

---

## Actualizar notebooks y tests desde main

Cuando el profesor actualice el repositorio, el estudiante puede traer únicamente las carpetas `notebooks` y `tests`.

```bash
git fetch origin
git checkout main
git pull origin main
git checkout Juan-RP
git checkout main -- notebooks
git checkout main -- tests
git add notebooks tests
git commit -m "Actualiza notebooks y tests"
```

También puede usarse:

```bash
git restore --source main notebooks
git restore --source main tests
```

---

## Módulos

### Calificaciones

Funciones relacionadas con conteo, promedio, moda, mediana, aprobados, reprobados y resumen estadístico.

### Asistencias

Funciones para analizar asistencias de alumnos usando listas con `1` y `0`.

### Encuestas

Funciones para analizar respuestas de encuestas usando listas y diccionarios.

### Reportes

Funciones que integran resultados de distintos módulos.


## Notebooks del proyecto

| Notebook | Tema |
|---|---|
| `01_calificaciones_basicas.ipynb` | Conteo, suma, máximos, mínimos y clasificación |
| `02_estadistica_calificaciones.ipynb` | Promedio, porcentajes, frecuencia, moda, mediana y resumen |
| `03_asistencias.ipynb` | Análisis de asistencias |
| `04_encuestas.ipynb` | Análisis de respuestas |
| `05_reportes.ipynb` | Integración del sistema |

---

## Importante

Los tests son la forma de verificar que una función cumple con lo solicitado. Si un test falla, revisa primero:

- nombre de la función;
- tipo de dato que recibe;
- tipo de dato que debe regresar;
- casos con listas vacías;
- valores esperados en el notebook.
