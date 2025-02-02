-- Crear la tabla Ubicacion
CREATE TABLE Ubicacion (
    id_ubicacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ubicacion VARCHAR(255) NOT NULL,
    direccion TEXT,
    ciudad VARCHAR(100),
    pais VARCHAR(100)
);

-- Crear la tabla Dependencia
CREATE TABLE Dependencia (
    id_dependencia INT PRIMARY KEY AUTO_INCREMENT,
    nombre_dependencia VARCHAR(255) NOT NULL,
    descripcion TEXT,
    contacto VARCHAR(255),
    telefono_contacto VARCHAR(20)
);

-- Crear la tabla Ubicacion_Dependencia (relación entre Ubicacion y Dependencia)
CREATE TABLE Ubicacion_Dependencia (
    id_ubicacion INT NOT NULL,
    id_dependencia INT NOT NULL,
    PRIMARY KEY (id_ubicacion, id_dependencia),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicacion(id_ubicacion) ON DELETE CASCADE,
    FOREIGN KEY (id_dependencia) REFERENCES Dependencia(id_dependencia) ON DELETE CASCADE
);

-- Crear la tabla Inventario
CREATE TABLE Inventario (
    id_inventario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    tipo_elemento VARCHAR(100),
    estado VARCHAR(50),
    fecha_adquisicion DATE,
    id_ubicacion INT NOT NULL,
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicacion(id_ubicacion)
);

-- Crear la tabla Detalles_Tecnicos
CREATE TABLE Detalles_Tecnicos (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_inventario INT NOT NULL,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    numero_serie VARCHAR(255) UNIQUE NOT NULL,
    sistema_operativo VARCHAR(100),
    version_firmware VARCHAR(100),
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) 
);

-- Crear la tabla Configuracion
CREATE TABLE Configuracion (
    id_configuracion INT PRIMARY KEY AUTO_INCREMENT,
    id_inventario INT NOT NULL,
    descripcion TEXT,
    parametros_personalizados TEXT,
    ultima_actualizacion DATE,
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) 
);

-- Crear la tabla Mantenimiento
CREATE TABLE Incidentes (
    id_incidentes INT PRIMARY KEY AUTO_INCREMENT,
    id_inventario INT NOT NULL,
    fecha_mantenimiento DATE,
    tipo_mantenimiento VARCHAR(100),
    descripcion TEXT,
    realizado_por VARCHAR(255),
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) ON DELETE CASCADE
);

-- Crear la tabla Historial_Cambios
CREATE TABLE Historial_cambios (
    id_historial INT PRIMARY KEY AUTO_INCREMENT,
    id_inventario INT NOT NULL,
    fecha_cambio DATE,
    cambio_realizado TEXT,
    realizado_por VARCHAR(255),
    FOREIGN KEY (id_inventario) REFERENCES Inventario(id_inventario) ON DELETE CASCADE
);

