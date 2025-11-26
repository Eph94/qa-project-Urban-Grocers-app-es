import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                        json=body,  # inserta el cuerpo de solicitud
                        headers=data.headers)  # inserta los encabezados

def get_user_token():
    response = post_new_user(data.user_body)

    #convertir a diccionario y obtener el auth_token
    response_json = response.json()
    auth_token = response_json['authToken']

    headers_token = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return headers_token


def post_new_kit(body):
    headers_token = get_user_token()
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                             json=body,  # inserta el cuerpo de solicitud
                             headers=headers_token)  # inserta los encabezados



