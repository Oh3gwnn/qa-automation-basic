# Test Strategy

## 1. Purpose
본 문서는 Sauce Demo 웹 애플리케이션에 대해 테스트 전략을 정의하고, 자동화 테스트의 범위와 접근 방식을 명확히 하기 위함임.

## 2. Test Target
- Application: Sauce Demo
- URL: https://www.saucedemo.com/

## 3. Test Scope
### In Scope
- 사용자 로그인
- 상품 목록 조회
- 상품 장바구니 추가/삭제
- 장바구니 페이지 이동

### Out of Scope
- 결제 기능
- 관리자 기능
- 성능 테스트

## 4. Test Types
- Smoke Test
- Functional Test
- Regression Test

## 5. Automation Strategy
- Playwright를 사용한 E2E 테스트 자동화
- 주요 사용자 플로우 중심 자동화
- 반복 실행이 잦은 테스트 우선 자동화

## 6. Test Environment
- Browser: Chromium
- OS: Windows
- Test Data: 고정 테스트 계정 사용

## 7. Risks & Mitigation
- 테스트 데이터 변경으로 인한 실패 가능성  
  → 테스트 전 데이터 상태 확인