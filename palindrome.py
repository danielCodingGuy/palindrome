def Palindrome(x):
    x = x.lower().replace(" ", "")
    n = len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
    return True; 
print("Program that checks if the selected word is palindrome")
print("Write a word")
s1 = input()
print("Selected word " + ("is " if(Palindrome(s1)) else "is not ") + "palindrome")
