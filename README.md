# Prueba-3-PGY-3121
- Nombre: Arnoldo Ramos
- curso: PROGRAMACIÓN WEB
- *DuocUc*

# comandos para levantar app
- git clone https://github.com/aramsac/Prueba-3-PGY-3121.git
- .\env\Scripts\activate (windows)
- source env/Scripts/activate
- pip install -r requirements.txt


# comandos para crear base del proyecto (windows)
- python -m venv env
- .\env\Scripts\activate
- pip install django
- django-admin startproject app
- cd app\app ; mkdir static , template , views
- cd template ; ni home.html , galeria.html , contacto.html , crear-usuario.html , mantenedor-usuario.html ;
- mkdir navbar ; cd navbar ; ni navbar.html
- sl ..\..\..\app\views\ ; ni home.py , galeria.py , contacto.py , crear-usuario.py , mantenedor-usuario.py
- sl ..\..\app\static\ ; mkdir js , css , img

- sl ..\..\ ; python -m manage runserver