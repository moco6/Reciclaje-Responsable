# Reciclaje Responsable - Grupo 10

Una aplicación/juego para fomentar el reciclaje. Permite registrar usuarios, sumar puntos por reciclaje, canjear recompensas y ver rankings, usando una interfaz gráfica en Python (Tkinter).

## Descripción

Este proyecto simula un sistema de reciclaje con puntaje:

- Los usuarios registran reciclaje (papel, plástico, vidrio) e incrementan su puntaje.
- Los datos se guardan en archivos de texto (`usuarios.txt`, `reciclaje.txt`) como base de datos simple.
- Se pueden canjear recompensas usando puntos.
- Incluye historial de reciclaje por usuario y ranking general.
- Se pueden agregar fácilmente más tipos de basura modificando el código.
- Los valores de puntos asignados a cada tipo de basura son configurables para ajustar el sistema según se desee.

## Uso

- Ingresa el ID de usuario (carnet de Key).
- Especifica el tipo de basura para reciclar (papel, plástico o vidrio).
- Indica la cantidad (en unidades).
- Presiona "Registrar Reciclaje" para sumar puntos.

También puedes:

- Ver Usuarios: lista de usuarios con puntaje.
- Ver Historial: historial de reciclaje de un usuario.
- Canjear Recompensas: intercambia puntos por premios.
- Ver Ranking: muestra el ranking de usuarios por puntaje.

## Recompensas

| Recompensa          | Puntos         |
| ------------------- | -------------- |
| Bolsa ecológica     | 50             |
| Descuento en tienda | 100            |
| Entrada a evento    | 150            |

---

## Requisitos

- Python 3.8 o superior.
- Librería `tkinter` 

---

## Instalación y ejecución

1. Descarga este repositorio.
2. Asegúrate de tener Python instalado.
3. Ejecuta la aplicación con:

```bash
python app_basurero.py
```

## Integrantes del grupo 10
- Ever Alejandro Montes Quintanilla
- Juan Pablo Quinatnilla Acuña
- Juan Pablo Ramírez Cierra
- Mariana Mocan Ibáñez
- Jorge Nicolás Saade
