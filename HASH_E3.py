def simple_hash(email):
    return hash(email)

def remove_duplicates_with_collision_handling(emails):
    hash_table = {}
    unique_emails = []

    for email in emails:
        hashed_email = simple_hash(email)
        if hashed_email not in hash_table:
            hash_table[hashed_email] = [email]
            unique_emails.append(email)
        else:
            if email not in hash_table[hashed_email]:
                hash_table[hashed_email].append(email)
                unique_emails.append(email)

    return unique_emails

# Lista de correos con posible colisión en el hash
emails = [
    "abc@gmail.com",
    "xyz@gmail.com",  # Posible colisión
    "user2@gmail.com",
    "user1@gmail.com",
    "abc@gmail.com",  # Duplicado exacto
]

# Prueba
print("Lista sin duplicados:", remove_duplicates_with_collision_handling(emails))
