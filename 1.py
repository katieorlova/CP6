try:
    n = int(input('Введите количество элеметов: '))
except ValueError:
    print ('Ошибка')
else:

    array = [0] * n
    
    try:
        for i in range(0, n):
            array[i] = int(input('Введите элемент: '))
    except ValueError:
        print ('Ошибка')
    else:
    
        try:
            delta = int(input('Введите число: '))
        except ValueError:
            print ('Ошибка')
        else:
        
            m = array.count(min(array) + delta)
            print('Количество элементов = ', m)