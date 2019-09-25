import sys
from argparse import ArgumentParser, REMAINDER
from terp.classes import info
from terp.classes.app import TerpApp


def main():
    """Create Main Window"""
    parser = ArgumentParser(description=f'terp version {info.VERSION}')
    parser.add_argument('-V', '--version', action='store_true')
    parser.add_argument('remain', nargs=REMAINDER)
    # TODO: Dokimastiko gia toys kaloys
    #     dfgdf dfgdfg dfgdfg
    # FIXME: This is a test

    args = parser.parse_args()

    if args.version:
        print(f'terp version {info.VERSION}')
        sys.exit()

    argv = [sys.argv[0]]
    for arg in args.remain:
        argv.append(arg)

    app = TerpApp(argv)
    # Passing info into run function in order to create settings file
    sys.exit(app.run(info))


if __name__ == '__main__':
    main()
