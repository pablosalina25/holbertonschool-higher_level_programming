#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for only_name in dir(hidden_4):
        if not only_name.startswith("__"):
            print(only_name)
