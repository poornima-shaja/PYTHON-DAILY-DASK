user = int(input("Enter the value: "))

def number(user):
    if user > 0:
        return "Postive"
    elif user < 0:
        return "Negative"
    else:
        return "Zero"
result= number(user)
print(result)
