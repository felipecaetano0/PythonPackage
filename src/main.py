import argparse

import src


def main():
    parser = argparse.ArgumentParser(
        prog='math',
        description='Python evaluator. Perfect for doing math in the bash terminal.',
    )
    parser.add_argument('expression', help='Python expression to be evaluated and printed')
    args = parser.parse_args()
    src.evaluate.evaluate_expression(args.expression)


if __name__ == '__main__':
    main()
