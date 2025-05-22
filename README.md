def validate_input(user_input: str, max_length=100) -> str:
    if not isinstance(user_input, str):
        raise TypeError("입력은 문자열이어야 합니다")
    if len(user_input) > max_length:
        raise ValueError(f"입력 길이 초과 (최대 {max_length}자)")
    return user_input.strip()
import hashlib
import os
def log_error(error_msg: str, error_level="ERROR"):
    """오류 발생 시 로깅하는 함수"""
    if error_level == "ERROR":
        logger.error(error_msg)
    elif error_level == "WARNING": 
        logger.warning(error_msg)
    elif error_level == "CRITICAL":
        logger.critical(error_msg)
    else:
        logger.info(error_msg)
def secure_hello_world(user_input: str = None) -> str:
    """
    안전한 Hello World 함수
    
    Args:
        user_input: 사용자 입력 (선택사항)
        
    Returns:
        str: 안전하게 처리된 메시지
        
    Raises:
        ValueError: 입력이 유효하지 않은 경우
    """
    try:
        # 입력값 검증
        if user_input:
            validated_input = validate_input(user_input)
            return f"Hello, {validated_input}!"
        return "Hello, World!"
    except Exception as e:
        log_error(f"메시지 생성 중 오류 발생: {str(e)}", "ERROR")
        return "Hello, World!"  # 기본값 반환

if __name__ == "__main__":
    try:
        result = secure_hello_world()
        print(result)
    except Exception as e:
        log_error(f"프로그램 실행 중 오류 발생: {str(e)}", "CRITICAL")


# 사용 예시
try:
    result = some_risky_operation()
except Exception as e:
    log_error(f"작업 중 오류 발생: {str(e)}")
    # 또는 
    # log_error(f"심각한 오류 발생: {str(e)}", "CRITICAL")

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
        # 결제 실패 시 로그를 남기되, 카드번호는 마지막 4자리만 마스킹하여 기록
        # e.g. "결제 실패: Gateway timeout (카드 마스킹: 1234)"
        logger.error(f"결제 실패: {e} (카드 마스킹: {card_number[-4:]})")

        # PaymentGatewayError를 PaymentError로 변환하여 재발생
        # from None을 사용하여 원본 예외 정보를 숨김 (보안상 이유)
        # 이는 외부에 상세 에러 정보가 노출되는 것을 방지
        raise PaymentError("결제 처리 중 오류 발생") from None  # 원본 예외 숨김
Validated input: 'test_user'
Hashed password (hex): 0304fde04e68294162bbda819ed3556565b2030167b30ce250a95e9800ccbbb5...
SQL query result: []
Generated secure token: 299fa659a367b15fb5a2deab695edbc0cd2f330f5a9e603b5bf99c75f1f91203
Safe file path: /allowed/path/data.txt
