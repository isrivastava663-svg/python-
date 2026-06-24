# ================================
#   Rock Paper Scissors - Python
# ================================

import random

CHOICES = ["Rock", "Paper", "Scissors"]

EMOJIS = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

def get_winner(player, computer):
    if player == computer:
        return "draw"
    wins = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    if wins[player] == computer:
        return "player"
    return "computer"

def display_scoreboard(player_name, p_score, c_score, draws):
    print(f"\n{'=' * 38}")
    print(f"  📊 SCOREBOARD")
    print(f"  {player_name:<18}: {p_score} wins")
    print(f"  {'Computer':<18}: {c_score} wins")
    print(f"  {'Draws':<18}: {draws}")
    print(f"{'=' * 38}")

def main():
    print("=" * 38)
    print("   🎮 ROCK  PAPER  SCISSORS")
    print("=" * 38)
    player_name = input("Enter your name: ").strip() or "Player"
    print(f"\nWelcome, {player_name}! Let's play!\n")

    p_score, c_score, draws = 0, 0, 0
    round_num = 0

    while True:
        round_num += 1
        print(f"\n--- Round {round_num} ---")
        print("Choose:")
        for i, choice in enumerate(CHOICES, 1):
            print(f"  {i}. {EMOJIS[choice]} {choice}")
        print("  4. 🚪 Quit")

        while True:
            pick = input("Your choice (1-4): ").strip()
            if pick in ['1', '2', '3', '4']:
                break
            print("⚠️  Please enter 1, 2, 3, or 4.")

        if pick == '4':
            break

        player_choice   = CHOICES[int(pick) - 1]
        computer_choice = random.choice(CHOICES)

        print(f"\n  You     : {EMOJIS[player_choice]} {player_choice}")
        print(f"  Computer: {EMOJIS[computer_choice]} {computer_choice}")

        result = get_winner(player_choice, computer_choice)

        if result == "draw":
            print("  🤝 It's a Draw!")
            draws += 1
        elif result == "player":
            print(f"  🎉 You Win this round!")
            p_score += 1
        else:
            print(f"  💻 Computer Wins this round!")
            c_score += 1

        display_scoreboard(player_name, p_score, c_score, draws)

    # Final result
    total = p_score + c_score + draws
    print(f"\n{'=' * 38}")
    print(f"   🏁 GAME OVER — Thanks, {player_name}!")
    print(f"   Total Rounds Played: {total}")
    if p_score > c_score:
        print("   🏆 Overall Winner: YOU!")
    elif c_score > p_score:
        print("   🤖 Overall Winner: Computer!")
    else:
        print("   🤝 Overall Result: It's a Tie!")
    print("=" * 38)

if __name__ == "__main__":
    main()
