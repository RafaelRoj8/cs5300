from src.task1 import hello

def test_hello_prints(capsys):
    # call the function
    hello()
    # capture stdout and verify
    out = capsys.readouterr().out.strip()
    assert out == "Hello, World!"