""" unit tests for parse_command_line_args"""
import pytest
from covid19_graphs.command_line_script import parse_command_line_args


def test_supply_output_dir():
    args = parse_command_line_args(test_override=['output_dir'])
    assert args.out_dir == 'output_dir'


def script_help_message(capsys):
    """ gets the script's -h help message"""
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=['-h'])
    return capsys.readouterr().out


def test_with_empty_args_raises_error():
    """ User passes no arguments
    This is invalid as they have to specify at least one input file/seq
    """
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=[])


def test_with_invalid_option_raises_error():
    """ User passes a string and -invalid_option.
    This must raise SystemExit.
    """
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=['A', '-invalid'])


def test_supply_2_strings_raises_error():
    with pytest.raises(SystemExit):
        parse_command_line_args(test_override=['1', '2'])
