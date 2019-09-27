import numpy as np

# 读入文件并计算矩阵乘积

matrixA = []
matrixB = []


def read_data(dir_str):
    temp = []
    with open(dir_str) as file:
        for line in file.readlines():
            temp.append([int(i) for i in line.split(",")])
    return np.array(temp)


matrixA = read_data("./data/matrixA.txt")
matrixB = read_data("./data/matrixB.txt")

result = np.matmul(matrixA, matrixB)
result = np.sort(result)

np.savetxt("./ans_one.txt", result, fmt="%d", newline="\n")
