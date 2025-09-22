# tests/test_task1.py

# Import the function we want to test from our source module.
from src.task1 import hello

def test_hello_prints(capsys):
    
    # Verifies that hello() prints the exact text 'Hello, World!'.
    # `capsys` is a pytest *fixture* that captures what is printed to stdout/stderr
    # so the test can make assertions about it.
   

    # 1) Call the function under test; it will do a print().
    hello()

    # 2) Ask pytest to give us what was printed.
    captured = capsys.readouterr()   # captured.out is stdout; captured.err is stderr

    # 3) The print() adds a newline at the end; .strip() removes it.
    out = captured.out.strip()

    # 4) Check that the text matches exactly.
    assert out == "Hello, World!"
