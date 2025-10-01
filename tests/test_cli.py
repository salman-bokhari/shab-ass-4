import pytest
from app.calculator import cli

def run_repl(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))
    with pytest.raises(StopIteration, match=None):
        cli.repl()

def test_help_and_exit(monkeypatch):
    inputs = ["help", "exit"]
    # simulate StopIteration at end to exit loop
    inputs.append(StopIteration)
    run_repl(monkeypatch, inputs)

def test_addition(monkeypatch, capsys):
    inputs = ["add 2 3", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    with pytest.raises(SystemExit, match=None):
        cli.repl()
    out, _ = capsys.readouterr()
    assert "Result: 5.0" in out

def test_division_by_zero(monkeypatch, capsys):
    inputs = ["div 1 0", "exit"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    with pytest.raises(SystemExit, match=None):
        cli.repl()
    out, _ = capsys.readouterr()
    assert "Cannot divide by zero" in out

def test
