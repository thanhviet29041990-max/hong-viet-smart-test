
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]

SCHEMA = json.loads(
    (ROOT / "schema" / "worksheet.schema.json").read_text(
        encoding="utf-8"
    )
)

FIXTURE = json.loads(
    (ROOT / "fixtures" / "grade3-math.sample.json").read_text(
        encoding="utf-8"
    )
)


def test_schema_is_valid():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)


def test_fixture_matches_schema():
    jsonschema.validate(FIXTURE, SCHEMA)


def test_a4_print_configuration():
    page = FIXTURE["page"]
    assert page["size"] == "A4"
    assert page["showAnswers"] is False


def test_vietnamese_curriculum():
    assert FIXTURE["locale"] == "vi-VN"
    assert FIXTURE["curriculum"]["framework"] == "GDPT 2018"


def test_question_ids_are_unique():
    ids = [q["id"] for q in FIXTURE["questions"]]
    assert len(ids) == len(set(ids))


def test_geometry_has_diagram():
    for question in FIXTURE["questions"]:
        if question["type"] == "geometry":
            assert "diagram" in question
            assert question["diagram"]["kind"] == "svg-primitives"


def test_invalid_grade_is_rejected():
    invalid = dict(FIXTURE)
    invalid["grade"] = 6

    assert not jsonschema.Draft202012Validator(
        SCHEMA
    ).is_valid(invalid)
