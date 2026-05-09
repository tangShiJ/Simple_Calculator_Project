import json
import pathlib
import builtins
import pytest
from simple_calculator import Calculator


def _load_test_data():
    # Resolve the directory containing this conftest.py (should be the tests/ directory)
    here = pathlib.Path(__file__).resolve().parent
    candidates = [
        here / 'data' / 'operators.json',           # tests/data/operators.json (preferred)
        here.parent / 'data' / 'operators.json',    # project_root/data/operators.json
        pathlib.Path.cwd() / 'tests' / 'data' / 'operators.json',
        pathlib.Path.cwd() / 'data' / 'operators.json',
    ]

    for p in candidates:
        try:
            if p.exists():
                return json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            # If a file is found but can't be read/parsed, re-raise with context
            raise

    # If we get here, none of the candidate files were found
    tried = '\n'.join(str(p) for p in candidates)
    raise FileNotFoundError(
        "Could not find operators.json in any of the expected locations.\nTried:\n" + tried
    )


# cache loaded data at module import so pytest_generate_tests can use it
_TEST_DATA = _load_test_data()


def pytest_generate_tests(metafunc):
    """Dynamically parametrize tests based on keys in tests/data/operators.json.

    Mapping (test function name -> (data_key, argnames)):
      - test_custom_operator_basic -> custom_operator_basic -> (x,y,op_choice,expected)
      - test_ran_operator_deterministic -> ran_operator -> (x,y,choice_key,expected)
      - test_additional_cases -> additional_cases -> (x,y,op_choice,expected)

    If no data key is present, leave the test unparametrized and let any existing @pytest.mark.parametrize handle it.
    """
    name = metafunc.function.__name__
    mapping = {
        'test_custom_operator_basic': ('custom_operator_basic', ['x', 'y', 'op_choice', 'expected']),
        'test_ran_operator_deterministic': ('ran_operator', ['x', 'y', 'choice_key', 'expected']),
        'test_additional_cases': ('additional_cases', ['x', 'y', 'op_choice', 'expected']),
    }

    if name in mapping:
        data_key, argnames = mapping[name]
        data = _TEST_DATA.get(data_key)
        if data:
            # parametrize using the list of rows from JSON
            metafunc.parametrize(argnames, data)


@pytest.fixture(scope='session')
def test_data():
    """Load parametrized test data from tests/data/operators.json"""
    return _TEST_DATA


@pytest.fixture
def calculator():
    """Provide a fresh Calculator instance for each test."""
    return Calculator()


@pytest.fixture
def mock_input(monkeypatch):
    """Helper fixture that lets tests set the next inputs via iterable.

    Usage:
        inputs = iter(['1', '2'])
        mock_input(inputs)
    """
    def _mock(inputs_iter):
        monkeypatch.setattr(builtins, 'input', lambda prompt='': next(inputs_iter))
    return _mock
