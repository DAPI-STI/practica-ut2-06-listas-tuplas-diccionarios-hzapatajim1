"""
EX04 (Tuplas)
Trabajar con una lista de tuplas (nombre, nota) y devolver una tupla.
"""

def best_student(records: list[tuple[str, float]]) -> tuple[str, float]:
    """
    Recibe una lista de tuplas (nombre, nota) y devuelve la tupla del alumno con mayor nota.

    - Si records está vacío, lanza ValueError.
    - Si hay empate, devuelve el primero que aparezca con esa nota.
    """
    if not records:
        raise ValueError("La lista de registros está vacía")

    best = records[0]

    for student in records[1:]:
        if student[1] > best[1]:
            best = student

    return best