number = int(input('enter your number : '))
sum = 0
if number <= 0 :
    print('your number must be a positive number')
else:
    for i in range(1,number):
        if number % i == 0 :
            sum += i

    if sum == number:
        print('your number is a perfect number')
    else:
        print('your number is not a perfect number')
