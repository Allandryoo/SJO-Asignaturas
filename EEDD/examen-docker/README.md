# Despliegue con Docker: Node.js, MongoDB, Flask y PostgreSQL

## 🐳 Parte 1: Docker Compose con Node.js y MongoDB

Se ha creado un archivo `docker-compose.yaml` que incluye:

### 🔹 Servicio Node.js
- Nombre del contenedor: `DoD`
- Imagen: `IT-CRM:v0.1`
- Como la imagen no existe, se utiliza `build: .` para construirla desde un `Dockerfile`
- Expone el puerto `3000`
- Depende del servicio MongoDB

### 🔹 Servicio MongoDB
- Imagen oficial: `mongo:latest`
- Usuario: `root`
- Contraseña: `DoD_CRM_DATABASE_25`
- Uso de volumen para persistencia de datos (`mongo-data`)

### 🔹 Red
- Red interna: `DoD-CRM-NETWORK` para comunicación entre contenedores

### 🔹 Volúmenes
- Se define un volumen para evitar pérdida de datos al reiniciar contenedores

---

## ⚙️ Dockerfile para Node.js

Se ha creado un `Dockerfile` para construir la imagen:

- Usa `node:18` como base
- Instala dependencias desde `package.json`
- Expone el puerto 3000
- Ejecuta la aplicación con `npm start`

---

## 🤖 Uso de Inteligencia Artificial

Se ha utilizado IA para:

- Diseñar el archivo `docker-compose.yaml`
- Configurar correctamente servicios, red y volúmenes
- Resolver la ausencia de la imagen con `build`
- Comprender la estructura de despliegue en Docker

---

## 🐍 Parte 2: Despliegue con Flask y PostgreSQL

Para levantar una aplicación Flask con PostgreSQL se requiere:

### 🔹 Contenedor Flask
- Aplicación en Python
- Archivo `Dockerfile`
- Dependencias en `requirements.txt` (Flask, psycopg2)

### 🔹 Contenedor PostgreSQL
- Imagen oficial de PostgreSQL
- Variables de entorno:
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `POSTGRES_DB`

### 🔹 Docker Compose
- Orquesta ambos servicios
- Define red compartida
- Usa `depends_on` para dependencias

### 🔹 Persistencia
- Uso de volumen para la base de datos

### 🔹 Conexión
- Flask se conecta usando el nombre del servicio como host (ej: `db`)
- Puerto: `5432`

---

## ✅ Conclusión

Se ha aprendido a:

- Contenerizar aplicaciones con Docker
- Usar Docker Compose para múltiples servicios
- Gestionar persistencia de datos
- Conectar aplicaciones con bases de datos en contenedores