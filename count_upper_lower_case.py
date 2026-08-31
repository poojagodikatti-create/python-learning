def count_case_letters():
    user_input = input("Enter string:")
    
    upper_count = 0
    lower_count = 0
    
    for char in user_input:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        
    print("Upper case:", upper_count)
    print("Lower  case:", lower_count)
    
count_case_letters()
    