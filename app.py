"""
SignBridge AI - Sistema de Consulta de Lenguaje de Señas Ecuatoriano

Aplicación web profesional para consulta y aprendizaje de señas ecuatorianas.
Desarrollado con Streamlit para una interfaz moderna y accesible.

Autor: SignBridge AI Team
Versión: 2.0.0
"""

import threading
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import streamlit as st

# Importar módulos del proyecto
from audio.speech_engine import get_speech_engine, get_voice_recognition
from core.sign_processor import SearchResult, get_processor
from database.signs_database import SignEntry, SignsDatabase

# Constantes de configuración
APP_TITLE = "SignBridge AI"
APP_ICON = "🤟"
APP_DESCRIPTION = "Sistema Profesional de Consulta de Lenguaje de Señas Ecuatoriano"

# CSS Variables - Tema profesional
CSS_VARIABLES = """
    :root {
        --primary-color: #2E86AB;
        --secondary-color: #A23B72;
        --accent-color: #F18F01;
        --success-color: #C73E1D;
        --background-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --card-background: rgba(255, 255, 255, 0.95);
        --text-primary: #2c3e50;
        --text-secondary: #7f8c8d;
        --border-radius: 12px;
        --shadow-soft: 0 4px 20px rgba(0, 0, 0, 0.1);
        --shadow-hover: 0 8px 30px rgba(0, 0, 0, 0.15);
    }
"""

# Configuración de la página
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': f"{APP_TITLE} - {APP_DESCRIPTION}"
    }
)


def load_custom_css() -> None:
    """Carga estilos CSS personalizados para la interfaz profesional."""
    custom_css = f"""
    <style>
    /* Variables CSS para tema profesional */
    {CSS_VARIABLES}
    
    /* Fondo principal */
    .stApp {{
        background: var(--background-gradient);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    
    /* Contenedor principal */
    .main-container {{
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 2rem;
        margin: 1rem;
        box-shadow: var(--shadow-soft);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    
    /* Estilos generales para mejorar la visibilidad del texto */
    .stApp, .stApp * {{
        color: #2c3e50 !important;
    }}
    
    /* Asegurar que todo el texto sea visible */
    p, span, div, label, .stMarkdown {{
        color: #2c3e50 !important;
    }}
    
    /* Título principal */
    .main-title {{
        text-align: center;
        color: #1a365d !important;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }}
    
    /* Mejora de contraste para h1 y h2 */
    h1, .main-title {{
        color: #1a365d !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3) !important;
        font-weight: 700 !important;
        background: none !important;
        -webkit-text-fill-color: #1a365d !important;
    }}
    
    h2 {{
        color: #1a365d !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2) !important;
        font-weight: 600 !important;
    }}
    
    /* Estilos específicos para títulos en tarjetas */
    .feature-card h2 {{
        color: #1a365d !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2) !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
    }}
    
    /* Forzar color en todos los elementos h1 de Streamlit */
    .stApp h1 {{
        color: #1a365d !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3) !important;
        font-weight: 700 !important;
    }}
    
    .subtitle {{
        text-align: center;
        color: var(--text-secondary);
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }}
    
    /* Tarjetas de funcionalidad */
    .feature-card {{
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-soft);
        border-left: 4px solid var(--primary-color);
        transition: all 0.3s ease;
    }}
    
    .feature-card:hover {{
        box-shadow: var(--shadow-hover);
        transform: translateY(-2px);
    }}
    
    /* Botones personalizados */
    .stButton > button {{
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-soft);
        width: 100%;
    }}
    
    .stButton > button:hover {{
        box-shadow: var(--shadow-hover);
        transform: translateY(-2px);
    }}
    
    /* Sidebar personalizada */
    .css-1d391kg {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
    }}
    
    /* Inputs personalizados */
    .stTextInput > div > div > input {{
        border-radius: var(--border-radius);
        border: 2px solid #e1e8ed;
        padding: 0.75rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1);
    }}
    
    /* Métricas personalizadas */
    .metric-card {{
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 1rem;
        text-align: center;
        box-shadow: var(--shadow-soft);
        margin: 0.5rem 0;
    }}
    
    /* Resultados de búsqueda */
    .search-result {{
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-soft);
        border-left: 4px solid var(--accent-color);
        transition: all 0.3s ease;
    }}
    
    .search-result:hover {{
        box-shadow: var(--shadow-hover);
        transform: translateY(-2px);
    }}
    
    /* Instrucciones destacadas */
    .instructions-box {{
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        border: 2px solid var(--primary-color);
        border-radius: var(--border-radius);
        padding: 1rem;
        margin: 0.5rem 0;
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a365d !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    
    /* Asegurar visibilidad en elementos específicos */
    .instructions-box *, .search-result *, .feature-card * {{
        color: #2c3e50 !important;
    }}
    
    /* Texto en botones debe mantenerse blanco */
    .stButton > button, .stButton > button * {{
        color: white !important;
    }}
    
    .category-badge {{
        background: var(--primary-color);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.2rem 0;
    }}
    
    .confidence-badge {{
        background: var(--success-color);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.2rem 0;
    }}
    
    /* Animaciones */
    .fade-in-up {{
        animation: fadeInUp 0.6s ease-out;
    }}
    
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    /* Responsive design */
    @media (max-width: 768px) {{
        .main-title {{
            font-size: 2rem;
        }}
        
        .main-container {{
            padding: 1rem;
            margin: 0.5rem;
        }}
        
        .feature-card {{
            padding: 1rem;
        }}
    }}
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def initialize_session_state() -> None:
    """Inicializa el estado de la sesión con valores por defecto."""
    # Inicializar valores básicos primero
    if 'voice_enabled' not in st.session_state:
        st.session_state.voice_enabled = True
    
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []
    
    if 'current_results' not in st.session_state:
        st.session_state.current_results = []
    
    # Inicializar el procesador de forma segura
    if 'processor' not in st.session_state:
        try:
            with st.spinner("Inicializando sistema de señas..."):
                st.session_state.processor = get_processor()
        except Exception as e:
            st.error(f"Error al inicializar el sistema: {e}")
            st.session_state.processor = None


def render_header() -> None:
    """Renderiza el encabezado principal de la aplicación."""
    header_html = f"""
    <div class="main-container fade-in-up">
        <h1 class="main-title">{APP_ICON} {APP_TITLE}</h1>
        <p class="subtitle">{APP_DESCRIPTION}</p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)


