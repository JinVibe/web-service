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

## 4. Sphinx 문서 (HTML)

`requirements-dev.txt`에 `sphinx`, `sphinx-rtd-theme`이 포함되어 있습니다.

```bash
# 프로젝트 루트에서 venv 활성화 후
pip install -r requirements-dev.txt

# 문서 빌드 (출력: docs/build/html/)
cd docs
sphinx-build -M html source build
```

Windows에서는 `docs` 폴더에서 `.\make.bat html`도 동일하게 동작합니다. 생성된 `docs/build/html/index.html`을 브라우저로 열면 됩니다.

`app` 패키지 구조가 바뀌면 **프로젝트 루트가 아니라 `docs` 폴더에서** 아래처럼 다시 생성할 수 있습니다. (`sphinx-apidoc`는 `pip install sphinx` 후 PATH에 있는 명령 이름입니다. `docs/sphinx-apidoc` 같은 경로는 없습니다.)

```bash
cd docs
sphinx-apidoc -o source -f -M ../app
```

이후 `source/index.rst`의 `toctree`에 `modules`가 포함되어 있는지 확인하세요.
