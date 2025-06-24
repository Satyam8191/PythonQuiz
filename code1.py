print(" Welcome to the Quiz Game!")
print("Answer the following questions:")

score = 0  # To keep track of correct answers

# Question 1
print("\n1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
answer1 = input("Enter your answer (a/b/c): ")

if answer1.lower() == "b":
    print(" Correct!")
    score += 1
else:
    print(" Wrong! The correct answer is b) Delhi")

# Question 2
print("\n2. Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Mars")
print("c) Jupiter")
answer2 = input("Enter your answer (a/b/c): ")

if answer2.lower() == "b":
    print(" Correct!")
    score += 1
else:
    print(" Wrong! The correct answer is b) Mars")

# Question 3
print("\n3. What is the result of 5 + 3?")
print("a) 6")
print("b) 7")
print("c) 8")
answer3 = input("Enter your answer (a/b/c): ")

if answer3.lower() == "c":
    print(" Correct!")
    score += 1
else:
    print(" Wrong! The correct answer is c) 8")

# Final score
print("\n You got", score, "out of 3 questions correct!")

# Feedback
if score == 3:
    print("Excellent! ")
elif score == 2:
    print("Good job! ")
else:
    print("Better luck next time! ")