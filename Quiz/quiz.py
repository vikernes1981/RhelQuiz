import random
import quizQuestions
import time

# Got this code from WikiHow and changed some things

questions = quizQuestions.QAList()

corrCount = 0
random.shuffle(questions)
for qaItem in questions:
  print("=" * 40 + "\n")
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.falseAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  print("=" * 40)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print('-' * 40)
  print("Please enter the number of your answer: \n")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("\n" * 2)
  time.sleep(1)

print("You answered " + str(corrCount) + " of " + str(len(questions)) + " questions correctly.")