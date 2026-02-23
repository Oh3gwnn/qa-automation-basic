import os
import shutil
import pytest
import base64
import pytest_html
from dotenv import load_dotenv

#1 [.env 자동화]
if not os.path.exists(".env") and os.path.exists(".env.example"):
    shutil.copy(".env.example", ".env")

#2 [환경 변수 로드]
load_dotenv(override=True)

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