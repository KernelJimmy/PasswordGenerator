# Usamos la imagen base de Alpine
FROM alpine:latest

WORKDIR /app/

COPY passGen.py /app/

# Instala las dependencias necesarias para pyperclip y python3
RUN apk --no-cache add python3 && \
    apk add --no-cache py3-pip  && \
    apk add --no-cache xclip && \
    apk add --no-cache xauth && \
    pip install pyperclip colorama && \
    rm -rf /var/cache/apk/*

# Define el comando que se ejecutará cuando se inicie el contenedor
ENTRYPOINT ["python3","passGen.py"]
