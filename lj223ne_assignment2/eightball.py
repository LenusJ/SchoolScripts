from random import randint


ans = ["Very doubtful", "As i see it, yes", "Ask again later", "Better not tell you now", "Yes", "No"]

end = 0

while end != 1:
    q = str(input("Ask the magic 8-ball your question: "))
    if q == "stop":
        end = 1
    else:
        x = randint(0, len(ans)-1)
        print(f"The magic 8-ball says: {ans[x]}")
