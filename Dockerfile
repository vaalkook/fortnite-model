# Imagen base de Python
FROM python:3.12-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación y el modelo
COPY ./app.py /app/app.py
COPY ./model /app/model

# Exponer el puerto
EXPOSE 80

# Comando de inicio
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
