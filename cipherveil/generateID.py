import uuid

def generate_alphanumeric_id():
    unique_id = str(uuid.uuid4().hex)
    return unique_id

# Example usage:
alphanumeric_id = generate_alphanumeric_id()
print(alphanumeric_id)
