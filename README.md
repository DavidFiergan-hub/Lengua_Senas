# 🤟 SignBridge AI

**Sistema Profesional de Consulta de Lenguaje de Señas Ecuatoriano**

SignBridge AI es una aplicación web moderna desarrollada en Python con Streamlit que permite consultar, buscar y aprender el lenguaje de señas ecuatoriano. El sistema incluye funcionalidades avanzadas de síntesis de voz, reconocimiento por voz y una interfaz intuitiva diseñada para facilitar el acceso a la información sobre señas.

## 📚 Contexto Académico

Este proyecto fue desarrollado como parte del **Samsung Innovation Hackathon**, un evento académico enfocado en crear soluciones tecnológicas innovadoras que mejoren la accesibilidad y la inclusión social. El objetivo principal es facilitar la comunicación entre personas oyentes y la comunidad sorda mediante tecnología de vanguardia.

## 🌟 Características Principales

- **🔍 Búsqueda Inteligente**: Sistema de búsqueda exacta y difusa (fuzzy matching) con algoritmos avanzados
- **🎤 Reconocimiento de Voz**: Búsqueda mediante comandos de voz usando Whisper AI
- **🔊 Síntesis de Voz**: Lectura automática de instrucciones de señas con gTTS
- **📱 Interfaz Responsiva**: Diseño moderno y profesional adaptable a diferentes dispositivos
- **🎲 Exploración Aleatoria**: Descubre nuevas señas de forma aleatoria
- **📊 Estadísticas en Tiempo Real**: Panel de control con métricas del sistema
- **🏗️ Arquitectura Modular**: Código organizado y mantenible con separación de responsabilidades
- **🎨 Interfaz Profesional**: CSS personalizado con tema moderno y accesible

## 🏗️ Estructura del Proyecto

```
SignBridge AI/
├── .venv/                      # Entorno virtual de Python
├── app.py                      # Aplicación principal de Streamlit
├── requirements.txt            # Dependencias del proyecto
├── setup.py                    # Configuración de instalación
├── señas_ecuatorianas.csv      # Base de datos de señas (187 entradas)
├── __init__.py                 # Inicialización del paquete
├── audio/                      # Módulo de procesamiento de audio
│   ├── speech_engine.py        # Motor de síntesis y reconocimiento de voz
│   └── __pycache__/           # Cache de Python
├── core/                       # Lógica central de la aplicación
│   ├── sign_processor.py       # Procesador de señas y búsquedas
│   └── __pycache__/           # Cache de Python
├── database/                   # Gestión de base de datos
│   ├── signs_database.py       # Interfaz de base de datos de señas
│   └── __pycache__/           # Cache de Python
├── utils/                      # Utilidades del sistema
│   ├── __init__.py            # Exportaciones del módulo
│   ├── config_utils.py        # Configuración de la aplicación
│   ├── file_utils.py          # Utilidades de archivos
│   ├── validation_utils.py    # Validación del sistema
│   └── __pycache__/           # Cache de Python
└── README.md                   # Documentación del proyecto
```

### 📁 Descripción Detallada de Módulos

#### 🎵 **audio/speech_engine.py**
- **Síntesis de voz**: Conversión de texto a voz usando gTTS
- **Reconocimiento de voz**: Transcripción de audio usando Whisper AI
- **Gestión de audio**: Reproducción y grabación de audio con pygame y sounddevice

#### 🧠 **core/sign_processor.py**
- **Algoritmos de búsqueda**: Búsqueda exacta y fuzzy matching
- **Procesamiento de resultados**: Cálculo de similitudes y confianza
- **Gestión de coincidencias**: Manejo de resultados exactos y aproximados

#### 🗄️ **database/signs_database.py**
- **Interfaz de datos**: Acceso a la base de datos CSV
- **Modelos de datos**: Definición de estructuras SignEntry
- **Operaciones CRUD**: Lectura y gestión de datos de señas

#### 🛠️ **utils/**
- **config_utils.py**: Configuración de audio, UI, base de datos y sistema
- **file_utils.py**: Gestión de archivos, directorios y backups
- **validation_utils.py**: Validación de dependencias y estructura del proyecto

## 🚀 Instalación y Configuración

### Prerrequisitos
- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Micrófono** (para funcionalidad de reconocimiento de voz)
- **Altavoces/Auriculares** (para síntesis de voz)

### Instalación Paso a Paso

#### Prerrequisitos
- Python 3.8 o superior instalado
- Git (opcional, para clonar el repositorio)

