from pypdf import PdfReader, PdfWriter

# 원본 PDF 파일 읽기
reader = PdfReader("input.pdf")
writer = PdfWriter(clone_from=reader)

# 비밀번호 설정 (예: 'securepassword123')
writer.encrypt("securepassword123")

# 암호화된 PDF 파일로 저장
with open("output_encrypted.pdf", "wb") as f:
    writer.write(f)
import os
from pypdf import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, password):
    if not os.path.exists(input_path):
        raise FileNotFoundError("입력 파일이 존재하지 않습니다.")

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter(clone_from=reader)
        writer.encrypt(password)
        with open(output_path, "wb") as f:
            writer.write(f)
        print("암호화 완료:", output_path)
    except Exception as e:
        print("에러 발생:", e)

# 환경변수에서 비밀번호 읽기 (예시)
import getpass
password = getpass.getpass("PDF 비밀번호 입력: ")
encrypt_pdf("input.pdf", "output_encrypted.pdf", password)
