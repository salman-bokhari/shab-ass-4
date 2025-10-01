from app.calculation.factory import CalculationFactory
from app.calculation.calculation import CalculationHistory
from app.operation.registry import OPERATIONS_HELP

PROMPT = 'calc> '

HELP_TEXT = f"""
Calculator CLI
Commands:
  help      Show this help message
  history   Show calculation history
  exit      Exit the REPL
Operations:
{OPERATIONS_HELP}
Usage: <operation> <num1> <num2>
Example: add 2 3
"""

def parse_input(line: str):
    parts = line.strip().split()
    if not parts:
        return None
    cmd = parts[0].lower()
    if cmd in ('help', 'history', 'exit'):
        return (cmd, parts[1:])
    return ('calc', parts)

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def repl():
    factory = CalculationFactory()
    history = CalculationHistory()
    print(HELP_TEXT)
    while True:
        try:
            line = input(PROMPT)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        parsed = parse_input(line)
        if parsed is None:
            continue
        cmd, args = parsed
        if cmd == 'help':
            print(HELP_TEXT)
            continue
        if cmd == 'history':
            for idx, item in enumerate(history.items(), 1):
                print(f"{idx}: {item}")
            continue
        if cmd == 'exit':
            print("Goodbye.")
            break
        if cmd == 'calc':
            if len(args) != 3:
                print("Invalid input. Example: add 2 3")
                continue
            op, a_str, b_str = args
            if not (is_number(a_str) and is_number(b_str)):
                print("Invalid numbers. Please enter valid numeric values.")
                continue
            a = float(a_str)
            b = float(b_str)
            try:
                calc = factory.create(op, a, b)
                result = calc.execute()
                history.add(calc)
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Cannot divide by zero")
            except Exception as exc:
                print(f"Error: {exc}")
