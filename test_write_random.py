import write_random
import re


def test_write_numbers(tmp_path):
    file = tmp_path / "my_test.txt"

    write_random.write_numbers(file.as_posix(), 19)

    infile = open(file.as_posix(), 'r')
    lines = infile.readlines()
    assert len(lines) == 19


def test_get_number_when_input_is_invalid():
    input_values = ['0', '0a', 'a', '-1', '13', ]
    write_random.input = lambda _: input_values.pop(0)

    result = write_random.get_number()

    assert result == 13

def test_get_number_when_input_is_valid():
    input_values = ['99']
    write_random.input = lambda _: input_values.pop(0)

    result = write_random.get_number()

    assert result == 99

def test_read_numbers(tmp_path, capsys):
    file = tmp_path / "my_test.txt"
    file.write_text("1\n2\n3\n4\n5\n")

    write_random.read_numbers(file.as_posix())
    out, err = capsys.readouterr()

    count = re.search(r'Count:\s+5', out)
    assert count, "Expected 'Count: 5' in output."

    total = re.search(r'Total:\s+15', out)
    assert total, "Expected 'Total: 15' in output."

    average = re.search(r'Average:\s+3.00', out)
    assert average, "Expected 'Average: 3.00' in output."
    assert err == ''
