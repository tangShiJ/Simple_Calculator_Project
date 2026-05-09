import pytest
import builtins
import random
from simple_calculator import Calculator


class TestCalculator:

    def test_custom_operator_basic(self, x, y, op_choice, expected, monkeypatch, calculator):
        c = calculator
        c.x = x
        c.y = y
        monkeypatch.setattr(builtins, 'input', lambda prompt='': op_choice)
        result = c.custom_operator()
        assert result == expected

    def test_custom_operator_divide_by_zero(self, monkeypatch, calculator, test_data):
        c = calculator
        c.x = test_data['custom_operator_divide_by_zero'][0][0]
        c.y = test_data['custom_operator_divide_by_zero'][0][1]
        monkeypatch.setattr(builtins, 'input', lambda prompt='': test_data['custom_operator_divide_by_zero'][0][2])
        with pytest.raises(ZeroDivisionError):
            c.custom_operator()

    @pytest.mark.skip(reason="skip demo: invalid operator")
    def test_custom_operator_invalid_choice(self, monkeypatch, calculator):
        c = calculator
        c.x = 1
        c.y = 2
        monkeypatch.setattr(builtins, 'input', lambda prompt='': '9')
        result = c.custom_operator()
        assert isinstance(result, str) and '请输入正确的运算符' in result

    def test_ran_operator_deterministic(self, monkeypatch, x, y, choice_key, expected, calculator):
        c = calculator
        c.x = x
        c.y = y
        monkeypatch.setattr(random, 'choice', lambda seq: choice_key)
        ope_value = c.operator[choice_key]
        result = eval(f"{x}{ope_value}{y}")
        assert result == expected

    @pytest.mark.skip(reason="skip demo: ran divide by zero")
    def test_ran_operator_divide_by_zero(self, monkeypatch, calculator):
        c = calculator
        c.x = 5
        c.y = 0
        monkeypatch.setattr(random, 'choice', lambda seq: 'divide')
        c.ran_operator()

    @pytest.mark.xfail(reason="xfail demo: get_number may throw", strict=False)
    def test_get_number_invalid_input(self, monkeypatch, calculator):
        c = calculator
        inputs = iter(['a', 'b'])
        monkeypatch.setattr(builtins, 'input', lambda prompt='': next(inputs))
        with pytest.raises(ValueError):
            c.get_number()

    def test_additional_cases(self, x, y, op_choice, expected, monkeypatch, calculator):
        c = calculator
        c.x = x
        c.y = y
        monkeypatch.setattr(builtins, 'input', lambda prompt='': op_choice)
        assert c.custom_operator() == expected

    def test_select_operator_exit_immediately(self, monkeypatch, calculator, test_data):
        c = calculator
        inputs = iter(test_data['select_operator_inputs'][0])
        monkeypatch.setattr(builtins, 'input', lambda prompt='': next(inputs))
        c.select_operator()
