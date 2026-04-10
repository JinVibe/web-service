# README / 포트폴리오용 이미지

`README.md`는 아래 파일을 참조합니다.

| 파일 | 용도 |
| --- | --- |
| `screenshot-*.svg` | 레이아웃 안내용 벡터 미리보기 (다크 테마 앱 색상에 맞춤) |
| `demo.gif` (선택) | 흐름 데모 — 없으면 README에서 해당 블록을 비워 두거나 주석 처리 |

## 실제 캡처로 바꾸기

1. `flask --app wsgi run` 후 브라우저에서 각 페이지를 연다.
2. 스크린샷 도구로 PNG 저장 (예: `home.png`, `projects.png`, `contact.png`, `apidocs.png`).
3. 루트 `README.md`의 이미지 경로를 `docs/assets/home.png` 등으로 바꾼다.
4. (선택) [ScreenToGif](https://www.screentogif.com/) 등으로 짧은 GIF를 `docs/assets/demo.gif`에 넣고 README의 GIF 섹션을 활성화한다.
