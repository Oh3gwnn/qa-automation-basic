from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

'''
#1-1 --headed: 브라우저가 뜨는 것을 직접 확인
#1-2 -s: 코드 내의 print문이 있다면 터미널에 출력
pytest tests/ui/test_login_ui.py --headed -s

#2-1 리포트와 함께 실행
pytest tests/ui/test_login_ui.py --html=report.html --self-contained-html
> --html=report_ui_login_qa_20260222.html : 이런식으로 작성할 수도 있음, 당연히 한 폴더에 모으기도 가능
> --self-contained-html : 파일 하나에 모든 내용이 담김(CSS, 로고 등)
#2-2 리포트 살펴보기
start report.html
- Duration: 각 테스트 케이스가 몇 초나 걸렸는지 (성능 측정의 기초)
- Status: 초록색 Passed가 잘 떠 있는지
- Environment: 파이썬 버전, OS 등 테스트가 실행된 환경 정보

#3-1 테스트를 돌리면서 모든 기록을 trace.zip에 저장
pytest tests/ui/test_login_ui.py --tracing on

#3-2 터미널에서 실행
playwright show-trace test-results/나타난-폴더-이름/trace.zip
ex1) playwright show-trace test-results/tests-ui-test-login-ui-py-test-login-failure-chromium/trace.zip
ex2) playwright show-trace test-results/tests-ui-test-login-ui-py-test-login-success-chromium/trace.zip
'''

def test_login_success(page: Page):
    # 1. 페이지 객체 초기화
    login_page = LoginPage(page)
    
    # 2. 동작 수행 (성공 케이스)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    
    # 3. 검증
    login_page.expect_login_success()

def test_login_failure(page: Page):
    # 1. 페이지 객체 초기화
    login_page = LoginPage(page)
    
    # 2. 동작 수행 (실패 케이스 - 잘못된 비밀번호)
    login_page.goto()
    login_page.login("standard_user", "wrong_password")
    
    # 3. 검증 (에러 메시지 확인)
    login_page.expect_login_failure()