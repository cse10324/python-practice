import hashlib 
  
result = hashlib.md5('cdac'.encode())

print(result.hexdigest())