#### Instalación Completa

```bash
# 1. Clonar o descargar el proyecto
# Opción A: Con Git
git clone [URL_DEL_REPOSITORIO]
cd Señas_Samsung

# Opción B: Descargar ZIP y extraer
# Navegar al directorio extraído

# 2. Crear un entorno virtual nuevo
python -m venv .venv

# 3. Activar el entorno virtual
# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
# source .venv/bin/activate

# 4. Actualizar pip (recomendado)
python -m pip install --upgrade pip

# 5. Instalar todas las dependencias
pip install -r requirements.txt

# 6. Verificar la instalación
pip list

# 7. Ejecutar la aplicación
streamlit run app.py
```

#### Ejecución Rápida (si ya está instalado)

```bash
# 1. Navegar al directorio del proyecto
cd ruta/al/proyecto/Señas_Samsung

# 2. Activar el entorno virtual
# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
# source .venv/bin/activate

# 3. Ejecutar la aplicación
streamlit run app.py
```

### Configuración del Entorno

El proyecto incluye un entorno virtual preconfigurado (`.venv/`) con todas las dependencias necesarias:

- **Streamlit**: Framework web principal
- **Whisper AI**: Reconocimiento de voz avanzado
- **gTTS**: Síntesis de voz de Google
- **Pandas/NumPy**: Procesamiento de datos
- **FuzzyWuzzy**: Búsqueda aproximada
- **Pygame**: Reproducción de audio
- **SoundDevice**: Grabación de audio

## 🎮 Uso del Sistema

### 1. **Interfaz Principal**

La aplicación se ejecuta en `http://localhost:8501` y presenta:

- **Header profesional**: Título y descripción del sistema
- **Panel de control lateral**: Configuraciones y estadísticas
- **Interfaz de búsqueda**: Tres métodos de búsqueda disponibles
- **Resultados dinámicos**: Visualización de señas encontradas
- **Exploración aleatoria**: Descubrimiento de nuevas señas

### 2. **Métodos de Búsqueda**

#### 🎯 **Búsqueda Exacta**
- **Propósito**: Encuentra coincidencias exactas de palabras
- **Uso**: Ideal cuando conoces la palabra exacta
- **Ejemplo**: "hola" → Encuentra exactamente "hola"

#### 🔄 **Búsqueda Inteligente**
- **Propósito**: Encuentra coincidencias aproximadas usando fuzzy matching
- **Uso**: Útil para palabras con errores tipográficos
- **Ejemplo**: "ola" → Sugiere "hola"

#### 🎤 **Búsqueda por Voz**
- **Propósito**: Reconocimiento de voz usando Whisper AI
- **Uso**: Habla la palabra que deseas buscar
- **Proceso**: Grabación → Transcripción → Búsqueda automática

### 3. **Funcionalidades Avanzadas**

#### 🔊 **Síntesis de Voz**
- **Activación**: Checkbox en panel lateral
- **Funcionalidad**: Lee automáticamente las instrucciones de señas
- **Tecnología**: gTTS (Google Text-to-Speech)

#### 📊 **Panel de Estadísticas**
- **Total de señas**: 187 señas disponibles
- **Búsquedas realizadas**: Contador de sesión
- **Historial**: Últimas 5 búsquedas realizadas

#### 🎲 **Exploración Aleatoria**
- **Propósito**: Descubrir nuevas señas
- **Funcionalidad**: Selección aleatoria de la base de datos
- **Audio automático**: Reproducción de instrucciones

## 🗄️ Base de Datos de Señas Ecuatorianas

### Estadísticas de la Base de Datos
- **Total de entradas**: 187 señas
- **Formato**: CSV (señas_ecuatorianas.csv)
- **Estructura**: Palabra, Descripción
- **Codificación**: UTF-8

### Categorías de Señas Incluidas
- **Saludos**: Hola, Adiós, Buenos días, Buenas tardes, Buenas noches
- **Cortesía**: Gracias, Por favor, Perdón, Disculpe
- **Respuestas**: Sí, No, Tal vez
- **Necesidades**: Agua, Comer, Baño, Ayuda
- **Lugares**: Casa, Colegio, Trabajo
- **Familia**: Mamá, Papá, Hermano, Hermana
- **Números**: Uno, Dos, Tres, etc.
- **Colores**: Rojo, Azul, Verde, etc.
- **Acciones**: Caminar, Correr, Estudiar, etc.

### Estructura de Datos

