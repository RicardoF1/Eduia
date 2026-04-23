Crear entorno virtual
python -m venv venv

Instalar Dependencias dentro del entorno virtual
pip install fastapi uvicorn pandas scikit-learn sqlalchemy pymysql python-multipart passlib[bcrypt] python-jose


Ejecutar 
uvicorn main:app --reload
npm start

Listar Dependencias instaladas
pip freeze

Crear archivo con las dependencias instaladas
pip freeze > requirements.txt

Activar Entorno Virtual 
venv\Scripts\activate