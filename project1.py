def __main__():
    """
    A simple budget helper tool.
    This small program lets a person record where they spent money,
    keeps track of their monthly income, and finally prints a neat
    little report showing total expenses and remaining balance.
    Nothing fancy—just something to make day-to-day money handling easier.
    """

    def get_spendings():
        # This function asks the user about their different spendings
        # and collects them one by one inside a list as tuples.
        all_spendings = []
        print("\nEnter each spending you made.")
        print('When you are done, simply type: done')

        while True:
            item = input("\nWhere did you spend money?: ").strip().lower()

            if item == "done":
                # stop asking once the user is finished
                break

            # trying to get a valid amount from the user
            try:
                amt = int(input("How much did you spend there?: "))
                all_spendings.append((item, amt))
            except ValueError:
                print("Please enter a valid number for amount!")
        
        return all_spendings


    def budget_body():
        # Asking the user about their income first
        print("\n========== BUDGET TRACKING SYSTEM ==========")

        while True:
            try:
                monthly_income = int(input("Enter your monthly income (₹): "))
                break
            except ValueError:
                print("Please enter a valid amount!")

        # Collecting all the spending details
        recorded_spendings = get_spendings()

        # Calculating the total money spent
        total_used = sum(amount for place, amount in recorded_spendings)
        remaining = monthly_income - total_used

        # Printing the final report
        print("\n*************** BUDGET REPORT ***************")
        print(f"Monthly Income: ₹{monthly_income}\n")

        print("Spending Category", " " * 10, "Amount")
        print("-" * 45)

        # Displaying each spending nicely
        for place, amount in recorded_spendings:
            print("{:<26}{:>10}".format(place, amount))

        print("-" * 45)
        print("{:<26}{:>10}".format("Total Expenses", total_used))
        print("{:<26}{:>10}".format("Remaining Balance", remaining))
        print("*********************** END ***********************\n")

    # running the main body of the program
    budget_body()


if __name__ == "__main__":
    __main__()


