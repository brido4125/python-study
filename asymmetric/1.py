from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


plain_msg = input("text 입력하세요 : ")

AES_key = Fernet.generate_key()

f = Fernet(AES_key)

enc_msg = f.encrypt(bytes(plain_msg, 'utf-8'))

# private_key.pem 으로부터 key 얻어오기
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
# public_key.pem 으로부터 key 얻어오기
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# AES key를 암호화 by public_key
enc_key = public_key.encrypt(
    AES_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 1) enc_key 복호화
# 2) aes_key를 통해서 enc_msg 복호화
def insecure_protocol(send_enc_key, send_enc_msg):
    original_key = private_key.decrypt(
        send_enc_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    fernet = Fernet(original_key)
    decrypt = fernet.decrypt(send_enc_msg)
    print(decrypt)


insecure_protocol(enc_key, enc_msg)
