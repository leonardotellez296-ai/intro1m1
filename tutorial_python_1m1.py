# tutorial_python_1m1.py
# Guía Interactiva de Python para Estudiantes de 1M1 (De PSeInt a Python)

def main():
    print("====================================================")
    print("   ¡BIdhfuojfENVENIDO AL TUTORIAL DE PYTHON PARA EL 1M1!- Hola   ")
    print("====================================================\n")
    print("Este archivo te ayudará a traducir lo que aprendiste en PSeInt a Python.")
    print("Python es un lenguaje 'identado', lo que significa que los espacios")
    print("al principio de la línea son obligatorios para definir bloques de código.\n")

    # --- 1. VARIABLES Y TIPOS DE DATOS ---
    print("--- 1. VARIABLES Y TIPOS DE DATOS ---")
    # En PSeInt: Definir nombre Como Cadena
    # En Python: No necesitas definir el tipo, se asigna automáticamente.
    nombre = "Estudiante 1M1"  # String (Cadena)
    edad = 18                   # Integer (Entero)
    promedio = 85.5            # Float (Real)
    es_estudiante = True       # Boolean (Lógico)

    print(f"Nombre: {nombre} (Tipo: {type(nombre)})")
    print(f"Edad: {edad} (Tipo: {type(edad)})")
    print(f"Promedio: {promedio} (Tipo: {type(promedio)})")
    print(f"Es estudiante: {es_estudiante} (Tipo: {type(es_estudiante)})\n")

    # --- 2. OPERADORES ---
    print("--- 2. OPERADORES ---")
    a = 10
    b = 3
    print(f"Suma (10 + 3): {a + b}")
    print(f"Resta (10 - 3): {a - b}")
    print(f"Multiplicación (10 * 3): {a * b}")
    print(f"División (10 / 3): {a / b}")
    print(f"División Entera (10 // 3): {a // b}") # Como el trunc(10/3)
    print(f"Módulo/Residuo (10 % 3): {a % b}\n")

    # --- 3. CONDICIONALES ---
    print("--- 3. CONDICIONALES ---")
    # En PSeInt: Si cond Entonces ... Sino ... FinSi
    print("Probemos un condicional interactivo:")
    try:
        nota = float(input("Ingresa tu nota (0-100): "))
        if nota >= 60:
            print("¡Felicidades! Has aprobado.")
            if nota > 90:
                print("Excelente desempeño.")
        elif nota >= 50:
            print("Estás en convocatoria.")
        else:
            print("Reprobado. A estudiar más.")
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
    print("")

    # --- 4. CICLOS (BUCLES) ---
    print("--- 4. CICLOS ---")
    
    # Mientras (While)
    print("Ciclo 'while' (Mientras) contando del 1 al 3:")
    contador = 1
    while contador <= 3:
        print(f"Contador: {contador}")
        contador += 1 # Es lo mismo que contador = contador + 1
    
    # Para (For)
    print("\nCiclo 'for' (Para) usando range(5):")
    # range(5) genera números del 0 al 4
    for i in range(5):
        print(f"Iteración: {i}")
    print("")

    # --- 5. ARREGLOS (LISTAS) ---
    print("--- 5. ARREGLOS (LISTAS) ---")
    # En PSeInt: Dimension lista[5]
    # En Python: Las listas son dinámicas (pueden cambiar de tamaño)
    frutas = ["Manzana", "Banano", "Naranja"]
    print(f"Lista original: {frutas}")
    
    # Agregar elemento (Como insertar en PSeInt)
    frutas.append("Uva")
    print(f"Después de append: {frutas}")
    
    # Acceder a un elemento (¡Ojo! En Python empezamos desde el índice 0)
    print(f"La primera fruta (índice 0): {frutas[0]}")
    
    # Recorrer una lista
    print("Recorriendo la lista de frutas:")
    for fruta in frutas:
        print(f"- {fruta}")
    print("")

    print("====================================================")
    print("   ¡Sigue practicando! El 1M1 llegará lejos.        ")
    print("====================================================")

if __name__ == "__main__":
    main()
