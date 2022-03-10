from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

file = open('data.txt', 'r')
sentence = file.read()

print(sentence)

token = f.encrypt(bytes(sentence, 'utf-8'))
print(token)
# saved token  => "encrypted.txt"
file = open('encrypted.txt', 'w')
sliced_token = str(token)[2:]
file.write(sliced_token)

# 이후, "encrypted.txt" 불러와서 다시 복호화
file = open('encrypted.txt', 'r')
read = file.read()
result = f.decrypt(bytes(read, 'utf-8'))

file.close()

print(result)
