from app.database.conexion import obtener_conexion

def iniciar_db():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_completo TEXT NOT NULL,
        usuario TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        empresa TEXT NOT NULL,
        rol TEXT DEFAULT 'operador',
        contrasenia TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        categoria TEXT DEFAULT 'General',
        precio REAL NOT NULL CHECK (precio >= 0),
        stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER NOT NULL,
        producto_nombre TEXT NOT NULL,
        cantidad_total INTEGER NOT NULL,
        cantidad_removida INTEGER NOT NULL,
        motivo TEXT,
        fecha DATETIME DEFAULT (DATETIME('now', 'localtime'))
    );
    """)

    conexion.commit()
    conexion.close()