from cryptography.fernet import Fernet

# 키 생성
key = Fernet.generate_key()
fernet = Fernet(key)

# 사용자 암호 암호화
password = "사용자_암호"
encrypted_password = fernet.encrypt(password.encode())

# 사용자 로그인 시, 입력된 암호 복호화 및 검증
user_input_password = "사용자_입력_암호"
decrypted_password = fernet.decrypt(encrypted_password).decode()

if user_input_password == decrypted_password:
    print("로그인 성공")
else:
    print("로그인 실패")
