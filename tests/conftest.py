import os
import shutil
import pytest
from dotenv import load_dotenv

# .env 파일이 없으면 .env.example을 복사해서 생성
if not os.path.exists(".env") and os.path.exists(".env.example"):
    shutil.copy(".env.example", ".env")
    print("\n💡 [INFO] .env 파일이 자동 생성되었습니다.")

# 환경 변수 로드
load_dotenv(override=True)