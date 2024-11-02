import random

def simulate_dice_rolls(num_rolls):
    min_sum = 2
    max_sum = 12
    sums = {i: 0 for i in range(min_sum, max_sum + 1)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_dice = dice1 + dice2
        sums[sum_dice] += 1

    return sums

def main():
    num_simulations = 1000
    sum_counts = simulate_dice_rolls(num_simulations)

    monte_carlo_probabilities = {key: count / num_simulations for key, count in sum_counts.items()}
    analytic_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }

    print("Sum | Monte Carlo Probability (%) | Analytical Probability (%)")
    print("----|----------------------------|----------------------------")
    for key in sorted(sum_counts.keys()):
        print(f"{key:>3} | {monte_carlo_probabilities[key]:>26.2f} | {analytic_probabilities[key]:>26.2f}")

if __name__ == "__main__":
    main()
