# 🤟 Signify - Sistema Multilingüe de Traductor de Lengua de Señas

## 📋 Descripción del Proyecto

**Signify** es una plataforma web profesional e inclusiva que facilita el aprendizaje y traducción de lengua de señas en **tres variantes regionales**: ecuatoriana, chilena y mexicana. Desarrollado como proyecto colaborativo, integra tecnologías de inteligencia artificial para ofrecer una experiencia de usuario moderna, accesible y educativa.

### 🎯 Objetivo Principal

Crear un puente de comunicación tecnológico que permita a personas oyentes y con discapacidad auditiva acceder fácilmente a información sobre señas, promoviendo la inclusión social y el aprendizaje intercultural de las lenguas de señas latinoamericanas.

## ✨ Características Principales

### 🌍 **Soporte Multilingüe**
- **Lengua de Señas Ecuatoriana**: 187+ señas documentadas
- **Lengua de Señas Chilena**: Base de datos especializada
- **Lengua de Señas Mexicana**: Variante regional incluida
- **Análisis Comparativo**: Comparación entre variantes regionales

### 🤖 **Inteligencia Artificial Integrada**
- **Reconocimiento de Voz**: Tecnología OpenAI Whisper
- **Síntesis de Voz**: Google Text-to-Speech (gTTS)
- **Búsqueda Inteligente**: Algoritmos de fuzzy matching
- **Procesamiento de Lenguaje Natural**: Análisis semántico avanzado

### 🔍 **Métodos de Búsqueda Avanzados**
- **Búsqueda Exacta**: Coincidencias precisas por palabra
- **Búsqueda Inteligente**: Tolerancia a errores tipográficos
- **Búsqueda por Voz**: Comando de voz con IA
- **Búsqueda por Categorías**: Organización temática
- **Exploración Aleatoria**: Descubrimiento de nuevas señas

### 📊 **Análisis y Estadísticas**
- **Panel de Control**: Métricas en tiempo real
- **Historial de Búsquedas**: Seguimiento de consultas
- **Análisis Comparativo**: Diferencias entre variantes
- **Estadísticas de Uso**: Datos de interacción del usuario

## 🚀 Instalación y Configuración

### Prerrequisitos del Sistema

- **Python**: 3.8 o superior
- **Sistema Operativo**: Windows, macOS, Linux
- **Memoria RAM**: Mínimo 4GB (recomendado 8GB)
- **Espacio en Disco**: 2GB libres
- **Conexión a Internet**: Para funcionalidades de IA

### 📥 Clonar el Repositorio

```bash
# Clonar el proyecto
git clone https://github.com/tu-usuario/signify-lengua-senas.git

# Navegar al directorio del proyecto
cd signify-lengua-senas
```

### 🔧 Configuración del Entorno

#### Instalación Completa (Recomendada)

```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno virtual
# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
source .venv/bin/activate

# 3. Actualizar pip
python -m pip install --upgrade pip

# 4. Instalar todas las dependencias
pip install -r requirements.txt

# 5. Verificar instalación
pip list
```

#### Instalación Mínima (Solo dependencias esenciales)

```bash
# Instalar solo dependencias críticas
pip install streamlit plotly pandas numpy python-dateutil gtts pygame sounddevice openai-whisper fuzzywuzzy python-Levenshtein
```

### ▶️ Ejecutar la Aplicación

```bash
# Ejecutar Signify
streamlit run app.py

# La aplicación estará disponible en:
# http://localhost:8501
```

#### Opciones de Ejecución Avanzadas

```bash
# Ejecutar en puerto específico
streamlit run app.py --server.port 8502

# Ejecutar con configuración personalizada
streamlit run app.py --server.headless true --server.enableCORS false

# Ejecutar con logs detallados
streamlit run app.py --logger.level=debug
```

## 🎮 Guía de Uso

### 1. **Interfaz Principal**

Al acceder a `http://localhost:8501`, encontrarás:

