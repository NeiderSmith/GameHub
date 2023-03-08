## GameHub
Plataforma para la distribución de juegos online.

### Funcionalidades
---
- Ver catalogo de juegos
- Añadir nuevos juegos
- Editar juegos
- Eliminar juegos
- Ranking (por desarrollar)
- Numero de veces jugadas (por desarrollar)

### Guia de instalación
---
- Instalar docker
- En la consola de comandos ejecutar los siguientes comandos
```bash
docker compose build
docker compose up
```
- Esto habrá desplegado una instancia de base de datos postgres; un microservicio construido en Python con la libreria Flask; un servicio web construido en Angular