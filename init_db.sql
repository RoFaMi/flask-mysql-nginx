CREATE TABLE IF NOT EXISTS mensajes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    mensaje VARCHAR(255) NOT NULL
);

INSERT INTO mensajes (mensaje) VALUES ('Hola mundo') ON DUPLICATE KEY UPDATE mensaje = 'Hola mundo';
