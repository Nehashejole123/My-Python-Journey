# def kunal():
#     print("kunal")


# kunal()

# def neha(a,b):
#     print(a + b)

# neha("kunal","neha")

#def function initialization
# def a(a,b = 23):
#     print(f"The sum is {a + b}")

# a(12, )

def palindrome(stri):
    rev=""
    for i in range(len(stri)-1,-1,-1):
        rev = rev + stri[i]
    if stri == rev:
        print("is palindrome")
    else:
        print("not palindrome")

palindrome("madam")



def hello(a, b):
    return a + b

print(hello(3, 5))