def render_sidebar() -> None:
    """Renderiza la barra lateral con opciones y estadísticas."""
    with st.sidebar:
        st.markdown("### 🎛️ Panel de Control")
        
        # Configuraciones de audio
        st.markdown("#### 🔊 Configuración de Audio")
        voice_enabled = st.checkbox(
            "Habilitar síntesis de voz",
            value=st.session_state.voice_enabled,
            help="Activa/desactiva la lectura automática de resultados"
        )
        st.session_state.voice_enabled = voice_enabled
        
        # Estadísticas de la base de datos
        _render_statistics()
        
        # Historial de búsquedas
        _render_search_history()


def _render_statistics() -> None:
    """Renderiza las estadísticas de la base de datos."""
    if st.session_state.processor:
        try:
            stats = st.session_state.processor.get_search_statistics()
            
            st.markdown("#### 📊 Estadísticas")
            col1, col2 = st.columns(2)
            
            with col1:
                # Obtener estadísticas de la base de datos
                db_stats = stats.get('database_stats', {})
            total_signs = db_stats.get('total_signs', 0)
            
            metric_html = f"""
            <div class="metric-card">
                <h3 style="color: var(--primary-color); margin: 0;">{total_signs}</h3>
                <p style="margin: 0; color: var(--text-secondary);">Total Señas</p>
            </div>
            """
            st.markdown(metric_html, unsafe_allow_html=True)
        
            with col2:
                total_searches = stats.get('total_searches', 0)
                metric_html = f"""
                <div class="metric-card">
                    <h3 style="color: var(--accent-color); margin: 0;">{total_searches}</h3>
                    <p style="margin: 0; color: var(--text-secondary);">Búsquedas</p>
                </div>
                """
                st.markdown(metric_html, unsafe_allow_html=True)
        except Exception as e:
            st.warning("No se pudieron cargar las estadísticas")
    else:
        st.warning("Sistema no inicializado correctamente")


