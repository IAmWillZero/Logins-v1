# Sistema de Autenticación Django

Un sistema completo de autenticación de usuarios construido con Django que incluye registro de usuarios, inicio de sesión, cierre de sesión, restablecimiento de contraseña y gestión de perfil.

## 📋 Características

- ✅ Registro de usuario con email y contraseña
- ✅ Inicio y cierre de sesión de usuario
- ✅ Funcionalidad de restablecimiento de contraseña
- ✅ Página de perfil para usuarios autenticados
- ✅ Diseño responsivo usando Bootstrap 5
- ✅ Vistas protegidas solo para usuarios autenticados
- ✅ Configuración completa de Docker para desarrollo y producción

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.8 o superior
- pip (instalador de paquetes de Python)

### Instalación

1. **Clona el repositorio**
    ```bash
    git clone <url-del-repositorio>
    cd Logins-v1
    ```

2. **Crea y activa un entorno virtual**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # macOS/Linux
    ```

3. **Instala las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecuta las migraciones**
    ```bash
    python manage.py migrate
    ```

5. **Crea un superusuario (opcional)**
    ```bash
    python manage.py createsuperuser
    ```

6. **Ejecuta el servidor**
    ```bash
    python manage.py runserver
    ```

7. **Abre tu navegador**
    - Aplicación principal: http://127.0.0.1:8000
    - Panel de administración: http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
Logins-v1/
├── accounts/                 # Aplicación de cuentas de usuario
│   ├── migrations/           # Migraciones de base de datos
│   ├── __init__.py
│   ├── admin.py             # Configuración de administrador
│   ├── apps.py              # Configuración de aplicación
│   ├── models.py            # Modelos de base de datos
│   ├── tests.py             # Pruebas
│   └── views.py             # Vistas
├── config/                  # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Configuraciones
│   ├── urls.py             # URLs principales
│   └── wsgi.py
├── static/                  # Archivos estáticos
├── templates/               # Plantillas HTML
├── requirements.txt         # Dependencias de Python
├── .gitignore               # Archivos ignorados por Git
├── .env                     # Variables de entorno
└── manage.py                # Script de gestión de Django
```

## 🌐 URLs Disponibles

- `/` - Página de inicio
- `/login/` - Inicio de sesión
- `/logout/` - Cierre de sesión
- `/register/` - Registro de usuario
- `/profile/` - Perfil de usuario (requiere login)
- `/password_change/` - Cambiar contraseña
- `/password_reset/` - Restablecer contraseña
- `/admin/` - Panel de administración

## 🔧 Personalización

### Estilos
Modifica las clases de Bootstrap en las plantillas o agrega CSS personalizado en `static/`.

### Modelo de Usuario
Para campos personalizados:
1. Crea un modelo que extienda `AbstractUser`
2. Actualiza `AUTH_USER_MODEL` en `settings.py`
3. Crea y ejecuta migraciones

## 📝 Notas

- El archivo `.env` contiene variables de entorno sensibles
- Para producción, configura `DEBUG=False` y un dominio en `ALLOWED_HOSTS`
- Usa SQLite para desarrollo rápido o configura PostgreSQL/MySQL para producción

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT.
