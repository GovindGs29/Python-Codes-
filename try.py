r = 0
b = 0
a = 0
while True:
    try:
        a = int(input('Please provide a number for A: '))
        b = int(input('Please provide a number for B: '))
        r = a+b
    except:
        print("Hey! You are having a error in the input ")
        continue
    else:
        print('Got the numbers')
        print(r)
        break
    finally:
        if r == a+b:
            print('Program completed')
        else:
            print('Whoops! I am gonna ask u again !')