def _render_search_history() -> None:
    """Renderiza el historial de búsquedas recientes."""
    if st.session_state.search_history:
        st.markdown("#### 📝 Historial Reciente")
        recent_searches = st.session_state.search_history[-5:]
        
        for i, search in enumerate(recent_searches):
            if st.button(f"🔍 {search}", key=f"history_{i}"):
                perform_search(search)


def perform_search(query: str, search_type: str = "exact") -> List[SearchResult]:
    """
    Realiza una búsqueda y actualiza el estado de la sesión.
    
    Args:
        query: Término de búsqueda
        search_type: Tipo de búsqueda ('exact', 'fuzzy', 'auto')
    
    Returns:
        Lista de resultados de búsqueda
    """
    if not query.strip():
        return []
    
    processor = st.session_state.processor
    
    # Realizar búsqueda según el tipo
    if search_type == "exact":
        # Búsqueda exacta solamente
        results = processor.search_sign(query, include_similar=False)
    elif search_type == "fuzzy":
        # Búsqueda con similares
        results = processor.search_sign(query, include_similar=True)
    else:
        # Búsqueda automática: incluye similares por defecto
        results = processor.search_sign(query, include_similar=True)
    
    # Actualizar historial si es una nueva búsqueda
    if query not in st.session_state.search_history:
        st.session_state.search_history.append(query)
    
    # Actualizar resultados actuales
    st.session_state.current_results = results
    
    return results


