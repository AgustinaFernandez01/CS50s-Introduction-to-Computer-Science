import csv
import sys


def main():
    # Verificar el uso correcto de la línea de comandos
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE SEQUENCE")
        sys.exit(1)

    # Leer el archivo de la base de datos en una variable
    database_filename = sys.argv[1]
    with open(database_filename) as database_file:
        database_reader = csv.DictReader(database_file)
        database = list(database_reader)

    # Leer el archivo de secuencia de ADN en una cadena
    sequence_filename = sys.argv[2]
    with open(sequence_filename) as sequence_file:
        sequence = sequence_file.read()

    # Crear un diccionario para almacenar los recuentos de STR en la secuencia de ADN
    str_counts = {}

    # Iterar a través de la base de datos para calcular el recuento de STR para cada persona
    for row in database:
        person_name = row["name"]
        str_counts[person_name] = {}

        # Iterar a través de cada STR en la base de datos (excluyendo la columna "name")
        for str_key in row.keys():
            if str_key != "name":
                str_counts[person_name][str_key] = longest_match(sequence, str_key)

    # Verificar la base de datos en busca de perfiles coincidentes
    for row in database:
        person_name = row["name"]
        match = all(
            int(row[str_key]) == str_counts[person_name][str_key]
            for str_key in row.keys()
            if str_key != "name"
        )
        if match:
            print(person_name)
            return

    # Si no se encuentra ninguna coincidencia, imprimir "No match"
    print("No match")


def longest_match(sequence, subsequence):
    """Devuelve la longitud de la secuencia más larga de subsecuencia repetida en la secuencia de ADN."""
    # Inicializar variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Comprobar cada carácter en la secuencia de ADN en busca de las secuencias más largas de subsecuencia repetida
    for i in range(sequence_length):
        # Inicializar el recuento de secuencias consecutivas
        count = 0

        # Comprobar si hay coincidencia con la subsecuencia en una "subcadena" (un subconjunto de caracteres) dentro de la secuencia de ADN
        # Si hay coincidencia, mover la subcadena a la siguiente coincidencia potencial en la secuencia de ADN
        # Continuar moviendo la subcadena y comprobando coincidencias hasta que no haya más coincidencias consecutivas
        while True:
            # Ajustar el inicio y el final de la subcadena
            start = i + count * subsequence_length
            end = start + subsequence_length

            # Si hay coincidencia en la subcadena de la secuencia de ADN
            if sequence[start:end] == subsequence:
                count += 1
            # Si no hay coincidencia en la subcadena de la secuencia de ADN
            else:
                break

        # Actualizar la secuencia más larga encontrada en la secuencia de ADN
        longest_run = max(longest_run, count)

    # Después de comprobar las secuencias en cada carácter de la secuencia de ADN, devolver la secuencia más larga encontrada
    return longest_run


if __name__ == "__main__":
    main()
