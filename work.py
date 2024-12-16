
print("""Welcome to your number systen calculator!
    What do you want to convert?
    Enter 1 to convert from Binary to Decimal
    Enter 2 to convert from Decimal to Binary
    Enter 3 to convert from Binary to Hexadecimal
    Enter 4 to convert from Hexadecimal to Decimal
    Enter 5 to convert from Decimal to Hexadecimal
    Enter 6 to convert from Hexadecimal to Binary
 """)






#BINARY TO DECIMAL
def binary_decimal(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        val = n[i]  # Integer number to string 

        if val != '0' and val != '1':
            print("Binary digits must be 0 or 1")  # Value must be 0 or 1
            return None
            
        sum += int(val) * 2**(len(n) - (i+1))  # multiply each value by 2 power the index from the right
    return sum   # Return the sum of the values to get the decimal equivalent






#DECIMAL TO BINARY
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
        result += i  # add values 
    return result






# BINARY TO HEXADECIMAL
def binary_hexadecimal(n):
    n = str(n)  # intger value converted to string
    for i in range(len(n)):  
        sort_list = []
            
        if len(n)%4 != 0: 
            """check if the length of the number can be grouped into 4 bits
        and also number is 0 or 1""" 
            for i in range(4 - len(n)%4): 
                num = i*0
                new_len = str(num) + n  # if lenth not divisible by 4, add leading 0's
                n = new_len
                
        
        for j in range(0, len(n), 4):  # group numbers into 4's
            sort_list.append(n[j:j+4])  # append the 4 bits into a sort_list list as an index each
                    
    result=[]    
    for k in range(len(sort_list)):
        result.append(binary_decimal(sort_list[k]))  # call the binary_decimal function on the indices in the sort_list

    hexa_val = ''
    for i in result[:]:
        hexa = str(i)
        
        if hexa == '10':  # converting values between 9 and 16 to their equivalent alphabets, ie. A to F 
            hexa = 'A'
        elif hexa == '11':
            hexa = 'B'
        elif hexa == '12':
            hexa = 'C'
        elif hexa == '13':
            hexa = 'D'
        elif hexa == '14':
            hexa = 'E'
        elif hexa == '15':
            hexa = 'F' 
        else:
            hexa 
        
        hexa_val += hexa  # concatenating string values

    return hexa_val
        





# HEXADECIMAL TO DECIMAL
def hexa_decimal(n):
    hexa_deca = ''
    li = []
    for i in range(len(n)):
        hd = n[i]  
        if hd == 'A':  # convert numbers from alfabets back to their original number values
            hd = '10'
        elif hd == 'B':
            hd = '11'
        elif hd == 'C':
            hd = '12'
        elif hd == 'D':
            hd = '13'
        elif hd == 'E':
            hd = '14'
        elif hd == 'F':
            hd = '15'
        else:
            hd

        li.append(hd)  #append each value of the user input into the empty list

    sum = 0 
    for k in range(len(li)):
        val = int(li[k])  #convert each value of the index of the list to integer
        sum += val * 16**(len(n) - (k+1))  # computing for the decimal equivalent
    return sum






# DECIMAL TO HEXADECIMAL
def decimal_hexadecimal(n):
    if n == 0:
        print(0)  # zeros will always result in 0
        return None
    
    else:
        dec_hex = []
        while n>0:
            mod = n % 16  # calculating for the remainder/modulo of base 16
            dec_hex.insert(0, mod)
            n = n//16

        hex_store = ''
        for i in dec_hex[:]: 
            i = str(i)  # finding values in the string representation
            """Getting the equivalent alphabetical values of numbers between 9 and 16"""
            if i == '10':    
                i = 'A'
            elif i == '11':
                i = 'B'
            elif i == '12':
                i = 'C'
            elif i == '13':
                i = 'D'
            elif i == '14':
                i = 'E'
            elif i == '15':
                i = 'F'
            else:
                i  #formatting the remaining values into string for concatenation
            hex_store = hex_store + i
    return hex_store





# HEXADECIMAL TO BINARY
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
        hex_bi.append(int(dig))  # convert string values back to integer for maipulation
    hex_bi2 = []
    
    for k in hex_bi[:]:
        hex_bi2.append(decimal_binary(k))  # call decimal to binary function to convert each value to it's equivalent binary digit
    
    concat_str = ''
    for l in hex_bi2[:]:
        if len(l) != 4:
            for i in range(4 - len(l)):  # Inserting leading zeros when the length is less than 4
                zero = i*0
                final_len = str(zero) + l  
                l = final_len
        
        concat_str = concat_str + l  # concatenating the each index to produce the final result
            
    return concat_str



choice = int(input("Enter a number: "))

# User choice to direct user to the desired computation


if choice == 1:    
    n =  int(input("Enter binary digits(0's or 1's) to convert to decimal: "))
    print(binary_decimal(n))
    
elif choice == 2:    
    n = int(input("Enter decimal value to convert to binary: "))
    print(decimal_binary(n))

elif choice == 3:    
    n = int(input("Enter binary digits(0's and 1's) to convert to hexadeximal: "))
    print(binary_hexadecimal(n))

elif choice == 4:    
    n = input("Enter hexadecimal equiv. to convert to decimal: ")
    print(hexa_decimal(n))    

elif choice == 5:   
    n = int(input("Enter decimal value to covnvert to Hexadecimal: "))
    print(decimal_hexadecimal(n))

elif choice == 6:   
    n = input("Enter hexadecimal value to convert to binary: ")
    print(hexadecimal_binary(n))

else:
    print("Invalid choice")




 







            
            





