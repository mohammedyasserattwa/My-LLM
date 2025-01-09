import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='This is a demonstration program.')
    parser.add_argument("--line", type=str, help="Please provide an llms")
    return parser.parse_args()

def main():
    args = parse_args()
    print(args.line)

if __name__ == '__main__':
    main()