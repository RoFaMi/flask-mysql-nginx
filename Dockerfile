FROM python:3.11-alpine

WORKDIR /app

# Instalar dependencias del sistema necesarias para MySQL client
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev

# Copiar requirements y instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY app.py .
COPY init_db.sql .

EXPOSE 5000

# Espera un poco a MySQL, luego ejecuta la app
CMD ["python", "app.py"]
