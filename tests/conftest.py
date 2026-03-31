import os
import shutil
import pytest
import base64
import pytest_html
from dotenv import load_dotenv
from datetime import datetime

#1 [.env 자동화]
def setup_env():
    if not os.path.exists(".env") and os.path.exists(".env.example"):
        try:
            shutil.copy(".env.example", ".env")
            print("\n[Auto-Setup] Created .env from .env.example")
        except Exception as e:
            print(f"\n[Auto-Setup] Failed to create .env: {e}")
    load_dotenv(override=True)

setup_env()

# 2. [리포트 상단 메타데이터 커스텀]
def pytest_html_report_title(report):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report.title = f"QA Automation Report ({now})"

#3 [UI TEST - failed - Screenshot-hook] 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_bytes = page.screenshot()
            b64 = base64.b64encode(screenshot_bytes).decode("utf-8")
            
            # 4.x는 extras (복수형), image()로 넣기
            report.extras = getattr(report, "extras", [])
            report.extras.append(pytest_html.extras.image(b64, mime_type="image/png"))