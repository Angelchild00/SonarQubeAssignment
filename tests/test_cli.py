from calculator.cli import evaluate, run


# ---------- Happy path ----------

def test_evaluate_addition():
    assert evaluate("2 + 3") == 5


def test_evaluate_without_spaces():
    assert evaluate("10/4") == 2.5


def test_evaluate_power():
    assert evaluate("2 ** 3") == 8


# ---------- Sad path ----------

def test_evaluate_divide_by_zero_returns_none():
    assert evaluate("10 / 0") is None


def test_evaluate_rejects_code_injection():
    # This input used to be executed by eval(); it must now be rejected.
    assert evaluate("__import__('os').getcwd()") is None


def test_evaluate_rejects_garbage():
    assert evaluate("hello") is None


def test_run_loop(monkeypatch, capsys):
    inputs = iter(["2 + 3", "bad input", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run()
    output = capsys.readouterr().out
    assert "5" in output
    assert "Error" in output
