import mysql.connector

conexion = mysql.connector.connect(
    host="bhdzotv7tpsf41t3miag-mysql.services.clever-cloud.com",
    user="uvcwgvm3y0jtyagn",
    password="kQnH3nJbpNqWwB52vQFR",
    database="bhdzotv7tpsf41t3miag"
)
if conexion.is_connected():
    print("conexion exitosa")
    
