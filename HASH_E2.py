# Función hash simple usando la función nativa hash()
def simple_hash(email):
    return hash(email)

# Función para eliminar correos duplicados sin manejo de colisiones
def remove_duplicates(emails):
    hash_table = {}
    unique_emails = []

    for email in emails:
        hashed_email = simple_hash(email)
        if hashed_email not in hash_table:
            hash_table[hashed_email] = email
            unique_emails.append(email)

    return unique_emails

# Función para eliminar correos duplicados con manejo de colisiones (encadenamiento)
def remove_duplicates_with_collision_handling(emails):
    hash_table = {}
    unique_emails = []

    for email in emails:
        hashed_email = simple_hash(email)
        if hashed_email not in hash_table:
            hash_table[hashed_email] = [email]
            unique_emails.append(email)
        else:
            if email not in hash_table[hashed_email]:  # Evitar duplicados en la lista de colisión
                hash_table[hashed_email].append(email)
                unique_emails.append(email)

    return unique_emails

# Función para buscar un correo en la tabla hash
def search_email(email, hash_table):
    hashed_email = simple_hash(email)
    return hash_table.get(hashed_email, "Email no encontrado")

# Pruebas
emails = [
    "usuario1@gmail.com",
    "usuario2@gmail.com",
    "usuario3@gmail.com",
    "usuario1@gmail.com",  # Duplicado
    "usuario4@yahoo.com",
    "usuario4@yahoo.com"   # Duplicado
]

# Prueba sin colisiones
print("Lista sin duplicados:", remove_duplicates(emails))

# Prueba con manejo de colisiones
print("Lista sin duplicados (con colisiones manejadas):", remove_duplicates_with_collision_handling(emails))

# Búsqueda de un correo
hash_table = {simple_hash(email): email for email in emails}
print(search_email("usuario1@gmail.com", hash_table))
print(search_email("usuario5@gmail.com", hash_table))
