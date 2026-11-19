# Hong Viet Smart Test — Worksheet Schema v0.1

**Status:** Public-ready specification and automated JSON contract tests. **Not** a working PDF renderer or completed product.

A curriculum-aware worksheet data contract for Vietnamese elementary grades 1–5, starting with a Grade 3 Mathematics fixture. This is intended as an implementation starting point for an editable A4 worksheet renderer.

## Files

- [`schema/worksheet.schema.json`](schema/worksheet.schema.json) — JSON Schema Draft 2020-12 contract.
- [`fixtures/grade3-math.sample.json`](fixtures/grade3-math.sample.json) — Vietnamese Grade 3 Math fixture including rectangle SVG primitives.
- [`tests/test_worksheet.py`](tests/test_worksheet.py) — executable positive and negative validation tests.
- [`.github/workflows/tests.yml`](.github/workflows/tests.yml) — GitHub Actions checks on every push and pull request.

## Run tests

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Planned rendering architecture

Structured worksheet JSON → JSON Schema/Zod validation → React + TypeScript → KaTeX for mathematical notation → controlled SVG geometry renderer → Chromium/Playwright print CSS → A4 PDF.

Planned rendering acceptance checks (not yet implemented): A4 210 × 297 mm, visible Vietnamese diacritics, correctly rendered math, page-break safety, no clipped diagrams or text, empty student answer areas, teacher-reviewed answers separately, visual diff tests, and physical print inspection.

## Curriculum and quality caveats

- Curriculum metadata currently identifies GDPT 2018 / Kết nối tri thức, but **alignment has not been independently verified** by a teacher.
- The schema validates structure; it **does not verify mathematical correctness** or page appearance.
- `targetPages: 2` is an intent, not proof that an A4 PDF renders as two pages.
- Student-facing fixture has `showAnswers: false`. A separate teacher-answer-key contract is not yet implemented.
- This repo is an initial build specification, not a public product launch.

## Day-one task for Devin

Implement a local renderer that reads the fixture, validates it, displays an A4 preview, exports an A4 PDF using Playwright Chromium, and adds screenshot/PDF acceptance tests. Avoid placing credentials in source code.
