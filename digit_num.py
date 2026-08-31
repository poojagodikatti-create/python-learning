ones = ["zero","one","two","three",
        "four","five","six","seven",
        "eight","nine","ten","eleven",
        "twelve","thirteen","fourteen",
        "fifteen","sixteen","seventh",
        "eighteen","nineteen"]

tens = ["","","twenty","thirty","forty","fifty",
        "sixty","seventy","eighty","ninety"]
        
n = int(input("Enter number between(0-99):"))

if 0<=n<2:
    print("In word:", ones[n])
elif 20<=n<=99:
    ten_digit=n//10
    one_digit=n%10
    if one_digit == 0:
        print("In word:", tens[ten_digit])
    else:
        print("In word:", tens[ten_digits]+ "-" +ones[one_digit])
else:
    print("Number out of range.Plz ente between (0-99):")