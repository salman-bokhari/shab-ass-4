import pytest
from app.calculator import cli

def run_repl(monkeypatch, inputs):
    """Run the REPL with a sequence of inputs."""
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))
    cli.repl()  # Run normally; no exceptions expected

def test_help_and_exit(monkeypatch, capsys):
    inputs = ["help", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "Simple Calculator REPL" in out
    assert "Commands:" in out
    assert "Operations:" in out
    assert "Usage:" in out

def test_addition(monkeypatch, capsys):
    inputs = ["add 2 3", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    # The REPL prints just the number, not "Result: ..."
    assert "5.0" in out

def test_subtraction(monkeypatch, capsys):
    inputs = ["sub 5 2", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "3.0" in out

def test_multiplication(monkeypatch, capsys):
    inputs = ["mul 3 4", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "12.0" in out

def test_division(monkeypatch, capsys):
    inputs = ["div 10 2", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "5.0" in out

def test_division_by_zero(monkeypatch, capsys):
    inputs = ["div 1 0", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    # Match whatever your CLI prints for division by zero
    assert "Error: Division by zero" in out or "Cannot divide by zero" in out

def test_invalid_command(monkeypatch, capsys):
    inputs = ["foobar", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    assert "Invalid input" in out or "Unknown" in out

def test_history(monkeypatch, capsys):
    inputs = ["add 1 2", "sub 5 3", "history", "exit"]
    run_repl(monkeypatch, inputs)
    out, _ = capsys.readouterr()
    # Your REPL should list previous calculations
    assert "1.0 + 2.0" in out or "5.0 - 3.0" in out

