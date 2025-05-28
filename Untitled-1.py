def validate_input(user_input: str, max_length=100) -> str:
    if not isinstance(user_input, str):
        raise TypeError("입력은 문자열이어야 합니다")
    if len(user_input) > max_length:
        raise ValueError(f"입력 길이 초과 (최대 {max_length}자)")
    return user_input.strip()
import hashlib
import os

def hash_password(password: str) -> bytes:
    salt = os.urandom(32)  # 256비트 솔트
    iterations = 600_000   # NIST 권장 최소 600,000회
    
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        iterations
    )
    return salt + key  # 솔트와 키를 함께 저장
import sqlite3

def get_user_safe(username: str) -> list:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 안전한 쿼리 실행
    cursor.execute(
        "SELECT * FROM users WHERE username = ?", 
        (validate_input(username),)
    )
    return cursor.fetchall()
from pathlib import Path

ALLOWED_BASE = Path('/var/www/uploads')

def safe_file_upload(filename: str) -> Path:
    clean_name = Path(filename).name  # 경로 정보 제거
    target_path = ALLOWED_BASE / clean_name
    
    if not target_path.resolve().is_relative_to(ALLOWED_BASE):
        raise ValueError("잘못된 파일 경로")
        
    return target_path
import secrets

def generate_csrf_token() -> str:
    return secrets.token_urlsafe(32)  # 256비트 (URL-safe Base64)

def generate_api_key() -> str:
    return secrets.token_hex(32)  # 256비트 (HEX)
import logging

logger = logging.getLogger(__name__)

def process_payment(card_number: str):
    try:
        # 결제 처리 로직
    except PaymentGatewayError as e:
        logger.error(f"결제 실패: {e} (카드 마스킹: {card_number[-4:]})")
        raise PaymentError("결제 처리 중 오류 발생") from None  # 원본 예외 숨김
Validated input: 'test_user'
Hashed password (hex): 0304fde04e68294162bbda819ed3556565b2030167b30ce250a95e9800ccbbb5...
SQL query result: []
Generated secure token: 299fa659a367b15fb5a2deab695edbc0cd2f330f5a9e603b5bf99c75f1f91203
Safe file path: /allowed/path/data.txt
