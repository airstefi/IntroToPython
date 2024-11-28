fails_allowed = int(input())

totalQuestions = 0
fails = 0
total = 0.0
lastqName = ""

while True:
    questionName = input()

    if questionName == "Enough":
        avg = total/totalQuestions
        print(f"Average score: {avg:.2f}")
        print(f"Number of problems: {totalQuestions}")
        print(f"Last problem: {lastqName}")
        break

    grade = int(input())

    if grade <= 4:
        fails +=1
        if fails >= fails_allowed:
            print(f"You need a break, {fails} poor grades.")
            break


    total = total +grade
    totalQuestions += 1
    lastqName = questionName