Cada entrada incluye:
```csv
Palabra,Descripción
"Hola","La mano se levanta a la altura del hombro y se mueve de lado a lado."
"Gracias","Las manos se juntan frente al pecho y se inclinan hacia adelante."
```

### Ejemplos de Señas

#### Señas Básicas
- **Hola**: La mano se levanta a la altura del hombro y se mueve de lado a lado
- **Gracias**: Las manos se juntan frente al pecho y se inclinan hacia adelante
- **Adiós**: La mano se desplaza desde un costado de la frente hacia delante

#### Señas de Necesidades
- **Agua**: Gestos específicos para indicar sed o necesidad de agua
- **Comer**: Movimientos que simulan el acto de alimentarse
- **Baño**: La mano toca dos veces el antebrazo contrario

## 📊 Características Técnicas

### Arquitectura del Sistema
- **Patrón MVC**: Separación clara entre modelo, vista y controlador
- **Programación modular**: Cada funcionalidad en módulos independientes
- **Gestión de estado**: Uso de Streamlit session_state
- **Threading seguro**: Manejo de audio en hilos separados

### Tecnologías Utilizadas
- **Frontend**: Streamlit con CSS personalizado
- **Backend**: Python 3.8+
- **Base de datos**: CSV con pandas
- **IA/ML**: OpenAI Whisper, gTTS
- **Audio**: pygame, sounddevice
- **Búsqueda**: FuzzyWuzzy, Levenshtein

### Rendimiento
- **Tiempo de carga**: < 3 segundos
- **Búsqueda**: < 1 segundo para 187 entradas
- **Reconocimiento de voz**: 2-5 segundos
- **Síntesis de voz**: 1-3 segundos

### Compatibilidad
- **Sistemas operativos**: Windows, macOS, Linux
- **Navegadores**: Chrome, Firefox, Safari, Edge
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **Dispositivos**: Desktop, tablet, móvil

## 🐛 Solución de Problemas

### Problemas Comunes

#### Error de Dependencias
```bash
ModuleNotFoundError: No module named 'streamlit'
```
**Solución**: 
```bash
# Activar entorno virtual
.venv\Scripts\activate
# Reinstalar dependencias
pip install -r requirements.txt
```

#### Error de Audio
```bash
Error en reconocimiento de voz: No se pudo acceder al micrófono
```
**Solución**: 
- Verificar permisos de micrófono
- Comprobar que el micrófono esté conectado
- Reiniciar la aplicación

#### Puerto Ocupado
```bash
Port 8501 is already in use
```
**Solución**: 
```bash
streamlit run app.py --server.port 8502
```

#### Problemas de Codificación CSV
```bash
UnicodeDecodeError: 'utf-8' codec can't decode
```
**Solución**: 
- Verificar que el archivo CSV esté en UTF-8
- Usar un editor que soporte UTF-8

### Logs y Debugging
```bash
# Ejecutar con logs detallados
streamlit run app.py --logger.level=debug

# Verificar estructura del proyecto
python -c "from utils.validation_utils import run_comprehensive_validation; run_comprehensive_validation()"
```

### Validación del Sistema
El proyecto incluye utilidades de validación automática:
- Verificación de dependencias
- Validación de estructura de archivos
- Comprobación de sistema de audio
- Verificación de base de datos

## 🔧 Desarrollo y Contribución

### Configuración de Desarrollo
```bash
# Instalar dependencias de desarrollo
pip install pytest black isort sphinx

# Ejecutar tests
pytest

# Formatear código
black .
isort .

# Generar documentación
sphinx-build -b html docs/ docs/_build/
```

### Estructura de Testing
- **Unit tests**: Pruebas de módulos individuales
- **Integration tests**: Pruebas de integración entre módulos
- **UI tests**: Pruebas de interfaz de usuario

### Estándares de Código
- **PEP 8**: Estilo de código Python
- **Type hints**: Tipado estático
- **Docstrings**: Documentación de funciones
- **Logging**: Sistema de logs estructurado

## 📈 Roadmap y Mejoras Futuras

### Próximas Funcionalidades
- [ ] **Ampliación de base de datos**: Más señas ecuatorianas
- [ ] **Soporte multiidioma**: Español, inglés, quechua
- [ ] **Reconocimiento visual**: Detección de señas por cámara
- [ ] **Modo offline**: Funcionamiento sin conexión a internet
- [ ] **API REST**: Integración con otras aplicaciones
- [ ] **Aplicación móvil**: Versión nativa para smartphones

