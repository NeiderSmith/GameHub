## GameHub
A continuación una lista de los pasos necesarios para inicializar aplicación.

### Inicialización de base de datos
---
- Inicializar un contenedor de base de datos postgres
```bash
docker run --name gamehub -p 5432:5432 -e POSTGRES_DB=gamehub -e POSTGRES_PASSWORD=password -d postgres
```

### Inicialización de backend
---
- Tener instalado python
- Tener instalado pipenv
- Crear entorno virtual pipenv en el directorio "backend/" e instalar dependencias
```bash
pipenv install sqlalchemy psycopg2-binary flask_cors
```
- Ejecutar bash script "start.sh" para iniciar aplicación (Asegurarse de que el archivo posea permisos de ejecución)
```bash
./start.sh
```

### Inicialización de frontend
---
- Tener instalado NodeJs 19.7.0
- Tener instalado Angular CLI 15.2.1
- Ubicarse dentro de la carpeta "frontend/videogames-front" y correr los comandos
```bash
npm install
ng serve
```
