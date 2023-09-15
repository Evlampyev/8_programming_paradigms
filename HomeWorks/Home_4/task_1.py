# я вычитал, что выборки должны быть обязательно одинаковой длины и формула по моему немножко не правильная
from random import randint
from math import sqrt
from scipy.stats import pearsonr


def pearson_correlation_numerator(mx, my, lstx, lsty):
    sum_numerator = 0
    sum_denominator_1 = 0
    sum_denominator_2 = 0

    for i in range(len(lstx)):
        sum_numerator += (lstx[i] - mx) * (lsty[i] - my)
        sum_denominator_1 += (lstx[i] - mx) * (lstx[i] - mx)
        sum_denominator_2 += (lsty[i] - my) * (lsty[i] - my)

    return sum_numerator, sqrt(sum_denominator_1)*sqrt(sum_denominator_2)


if __name__ == '__main__':
    length = 25
    lst_x = [i for i in range(length)]
    lst_y = [randint(1, 50) for i in range(length)]
    # lst_y = [2 * x + 2 for x in lst_x] # при линнейной зависимости корреляция пирсона положительна и равна 1
    Mx = sum(lst_x) / length
    My = sum(lst_y) / length
    print('Rxy = ', end="")
    numerator, denominator = pearson_correlation_numerator(Mx, My, lst_x, lst_y)

    print(numerator, end=' / ')
    print(denominator, end=' = ')
    print(numerator / denominator)

    corr, _ = pearsonr(lst_x, lst_y)
    print('Pearsons correlation: %.3f' % corr)
