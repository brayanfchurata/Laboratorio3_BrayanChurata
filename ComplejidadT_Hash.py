import time
import random
import string

# Función hash simple
def simple_hash(email):
    return hash(email.lower())

# Función para eliminar duplicados con manejo de colisiones y medir tiempos
def remove_duplicates_with_collision_handling(emails):
    hash_table = {}
    unique_emails = []

    start_time = time.time()  # Iniciar el cronómetro
    for email in emails:
        hashed_email = simple_hash(email)
        if hashed_email not in hash_table:
            hash_table[hashed_email] = [email]
            unique_emails.append(email)
        else:
            if email not in hash_table[hashed_email]:
                hash_table[hashed_email].append(email)
                unique_emails.append(email)
    end_time = time.time()  # Terminar el cronómetro

    print(f"Tiempo de insercion y eliminacion de duplicados: {end_time - start_time:.6f} segundos")
    return unique_emails

# Función para generar una lista grande de correos electrónicos aleatorios
def generate_random_emails(num_emails):
    emails = []
    for _ in range(num_emails):
        # Generar correos con nombres y dominios aleatorios
        name = ''.join(random.choices(string.ascii_lowercase, k=10))
        domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"])
        email = f"{name}@{domain}"
        emails.append(email)
    return emails

# Generar 1,000,000 de correos electrónicos aleatorios (algunos pueden ser duplicados)
emails = generate_random_emails(1000000)

# Prueba y medición de tiempo con un conjunto grande de correos
unique_emails = remove_duplicates_with_collision_handling(emails)
print(f"Numero de correos unicos: {len(unique_emails)}")
