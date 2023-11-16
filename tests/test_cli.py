from eli.cli import parser


def test_argparse():
    args = parser.parse_args([])
    assert args.ask == []

    args = parser.parse_args(['capital', 'London'])
    assert args.ask == ['capital', 'London']


def test_set_password_parser():
    pass
