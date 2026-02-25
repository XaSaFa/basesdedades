-- Script de configuración de base de datos y usuario para MariaDB
-- Ejecutar como root: mysql -u root -p < setup_database.sql

-- Crear usuario para la aplicación
CREATE USER IF NOT EXISTS 'aventura_user'@'localhost' IDENTIFIED BY 'Aventura2024!';

-- Otorgar permisos sobre la base de datos Aventura
GRANT SELECT, INSERT, UPDATE, DELETE ON Aventura.* TO 'aventura_user'@'localhost';

-- Aplicar cambios
FLUSH PRIVILEGES;

-- Verificar que las tablas existen
USE Aventura;
SHOW TABLES;

-- Mostrar estructura de las tablas
DESCRIBE localitzacions;
DESCRIBE canins;
