import hashlib

# 사용자 암호를 해싱하여 저장
password = "사용자_암호1"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# 사용자 로그인 시, 입력된 암호를 해싱하여 저장된 해시와 비교
user_input_password = "사용자_암호"
if hashlib.sha256(user_input_password.encode()).hexdigest() == hashed_password:
    print("로그인 성공")
else:
    print("로그인 실패")