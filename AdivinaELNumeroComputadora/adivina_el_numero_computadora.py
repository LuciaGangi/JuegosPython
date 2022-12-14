import random

def adivina_el_numero_computadora (x):
    
    print("==========================")
    print(" ¡Bienvenido(a) al juego! ")
    print("==========================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")
    
    
    límite_inferior = 1 # [1,x]
    límite_superior = x 
    
    respuesta = ""
    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior: # [1, 10]
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior # también podría ser el límite superior.
            
        #Obtener una respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()
        
        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1
            
    print(f"¡Siiiii! La computadora adivinó tu número correctamente: {predicción}")
    

adivina_el_numero_computadora(10)