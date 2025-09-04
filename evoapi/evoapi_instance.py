from dotenv import load_dotenv
import requests
import os
from requests.exceptions import HTTPError, ConnectionError, RequestException, Timeout

class EvoAPI:
    def __init__(self, url_evoapi, api_key):
        self.url_evoapi = url_evoapi
        self.headers = {
                        "apikey":api_key, 
                        "Content-Type": "application/json"
                        }

    def _request(self, method:str , endpoint:str, **kwargs) -> dict:
            url = f"{self.url_evoapi}{endpoint}"  
            try: 
                response = requests.request(method, url, headers=self.headers, timeout=10, **kwargs)
                response.raise_for_status()
                return response.json()
            except HTTPError as http_error:
                return {"Error": f"HTTP error: {http_error}", "status": response.status_code}
            except ConnectionError:
                return {"Error": "No se pudo establecer contacto con el servidor de evoapi"}
            except Timeout:
                return {"Error": "La solicitud al servidor demoro demasiado y expiro"}
            except RequestException as req_err:
                return {"Error": f"Ocurrio un error inesperado: {req_err}"}

    def create_instance(self, name_instance, token, qrcode, number, integration):

        payload = {
                   "instanceName":name_instance, 
                   "token":token, 
                   "qrcode":qrcode, 
                   "number":number,
                   "integration": integration,
                    }
        
        return self._request("POST", "/instance/create", json=payload)
    
    def fetch_instances(self):
        return self._request("GET", "/instance/fetchInstances")

    def connect_instances(self, name_instance, number_phone): 
        querystring = {"number":number_phone}
        return self._request("GET", f"/instance/connect/{name_instance}", params=querystring)
        
    def qr_connect(self, name_instance:str):
        return self._request("GET", f"/instance/qr/{name_instance}")

load_dotenv()

URL_EVOAPI = os.getenv("BASE_URL")
KEY_EVOAPI = os.getenv("API_KEY_EVOLU")
NAME_INSTANCE = "Nueva_intancia_prueba_1"
NUMBER_PHONE = "595991805304"
TOKEN = "JAKLJSD423490293J"
INTEGRATION = "WHATSAPP-BAILEYS"
QR = True


api_instance = EvoAPI(URL_EVOAPI, KEY_EVOAPI)
conexion= api_instance.connect_instances(NAME_INSTANCE, NUMBER_PHONE)
consulta_qr = api_instance.qr_connect(NAME_INSTANCE)
print(conexion)
print(consulta_qr)