- **Header Profesional**: Título y descripción del sistema
- **Selector de Idioma**: Cambio entre variantes de señas
- **Panel Lateral**: Configuraciones y estadísticas
- **Área de Búsqueda**: Múltiples métodos de consulta
- **Resultados Dinámicos**: Visualización interactiva de señas

### 2. **Métodos de Búsqueda**

#### 🎯 **Búsqueda Exacta**
```
Entrada: "hola"
Resultado: Coincidencia exacta de la seña "hola"
Uso: Cuando conoces la palabra precisa
```

#### 🧠 **Búsqueda Inteligente (Fuzzy)**
```
Entrada: "ola" (con error tipográfico)
Resultado: Sugiere "hola" con 85% de similitud
Uso: Tolerancia a errores de escritura
```

#### 🎤 **Búsqueda por Voz**
```
Proceso: Hablar → Whisper AI → Transcripción → Búsqueda
Tecnología: OpenAI Whisper
Idiomas: Español (múltiples acentos)
```

### 3. **Funcionalidades Multilingües**

#### 🌎 **Comparación entre Variantes**
- **Vista Paralela**: Comparar señas entre países
- **Análisis de Diferencias**: Identificar variaciones regionales
- **Estadísticas Comparativas**: Métricas de similitud

#### 🔊 **Síntesis de Voz Multilingüe**
- **Activación**: Checkbox en panel lateral
- **Idiomas**: Español (Ecuador, Chile, México)
- **Funcionalidad**: Lectura automática de instrucciones

### 4. **Panel de Estadísticas**

#### 📊 **Métricas en Tiempo Real**
- **Total de Señas**: Contador por idioma
- **Búsquedas Realizadas**: Estadísticas de sesión
- **Historial Reciente**: Últimas 10 consultas
- **Tiempo de Respuesta**: Métricas de rendimiento

## 🗄️ Base de Datos Multilingüe

### Estadísticas Generales
- **Total de Entradas**: 200+ señas
- **Idiomas Soportados**: 3 variantes regionales
- **Formato**: CSV con codificación UTF-8
- **Estructura**: Palabra, Descripción, Categoría

### Distribución por Idioma

#### 🇪🇨 **Lengua de Señas Ecuatoriana**
- **Archivo**: `señas_ecuatorianas.csv`
- **Entradas**: 187 señas
- **Categorías**: 12 temáticas principales
- **Cobertura**: Vocabulario básico y avanzado

#### 🇨🇱 **Lengua de Señas Chilena**
- **Archivo**: `señas_chilenas.csv`
- **Entradas**: 10 señas base
- **Enfoque**: Señas fundamentales y saludos
- **Características**: Variaciones regionales específicas

#### 🇲🇽 **Lengua de Señas Mexicana**
- **Archivo**: `señas_mexicanas.csv`
- **Entradas**: 10 señas base
- **Enfoque**: Comunicación básica
- **Características**: Adaptaciones culturales mexicanas

### Estructura de Datos

```csv
Palabra,Descripción,Categoría
"Hola","La mano se levanta a la altura del hombro y se mueve de lado a lado","Saludos"
"Gracias","Las manos se juntan frente al pecho y se inclinan hacia adelante","Cortesía"
"Buenos Días","Se coloca una letra b sobre el corazón y se mueve al frente","Saludos"
```

### Categorías Temáticas

#### 👋 **Saludos y Cortesía**
- Hola, Adiós, Buenos días, Buenas tardes, Buenas noches
- Gracias, Por favor, Perdón, Disculpe

#### 👨‍👩‍👧‍👦 **Familia y Relaciones**
- Mamá, Papá, Hermano, Hermana, Hijo, Hija
- Abuelo, Abuela, Tío, Tía, Primo, Prima

#### 🔢 **Números y Colores**
- Números del 1 al 20
- Colores básicos: Rojo, Azul, Verde, Amarillo, etc.

#### 🏃‍♂️ **Acciones y Verbos**
- Caminar, Correr, Estudiar, Trabajar, Comer, Beber
- Leer, Escribir, Escuchar, Ver, Hablar