def render_search_interface() -> None:
    """Renderiza la interfaz de búsqueda principal."""
    st.markdown("""
    <div class="feature-card fade-in-up">
        <h2 style="color: var(--primary-color); margin-bottom: 1rem;">🔍 Búsqueda de Señas</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Pestañas de búsqueda
    tab1, tab2, tab3 = st.tabs([
        "🎯 Búsqueda Exacta", 
        "🔄 Búsqueda Inteligente", 
        "🎤 Búsqueda por Voz"
    ])
    
    with tab1:
        _render_exact_search_tab()
    
    with tab2:
        _render_fuzzy_search_tab()
    
    with tab3:
        _render_voice_search_tab()


def _render_exact_search_tab() -> None:
    """Renderiza la pestaña de búsqueda exacta."""
    st.markdown("Busca una seña específica por su nombre exacto:")
    query = st.text_input(
        "Ingresa la palabra a buscar:",
        placeholder="Ejemplo: hola, gracias, por favor...",
        key="exact_search"
    )
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔍 Buscar", key="exact_btn"):
            if query:
                results = perform_search(query, "exact")
                _play_search_results_audio(results)


def _render_fuzzy_search_tab() -> None:
    """Renderiza la pestaña de búsqueda inteligente."""
    st.markdown("Búsqueda inteligente que encuentra coincidencias aproximadas:")
    query = st.text_input(
        "Ingresa la palabra a buscar:",
        placeholder="Ejemplo: ola, grasias, porfavor...",
        key="fuzzy_search"
    )
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔍 Buscar", key="fuzzy_btn"):
            if query:
                results = perform_search(query, "fuzzy")
                _play_search_results_audio(results)


def _render_voice_search_tab() -> None:
    """Renderiza la pestaña de búsqueda por voz."""
    st.markdown("Usa tu voz para buscar señas:")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.info("Haz clic en el botón y habla claramente la palabra que deseas buscar.")
    
    with col2:
        if st.button("🎤 Escuchar", key="voice_btn"):
            _handle_voice_search()


def _handle_voice_search() -> None:
    """Maneja la búsqueda por reconocimiento de voz."""
    with st.spinner("Escuchando... Habla ahora"):
        try:
            voice_engine = get_voice_recognition()
            recognized_text = voice_engine.record_and_transcribe()
            
            if recognized_text:
                # Limpiar y normalizar el texto reconocido
                cleaned_text = recognized_text.strip().lower()
                st.success(f"Reconocido: {recognized_text}")
                
                # Intentar primero búsqueda exacta, luego fuzzy
                results = perform_search(cleaned_text, "exact")
                if not results.found:
                    # Si no se encuentra exacta, intentar con fuzzy
                    results = perform_search(cleaned_text, "fuzzy")
                    if results.found:
                        st.info(f"Búsqueda aproximada encontrada para: {cleaned_text}")
                
                _play_search_results_audio(results)
            else:
                st.warning("No se pudo reconocer el audio. Intenta de nuevo.")
        except Exception as e:
            st.error(f"Error en reconocimiento de voz: {str(e)}")


def _play_search_results_audio(results: SearchResult) -> None:
    """
    Reproduce audio de los resultados de búsqueda en segundo plano.
    
    Args:
        results: Resultado de búsqueda (SearchResult)
    """
    if not results:
        return
        
    if not st.session_state.voice_enabled:
        return
        
    # Verificar que el processor esté inicializado
    if not hasattr(st.session_state, 'processor') or not st.session_state.processor:
        st.error("Procesador no inicializado")
        return
    
    # Obtener referencia al speech_engine ANTES del threading
    speech_engine = st.session_state.processor.speech_engine
    
    try:
        if results.found and results.exact_match:
            # Reproducir resultado exacto
            def play_audio():
                try:
                    speech_engine.speak_sign_instruction(
                        results.exact_match.word, 
                        results.exact_match.instructions
                    )
                except Exception as e:
                    print(f"Error reproduciendo audio: {e}")
            
            threading.Thread(target=play_audio, daemon=True).start()
            
        elif results.similar_matches:
            # Reproducir mejor coincidencia similar
            best_match, similarity = results.similar_matches[0]
            
            def play_similar_audio():
                try:
                    suggestion_text = (
                        f"No encontré exactamente '{results.query}', "
                        f"pero encontré '{best_match.word}' que es similar. "
                        f"{best_match.instructions}"
                    )
                    speech_engine.speak_text(suggestion_text)
                except Exception as e:
                    print(f"Error reproduciendo audio similar: {e}")
            
            threading.Thread(target=play_similar_audio, daemon=True).start()
            
        else:
            # No se encontraron resultados
            def play_no_results():
                try:
                    no_results_text = f"No se encontraron resultados para '{results.query}'"
                    speech_engine.speak_text(no_results_text)
                except Exception as e:
                    print(f"Error reproduciendo mensaje de no resultados: {e}")
            
            threading.Thread(target=play_no_results, daemon=True).start()
            
    except Exception as e:
        st.error(f"Error en reproducción de audio: {str(e)}")
        print(f"Error detallado en _play_search_results_audio: {e}")


def render_results() -> None:
    """Renderiza los resultados de búsqueda."""
    if not st.session_state.current_results:
        return
    
    st.markdown("""
    <div class="feature-card fade-in-up">
        <h2 style="color: var(--primary-color); margin-bottom: 1rem;">📋 Resultados de Búsqueda</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # current_results ahora es un SearchResult, no una lista
    result = st.session_state.current_results
    _render_single_result(result, 0)


def _render_single_result(result: SearchResult, index: int) -> None:
    """
    Renderiza un resultado individual de búsqueda.
    
    Args:
        result: Resultado de búsqueda
        index: Índice del resultado
    """
    if not result.found:
        st.warning(f"No se encontraron resultados para '{result.query}'")
        return
    
    # Obtener la mejor coincidencia
    best_match = result.get_best_match()
    if not best_match:
        st.warning("No hay coincidencias disponibles")
        return
    
    confidence = result.get_confidence_score()
    
    result_html = f"""
    <div class="search-result fade-in-up">
        <div style="background: linear-gradient(45deg, var(--primary-color), var(--secondary-color)); 
                    color: white; padding: 1rem; border-radius: var(--border-radius); 
                    margin-bottom: 1rem; text-align: center; box-shadow: var(--shadow-soft);">
            <h2 style="margin: 0; font-size: 2rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                🤟 {best_match.word}
            </h2>
        </div>
        <div class="instructions-box">
            <strong>Instrucciones:</strong> {best_match.instructions}
        </div>
        <div style="margin: 1rem 0;">
            <span class="category-badge">Categoría: {best_match.category}</span>
            <span class="confidence-badge">Coincidencia: {confidence:.1%}</span>
        </div>
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
    
    # Botón para reproducir audio
    if st.session_state.voice_enabled:
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button(f"🔊 Reproducir", key=f"speak_{index}"):
                # Verificar que el processor esté inicializado
                if hasattr(st.session_state, 'processor') and st.session_state.processor:
                    # Obtener referencia al speech_engine ANTES del threading
                    speech_engine = st.session_state.processor.speech_engine
                    
                    def play_instruction():
                        try:
                            speech_engine.speak_sign_instruction(
                                best_match.word, best_match.instructions
                            )
                        except Exception as e:
                            print(f"Error reproduciendo instrucción: {e}")
                    
                    threading.Thread(target=play_instruction, daemon=True).start()
                    st.success("Reproduciendo...")


def render_random_signs() -> None:
    """Renderiza sección de señas aleatorias para exploración."""
    st.markdown("""
    <div class="feature-card fade-in-up">
        <h2 style="color: var(--primary-color); margin-bottom: 1rem;">🎲 Explorar Señas</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 Seña Aleatoria", key="random_sign"):
            _show_random_sign()
    
    with col2:
        if st.button("📚 5 Señas Aleatorias", key="random_signs"):
            _show_multiple_random_signs()


def _show_random_sign() -> None:
    """Muestra una seña aleatoria."""
    random_signs = st.session_state.processor.get_random_signs(1)
    if random_signs:
        sign = random_signs[0]
        result_html = f"""
        <div class="search-result">
            <div style="background: linear-gradient(45deg, var(--primary-color), var(--secondary-color)); 
                        color: white; padding: 0.8rem; border-radius: var(--border-radius); 
                        margin-bottom: 1rem; text-align: center; box-shadow: var(--shadow-soft);">
                <h2 style="margin: 0; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                    🤟 {sign.word}
                </h2>
            </div>
            <div class="instructions-box">
                <strong>Instrucciones:</strong> {sign.instructions}
            </div>
            <div style="margin: 1rem 0;">
                <span class="category-badge">Categoría: {sign.category}</span>
            </div>
        </div>
        """
        st.markdown(result_html, unsafe_allow_html=True)
        
        if st.session_state.voice_enabled:
            # Obtener referencia al speech_engine ANTES del threading
            speech_engine = st.session_state.processor.speech_engine
            
            def play_random_sign():
                try:
                    speech_engine.speak_sign_instruction(
                        sign.word, sign.instructions
                    )
                except Exception as e:
                    print(f"Error reproduciendo seña aleatoria: {e}")
            
            threading.Thread(target=play_random_sign, daemon=True).start()


def _show_multiple_random_signs() -> None:
    """Muestra múltiples señas aleatorias."""
    random_signs = st.session_state.processor.get_random_signs(5)
    for sign in random_signs:
        result_html = f"""
        <div class="search-result">
            <div style="background: linear-gradient(45deg, var(--primary-color), var(--secondary-color)); 
                        color: white; padding: 0.6rem; border-radius: var(--border-radius); 
                        margin-bottom: 0.8rem; text-align: center; box-shadow: var(--shadow-soft);">
                <h3 style="margin: 0; font-size: 1.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                    🤟 {sign.word}
                </h3>
            </div>
            <div class="instructions-box">
                {sign.instructions}
            </div>
        </div>
        """
        st.markdown(result_html, unsafe_allow_html=True)


def render_footer() -> None:
    """Renderiza el pie de página de la aplicación."""
    footer_html = """
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; color: var(--text-secondary);">
        <p>SignBridge AI - Sistema de Consulta de Lenguaje de Señas Ecuatoriano</p>
        <p>Desarrollado con ❤️ para la comunidad sorda ecuatoriana</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


def main() -> None:
    """Función principal de la aplicación."""
    # Cargar CSS personalizado
    load_custom_css()
    
    # Inicializar estado de sesión
    initialize_session_state()
    
    # Renderizar componentes principales
    render_header()
    render_sidebar()
    render_search_interface()
    render_results()
    render_random_signs()
    render_footer()


if __name__ == "__main__":
    main()