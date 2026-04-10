# Dev-Log — Personal Tech Portfolio & Blog

Flask 기반 **개인 포트폴리오·기술 블로그**입니다. 홈·프로젝트·연락처 화면에 더해 **JSON API**, **Swagger UI**, **Sphinx 기술 문서**, **GitHub Pages 배포**까지 한 흐름으로 보여 줄 수 있게 구성했습니다.

![Python](https://img.shields.io/badge/python-3.11+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000?logo=flask&logoColor=white)
![pytest](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)

## 이 프로젝트로 보여 주는 것

- **제품 감각**: 방문자가 바로 이해할 수 있는 내비게이션과 카드형 프로젝트 목록, 다크 톤 UI (`app/static/css/main.css`)
- **유지보수**: Blueprint 분리, `site_data`로 JSON 콘텐츠 로딩, 연락처 표시 규칙 분리 (`contact_display`)
- **품질**: README 명세(R1–R3)를 `pytest`로 고정하는 **TDD** 흐름 (`tests/`)
- **문서화**: **Sphinx** autodoc + (선택) **GitHub Actions → Pages**, **Flasgger**로 API 스펙·Try-it-out

## 스크린샷

아래는 **벡터 미리보기**(실제 UI와 톤을 맞춘 플레이스홀더)입니다. 제출·포트폴리오용으로는 `docs/assets/README.md` 안내에 따라 **브라우저 캡처 PNG**로 바꾸는 것을 권장합니다.

| 홈 `/home` | 프로젝트 `/projects` |
| --- | --- |
| ![홈 화면 미리보기](docs/assets/screenshot-home.svg) | ![프로젝트 목록 미리보기](docs/assets/screenshot-projects.svg) |

| 연락처 `/contact` | API 문서 `/apidocs/` |
| --- | --- |
| ![연락처 미리보기](docs/assets/screenshot-contact.svg) | ![Swagger UI 미리보기](docs/assets/screenshot-apidocs.svg) |

### 데모 GIF (선택)

[ScreenToGif](https://www.screentogif.com/) 등으로 녹화해 `docs/assets/demo.gif`로 저장한 뒤, 이 섹션 아래에 다음 한 줄을 붙이면 됩니다.

```markdown
![데모 GIF](docs/assets/demo.gif)
```

## 문서 · 링크

| 항목 | 링크 / 위치 |
| --- | --- |
| **환경 설정·Sphinx·Pages·Flasgger** | [`docs/SETUP.md`](docs/SETUP.md) |
| **기술 문서 (Sphinx, 로컬)** | `docs/source/` → `sphinx-build -M html docs/source docs/build` → `docs/build/html/index.html` |
| **기술 문서 (온라인)** | GitHub 저장소 **Settings → Pages**에서 Actions 배포 후 표시되는 URL (예: `https://<user>.github.io/<repo>/`) |
| **REST API (JSON)** | `GET /api/projects`, `GET /api/contact/channels` |
| **Swagger UI** | 서버 실행 후 브라우저에서 `/apidocs/` · OpenAPI JSON: `/apispec_1.json` |
| **Docker** | 루트 [`Dockerfile`](Dockerfile) |

## 빠른 시작

전체 절차·트러블슈팅은 **[`docs/SETUP.md`](docs/SETUP.md)** 를 기준으로 합니다.

```bash
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt   # Pytest, Sphinx 등

flask --app wsgi run
# 브라우저: http://127.0.0.1:5000/home
```

**진입점**

| 파일 | 역할 |
| --- | --- |
| **`app/`** (패키지) | `create_app`, Blueprint, 템플릿, 정적 리소스 |
| **`wsgi.py`** | 권장: `app` 인스턴스 (Docker·`FLASK_APP`) |
| **`app.py`** | Lab 호환: `wsgi`와 동일 앱 재노출 |
| **`run.py`** | 로컬 실행 래퍼 (디버그는 `FLASK_DEBUG=1` 등) |

**로컬 검증 (`curl`)**

```bash
curl -sI http://127.0.0.1:5000/          # → /home 리다이렉트
curl -s http://127.0.0.1:5000/api/projects | head -c 200
curl -s http://127.0.0.1:5000/apispec_1.json | head -c 120
```

**엔드포인트 요약**

- **페이지**: `/` → `/home`, `/home`, `/projects`, `/contact`
- **API**: `/api/projects`, `/api/contact/channels`
- **문서 UI**: `/apidocs/`, `/apispec_1.json`

**구조·데이터**

- Blueprint 등록: `app/bootstrap.py` · 공통 스타일: `app/static/css/main.css`
- 콘텐츠: `app/data/projects.json`, `app/data/contact.json` (`app/site_data.py`)
- 비속어 마스킹: `app/data/profanity_words.json`, `app/profanity.py`

---

## TDD & Pytest (AI Assistant 협업)

**목표**: README의 기능 명세(R1–R3)를 **테스트로 먼저 고정**하고, 구현은 테스트가 초록일 때까지 맞춘다.

| 단계 | 누가 | 내용 |
| --- | --- | --- |
| **1. Setup** | 개발자 | `docs/SETUP.md`대로 venv 생성 후 `pip install -r requirements-dev.txt` → Pytest + `tests/conftest.py` |
| **2. Branch** | 개발자 | `git checkout -b test` (기능/테스트 작업 브랜치) |
| **3. RED** | 사람(명세) | 예: `tests/test_app.py`에 `mask_profanity` 등 **실패할 테스트**를 먼저 작성 (`tests/test_web_routes.py`는 라우트용) |
| **4. GREEN** | AI/페어 | 라우트·템플릿 등 **최소 구현**으로 `pytest` 통과 |
| **5. REFACTOR** | 공동 | 중복 제거·이름 정리 등 (테스트는 계속 통과) |
| **6. 검증** | 개발자 | `pytest` + 브라우저에서 `/home`, `/projects`, `/contact` 확인 |
| **7. Push** | 개발자 | PR 후 `main`에 머지 |

```bash
# 테스트 전용 의존성
pip install -r requirements-dev.txt

# 전체 테스트
pytest

# 한 파일만
pytest tests/test_web_routes.py -v
```

- **RED → GREEN**: 새 기능을 넣을 때는 **테스트 추가(RED) → 구현(GREEN)** 순서를 지키면 TDD 사이클이 된다.
- **Web routes**: `client.get("/경로")`로 서버 없이 응답 코드·HTML 일부를 검증한다.
- **Client-side(네비)**: `url_for`로 링크 대상 엔드포인트가 존재하는지 검증한다.

---

## 1. 요구 분석 (Requirement Analysis)

### 1.1 기능적 요구사항 (Functional Requirements)

시스템이 제공해야 하는 **동작**을 정의한 요구사항이다.

| ID | 요구사항 | 설명 | 우선순위 |
| --- | --- | --- | --- |
| **R1** | 홈 화면 제공 | 사용자가 접속했을 때 서비스의 목적과 환영 메시지를 보여준다. (`/`, `/home`) | 필수 |
| **R2** | 프로젝트 목록 조회 | 개발자가 수행한 프로젝트 리스트(기술 스택, 설명 포함)를 사용자에게 노출한다. (`/projects`) | 필수 |
| **R3** | 연락처 정보 제공 | 협업·문의를 위해 개발자의 이메일, GitHub 등 연락 채널을 확인할 수 있다. (`/contact`) | 필수 |

### 1.2 비기능적 요구사항 (Non-functional Requirements)

동작 외에 **품질·제약**을 정의한 요구사항이다.

| ID | 분류 | 요구사항 | 설명 |
| --- | --- | --- | --- |
| **NFR1** | 성능(Performance) | 응답 시간 | 각 페이지 요청에 대해 로컬 환경에서 1초 이내 응답한다. |
| **NFR2** | 가용성(Availability) | 서비스 가동 | Flask 서버 구동 중에는 중단 없이 서비스가 제공된다. |
| **NFR3** | 코드 품질 | 가독성·표준 | 변수·함수명을 명확히 하고 PEP8 스타일 가이드를 준수한다. |
| **NFR4** | 유지보수성(Maintainability) | 모듈화 | Flask Blueprint를 활용해 기능별로 분리하여 확장·수정이 용이하다. |
| **NFR5** | 확장성(Scalability) | 구조 | 추후 DB(SQLite 등) 연동을 고려한 라우트·레이어 구조를 따른다. |

---

## 2. 유즈 케이스 (Use Case)

### 2.1 유즈 케이스 목록

| UC-ID | 유즈 케이스명 | 액터 | 요약 |
| --- | --- | --- | --- |
| UC-01 | 자기소개 확인 | 방문자 | 홈에서 개발자 소개 및 서비스 목적을 확인한다. |
| UC-02 | 프로젝트·기술 스택 열람 | 방문자 | 프로젝트 목록에서 기술 스택과 상세 설명을 파악한다. |
| UC-03 | 연락처 확인 및 협업 문의 | 방문자 | 연락처 페이지에서 이메일·GitHub 등 채널을 확인한다. |

### 2.2 유즈 케이스 상세

#### UC-01: 자기소개 확인

| 항목 | 내용 |
| --- | --- |
| **액터** | 방문자(비로그인 사용자) |
| **목표** | 개발자 소개와 서비스 목적을 파악한다. |
| **사전 조건** | 웹 브라우저로 서비스에 접근 가능하다. |
| **사후 조건** | 홈 페이지 내용을 확인한 상태가 된다. |
| **메인 플로우** | 1. 방문자가 `/` 또는 `/home`에 접속한다.<br>2. 시스템이 서비스 목적·환영 메시지·개발자 소개를 담은 홈 화면을 응답한다.<br>3. 방문자가 해당 내용을 확인한다. |
| **대안 플로우** | 2-a. `/` 접속 시 시스템이 `/home`으로 리다이렉트한 뒤 동일한 홈 화면을 보여준다. |
| **관련 요구사항** | R1 |

#### UC-02: 프로젝트·기술 스택 열람

| 항목 | 내용 |
| --- | --- |
| **액터** | 방문자 |
| **목표** | 개발자가 참여한 프로젝트와 사용 기술 스택을 파악한다. |
| **사전 조건** | 웹 브라우저로 서비스에 접근 가능하다. |
| **사후 조건** | 프로젝트 목록 및 각 항목의 스택·설명을 확인한 상태가 된다. |
| **메인 플로우** | 1. 방문자가 `/projects`에 접속한다.<br>2. 시스템이 프로젝트 리스트(제목, 기술 스택, 상세 설명)를 포함한 페이지를 응답한다.<br>3. 방문자가 목록을 열람한다. |
| **관련 요구사항** | R2 |

#### UC-03: 연락처 확인 및 협업 문의

| 항목 | 내용 |
| --- | --- |
| **액터** | 방문자 |
| **목표** | 개발자에게 연락할 수 있는 채널(이메일, GitHub 등)을 확인한다. |
| **사전 조건** | 웹 브라우저로 서비스에 접근 가능하다. |
| **사후 조건** | 연락처 정보를 확인하고, 필요 시 외부 도구(메일 클라이언트, GitHub)로 연락할 수 있다. |
| **메인 플로우** | 1. 방문자가 `/contact`에 접속한다.<br>2. 시스템이 연락처 채널(이메일, GitHub 링크 등)을 노출한 페이지를 응답한다.<br>3. 방문자가 링크를 통해 메일 작성 또는 GitHub 페이지로 이동한다. |
| **관련 요구사항** | R3 |

---

## 3. 기능 명세서 (Functional Specification)

### 3.1 기능 개요

| 기능 ID | 기능명 | 경로 | HTTP 메서드 | 설명 |
| --- | --- | --- | --- | --- |
| F1 | 루트 리다이렉트 | `/` | GET | `/home`으로 302 리다이렉트한다. |
| F2 | 홈 화면 | `/home` | GET | 서비스 소개·개발자 소개를 담은 HTML 페이지를 반환한다. |
| F3 | 프로젝트 목록 | `/projects` | GET | 프로젝트 제목·스택·설명이 포함된 HTML 페이지를 반환한다. |
| F4 | 연락처 | `/contact` | GET | 연락 채널(이메일, GitHub 등)이 포함된 HTML 페이지를 반환한다. |

### 3.2 기능별 상세 명세

#### F1: 루트 리다이렉트

| 항목 | 명세 |
| --- | --- |
| **입력** | 없음 (GET `/`) |
| **출력** | HTTP 302, `Location: /home` |
| **비고** | 브라우저·클라이언트는 `/home`으로 재요청한다. |

#### F2: 홈 화면

| 항목 | 명세 |
| --- | --- |
| **입력** | GET `/home` |
| **출력** | HTML (200). 포함 내용: 서비스 목적, 환영 메시지, 개발자 소개 |
| **화면 요소** | 제목, 본문 텍스트, 네비게이션(홈/프로젝트/연락처) |
| **예외** | 없음 (정적 페이지) |

#### F3: 프로젝트 목록

| 항목 | 명세 |
| --- | --- |
| **입력** | GET `/projects` |
| **출력** | HTML (200). 포함 내용: 프로젝트 카드 목록(제목, 기술 스택 태그, 상세 설명) |
| **데이터** | 프로젝트별: `title`, `stack[]`, `description` (`app/data/projects.json`, 추후 DB 연동 가능) |
| **화면 요소** | 목록 제목, 카드 단위 표시, 네비게이션 |

#### F4: 연락처

| 항목 | 명세 |
| --- | --- |
| **입력** | GET `/contact` |
| **출력** | HTML (200). 포함 내용: 연락 채널 목록(라벨, URL) |
| **데이터** | 채널별: `label`, `url` (`app/data/contact.json`; 예: Email → mailto:, GitHub → https://...) |
| **화면 요소** | 제목, 채널 링크 목록, 네비게이션 |
| **비고** | http(s) 링크는 `app/contact_display.py`에서 새 탭·`rel` 여부를 결정, 템플릿은 플래그만 사용 |

### 3.3 공통 화면 요구사항

- 모든 페이지는 **공통 레이아웃**(base 템플릿)을 사용한다.
- 상단 **네비게이션**: 홈, 프로젝트, 연락처 링크를 포함한다.
- 반응형·가독성을 고려한 단순한 스타일을 적용한다.
