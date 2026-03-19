🤖 AI Tutor — Chatbot con Avatar 3D

Tutor conversacional con avatar 3D animado, impulsado por Azure Speech Services y GPT-4.1.


📸 Demo

El avatar responde a los mensajes del usuario con síntesis de voz en tiempo real mediante Azure.
https://youtu.be/2OW0SeOO0dM


🧠 ¿Qué es esto?
AI Tutor es una aplicación web que combina:

Un backend de IA conversacional (Azure OpenAI / GPT-4.1) para procesar y responder preguntas del usuario
Un avatar 3D animado (Azure Avatar SDK) que habla las respuestas con síntesis de voz
Un servidor Flask que expone las credenciales de forma segura mediante variables de entorno
Un frontend personalizado en HTML/JS con panel de chat, controles de sesión e interacción en tiempo real

El proyecto explora la intersección entre servicios de IA en la nube, UX conversacional y síntesis de voz — todo corriendo localmente con una configuración sencilla.

🛠️ Stack Tecnológico
CapaTecnologíaModelo de LenguajeAzure OpenAI — GPT-4.1Voz y AvatarAzure Speech Services — Avatar SDKPlataforma CloudMicrosoft Azure (AI Foundry)BackendPython — FlaskFrontendJavaScript, HTML, CSSConfiguración.env con python-dotenv

📁 Estructura del Proyecto
AI-Tutor/
├── app.py              # Servidor Flask — sirve el frontend y expone el endpoint /config
├── config.json         # Configuración local opcional (no subir credenciales)
├── .env                # Variables de entorno — NO se sube al repo (ver .env.example)
├── static/             # CSS, JS, assets
└── templates/
    └── chat.html       # Interfaz principal del chat con avatar 3D

⚙️ Requisitos Previos

Python 3.9+
Una cuenta de Azure (la capa gratuita funciona — ~$200 de crédito en cuentas nuevas)
Recurso de Azure Speech Service desplegado en una de estas regiones:

westeurope
westus2
southeastasia


⚠️ La función de Avatar NO está disponible en todas las regiones de Azure. Asegúrate de usar una de las regiones listadas arriba.


Recurso de Azure OpenAI con un modelo desplegado (GPT-4.1 o GPT-3.5-Turbo)


🚀 Instalación y Configuración
1. Clonar el repositorio
bashgit clone https://github.com/Dfdragon12/AI-Tutor.git
cd AI-Tutor
2. Instalar dependencias
bashpip install flask python-dotenv
3. Configurar las credenciales
Crea un archivo .env en la raíz del proyecto:
envSPEECH_REGION=westeurope
SPEECH_KEY=tu_clave_de_azure_speech_aqui

OPENAI_ENDPOINT=https://tu-recurso.openai.azure.com/
OPENAI_KEY=tu_clave_de_azure_openai_aqui
OPENAI_DEPLOYMENT=gpt-4o   # o gpt-35-turbo

🔐 Nunca subas tu archivo .env al repositorio. El endpoint /config en Flask expone estos valores en tiempo de ejecución — tus claves nunca quedan expuestas en el código del frontend.

4. Ejecutar la aplicación
bashpython app.py
Abre tu navegador en: http://localhost:8000

🌐 Cómo Obtener tus Credenciales de Azure
Clave del Speech Service

Ve al Portal de Azure
Busca Speech Services → Crea un nuevo recurso
Selecciona la región West Europe (u otra región soportada)
Pricing tier: Standard S0
Una vez desplegado → Claves y Punto de Conexión → copia Clave 1

Clave y Endpoint de Azure OpenAI

Busca Azure OpenAI → Crea un recurso
Una vez desplegado → abre el portal de Azure AI Foundry
Ve a Implementaciones → Implementa un modelo base (GPT-4.1 o GPT-3.5-Turbo)
Copia la URL de destino (quita /chat/completions si aparece al final) y la Clave de API


💬 Funcionalidades

✅ Avatar 3D animado con sincronización de labios en tiempo real
✅ Respuestas en lenguaje natural vía GPT-4.1
✅ Panel de historial de chat
✅ Controles de inicio y cierre de sesión
✅ Carga segura de credenciales con Flask + .env
✅ Voz, idioma y estilo de avatar configurables


⚠️ Limitaciones Conocidas

La capa gratuita de Azure tiene límites de cuota en el deployment de OpenAI. Si envías solicitudes muy seguidas, puede aparecer el error 429 - Quota Exceeded. Espera ~30 segundos entre solicitudes o incrementa tu cuota.
La función de Avatar está restringida por región — solo disponible en westeurope, westus2 y southeastasia.


📚 Referencias
Este proyecto fue construido con apoyo del SDK oficial de Azure Avatar y el siguiente tutorial:
Azure AI Avatar — Chat Sample Setup
Repositorio oficial del SDK: Azure-Samples/cognitive-services-speech-sdk

👤 Autor
Diego Felipe Rodríguez Abondano
Analista de Infraestructura · Cloud & Seguridad · @dfra
LinkedIn · GitHub

📄 Licencia
Licencia MIT — libre para usar, modificar y compartir.
