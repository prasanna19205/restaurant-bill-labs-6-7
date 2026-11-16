
def clean_dish_name(name):
    """Clean a dish name safely."""
    if not isinstance(name, str):
        return ""

    name = name.strip()

    for ch in ['*', '#', '~']:
        name = name.replace(ch, '')

    return name.title()


def parse_item_prices(text):
    """Parse comma-separated prices safely."""
    if not isinstance(text, str) or not text.strip():
        return []

    try:
        prices = [int(price.strip()) for price in text.split(',')]

        if any(price < 0 for price in prices):
            return []

        return prices

    except (ValueError, TypeError):
        return []


def split_amount(text):
    """Calculate each person's share safely."""
    if not isinstance(text, str):
        return 0

    try:
        parts = text.split('/')

        if len(parts) != 2:
            return 0

        total = int(parts[0].strip())
        people = int(parts[1].strip())

        if total < 0 or people <= 0:
            return 0

        return total // people

    except (ValueError, TypeError, ZeroDivisionError):
        return 0


def main():
    print("==== Running clean_dish_name ====")
    value = input("Enter a dish name from the menu (e.g. *paneer tikka*): ")
    print("Dish name:", clean_dish_name(value))

    print("\n==== Running parse_item_prices ====")
    value = input("Enter item prices separated by commas (e.g. 250,180,320): ")
    print("Item prices:", parse_item_prices(value))

    print("\n==== Running split_amount ====")
    value = input("Enter the bill and number of people as TOTAL/PEOPLE (e.g. 1200/4): ")
    print("Each person pays:", split_amount(value))


if __name__ == "__main__":
    main()
