# TAULES

Per a fer el nostre projecte (a nivell bàsic) necessitem dues taules: localitzacions i camins.

La taula localitzacions guarda la informació de cada sala visitable durant el joc, té la següent estructura:

<img width="614" height="167" alt="image" src="https://github.com/user-attachments/assets/16b6e268-68c8-4a27-8082-3724ad5a1c9d" />

La taula camins indica els camins possibles entre diferents localitzacions, ja siguin portes, accés natural per un passadís... I té la següent estructura:

<img width="639" height="146" alt="image" src="https://github.com/user-attachments/assets/0b6b11f1-5485-4bee-a84e-5bb3679cd855" />

Amb aquestes dues taules ja tenim prou per fer l'estructura bàsica del nostre projecte.

Tabla localitzacions

```
CREATE TABLE IF NOT EXISTS localitzacions (
    id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    descripcio BLOB,
    imatge VARCHAR(250),
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

Tabla camins

```
CREATE TABLE IF NOT EXISTS camins (
    id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    localitzacio1 BIGINT(20) UNSIGNED NOT NULL,
    localitzacio2 BIGINT(20) UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    KEY idx_localitzacio1 (localitzacio1),
    KEY idx_localitzacio2 (localitzacio2),
    CONSTRAINT fk_camins_localitzacio1 FOREIGN KEY (localitzacio1) REFERENCES localitzacions(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_camins_localitzacio2 FOREIGN KEY (localitzacio2) REFERENCES localitzacions(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
