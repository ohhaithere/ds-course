import numpy as np

def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

def game_core_v3(number):
    count = 1
    predict = np.random.randint(1,101)
    print(number, predict)
    while number != predict:
        count+=1
        if number > predict:
            if(number - predict) > 10:
                predict += 10
            else:
                 predict += 1
        elif number < predict:
            if(predict - number) > 10:
                predict -= 10
            else:
                predict -= 1
    return(count) # выход из цикла, если угадали

score_game(game_core_v3)
