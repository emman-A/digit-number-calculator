def decimal_binary(n):
    if n == 0:
        print(0) # print 0 whenever n is zero
        return None
    else:
        bi_to_dec = []
        while n > 0:  # looping for the remainder and thhe floor division of n by 2
            div = n%2
            bi_to_dec.append(div) # storing the remainder in the list
            n = n//2  # assigning a new value to n
    result=''
    for i in bi_to_dec[::-1]:  # reverse the list
        i=str(i)
        result+=i  # add values 
    return result

# n = int(input("Enter decimal value to convert to binary: "))
# print(decimal_binary(n))



def hexadecimal_binary(n):
    n = str(n)

    hex_bi = []
    for i in range(len(str(n))):
        dig = str(n[i])

        if dig == 'A':
            dig = '10'
        elif dig == 'B':
            dig = '11'
        elif dig == 'C':
            dig = '12'
        elif dig == 'D':
            dig = '13'
        elif dig == 'E':
            dig = '14'
        elif dig == 'F':
            dig = '15'
        else:
            dig

        # dig = int(dig)
        hex_bi.append(int(dig))  # convert string values back to integer for maipulation
    hex_bi2 = []
    
    for k in hex_bi[:]:
        hex_bi2.append(decimal_binary(k))  # call decimal to binary function to convert each value to it's equivalent binary digit
    
    concat_str = ''
    for l in hex_bi2[:]:
        if len(l) != 4:
            for i in range(4 - len(l)):
                zero = i*0
                final_len = str(zero) + l
                l = final_len
        
        concat_str = concat_str + l
            


    return concat_str
n = input("Enter number: ")
print(hexadecimal_binary(n))