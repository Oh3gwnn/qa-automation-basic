# Test Strategy

## 1. Purpose
본 문서는 Sauce Demo 웹 애플리케이션 및 Shopify API를 대상으로, 안정적이고 효율적인 테스트 자동화 환경을 구축하여 전반적인 품질을 검증하는 것을 목적으로 합니다.

## 2. Test Target
- **UI Application**: Sauce Demo (https://www.saucedemo.com/)
- **API Target**: Shopify Storefront API (https://sauce-demo.myshopify.com/)

## 3. Test Scope
### In Scope
- **API Layer**: 장바구니 추가/삭제 컨트랙트 검증 및 상태 코드 확인
- **UI Layer**: 주요 비즈니스 플로우(로그인, 장바구니, 상품 선택) E2E 테스트
- **Hybrid Test**: API로 데이터를 생성(장바구니 추가)하고, UI로 결과를 확인하여 테스트 속도 및 효율성 극대화
- **Checkout Flow**: Data-Driven Testing(DDT)을 적용한 결제 폼 유효성 검증

## 4. Test Types
- Smoke Test
- Functional Test
- Regression Test (GitHub Actions 기반 CI 연동)

## 5. Automation Strategy
- **Architecture**: Page Object Model(POM) 기반 설계로 코드 재사용성 및 유지보수성 극대화
- **Data-Driven Testing (DDT)**: `pytest.mark.parametrize`를 활용하여 다양한 경계값 및 실패 시나리오를 단일 코드로 검증
- **Configuration**: `python-dotenv`를 활용한 민감 정보(`SAUCE_USERNAME`, `API_BASE_URL` 등) 분리 및 `conftest.py`를 통한 환경 자동 셋업
- **Reporting**: `pytest-html`을 활용해 테스트 실패 시 자동으로 브라우저 스크린샷을 캡처하고 리포트에 내장(Self-contained)
- **CI/CD Pipeline**: GitHub Actions를 구축하여 코드가 Push될 때마다 Ubuntu 환경에서 자동으로 전체 테스트가 실행되도록 파이프라인 구성

## 6. Test Environment
**Browser**: Chromium (Playwright)
- **OS**: Window(Initial setting), macOS (Local Development), Ubuntu (GitHub Actions CI)
- **Language & Framework**: Python 3.11, Pytest, Playwright(Python-based)

## 7. Risks & Mitigation
- **민감 정보 노출 리스크**: GitHub Secrets를 활용하여 CI 환경에 안전하게 환경 변수 주입
- **환경 셋업 누락**: `conftest.py`에 `.env.example`을 `.env`로 자동 복사하는 훅(Hook)을 구현하여 협업 시 초기 셋업 허들 제거

## 8. How to Run

**1. 가상 환경 생성 및 활성화**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# Windows: .\venv\Scripts\activate
```

**2. 패키지 및 브라우저 설치**

```bash
pip install -r requirements.txt
playwright install chromium
```

**3. 환경 변수 세팅**

pytest 실행 시 conftest.py에 의해 .env.example 파일이 .env로 자동 복사됩니다.

생성된 .env 파일에 실제 접속 정보 및 API 키를 입력합니다.

---

### Execute Tests

**전체 실행 및 리포트 생성**
```bash
pytest --html=reports/report.html --self-contained-html
```

**특정 테스트 실행 (UI 모드)**
```bash
pytest --html=reports/report.html --self-contained-html
```

---

### Reporting
테스트 완료 후 `reports/report.html` 파일을 브라우저로 엽니다.
```bash
open reports/report.html  # Mac
start reports/report.html # Window
```

실패(Failed)한 케이스의 경우 에러 로그와 함께 실패 시점의 화면 스크린샷을 바로 확인할 수 있습니다.