#### 🏠 **Lugares y Necesidades**
- Casa, Colegio, Trabajo, Hospital, Baño
- Agua, Comida, Ayuda, Emergencia

## 📊 Arquitectura Técnica

### Estructura del Proyecto

```
Lengua_Senas/
├── app.py                      # Aplicación principal Streamlit
├── requirements.txt            # Dependencias del proyecto
├── señas_ecuatorianas.csv     # Base de datos ecuatoriana
├── señas_chilenas.csv         # Base de datos chilena
├── señas_mexicanas.csv        # Base de datos mexicana
├── analysis/                   # Módulos de análisis
│   ├── comparative_analysis.py # Análisis comparativo
│   └── statistical_analysis.py # Análisis estadístico
├── audio/                      # Procesamiento de audio
│   ├── speech_engine.py       # Motor de síntesis de voz
│   └── voice_recognition.py   # Reconocimiento de voz
├── core/                       # Lógica central
│   ├── sign_processor.py      # Procesador de señas
│   └── search_engine.py       # Motor de búsqueda
├── database/                   # Gestión de datos
│   └── signs_database.py      # Base de datos de señas
├── utils/                      # Utilidades
│   ├── file_utils.py          # Utilidades de archivos
│   ├── validation_utils.py    # Validaciones del sistema
│   └── ui_utils.py            # Utilidades de interfaz
└── .venv/                      # Entorno virtual
```

### Tecnologías Utilizadas

#### 🖥️ **Frontend y UI**
- **Streamlit**: Framework web principal
- **Plotly**: Visualizaciones interactivas
- **CSS Personalizado**: Diseño profesional
- **Responsive Design**: Adaptable a dispositivos

#### 🧠 **Inteligencia Artificial**
- **OpenAI Whisper**: Reconocimiento de voz avanzado
- **Google gTTS**: Síntesis de voz multilingüe
- **FuzzyWuzzy**: Búsqueda aproximada inteligente
- **Levenshtein**: Cálculo de distancia de cadenas

#### 📊 **Procesamiento de Datos**
- **Pandas**: Manipulación de datos CSV
- **NumPy**: Operaciones numéricas
- **SciPy**: Algoritmos científicos
- **Scikit-learn**: Machine Learning

#### 🔊 **Audio y Multimedia**
- **Pygame**: Reproducción de audio
- **SoundDevice**: Captura de audio del micrófono
- **PyAudio**: Procesamiento de audio en tiempo real

### Patrones de Diseño

#### 🏗️ **Arquitectura Modular**
- **Separación de Responsabilidades**: Cada módulo tiene una función específica
- **Inyección de Dependencias**: Gestión centralizada de instancias
- **Patrón Singleton**: Instancias únicas para recursos compartidos

#### 🔄 **Gestión de Estado**
- **Streamlit Session State**: Persistencia de datos de sesión
- **Caché Inteligente**: Optimización de consultas repetidas
- **Threading Seguro**: Manejo concurrente de audio

### Rendimiento y Optimización

#### ⚡ **Métricas de Rendimiento**
- **Tiempo de Carga Inicial**: < 3 segundos
- **Búsqueda de Señas**: < 1 segundo (200+ entradas)
- **Reconocimiento de Voz**: 2-5 segundos
- **Síntesis de Voz**: 1-3 segundos
- **Análisis Comparativo**: < 2 segundos

#### 🚀 **Optimizaciones Implementadas**
- **Carga Lazy**: Módulos cargados bajo demanda
- **Caché de Resultados**: Almacenamiento temporal de búsquedas
- **Compresión de Datos**: Optimización de archivos CSV
- **Threading Asíncrono**: Procesamiento paralelo de audio

## 🔧 Desarrollo y Contribución

### Configuración de Desarrollo

```bash
# Instalar dependencias de desarrollo
pip install pytest black isort sphinx mypy

# Ejecutar tests
pytest tests/ -v

# Formatear código
black . --line-length 88
isort . --profile black

# Verificar tipos
mypy . --ignore-missing-imports

# Generar documentación
sphinx-build -b html docs/ docs/_build/
```

