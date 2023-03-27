from program3 import average_steps_taken as steps
import pytest


def test_open_input_file_when_file_not_found(tmp_path):
    file = tmp_path / "nonexistent_file.txt"
    steps_file = tmp_path / "my_steps.txt"
    steps_file.write_text("10\n")
    input_values = [file.as_posix(), steps_file.as_posix()]
    steps.input = lambda _: input_values.pop(0)

    err_msg = None
    try:
        steps_file = steps.open_input_file()
    except FileNotFoundError as e:
        err_msg = "This function should not raise a FileNotFoundException."
    except IndexError as idx_error:
        err_msg = "This function should prompt the user until they enter the correct file name."

    assert err_msg is None, err_msg
    assert steps_file, "This function should return the file object."


def test_average_steps(tmp_path):
    steps_file = tmp_path / "my_steps.txt"
    steps_file.write_text("10\n20\n30\n40\n50\n")

    average = steps.average_steps(steps_file.open(), 5)

    assert 30.0 == average


def test_average_steps_exits_program_when_value_error(tmp_path):
    steps_file = tmp_path / "my_steps.txt"
    steps_file.write_text("10\n20\n30\n40\n50\n")

    with pytest.raises(SystemExit):
        steps.average_steps(steps_file.open(), 6)
