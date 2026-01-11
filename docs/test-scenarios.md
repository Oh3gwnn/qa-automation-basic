# Test Scenarios

본 문서는 Sauce Demo 웹 애플리케이션의
핵심 사용자 플로우를 기준으로 테스트 시나리오를 정의한다.
본 시나리오는 이후 테스트 케이스 및 자동화 테스트 코드의 기준이 된다.

---

## 1. Login Feature

### Scenario 1: Valid user login
**Description**  
정상적인 사용자 계정으로 로그인 시, 사용자는 상품 목록(Inventory) 페이지로 이동할 수 있어야 한다.

**Expected Result**
- 로그인 성공 후 Inventory 페이지로 이동한다.
- 상품 목록이 정상적으로 표시된다.

---

### Scenario 2: Invalid user login
**Description**  
잘못된 사용자 계정 정보로 로그인 시, 시스템은 로그인 실패를 사용자에게 안내해야 한다.

**Expected Result**
- 로그인 실패 메시지가 화면에 표시된다.
- 페이지 이동이 발생하지 않는다.

---

## 2. Inventory Feature

### Scenario 3: View product list
**Description**  
로그인에 성공한 사용자는 상품 목록 페이지에서 여러 개의 상품을 확인할 수 있어야 한다.

**Expected Result**
- 상품 리스트가 화면에 표시된다.
- 각 상품에 이름, 가격, Add to Cart 버튼이 존재한다.

---

## 3. Cart Feature

### Scenario 4: Add product to cart
**Description**  
사용자는 상품 목록 페이지에서 상품을 장바구니에 추가할 수 있어야 한다.

**Expected Result**
- Add to Cart 버튼 클릭 시 장바구니에 상품이 추가된다.
- 장바구니 아이콘의 상품 수량이 증가한다.

---

### Scenario 5: Remove product from cart
**Description**  
사용자는 장바구니에 추가한 상품을 제거할 수 있어야 한다.

**Expected Result**
- Remove 버튼 클릭 시 상품이 장바구니에서 제거된다.
- 장바구니 수량이 감소하거나 표시되지 않는다.

---

## 4. Cart Navigation Feature

### Scenario 6: Navigate to cart page
**Description**  
사용자는 장바구니 아이콘을 클릭하여 장바구니 상세 페이지로 이동할 수 있어야 한다.

**Expected Result**
- Cart 페이지로 정상 이동한다.
- 장바구니에 담긴 상품 목록이 표시된다.