# Week 2 Practice Activity 1
user_input = input("Enter a string to reverse: ")

# Reverse using slicing [start:stop:step] - step -1 goes backwards
reversed_string = user_input[::-1]

print(f"Original: {user_input}")
print(f"Reversed: {reversed_string}")

# How this works
# ' input() ' captures user string
# ' [::-1] ' slicing: start=end (implied), stop=0 (implied), step=-1 (backwards)
