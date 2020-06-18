#My first program

#defining a function for finding the armstrong number

def armstrong_number(number):
    if number < 0:
        print('invalid number')
    elif number == 0:
        print('Armstrong Number')
    # Logic for armstrong number
    sum = 0
    length_of_int = len(str(number))
    # Check if the length of the int is greater than 1 if not terminate
    if length_of_int == 0:
        print('invalid number')
    # assign the number to the temp var and operate on each digit
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** length_of_int
        temp //= 10
    # display the result
    if sum == number:
        print(number, ' is an Armstrong number')
    #else:
        #print(number, 'is not an Armstrong number')

print("**************************************")
print("Hello Everyone! Execution starts here")
print("**************************************")

armstrong_number(153)
armstrong_number(1065)
armstrong_number(1634)
armstrong_number(9474)

print("**************************************")
print("I am done with the validation")
print("**************************************")

print("***************************************************")
print("now let's find all the armstrong numbers until 9999")
print("***************************************************")

for index in range (0,99999999):
    armstrong_number(index)
