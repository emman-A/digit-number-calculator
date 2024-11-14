
def binary_decimal(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        val = n[i]  # Integer number to string 

        if val != '0' and val != '1':
            print("Binary value must be 0 or 1")  # Value must be 0 or 1
            return None
            
        sum += int(val) * 2**(len(n) - (i+1))  # multiply each value by 2 power the index from the right
    return sum   # Return the sum of the values to get the decimal equivalent
n =  int(input("enter binary value to convert: "))
print(binary_decimal(n))



def binary_hexadecimal(n):
    n = str(n)  # intger value converted to string
    for i in range(len(n)):  
        val = n[i]  # find string index of n
        sort_list = []
        if val != '0' and val != '1':  # value must be 0 or 1
            print("Invalid input of binary digit")
            return None
            
        
        if len(n)%4 != 0 and val == '0' and val == ' 1':
            """check if the length of the number is can be grouped into 4 bits
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
    # return result

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
         
n = int(input("Enter binary digits to convert to hexadeximal: "))
print(binary_hexadecimal(n))