### Estándares de Código

#### 📝 **Convenciones de Python**
- **PEP 8**: Estilo de código estándar
- **Type Hints**: Tipado estático obligatorio
- **Docstrings**: Documentación completa de funciones
- **Logging**: Sistema de logs estructurado

#### 🧪 **Testing y Calidad**
- **Unit Tests**: Cobertura mínima 80%
- **Integration Tests**: Pruebas de módulos integrados
- **UI Tests**: Validación de interfaz de usuario
- **Performance Tests**: Pruebas de rendimiento

### Estructura de Testing

```bash
tests/
├── unit/                       # Pruebas unitarias
│   ├── test_database.py       # Tests de base de datos
│   ├── test_search_engine.py  # Tests de búsqueda
│   └── test_audio_processing.py # Tests de audio
├── integration/                # Pruebas de integración
│   ├── test_full_workflow.py  # Flujo completo
│   └── test_multilingual.py   # Funcionalidad multilingüe
└── ui/                         # Pruebas de interfaz
    ├── test_streamlit_app.py   # Tests de Streamlit
    └── test_user_interactions.py # Interacciones de usuario
```

## 🐛 Solución de Problemas

### Problemas Comunes y Soluciones

#### ❌ **Error de Dependencias**
```bash
ModuleNotFoundError: No module named 'streamlit'
```
**Solución:**
```bash
# Verificar entorno virtual activo
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstalar dependencias
pip install -r requirements.txt
```

#### 🎤 **Error de Audio/Micrófono**
```bash
Error en reconocimiento de voz: No se pudo acceder al micrófono
```
**Soluciones:**
1. Verificar permisos de micrófono en el sistema
2. Comprobar que el micrófono esté conectado y funcionando
3. Reiniciar la aplicación
4. Verificar drivers de audio actualizados

#### 🌐 **Puerto Ocupado**
```bash
Port 8501 is already in use
```
**Solución:**
```bash
# Usar puerto alternativo
streamlit run app.py --server.port 8502

# O terminar proceso existente
# Windows: taskkill /f /im streamlit.exe
# macOS/Linux: pkill -f streamlit
```

#### 📄 **Problemas de Codificación CSV**
```bash
UnicodeDecodeError: 'utf-8' codec can't decode
```
**Soluciones:**
1. Verificar que archivos CSV estén en UTF-8
2. Usar editor que soporte UTF-8 (VS Code, Notepad++)
3. Reconvertir archivos: `iconv -f ISO-8859-1 -t UTF-8 archivo.csv > archivo_utf8.csv`

### Validación del Sistema

```bash
# Ejecutar validación completa
python -c "from utils.validation_utils import run_comprehensive_validation; run_comprehensive_validation()"

# Verificar estructura del proyecto
python -c "from utils.file_utils import validate_project_structure; validate_project_structure()"

# Test de conectividad de audio
python -c "from audio.voice_recognition import test_microphone; test_microphone()"
```

### Logs y Debugging

```bash
# Ejecutar con logs detallados
streamlit run app.py --logger.level=debug

# Ver logs en tiempo real
tail -f ~/.streamlit/logs/streamlit.log  # macOS/Linux
Get-Content -Path "$env:USERPROFILE\.streamlit\logs\streamlit.log" -Wait  # Windows

# Habilitar modo debug en la aplicación
export STREAMLIT_DEBUG=true  # macOS/Linux
set STREAMLIT_DEBUG=true     # Windows
```

## 📈 Roadmap y Mejoras Futuras

### 🎯 **Próximas Funcionalidades (v2.1)**
- [ ] **Ampliación de Base de Datos**: 500+ señas por idioma
- [ ] **Reconocimiento Visual**: Detección de señas por cámara web
- [ ] **Modo Offline**: Funcionamiento sin conexión a internet
- [ ] **Gamificación**: Sistema de logros y progreso de aprendizaje
- [ ] **Comunidad**: Foro integrado y comentarios de usuarios

