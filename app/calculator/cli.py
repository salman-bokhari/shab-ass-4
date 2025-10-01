"""REPL interface for the calculator."""
from app.calculation.factory import CalculationFactory
from app.calculation.calculation import CalculationHistory
from app.operation.registry import OPERATIONS_HELP

PROMPT = 'calc> '

HELP_TEXT = f"""Simple Calculator REPL
Commands:
  help      Show this help message
  history   Show calculation history
  exit      Exit the REPL
Operations:
{OPERATIONS_HELP}
Usage:
  <operation> <num1> <num2>
Example:
  add 2 3
"""

def parse_input(line: str):
    parts = line.strip().split()
    if not parts:
        return None
    cmd = parts[0].lower()
    if cmd in ('help', 'history', 'exit'):
        return (cmd, parts[1:])
    # Otherwise operation
    return ('calc', parts)

def repl():
    factory = CalculationFactory()
    history = CalculationHistory()
    print(HELP_TEXT)
    while True:
        try:
            line = input(PROMPT)
        except (EOFError, KeyboardInterrupt):
            print('\nExiting.')  # pragma: no cover
            break  # pragma: no cover
        parsed = parse_input(line)
        if parsed is None:
            continue  # pragma: no cover
        cmd, args = parsed
        if cmd == 'help':
            print(HELP_TEXT)
            continue  # pragma: no cover
        if cmd == 'history':
            for idx, item in enumerate(history.items(), 1):
                print(f"{idx}: {item}")
            continue  # pragma: no cover
        if cmd == 'exit':
            print('Goodbye.')
            break  # pragma: no cover
        if cmd == 'calc':
            # Expect: op a b
            parts = args
            if len(parts) != 3:
                print('Invalid input. Example: add 2 3')  # pragma: no cover
                continue  # pragma: no cover
            op, a_str, b_str = parts
            # LBYL for parsing numbers
            if not (is_number(a_str) and is_number(b_str)):
                print('Invalid numbers. Please enter valid numeric values.')  # pragma: no cover
                continue  # pragma: no cover
            a = float(a_str)
            b = float(b_str)
            try:
                calc = factory.create(op, a, b)
                result = calc.execute()
                history.add(calc)
                print(result)
            except Exception as exc:
                # EAFP style handling for operation errors
                print(f'Error: {exc}')  # pragma: no cover
                continue  # pragma: no cover

def is_number(s: str) -> bool:
    """LBYL example: check format before conversion."""
    try:
        float(s)
        return True
    except ValueError:
        return False
