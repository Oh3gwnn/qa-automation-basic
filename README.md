# Test Strategy

## 1. Purpose
본 문서는 Sauce Demo 웹 애플리케이션에 대해 테스트 전략을 정의하고, 자동화 테스트의 범위와 접근 방식을 명확히 하기 위함임.

## 2. Test Target
- Application: Sauce Demo
- URL: https://www.saucedemo.com/

## 3. Test Scope
### In Scope
  - **API Layer**: 장바구니 추가/삭제 컨트랙트 검증 및 상태 코드 확인 (Shopify API)

  - **UI Layer**: 주요 비즈니스 플로우(로그인, 상품 선택) E2E 테스트

  - **Hybrid**: API로 데이터를 생성하고 UI로 결과를 확인하는 효율적인 테스트 방식

### Out of Scope
- 결제 기능
- 관리자 기능
- 성능 테스트

## 4. Test Types
- Smoke Test
- Functional Test
- Regression Test

## 5. Automation Strategy
- Architecture: Page Object Model(POM)을 적용하여 유지보수성 향상 (진행 중)

- Configuration: python-dotenv를 활용한 민감 정보(.env) 관리 및 환경별 유연한 대응

- Robustness: UTF-8 기반 환경 설정 최적화 및 에러 핸들링 로직 포함

- Reporting: pytest-html을 활용한 자동화된 테스트 결과 리포팅 및 실패 시 스크린샷 캡처 (예정)

## 6. Test Environment
- Browser: Chromium
- OS: Windows
- Test Data: 고정 테스트 계정 사용

## 7. Risks & Mitigation
- 민감 정보 노출 리스크: .gitignore 및 환경 변수 관리를 통해 보안성 강화

- 테스트 환경 일관성: 환경 변수 로드 실패 시 테스트 즉시 중단 및 명확한 에러 메시지 제공

## 8. How to Run (수정 중)

프로젝트 실행 가이드
1. 초기 설정 (Setup)

가상 환경 생성: python -m venv venv

가상 환경 활성화 (Windows): .\venv\Scripts\activate

가상 환경 활성화 (Mac/Linux): source venv/bin/activate

필수 패키지 설치: pip install -r requirements.txt

브라우저 설치: playwright install

2. 환경 변수 관리

프로젝트 루트에 .env 파일이 필요합니다.

처음 실행 시 .env.example 파일이 자동으로 .env로 복사되도록 설정되어 있습니다.

3. 테스트 실행 방법

전체 테스트 실행 및 리포트 생성: pytest --html=reports/result.html --self-contained-html

특정 테스트 파일 실행: pytest tests/ui/test_login_ui.py --html=reports/result.html --self-contained-html

브라우저 화면을 보면서 실행: pytest --headed

4. 결과 확인 (Reporting)

테스트 완료 후 reports 폴더 안의 result.html 파일을 웹 브라우저로 엽니다.

테스트 실패 시, 해당 항목의 'expand' 버튼을 누르면 실패 시점의 스크린샷과 에러 로그를 한눈에 확인할 수 있습니다.

모든 스크린샷은 리포트 파일 하나에 내장(Self-contained)되어 있어 별도의 이미지 파일 관리가 필요 없습니다.

5. 프로젝트 주요 구조

tests/: UI 및 API 테스트 케이스

pages/: Page Object Model (POM) 설계 파일

reports/: 생성된 테스트 리포트 저장소

conftest.py/: 스크린샷 훅 및 환경 설정 로직