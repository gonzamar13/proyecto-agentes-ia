from dotenv import load_dotenv
import requests
import os

class EvoAPI:
    def __init__(self, url_evoapi, api_key):
        self.url_evoapi = url_evoapi
        self.headers = {
                        "apikey":api_key, 
                        "Content-Type": "application/json"
                        }
        
    def create_instance(self, name_instance, token, qrcode, number, integration):
        url = f"{self.url_evoapi}/instance/create"  

        payload = {
                   "instanceName":name_instance, 
                   "token":token, 
                   "qrcode":qrcode, 
                   "number":number,
                   "integration": integration,
                    }
        respose = requests.post(url, json=payload, headers=self.headers)

        return respose.json()

load_dotenv()

URL_EVOAPI = os.getenv("BASE_URL")
KEY_EVOAPI = os.getenv("API_KEY_EVOLU")
NAME_INTANCE = "Nueva_intancia_prueba_1"
NUMBER_PHONE = "595991805304"
TOKEN = "JAKLJSD423490293J"
INTEGRATION = "WHATSAPP-BAILEYS"
QR = True

print(URL_EVOAPI)

api_client = EvoAPI(URL_EVOAPI, KEY_EVOAPI)
instance_create = api_client.create_instance(NAME_INTANCE, TOKEN, QR, NUMBER_PHONE, INTEGRATION)
print(instance_create)
    