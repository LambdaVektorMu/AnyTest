# coding: utf-8

# root(P)を計算する

P_number = 2  # 平方根を求める値
initial_value = P_number  # 初期値
epsilon = 1.0E-7  # Pと求めた平方根の2乗の差分の終了値

print("計算開始")

value1 = initial_value  # 計算ターンの初期値を入れる
value2 = P_number / value1  # 計算ターンの初期値から計算した値を入れる
avarage_value = (value1 + value2) / 2.0  # 上記の平均値を取る

for i in range(10**5):  # 最大計算回数は固定
    # 判定処理
    diff_value = abs(P_number - avarage_value**2)  # 計算値と真の値の差分を取る
    print(i, avarage_value, diff_value)  # カウント、計算値、差分
    if diff_value < epsilon:
        break

    # 計算処理
    value1 = avarage_value
    value2 = P_number / value1
    avarage_value = (value1 + value2) / 2.0

print("計算終了")
