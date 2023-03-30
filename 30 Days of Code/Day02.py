def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = meal_cost + (meal_cost * (tip_percent / 100)) + (meal_cost * (tax_percent / 100))

    meal_cost = round(meal_cost)
    print(meal_cost)


if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)