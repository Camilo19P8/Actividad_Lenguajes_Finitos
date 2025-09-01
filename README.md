# Actividad CADI: Operaciones con Lenguajes Finitos

**Grupo**: CRISTIAN CAMILO ALARCON DELGADILLO ; BRAYAN ARLEY SAENZ CORTES

## Proceso de trabajo

- Organización del grupo:
  -CRISTIAN CAMILO ALARCON DELGADILLO (rama-A)

  Revisar y pulir la sección Unión (ya hay script).
  Preparar README (portada, nombres, comandos).

  -BRAYAN ARLEY SAENZ CORTES (rama-B)

  Implementar Intersección (scripts + pruebas).
  Implementar Concatenación (scripts + pruebas).

- Comandos de Git usados por cada miembro (ejemplos):
  ```bash
  git checkout -b rama-a
  git add .
  git commit -m "Implementa unión y ejercicios"
  git push origin rama-a
  ```
- Resumen del flujo de Pull Request y revisión de código.

## Estructura del proyecto

```
.
├── lenguajes.py                # Funciones base y lenguajes L1..L5
└── scripts
    ├── union_ejercicios.py     # Rama 1: ejercicios resueltos de unión
    ├── interseccion_ejercicios.py  # Rama 2: plantilla
    └── concatenacion_ejercicios.py # Rama 3: plantilla
```

## Instrucciones de uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Camilo19P8/Actividad_Lenguajes_Finitos.git
   cd Actividad_Lenguajes_Finitos
   ```
2. Ejecutar los ejercicios de **unión**:
   ```bash
   python scripts/union_ejercicios.py
   ```
3. Ejecutar los ejercicios de **Intersección**:
   ```bash
   python scripts/Interseccion_ejercicios.py
   ```
4. Ejecutar los ejercicios de **Concatenación**:
   ```bash
   python scripts/Concatenación_ejercicios.py
   ```
