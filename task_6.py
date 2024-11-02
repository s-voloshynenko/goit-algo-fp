def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append({ item: details["cost"] })
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    item_costs = [items[name]["cost"] for name in item_names]
    item_calories = [items[name]["calories"] for name in item_names]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(1, budget + 1):
            if item_costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - item_costs[i - 1]] + item_calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append({ item_names[i - 1]: item_costs[i - 1] })
            b -= item_costs[i - 1]

    return selected_items, total_calories

def main():
    user_input = input("Enter budget (default is 100): ")

    if not user_input:
        budget = 100
    else:
        budget = int(user_input)

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    selected_items_dynamic, total_calories_dynamic = dynamic_programming(items, budget)

    print("Greedy:")
    print(f"Items: {selected_items_greedy}")
    print(f"Calories total: {total_calories_greedy}")

    print("\nDynamic:")
    print(f"Items: {selected_items_dynamic}")
    print(f"Calories total: {total_calories_dynamic}")

if __name__ == "__main__":
    main()
