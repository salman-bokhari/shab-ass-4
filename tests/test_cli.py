import pytest
from app.calculator import cli

def run_repl(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))
    cli.repl()  # Do NOT expect exception

def test_help_and_exit(monkeypatch, capsys):
    inputs = ["help", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "Commands:" in out
    assert "Simple Calculator REPL" in out

def test_addition(monkeypatch, capsys):
    inputs = ["add 2 3", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "Result: 5.0" in out

def test_division_by_zero(monkeypatch, capsys):
    inputs = ["div 1 0", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "Error: Division by zero" in out or "Cannot divide by zero" in out

def test_invalid_command(monkeypatch, capsys):
    inputs = ["foobar", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "Invalid input" in out or "Unknown" in out
