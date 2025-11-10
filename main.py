from data.make_data import make_data

def main():
    data = make_data()
    for d in data:
        print(d)


if __name__ == "__main__":
    main()
