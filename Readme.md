# Backend – API REST con Django

## 📄 Descripción
API REST desarrollada con Django y Django REST Framework.
Implementa autenticación mediante JWT y expone endpoints protegidos que son consumidos por un frontend en React.

Este backend forma parte de un proyecto full stack orientado a aprendizaje y portfolio profesional.

## 🚀 Funcionalidades
- API REST con Django REST Framework
- Autenticación JWT
- Endpoints protegidos
- Gestión de usuarios
- Integración con frontend React
- Configuración CORS

## 🛠️ Tecnologías utilizadas
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- django-cors-headers

## ▶️ Cómo ejecutar el proyecto

### 1. Crear entorno virtual
```bash
python -m venv venv

### 2. Activar entorno virtual
En Windows:
bash
venv\Scripts\activate

En Linux / Mac:
bash
source venv/bin/activate

### 3. Instalar dependencias
bash
pip install -r requirements.txt

### 4. Ejecutar migraciones
bash
python manage.py migrate

### 5. Crear superusuario (opcional)
bash
python manage.py createsuperuser

### 6. Ejecutar servidor
bash
python manage.py runserver

La API estará disponible en:
http://127.0.0.1:8000

🔐 Autenticación
La API utiliza JWT para proteger los endpoints.
El token se obtiene a través del endpoint de login y debe enviarse en la cabecera Authorization.

🔗 Frontend del proyecto
https://github.com/Luis100704/frontend-react-ts

