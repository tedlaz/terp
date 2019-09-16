import sys
from argparse import ArgumentParser, REMAINDER

try:
    from classes import info
    print('Loaded normally parameters from current directory: %s' % info.PATH)
except ImportError:
    print('Error importing trying differently')
    import terp
    sys.path.append(terp.TERP_PATH)
    from classes import info
    print('Loaded parameters from current directory: %s' % info.PATH)


from classes.app import TerpApp


def main():
    """Create Main Window"""
    parser = ArgumentParser(description=f'terp version {info.VERSION}')
    parser.add_argument('-V', '--version', action='store_true')
    parser.add_argument('remain', nargs=REMAINDER)

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
