import argparse
from encryption import str_encryption
from decryption import str_decryption


def get_argument():
    parser = argparse.ArgumentParser(
        prog="cryption",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True,
    )

    encrypt_parser = commands.add_parser(
        "e",
        help="encrypt string",
    )

    encrypt_parser.add_argument(
        "init_str",
        type=str,
    )

    encrypt_parser.set_defaults(func=str_encryption)

    decrypt_parser = commands.add_parser(
        "d",
        help="decrypt string",
    )

    decrypt_parser.add_argument(
        "init_str",
        type=str,
    )

    decrypt_parser.set_defaults(func=str_decryption)

    return parser