### 🚀 **Mejoras Técnicas (v2.2)**
- [ ] **API REST**: Endpoints para integración externa
- [ ] **Base de Datos Externa**: PostgreSQL/MongoDB
- [ ] **Caché Redis**: Optimización de rendimiento
- [ ] **Microservicios**: Arquitectura distribuida
- [ ] **Docker**: Containerización completa

### 🌟 **Expansión Regional (v3.0)**
- [ ] **Más Países**: Argentina, Colombia, Perú, Venezuela
- [ ] **Lenguas Indígenas**: Quechua, Guaraní, Mapuche
- [ ] **Certificación**: Validación con instituciones oficiales
- [ ] **Aplicación Móvil**: iOS y Android nativas
- [ ] **Realidad Aumentada**: Visualización 3D de señas

### 🎨 **Mejoras de UX/UI (v2.3)**
- [ ] **Modo Oscuro**: Tema alternativo profesional
- [ ] **Personalización**: Configuración de usuario avanzada
- [ ] **Accesibilidad**: WCAG 2.1 AA compliance
- [ ] **PWA**: Progressive Web App
- [ ] **Multiidioma UI**: Interfaz en español, inglés, portugués

## 📄 Licencia y Uso

### Licencia del Proyecto

Este proyecto se distribuye bajo **Licencia MIT**, permitiendo uso libre con atribución.

