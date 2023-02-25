import hashlib



# hashed password function 

def hashedpassword(input) :
    hash = hashlib.sha256(input)
    hash = hash.hexdigest()
    return hash