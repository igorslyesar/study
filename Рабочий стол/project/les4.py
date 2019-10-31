while True:
    x_from, x_to = 1, 1000
    x = input("Vvedit znachenia vid 1 do 1000")
    x = int(x)

    if x_from <= x <= x_to:
        break
    else:
        print("Sprobuite sche raz!")

while True:
    y = input("Znachennia 2 =")

    if int(y) - 10 == x:
        print('Hureyyyyy!!! You got me!!!!')
        break
    else:
        print('Povtorit')
