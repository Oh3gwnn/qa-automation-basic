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