### Mejoras Técnicas
- [ ] **Optimización de rendimiento**: Carga más rápida
- [ ] **Base de datos externa**: PostgreSQL o MongoDB
- [ ] **Caché inteligente**: Mejora de velocidad de búsqueda
- [ ] **Análisis de uso**: Métricas y analytics
- [ ] **Seguridad**: Autenticación y autorización
- [ ] **Escalabilidad**: Soporte para múltiples usuarios

### Mejoras de UX/UI
- [ ] **Modo oscuro**: Tema alternativo
- [ ] **Personalización**: Configuración de usuario
- [ ] **Accesibilidad**: Mejoras para usuarios con discapacidades
- [ ] **Gamificación**: Sistema de logros y progreso
- [ ] **Comunidad**: Foro y comentarios de usuarios

## 📄 Licencia y Derechos

Este proyecto fue desarrollado como parte del **Samsung Innovation Hackathon** con fines académicos y educativos. 

### Uso Académico
- ✅ Permitido para investigación y educación
- ✅ Permitido para presentaciones académicas
- ✅ Permitido para desarrollo de tesis o proyectos estudiantiles

### Uso Comercial
- ⚠️ Requiere autorización previa
- ⚠️ Sujeto a términos del hackathon Samsung Innovation

## 👥 Equipo de Desarrollo

### Desarrollador Principal
- **Miguel** - Desarrollo Full Stack, Arquitectura del Sistema, Diseño de Interfaz

### Contribuciones Específicas
- **Arquitectura modular**: Diseño de estructura de proyecto escalable
- **Integración de IA**: Implementación de Whisper y gTTS
- **Base de datos**: Curación y estructuración de señas ecuatorianas
- **Interfaz de usuario**: Diseño responsivo y accesible
- **Documentación**: Documentación completa del proyecto
- **Testing**: Implementación de validaciones y pruebas

### Reconocimientos
- **Samsung Innovation**: Por proporcionar la plataforma del hackathon
- **Comunidad sorda ecuatoriana**: Por la información sobre señas
- **OpenAI**: Por la tecnología Whisper
- **Google**: Por la tecnología gTTS

## 📞 Contacto y Soporte

### Información del Proyecto
- **Nombre**: SignBridge AI - Sistema de Consulta de Lenguaje de Señas Ecuatoriano
- **Versión**: 2.0.0
- **Estado**: Proyecto académico activo
- **Contexto**: Samsung Innovation Hackathon

### Ubicación del Proyecto
- **Directorio**: `C:\Users\migue\OneDrive\Documents\Señas_Samsung`
- **Aplicación principal**: `app.py`
- **Base de datos**: `señas_ecuatorianas.csv`

### Soporte Técnico
Para reportar problemas o solicitar ayuda:
1. Verificar la sección [Solución de Problemas](#-solución-de-problemas)
2. Ejecutar validación del sistema: `python -c "from utils.validation_utils import run_comprehensive_validation; run_comprehensive_validation()"`
3. Revisar logs de la aplicación
4. Verificar dependencias: `pip list`

### Contribuciones
Si deseas contribuir al proyecto:
1. Revisar la estructura de código existente
2. Seguir los estándares de desarrollo establecidos
3. Documentar nuevas funcionalidades
4. Incluir pruebas para nuevas características

## 🙏 Agradecimientos

### Instituciones y Organizaciones
- **Samsung Innovation**: Por crear la plataforma del hackathon y fomentar la innovación tecnológica
- **Comunidad sorda ecuatoriana**: Por compartir conocimiento sobre el lenguaje de señas
- **Instituciones educativas**: Por promover proyectos de inclusión social

### Tecnologías y Herramientas
- **OpenAI**: Por Whisper, tecnología de reconocimiento de voz de vanguardia
- **Google**: Por gTTS, síntesis de voz accesible y de calidad
- **Streamlit**: Por el framework que hace posible interfaces web rápidas
- **Python Community**: Por las librerías y herramientas utilizadas

### Inspiración y Motivación
Este proyecto nace de la necesidad de crear puentes de comunicación entre la comunidad oyente y la comunidad sorda, promoviendo la inclusión social a través de la tecnología. Cada línea de código está dedicada a hacer el mundo más accesible y conectado.

---

**SignBridge AI** - Conectando mundos a través del lenguaje de señas 🤟

*Desarrollado con ❤️ para el Samsung Innovation Hackathon*  
*Tecnologías: Python • Streamlit • Whisper AI • gTTS • Machine Learning*

**"La tecnología al servicio de la inclusión social"**