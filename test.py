if __name__ == '__main__':
    size = 13
    max_num = size * size
    arr = np.zeros((size, size))
    pos = np.array([size, size]) // 2
    step = 1
    num = 1

    for iterations in range(0, size * size):
        for i in range(iterations):
            if num == max_num:
                break
            arr[pos[1], pos[0]] = num
            pos[0] -= step
            num += 1

        for i in range(iterations):
            if num == max_num:
                break
            arr[pos[1], pos[0]] = num
            pos[1] += step
            num += 1

        step *= -1

    print('\n',arr)


