# 가상환경 & Pytest 환경 설정

## 1. 가상환경 (venv)

프로젝트 루트(`web-service/`)에서 실행합니다.

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

- **`venv/`** 폴더는 `.gitignore`에 포함되어 있어 Git에 올라가지 않습니다.
- 터미널을 새로 열 때마다 **활성화**가 필요합니다 (`Activate` / `source venv/bin/activate`).

## 2. Pytest

개발 의존성에 `pytest`가 포함되어 있습니다 (`requirements-dev.txt`).

```bash
# 전체 테스트
pytest

# 특정 파일만
pytest tests/test_web_routes.py -v
pytest tests/test_app.py -v
```

- 설정: 루트의 **`pytest.ini`** (`testpaths=tests`, `pythonpath=.`).
- 픽스처: **`tests/conftest.py`** (`app`, `client`).

## 3. 앱 실행 (참고)

```bash
flask --app wsgi run
# 또는
python run.py
# 디버그(리로더 등): FLASK_DEBUG=1 python run.py  — 기본은 debug 비활성
```
