input_number = 0
number_to_guess = 5

while input_number != number_to_guess:

    input_number = int(input("Введите число:"))
    if input_number == number_to_guess:


        print("поздравляем. вы угадали!")
    else:
        print("попробуйте ещу раз")
print ("game over")
