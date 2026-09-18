from decryption import str_decryption 
from encryption import str_encryption
from parser import get_argument


def main():
    parser = get_argument()
    args = parser.parse_args()

    if len(args.init_str) <= 1:
        parser.error("string must contain at least 2 characters")

    args.func(args.init_str)




if __name__ == "__main__":
    main()
    


       




