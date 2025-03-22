def score(num):
    total = 0
    for i in range(num):
        score = int(input("Enter score:"))
        total += score
    average = total/num
    print(average)

score(5)