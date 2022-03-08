from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

file = open('data.txt', 'r')
sentence = file.read()
file.close()

print(sentence)

token = f.encrypt(bytes(sentence, 'utf-8'))

# token 저장 => "encrypted.txt"
# 이후, "encrypted.txt" 불러와서 다시 복호화

print(token)

d = f.decrypt(token)

print(d)

