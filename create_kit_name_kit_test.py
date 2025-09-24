import sender_stand_request
import data
from data import kit_body


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["name"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit_body = get_user_body(first_name)

    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["name"] == kit_body["name"]

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_code_400(kit_body):
    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    user_response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert user_response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert user_response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert user_response.json()["message"] == 'Unexpected token \'"\', "#" is not valid JSON'



# Primer Test Case Description: El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_user_1_letter_in_first_name_get_success_response():
    positive_assert("a")

# Segundo Test Case Description: El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Tercer Test Case Description: 	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_user_3_letter_in_first_name_get_negative_response():
    negative_assert_code_400("")

# Cuarto Test Case Description: 	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_creatte_user_4_letter_in_first_name_get_negative_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Quinto Test Case Description: Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_user_5_letter_in_first_name_get_success_response():
    positive_assert("\"№%@\",")

# Sexto Test Case Description: Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_user_6_letter_in_first_name_get_success_response():
    positive_assert("A Aaa")

# Septimo Test Case Description: Se permiten números: kit_body = { "name": "123" }
def test_create_user_7_letter_in_first_name_get_success_response():
    positive_assert("123")

# Octavo Test Case Description: El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_user_8_letter_in_first_name_get_success_response():
    negative_assert_code_400("")

# Noveno Test Case Description: Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_user_9_letter_in_first_name_get_success_response():
    negative_assert_code_400(123)