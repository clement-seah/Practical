def main():
    total = 0
    items = int(input("Number of items: "))
    while items <= 0:
        print("Invalid number of items!")
        items = int(input("Number of items: "))
    for i in range(items):
        price = float(input("Price of item: "))
        total += price
    if total > 100:
        total *= 0.9

    print("Total price for {} items is ${:.2f}".format(items, total))


if __name__ == '__main__':
    main()