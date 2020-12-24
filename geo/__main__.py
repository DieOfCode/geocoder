from geo.CLI import CLI


def main():
    user_cli = CLI()
    for geo_answer in user_cli.get_answer():
        print(geo_answer)


if __name__ == '__main__':
    main()
