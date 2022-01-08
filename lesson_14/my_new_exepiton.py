class NewError(Exception):
    def __init__(self, value):
        self.a = value

    def __str__(self):
        return self.a


if __name__ == "__main__":
    try:
        raise NewError("NewError: An unexpected error has occurred.")
    except NewError as err:
        print(err)