```
MIT License

Copyright (c) 2024 Signify Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

### Uso Permitido

#### ✅ **Uso Académico y Educativo**
- Investigación y desarrollo académico
- Proyectos estudiantiles y tesis
- Presentaciones en conferencias
- Material educativo y cursos

#### ✅ **Uso Comercial**
- Integración en productos comerciales
- Servicios de consultoría
- Desarrollo de aplicaciones derivadas
- Uso empresarial interno

#### ⚠️ **Restricciones**
- Mantener atribución original
- No usar marca "Signify" sin autorización
- Respetar derechos de terceros (OpenAI, Google)

## 👥 Equipo de Desarrollo

### Información del Proyecto
- **Nombre**: Signify - Sistema Multilingüe de Consulta de Lengua de Señas
- **Versión**: 2.0.0
- **Estado**: Proyecto colaborativo activo
- **Tipo**: Aplicación web educativa e inclusiva

### Contribuciones del Equipo

#### 🏗️ **Arquitectura y Desarrollo**
- **Diseño de Sistema**: Arquitectura modular y escalable
- **Backend Development**: Lógica de negocio y procesamiento
- **Frontend Development**: Interfaz de usuario con Streamlit
- **Database Design**: Estructura multilingüe de datos

#### 🤖 **Integración de IA**
- **Whisper AI**: Implementación de reconocimiento de voz
- **gTTS Integration**: Sistema de síntesis de voz
- **NLP Processing**: Algoritmos de búsqueda inteligente
- **Machine Learning**: Análisis comparativo automatizado

#### 📊 **Análisis y Datos**
- **Data Curation**: Recopilación y estructuración de señas
- **Statistical Analysis**: Métricas y análisis comparativo
- **Performance Optimization**: Optimización de rendimiento
- **Quality Assurance**: Testing y validación

#### 📚 **Documentación y UX**
- **Technical Documentation**: Documentación completa del código
- **User Experience**: Diseño de interfaz accesible
- **Testing Framework**: Implementación de pruebas automatizadas
- **Deployment**: Configuración de entorno y despliegue

## 📞 Contacto y Soporte

### Información de Contacto

- **Proyecto**: Signify v2.0.0
- **Repositorio**: [GitHub - Signify](https://github.com/tu-usuario/signify-lengua-senas)
- **Documentación**: [Docs Online](https://signify-docs.readthedocs.io)
- **Demo en Vivo**: [signify-demo.streamlit.app](https://signify-demo.streamlit.app)

### Soporte Técnico

#### 🆘 **Reportar Problemas**
1. Verificar [Sección de Solución de Problemas](#-solución-de-problemas)
2. Ejecutar validación del sistema
3. Revisar logs de la aplicación
4. Crear issue en GitHub con detalles completos

#### 💡 **Solicitar Funcionalidades**
1. Revisar roadmap actual
2. Verificar que no exista solicitud similar
3. Crear feature request detallado
4. Participar en discusiones de la comunidad

#### 🤝 **Contribuir al Proyecto**
1. Fork del repositorio
2. Crear branch para nueva funcionalidad
3. Seguir estándares de código establecidos
4. Incluir tests para nuevas características
5. Crear pull request con descripción detallada

### Recursos Adicionales

#### 📖 **Documentación Técnica**
- [API Reference](docs/api-reference.md)
- [Development Guide](docs/development.md)
- [Deployment Guide](docs/deployment.md)
- [Contributing Guidelines](CONTRIBUTING.md)

#### 🎓 **Recursos Educativos**
- [Tutorial de Uso](docs/tutorial.md)
- [Guía de Lengua de Señas](docs/sign-language-guide.md)
- [Videos Demostrativos](https://youtube.com/signify-tutorials)
- [Webinars y Talleres](docs/workshops.md)

## 🙏 Reconocimientos

### Tecnologías y Herramientas

#### 🤖 **Inteligencia Artificial**
- **OpenAI**: Por Whisper, tecnología revolucionaria de reconocimiento de voz
- **Google**: Por gTTS, síntesis de voz accesible y de alta calidad
- **Hugging Face**: Por modelos de procesamiento de lenguaje natural

#### 🛠️ **Frameworks y Librerías**
- **Streamlit**: Por facilitar el desarrollo de aplicaciones web interactivas
- **Python Community**: Por el ecosistema de librerías científicas
- **Pandas Team**: Por herramientas de manipulación de datos
- **SciPy Community**: Por algoritmos científicos avanzados

#### 🎨 **Diseño y UX**
- **Material Design**: Por principios de diseño accesible
- **Accessibility Guidelines**: Por estándares de inclusión digital
- **Open Source Community**: Por recursos de diseño libre

### Inspiración y Propósito

Este proyecto nace del compromiso con la **inclusión social** y la **accesibilidad digital**. Cada línea de código está dedicada a construir puentes de comunicación entre comunidades, promoviendo un mundo más conectado e inclusivo a través de la tecnología.

### Impacto Social

**Signify** representa más que una aplicación técnica; es una herramienta de **transformación social** que:

- 🌍 **Conecta Culturas**: Facilita el intercambio entre variantes regionales de lengua de señas
- 🎓 **Democratiza el Aprendizaje**: Hace accesible el conocimiento de señas a cualquier persona
- 🤝 **Promueve la Inclusión**: Reduce barreras de comunicación entre comunidades
- 🚀 **Impulsa la Innovación**: Demuestra el potencial de la IA para el bien social

---

## 🌟 Conclusión

**Signify v2.0.0** representa la evolución de un proyecto académico hacia una plataforma profesional de impacto social. Con soporte para **tres variantes regionales** de lengua de señas, tecnologías de **inteligencia artificial** de vanguardia, y un enfoque centrado en la **accesibilidad universal**, Signify se posiciona como una herramienta transformadora para la educación inclusiva.

### Próximos Pasos

1. **Expandir la Base de Datos**: Incorporar más señas y países
2. **Mejorar la IA**: Optimizar algoritmos de reconocimiento
3. **Fortalecer la Comunidad**: Crear espacios de colaboración
4. **Validar con Expertos**: Certificación con instituciones especializadas

---

<div align="center">

**🤟 Signify - Conectando Mundos a Través de la Lengua de Señas 🤟**

*Desarrollado con ❤️ para promover la inclusión social*

**Tecnologías**: Python • Streamlit • Whisper AI • gTTS • Machine Learning • NLP

[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Built%20with-Python-blue?style=flat-square&logo=python)](https://python.org)
[![AI](https://img.shields.io/badge/Enhanced%20by-AI-orange?style=flat-square&logo=openai)](https://openai.com)

**"La tecnología al servicio de la inclusión social"**

*Versión 2.0.0 | Proyecto Colaborativo | Licencia MIT*

</div>