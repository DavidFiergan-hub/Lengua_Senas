"""
Módulo de Base de Datos para Señas Ecuatorianas.

Maneja la carga, búsqueda y gestión de señas desde el archivo CSV.
Proporciona funcionalidades de búsqueda exacta, difusa y por categorías.

Autor: Signify Team
Versión: 2.0.0
"""

import csv
import os
import random
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import difflib


@dataclass
class SignEntry:
    """
    Representa una entrada de seña en la base de datos.
    
    Attributes:
        word: Palabra o término de la seña
        instructions: Instrucciones detalladas para realizar la seña
        category: Categoría temática de la seña
        description: Descripción adicional (mantenido por compatibilidad)
    """
    word: str
    instructions: str
    category: str = "General"
    description: str = ""
    
    def __post_init__(self) -> None:
        """Inicialización posterior para mantener compatibilidad."""
        if not self.description:
            self.description = self.instructions
    
    def __str__(self) -> str:
        """Representación en cadena de la entrada de seña."""
        return f"{self.word}: {self.instructions}"


class SignsDatabase:
    """
    Clase principal para manejar la base de datos de señas ecuatorianas.
    
    Proporciona funcionalidades para cargar, buscar y gestionar señas
    desde un archivo CSV con soporte para búsquedas exactas, difusas
    y por categorías.
    """
    
    def __init__(self, csv_file_path: Optional[str] = None) -> None:
        """
        Inicializa la base de datos de señas.
        
        Args:
            csv_file_path: Ruta al archivo CSV con las señas.
                          Si es None, usa la ruta por defecto.
        """
        self.signs: Dict[str, SignEntry] = {}
        self.csv_file_path = csv_file_path or self._get_default_csv_path()
        self._load_signs()
    
    def _get_default_csv_path(self) -> str:
        """
        Obtiene la ruta por defecto del archivo CSV.
        
        Returns:
            Ruta absoluta al archivo señas_ecuatorianas.csv
        """
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, "señas_ecuatorianas.csv")
    
    def _load_signs(self) -> None:
        """
        Carga las señas desde el archivo CSV.
        
        Raises:
            FileNotFoundError: Si el archivo CSV no existe
            Exception: Si hay errores durante la carga
        """
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file, quotechar='"', skipinitialspace=True)
                
                loaded_count = 0
                for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 because of header
                    try:
                        # Obtener y limpiar los datos - manejar BOM si existe
                        palabra_key = next((k for k in row.keys() if 'Palabra' in k), 'Palabra')
                        descripcion_key = next((k for k in row.keys() if 'Descripción' in k), 'Descripción')
                        categoria_key = next((k for k in row.keys() if 'Categoría' in k), 'Categoría')
                        
                        raw_word = row.get(palabra_key, '').strip()
                        instructions = row.get(descripcion_key, '').strip()
                        category = row.get(categoria_key, 'General').strip()
                        
                        # Remover comillas adicionales si existen
                        if raw_word.startswith('"') and raw_word.endswith('"'):
                            raw_word = raw_word[1:-1]
                        
                        # Normalizar la palabra: primera letra mayúscula, resto minúsculas
                        word_normalized = self._normalize_word(raw_word)
                        word_key = raw_word.lower().strip()  # Clave para búsqueda
                        
                        if word_key and instructions:
                            self.signs[word_key] = SignEntry(
                                word=word_normalized,  # Palabra normalizada para mostrar
                                instructions=instructions,
                                category=category
                            )
                            loaded_count += 1
                        else:
                            print(f"⚠️ Fila {row_num}: Datos incompletos - Palabra: '{raw_word}', Descripción: '{instructions[:50]}...'")
                            
                    except Exception as row_error:
                        print(f"⚠️ Error en fila {row_num}: {row_error}")
                        continue
            
            print(f"✅ Base de datos cargada: {loaded_count} señas disponibles de {row_num-1} filas procesadas")
            
        except FileNotFoundError:
            error_msg = f"❌ Error: No se encontró el archivo {self.csv_file_path}"
            print(error_msg)
            raise FileNotFoundError(error_msg)
        except Exception as e:
            error_msg = f"❌ Error al cargar la base de datos: {e}"
            print(error_msg)
            raise Exception(error_msg) from e
    
    def _normalize_word(self, word: str) -> str:
        """
        Normaliza una palabra para mostrar con formato consistente.
        
        Args:
            word: Palabra a normalizar
            
        Returns:
            Palabra normalizada (primera letra mayúscula, resto minúsculas)
        """
        if not word or not word.strip():
            return ""
        
        # Limpiar espacios y caracteres especiales
        cleaned = word.strip()
        
        # Manejar casos especiales con comas o múltiples palabras
        if ',' in cleaned:
            # Para casos como "Ambos, as" -> "Ambos, As"
            parts = [part.strip() for part in cleaned.split(',')]
            normalized_parts = []
            for part in parts:
                if part:
                    normalized_parts.append(part.capitalize())
            return ', '.join(normalized_parts)
        else:
            # Caso normal: primera letra mayúscula, resto minúsculas
            return cleaned.capitalize()

    def reload_database(self) -> None:
        """Recarga la base de datos desde el archivo CSV."""
        self.signs.clear()
        self._load_signs()
    
    def search_exact(self, word: str) -> Optional[SignEntry]:
        """
        Busca una seña exacta en la base de datos.
        
        Args:
            word: Palabra a buscar (insensible a mayúsculas)
            
        Returns:
            SignEntry si se encuentra, None si no existe
        """
        if not word or not word.strip():
            return None
        
        # Normalizar la búsqueda a minúsculas para la clave
        search_key = word.lower().strip()
        return self.signs.get(search_key)
    
    def search_fuzzy(self, word: str, max_results: int = 5, 
                    min_similarity: float = 0.3) -> List[Tuple[SignEntry, float]]:
        """
        Busca señas similares usando coincidencia difusa.
        
        Args:
            word: Palabra a buscar
            max_results: Número máximo de resultados
            min_similarity: Umbral mínimo de similitud (0.0 - 1.0)
            
        Returns:
            Lista de tuplas (SignEntry, similarity_score) ordenada por similitud
        """
        if not word or not word.strip():
            return []
        
        word = word.lower().strip()
        matches = []
        
        for sign_word, sign_entry in self.signs.items():
            similarity = difflib.SequenceMatcher(None, word, sign_word).ratio()
            if similarity >= min_similarity:
                matches.append((sign_entry, similarity))
        
        # Ordenar por similitud descendente
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:max_results]
    
    def search_partial(self, partial_word: str, max_results: int = 10) -> List[SignEntry]:
        """
        Busca señas que contengan la palabra parcial.
        
        Args:
            partial_word: Parte de la palabra a buscar
            max_results: Número máximo de resultados
            
        Returns:
            Lista de SignEntry que contienen la palabra parcial
        """
        if not partial_word or not partial_word.strip():
            return []
        
        partial_word = partial_word.lower().strip()
        matches = []
        
        for sign_word, sign_entry in self.signs.items():
            if partial_word in sign_word:
                matches.append(sign_entry)
                if len(matches) >= max_results:
                    break
        
        return matches
    
    def search_by_category(self, category: str, max_results: int = 20) -> List[SignEntry]:
        """
        Busca señas por categoría específica.
        
        Args:
            category: Categoría a buscar
            max_results: Número máximo de resultados
            
        Returns:
            Lista de SignEntry de la categoría especificada
        """
        if not category or not category.strip():
            return []
        
        category = category.lower().strip()
        matches = []
        
        for sign_entry in self.signs.values():
            if category in sign_entry.category.lower():
                matches.append(sign_entry)
                if len(matches) >= max_results:
                    break
        
        return matches
    
    def get_all_words(self) -> List[str]:
        """
        Retorna todas las palabras disponibles en la base de datos.
        
        Returns:
            Lista ordenada de todas las palabras
        """
        return sorted(list(self.signs.keys()))
    
    def get_all_categories(self) -> List[str]:
        """
        Retorna todas las categorías únicas disponibles.
        
        Returns:
            Lista ordenada de categorías únicas
        """
        categories = set()
        for sign_entry in self.signs.values():
            categories.add(sign_entry.category)
        return sorted(list(categories))
    
    def get_random_signs(self, count: int = 5) -> List[SignEntry]:
        """
        Obtiene señas aleatorias de la base de datos.
        
        Args:
            count: Número de señas aleatorias a obtener
            
        Returns:
            Lista de SignEntry aleatorias
        """
        if count <= 0:
            return []
        
        available_signs = list(self.signs.values())
        if len(available_signs) <= count:
            return available_signs
        
        return random.sample(available_signs, count)
    
    def get_signs_by_keywords(self, keywords: List[str], 
                             max_results: int = 15) -> List[SignEntry]:
        """
        Obtiene señas que contengan palabras clave específicas.
        
        Args:
            keywords: Lista de palabras clave para filtrar
            max_results: Número máximo de resultados
            
        Returns:
            Lista de SignEntry que contienen las palabras clave
        """
        if not keywords:
            return []
        
        keywords = [kw.lower().strip() for kw in keywords if kw.strip()]
        if not keywords:
            return []
        
        matches = []
        
        for sign_entry in self.signs.values():
            # Buscar en palabra, instrucciones y categoría
            search_text = f"{sign_entry.word} {sign_entry.instructions} {sign_entry.category}".lower()
            
            if any(keyword in search_text for keyword in keywords):
                matches.append(sign_entry)
                if len(matches) >= max_results:
                    break
        
        return matches
    
    def get_database_stats(self) -> Dict[str, int]:
        """
        Obtiene estadísticas de la base de datos.
        
        Returns:
            Diccionario con estadísticas de la base de datos
        """
        categories = self.get_all_categories()
        category_counts = {}
        
        for category in categories:
            category_counts[category] = len(self.search_by_category(category, max_results=1000))
        
        return {
            'total_signs': len(self.signs),
            'total_categories': len(categories),
            'categories': category_counts,
            'average_instruction_length': self._calculate_average_instruction_length()
        }
    
    def _calculate_average_instruction_length(self) -> float:
        """
        Calcula la longitud promedio de las instrucciones.
        
        Returns:
            Longitud promedio de las instrucciones
        """
        if not self.signs:
            return 0.0
        
        total_length = sum(len(sign.instructions) for sign in self.signs.values())
        return total_length / len(self.signs)
    
    def export_to_dict(self) -> Dict[str, Dict[str, str]]:
        """
        Exporta la base de datos a un diccionario.
        
        Returns:
            Diccionario con todas las señas
        """
        return {
            word: {
                'word': sign.word,
                'instructions': sign.instructions,
                'category': sign.category,
                'description': sign.description
            }
            for word, sign in self.signs.items()
        }
    
    def __len__(self) -> int:
        """Retorna el número total de señas en la base de datos."""
        return len(self.signs)
    
    def __contains__(self, word: str) -> bool:
        """Verifica si una palabra existe en la base de datos."""
        return word.lower().strip() in self.signs
    
    def __getitem__(self, word: str) -> Optional[SignEntry]:
        """Permite acceso directo a las señas usando indexación."""
        return self.search_exact(word)


# Funciones de utilidad para compatibilidad
def load_signs_database(csv_file_path: Optional[str] = None) -> SignsDatabase:
    """
    Función de utilidad para cargar la base de datos de señas.
    
    Args:
        csv_file_path: Ruta opcional al archivo CSV
        
    Returns:
        Instancia de SignsDatabase cargada
    """
    return SignsDatabase(csv_file_path)


def get_default_database() -> SignsDatabase:
    """
    Obtiene una instancia por defecto de la base de datos.
    
    Returns:
        Instancia de SignsDatabase con configuración por defecto
    """
    return SignsDatabase()


# Instancia global para uso singleton (opcional)
_default_database: Optional[SignsDatabase] = None


def get_database_instance() -> SignsDatabase:
    """
    Obtiene la instancia singleton de la base de datos.
    
    Returns:
        Instancia singleton de SignsDatabase
    """
    global _default_database
    if _default_database is None:
        _default_database = SignsDatabase()
    return _default_database