


def binary_decimal(n):
    sum = 0
    for i in range(len(n)):
        val = int(n[i])

        if val != 0 and val != 1:
            print("Binary value must be 0 or 1")
            return None
            
        sum += val * 2**(len(n) - (i+1))
    return sum
n =  int(input("Enter binary value(ie. 0's and 1's) to convert: "))
print(binary_decimal(str(n)))


#Decimal to Binary
def decimal_binary(n):
    if n == 0:
        print(0)
        return None
    else:
        bi_to_dec = []
        while n > 0:
            div = n%2
            bi_to_dec.append(div)
            n = n//2
    result=''
    for i in bi_to_dec[::-1]:
        i=str(i)
        result+=i
    return result

n = int(input("Enter decimal value to convert to binary: "))
print(decimal_binary(n))


# #Binary to Hexadecimal
# #Get Input: Binary string is "1011101".
# Determine Length: The length is 7 bits.
# Calculate Padding: 
# 7mod4=3 (needs 1 more bit to complete a group).
# Add Leading Zeros: New string becomes "01011101".
# Initialize List: Prepare an empty list for groups.
# Loop Through String:
# Extract "0101" (first 4 bits).
# Extract "1101" (next 4 bits).
# Store Groups: Add "0101" and "1101" to the list
def binary_hexadecimal(n):
    for i in range(len(n)):
        val = int(n[i])
        sort_list = []
        number = []


        if val != 0 and val != 1:
            print("Invalid input of binary digit")
            return None
        
        else:
            if len(n)%4 != 0:
                for i in range(4 - len(n)%4):
                    val = i*0
                    new_len = str(val) + n
                    n = new_len
                    new_len = n
                return n
            
            for j in range(0, len(n), 4):
                sort_list.append(n[j:j+4])
                return sort_list
            
            for k in range(len(sort_list)):
                return binary_decimal(k)
            # return number.append(binary_decimal(k))

    return         


                



