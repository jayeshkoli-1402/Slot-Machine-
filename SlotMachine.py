import numpy as np

print("Welcome to SlotMachine Game\n\n".center(100))
money = 100

#take choice
choice = int(input("\nEnter your choice: 1: Play, 2: Rules, 3: Exit → "))

#loop for running program continuously until user chooses exit
while choice != 3:  
    if choice == 1:
        if money <= 0:
            print("💀 You have no money left! Game Over.")
            break

        print(f"\n💰 Your balance: {money}")
        bet = int(input("\n\nEnter your bet: "))
        if bet > money or bet <= 0:
            print("❌ Invalid bet!")
            choice = 1
            continue

        arr = np.array([
            ["🍒", "🍒", "🍒"],
            ["💎", "💎", "💎"],
            ["7️⃣", "7️⃣", "7️⃣"]
        ])
        #logic to shuffle only columns
        for col in range(arr.shape[1]):
            np.random.shuffle(arr[:, col])

        print("\n🎰 Slot Machine 🎰")
        for row in arr:
            print("  ".join(row))

        middle_row = arr[1]
        unique_symbols = np.unique(middle_row)

        #winning calculations
        winnings = 0
        if len(unique_symbols) == 1:
            winnings = bet * 3  
        elif len(unique_symbols) == 2:
            winnings = bet * 2  

        money = money - bet + winnings

        if winnings > 0:
            print(f"\n🎉 You won {winnings}!")
            print(f"\n💰 Your balance: {money}")
            
        else:
            print("\n😢 You lost.")
            print(f"\n💰 Your balance: {money}")

    elif choice == 2:
        print("\n\n🎰 Slot Machine — Rules\n\n"
              "1️⃣ Starting the Game\n"
              "You start with a certain amount of money (balance).\n"
              "You choose how much to bet before each spin.\n\n"
              "2️⃣ How to Play\n"
              "1. Place your bet.\n"
              "2. Press Spin (or type 1 to play in your version).\n"
              "3. The slot machine will spin and randomly stop on 3 rows × 3 columns of symbols.\n"
              "4. Only the middle row counts for winning.\n\n"
              "3️⃣ Winning Rules (Middle Row Only)\n"
              "Three of the same symbol → 🎉 Big Win (3× your bet).\n"
              "Two of the same symbol → 😊 Small Win (2× your bet).\n"
              "No matching symbols → ❌ You lose your bet.\n\n"
              "4️⃣ Symbols & Payouts (Optional for you to add)\n"
              "🍒 → Common symbol (appears more often)\n"
              "💎 → Rare symbol (bigger payout)\n"
              "7️⃣ → Jackpot symbol (highest payout)\n\n"
              "5️⃣ Ending the Game\n"
              "Keep spinning until:\n"
              "You choose to stop.\n"
              "Or your balance runs out.")
        choice = 1  # after showing rules, go back to play

    else:
        print("❌ Invalid choice! Please select 1, 2, or 3.")

    choice = int(input("\nEnter your choice: 1: Play, 2: Rules, 3: Exit → "))

print("Program stopped successfully")