#!/usr/bin/python3
""" Prime Game """


def Prime_numbers(n):
    """ Function that check the numbers is Prime
    with given n.
    """
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for nums in range(3, int(n**(1/2)) + 1, 2):
            if n % nums == 0:
                return False
        return True


def RoundWinner_game(n, x):
    """ Fucntion that find the round winner """
    list = [i for i in range(1, n + 1)]
    gamers = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = gamers[i % 2]
        index = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    index.append(idx)
            else:
                if Prime_numbers(num):
                    index.append(idx)
                    prime = num
        if prime == -1:
            if currentPlayer == gamers[0]:
                return gamers[1]
            else:
                return gamers[0]
        else:
            for idx, val in enumerate(index):
                del list[val - idx]
    return None


def isWinner(x, nums):
    """ Function that find the winner of game """
    Count_winner = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = RoundWinner_game(nums[i], x)
        if roundWinner is not None:
            Count_winner[roundWinner] += 1

    if Count_winner['Maria'] > Count_winner['Ben']:
        return 'Maria'
    elif Count_winner['Ben'] > Count_winner['Maria']:
        return 'Ben'
    else:
        return None


if __name__ == '__main__':
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
