from application.main import App


def main():
    try:
        application = App()
        application.start()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
