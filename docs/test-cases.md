# Test Cases

본 문서는 Test Scenario를 기반으로 실행 가능한 테스트 케이스를 정의한다.
각 테스트 케이스는 자동화 테스트 구현 시 1:1 매핑을 목표로 한다.

---

## Login Feature

### TC-LOGIN-001: Valid user login
**Precondition**
- Sauce Demo 접속 가능
- 정상 계정 존재(standard_user)

**Steps**
1. 로그인 페이지 접속
2. Username에 `standard_user` 입력
3. Password에 `secret_sauce` 입력
4. Login 버튼 클릭

**Expected Result**
- Inventory(상품 목록) 페이지로 이동한다.
- 상품 목록 컨테이너가 화면에 표시된다.

---

### TC-LOGIN-002: Invalid user login (wrong password)
**Precondition**
- Sauce Demo 접속 가능

**Steps**
1. 로그인 페이지 접속
2. Username에 `standard_user` 입력
3. Password에 `wrong_password` 입력
4. Login 버튼 클릭

**Expected Result**
- 로그인 실패 에러 메시지가 표시된다.
- Inventory 페이지로 이동하지 않는다.

---

### TC-LOGIN-003: Invalid user login (empty username)
**Precondition**
- Sauce Demo 접속 가능

**Steps**
1. 로그인 페이지 접속
2. Username을 비운다.
3. Password에 `secret_sauce` 입력
4. Login 버튼 클릭

**Expected Result**
- Username required 관련 에러 메시지가 표시된다.
- 페이지 이동이 발생하지 않는다.