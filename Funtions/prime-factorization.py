# prime factorization

def prime_factorization(number):
    for i in range(2, number + 1):
        if number % i == 0:
            print(i) # 2 2 5 5
            number = number // i 
prime_factorization(int(input("Enter a number: "))) # 100

# LOGIC:
# 100                        # 50                      # 25                     # 5
# 2, 100 + 1 = (2, 101)      # 2, 50 + 1 = (2, 51)     # 2, 25 + 1 = (2, 26)    # 2, 5 + 1 = (2, 6)
# 100 % 2 == 0               # 50 % 2 == 0             # 25 % 5 == 0            # 5 % 5 == 0
# print 2                    # print 2                 # print 5                # print 5
# 100 // 2 = 50              # 50 // 2 = 25            # 25 // 5 = 5            # 5 // 5 = 1

#----------------------------------------------------------
