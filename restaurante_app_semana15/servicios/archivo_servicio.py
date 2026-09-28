import json
import os


class ArchivoServicio:
    def leer_json(self, ruta):
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos if isinstance(datos, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def guardar_json(self, ruta, datos):
        try:
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except OSError:
            return False
