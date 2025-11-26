# 🚀 Urban Grocers – API Test Suite
Autor: Enrique Palomares Hurtado
Cohort: 38 – TripleTen Sprint 7

Suite de pruebas automatizadas para validar la funcionalidad del servicio Urban Grocers API, utilizando Python + Pytest + Requests.
El proyecto valida parámetros, códigos de estado y comportamiento esperado al crear kits de usuarios/as.


📌 Objetivo del Proyecto

Automatizar pruebas funcionales para los endpoints de Urban Grocers.
Validar comportamiento positivo y negativo al crear un kit (parámetro name).
Garantizar que los requests enviados cumplen con los requerimientos del sistema.
Detectar TCs que no cumplen con los criterios esperados (fallos intencionales para el ejercicio).
Consolidar buenas prácticas en estructuras de proyectos de QA Automation.

🛠️ Tecnologías utilizadas
Python 3.x
Pytest
Requests (librería para API testing)
Git / GitHub
IDE recomendado: PyCharm

📂 Estructura del Proyecto
├── configuration.py          # URLs y paths del servicio
├── create_kit_name_kit_test.py   # Archivo principal con los test cases (TCs)
├── data.py                   # Diccionarios y payloads para los requests
├── sender_stand_request.py   # Funciones que envían requests a la API
└── resources/                # Carpeta opcional para archivos adicionales

▶️ Cómo ejecutar el proyecto
1. Clonar el repositorio
git clone https://github.com/Eph94/qa-project-Urban-Grocers-app-es.git
2. Instalar dependencias
Necesitas tener instalado pytest y requests:
pip install pytest requests
3. Ejecutar los tests
Ubícate en la raíz del proyecto y corre:
pytest
4. Ejecutar tests individuales
En PyCharm:
Run → Edit Configurations → Add new Pytest configuration
Elige el archivo:
create_kit_name_kit_test.py

🧪 Descripción de los Test Cases
Los tests del ejercicio se encuentran en:
create_kit_name_kit_test.py
Incluye:
✔️ Tests positivos
✔️ Tests negativos
❌ Tests diseñados para fallar (según instrucciones del sprint)
Test cases que fallan intencionalmente:
Los siguientes TCs no cumplen el criterio esperado, por lo que el resultado final es fallido:
Tercero
Cuarto
Octavo
Noveno
Total: 4 TCs fallidos (esperado para el ejercicio).


🔧 Archivos clave
📌 data.py
Contiene todos los payloads y diccionarios necesarios para enviar los requests correctamente.
📌 configuration.py
Incluye las URLs y paths del servicio:
URL_SERVICE
CREATE_USER_PATH
CREATE_KIT_PATH
⚠️ Nota: Es necesario actualizar URL_SERVICE con un endpoint vigente del API Urban Grocers.
📌 sender_stand_request.py
Contiene todas las funciones que envían requests HTTP hacia el servicio, utilizadas por los tests.

📝 Conclusión

Este proyecto demuestra conocimientos sólidos en:
Testing de APIs
Validación positiva/negativa
Automatización con Pytest
Manejo de payloads
Buenas prácticas de estructura en proyectos de QA
Uso de Git y control de versiones