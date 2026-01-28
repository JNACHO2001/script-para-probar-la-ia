import requests

API_URL = "https://polyphyodont-elke-stuntingly.ngrok-free.dev/api/v1/analizar" # url local es http://localhost:8000/api/v1/analizar
API_KEY = "jogo_bonito_2001"

def analizar_texto(texto):
    response = requests.post(
        API_URL,
        headers={"X-API-Key": API_KEY},
        json={
            "texto": texto,
            "tarea": "analizar"  # Analiza el texto completo
        }
    )
    return response.json()["resultado"]

# Usar
mi_texto = """
hola cuanto es 2 +2
"""

resultado = analizar_texto(mi_texto)
print(resultado)