class Week2:

    def calculate_total_sales(self):
        price = 50
        quantity = 10
        total_sales = price * quantity
        print(f"Total Sales: {total_sales}")

    def check_prime(self, num):
        if num <= 1:
            print(f"{num} is not a prime number")
            return
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                return
        print(f"{num} is a prime number")

    def maximum_of_three(self, a, b, c):
        maximum = max(a, b, c)
        print(f"Maximum of {a}, {b}, and {c} is {maximum}")
        return maximum

    def print_filenames(self, filenames):
        print("List of filenames:")
        for file in filenames:
            print(file)


def main():
    obj = Week2()

    obj.calculate_total_sales()
    obj.check_prime(29)
    obj.maximum_of_three(12, 45, 27)
    obj.print_filenames(["file1.txt", "report.pdf", "image.png"])


if __name__ == "__main__":
    main()
