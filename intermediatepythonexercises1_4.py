nums = []
for i in range(5):
    while True:
        try:
            nums.append(int(input(f"Enter integer {i+1}: ")))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

print(f"The sum of the integers is: {sum(nums)}")
