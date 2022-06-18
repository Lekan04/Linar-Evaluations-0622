#percentage Error
def Answer(Approx, Exact):
    print("This program is for calculating Percentage Error")
    print("Input Approximated value")
    Approx = int(input())
    print("Input Exact value")
    Exact = int(input())
    Num = Approx - Exact
    Deno = Exact
    Ans = Num/Deno*100
    print("Percentage error =", + Ans)
Answer("Approx", "Exact")