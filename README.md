# Crypto Data Stream: Análisis de Mercado en Tiempo Real con Apache Kafka y Python
## 🚀 Resumen del Proyecto
Este proyecto presenta una solución robusta y escalable para el streaming y análisis de datos de mercado de criptomonedas en tiempo real.
Aprovechando Apache Kafka para una ingesta de datos fiable y Python para el procesamiento, se capturan actualizaciones de precios en vivo desde la API de Binance.
Esto establece una arquitectura fundamental para el monitoreo de mercado en tiempo real, trading algorítmico o aplicaciones analíticas avanzadas.

Esta configuración ejemplifica principios clave de ingeniería de datos a la vez que sienta las bases para el análisis y visualización de datos de alto volumen en tiempo real.

## ✨ Características Clave y Tecnologías
Ingesta de Datos en Tiempo Real: Captura datos de precios de criptomonedas en vivo desde la API de Binance.

Procesamiento Asíncrono: Utiliza asyncio para un manejo eficiente de flujos de datos concurrentes.

Broker de Mensajes: Emplea Apache Kafka como un broker de mensajes de alto rendimiento y tolerante a fallos para una entrega de datos fiable.

Serialización de Datos: Serializa datos eficientemente usando json para los mensajes de Kafka.

Contenerización: Usa Docker Compose para orquestar los servicios de Kafka, Zookeeper y los scripts Python (productor/consumidor), asegurando una implementación sencilla y consistencia del entorno.

Python: Lenguaje principal para la adquisición de datos (productor) y el procesamiento (consumidor).

## 🛠️ Stack Tecnológico
Lenguajes: Python 🐍

Plataforma de Streaming: Apache Kafka

Orquestación: Docker Compose, Docker

Integración de API: Binance WebSocket API

Librerías: websocket-client, json, asyncio, confluent-kafka (consumidor)

## 📂 Estructura del Proyecto
crypto_data_Stream/
├── docker-compose.yml              # Define los servicios para Kafka, Zookeeper, Productor, Consumidor
├── producer.py                     # Script Python para obtener datos de Binance API y enviarlos a Kafka
├── consumer.py                     # Script Python para consumir datos de Kafka y procesarlos
└── README.md                       # Documentación del proyecto (este archivo)

##🚀 Cómo Ejecutar Localmente
Para poner en marcha este flujo de datos criptográficos en tiempo real en tu máquina, sigue estos sencillos pasos:

Clona el repositorio:

Bash

git clone https://github.com/alexmamani01/crypto_data_Stream.git
cd crypto_data_Stream
Asegúrate de que Docker esté en ejecución: Verifica que Docker Desktop o tu demonio de Docker esté activo.

Inicia los servicios:

Bash

docker-compose up --build
Este comando:

Construirá las imágenes Docker de producer y consumer.

Iniciará un contenedor de Zookeeper (requerido por Kafka).

Iniciará un contenedor de broker de Kafka.

Iniciará el contenedor producer.py, que comenzará a obtener datos de Binance y a enviarlos al tema binance_topic de Kafka.

Iniciará el contenedor consumer.py, que leerá los mensajes del tema binance_topic y los imprimirá en la consola (verás el flujo de datos en tiempo real).

Monitorea la salida:
Verás los logs del producer indicando que se están enviando datos, y los logs del consumer mostrando los datos de criptomonedas en tiempo real que se reciben y procesan.

Detén los servicios:

Bash

docker-compose down
## 🔮 Mejoras Futuras
Almacenamiento de Datos: Integrar con una base de datos (ej. PostgreSQL, MongoDB, Data Lake) para el almacenamiento persistente de los datos transmitidos.

Dashboard en Tiempo Real: Conectar el flujo de Kafka a una herramienta de visualización (ej. Power BI, Tableau, Grafana) para un dashboard en vivo.

Detección de Anomalías: Implementar algoritmos de detección de anomalías en tiempo real sobre los datos consumidos.

Escalabilidad: Explorar la escalabilidad de clústeres de Kafka y el despliegue en plataformas cloud (AWS MSK, Confluent Cloud).

##👋 ¡Conectemos!
¡No dudes en explorar el código, contribuir o contactarme si tienes alguna pregunta o idea de colaboración!
