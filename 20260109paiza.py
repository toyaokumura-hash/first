#　Cランクアップ問題
# ・1 行目にはそれぞれ整数 N, X, Y がこの順で半角スペース区切りで与えられます。
# これらは応募者が N 人であることを示し、X の倍数番目の応募者がプレゼント A の当選者となり、
# Y の倍数番目の応募者がプレゼント B の当選者となることを示します。
# ・入力は 1 行となり、末尾に改行が 1 つ入ります。

input_line = input().split()
N = int(input_line[0])
A = int(input_line[1])
B = int(input_line[2])

for i in range(1,N+1):
    if i % B == 0 and i % A == 0:
        print("AB")
    elif i % A ==0:
        print("A")
    elif i % B == 0:
        print("B")
    else:
        print("N")
#　iの使いところ間違えてるのに気付かずに他のところいじって時間かかったから
#　解答時間は中央値より大きく伸びた


# 入力例 1 では "Paiza" という文字列を送ります。
# この文字を枠で囲み装飾すると、以下のようになります。

# +++++++
# +Paiza+
# +++++++
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
M = int(len(input_line))
print("+" *( M + 2))
print(f'+{input_line}+')
print("+" * (M + 2))

# 文字列 s が 1 行で与えられるので s をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
print(input_line)

# 文字列 s と t が 2 行で与えられるので、s と t の 2 行をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
input_line2 = input()
print(input_line)
print(input_line2)

# 文字列 s, t, u が 3 行で与えられるので、s, t, u の 3 行をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
input_line1 = input()
input_line2= input()
print(input_line)
print(input_line1)
print(input_line2)

# s_1, s_2, s_3, ... s_9, s_10 の 10 個の文字列が与えられます。
# 文字列を与えられた順番通りに出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for _ in range(10):
    line = input() #rangeを前につけると複数行の入力も受け取れる
    print(line)

# s_1, s_2, s_3, ... s_999, s_1000 の 1,000 個の文字列が与えられます。
# 文字列を与えられた順番通りに出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for _ in range(1000):
    line = input() #rangeを前につけると複数行の入力も受け取れる
    print(line) #1000行あっても一緒

# 文字列Hello paizaを、半角スペースで分割して出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = "Hello paiza"
a, b = s.split(" ")
print(a)
print(b)

# 文字列He likes paizaを、半角スペースで分割して出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = "He likes paiza"
a, b,c = s.split(" ")
print(a)
print(b)
print(c)

# 文字列one two three four fiveを、半角スペースで分割して出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = "one two three four five"
for i in s.split(" "): #for文にsplitも入れれるよ
    print(i)

# 半角スペースを含まない文字列 s が 1 行で与えられるので、そのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
print(input_line)

# 半角スペース区切りの 2 つの入力
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
inputline = input()
a,b = inputline.split()
print(a)
print(b)
# s, t = input().split(" ")
# print(s)
# print(t)

# 文字列 s_1, s_2, s_3 が半角スペースで区切られて 1 行で与えられます。
# 各文字列を出力するごとに改行し 3 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s, t, u = input().split(" ")
print(s)
print(t)
print(u)

# 文字列 s_1, s_2, ... s_9, s_10 が半角スペースで区切られて 1 行で与えられます。
# 各文字列を出力するごとに改行し 10 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

line = input()
for i in line.split(" "):
    print(i)
# s = input().split(" ")
# for i in range(10):
#     print(s[i])
# これでも出せるよ

# 文字列 s_1, s_2, ... s_999, s_1000 が半角スペースで区切られて 1 行で与えられます。
# 各文字列を出力するごとに改行し 1,000 行で出力してください。
line = input()
for i in line.split(" "):
    print(i)
#上のやつと同じやった

# 整数 a が 1 行で与えられるので a を 1 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
print(input_line)

# 整数 a, b が 2 行で与えられるので a, b を 2 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
input_line2 = input()
print(input_line)
print(input_line2)

# 整数 a_1, a_2, a_3, a_4, a_5 が 5 行で与えられるので
# a_1, a_2, a_3, a_4, a_5 を 5 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for _ in range(5):
    line = input() #rangeを前につけると複数行の入力も受け取れる
    print(line)

# 解答例
# a = []
# for i in range(5):
#     a_i = int(input())
#     a.append(a_i)

# for i in range(5):
#     print(a[i])
# 空のリスト a を用意し、for 文を用いて、
# 入力を受け取って整数に変換しリスト a に追加することを 5 回繰り返します。
# 最後に、もう一度 for 文を用いて、リスト a の各要素を順番に出力していけばよいです。

# 整数 a_1, a_2, ... , a_99, a_100 が 100 行で与えられるので
# a_1, a_2, ... , a_99, a_100 を 100 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
a = []
for i in range(100):
    ai = int(input())
    a.append(ai)

for i in range(100):
    print(a[i])

# 整数 a_1, a_2, ... , a_999, a_1000 が 1,000 行で与えられるので
# a_1, a_2, ... , a_999, a_1000 を 1,000 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for _ in range(1000):
    line = input() #rangeを前につけると複数行の入力も受け取れる
    print(line)

# 整数 a が与えられるので a を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
print(input_line)

# 整数 a, b が半角スペース区切りで与えられるので、改行区切りにして 2 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
a,b = input_line.split()
print(a)
print(b)

# 整数 a_1, a_2, a_3, a_4, a_5
# が半角スペース区切りで与えられるので、改行区切りにして 5 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
for i in input_line.split():
    print(i)

# a = map(int, input().split(" "))　map関数で出したやつはintじゃなくてもforで繰り返せる
# for a_i in a:
#     print(a_i)

# 整数 a_1, a_2, ... , a_9, a_10
# が半角スペース区切りで与えられるので、改行区切りにして 10 行で出力してください。
input_line = input()
for i in input_line.split():
    print(i)
# これと一緒

# 整数 a_1, a_2, ... , a_999, a_1000
# が半角スペース区切りで与えられるので、改行区切りにして 1000 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
for i in input_line.split():
    print(i)

# 1 行目で整数 N が与えられます。
# 2 行目以降で、N 個の整数 a_1, ... , a_N が N 行で与えられます。
# a_1, ... , a_N を改行区切りで出力してください。
# coding: utf-8
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

N = int(input())
a = [] #空のaを作る
for i in range(N): #範囲を決めてから
    a_i = int(input()) #a_iに整数を代入する
    a.append(a_i) #a_iをaに合致させる
for i in range(N):
    print(a[i])

# 1 行目で整数 N が与えられます。
# 2 行目で、N 個の整数 a_1, ... , a_N が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N_and_a = list(map(int, input().split(" "))) #入力をforで使えるように整数で分割して受け取る
N = N_and_a[0]
a = N_and_a[1:]
for i in range(N):
    print(a[i])

# 1 行目で整数 N が与えられます。
# 2 行目で、N 個の整数 a_1, ... , a_N が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = list(map(int, input().split(" ")))

for i in range(N):
    print(M[i])


# 1 行目で、整数 N と、続けて N 個の整数 a_1, ... , a_N が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N_and_a = list(map(int, input().split(" "))) #
N = N_and_a[0]
a = N_and_a[1:]
for i in range(N):
    print(a[i])


# 1 行目に整数 N が与えられます。
# 2 行目以降に、N 個の文字列 s_1, ... , s_N が N 行で与えられます。
# s_1, ... , s_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = []

for i in range(N):
    M_i = input()
    M.append(M_i)
    print(M[i])
# これまでのやつを組み合わせたやつ。先に空のMを作って回数決めてから改めて数値入れるやつ

# 1 行目に整数 N が与えられます。
# 2 行目に、N 個の文字列 s_1, ... , s_N が半角スペース区切りで与えられます。
# s_1, ... , s_N を改行区切りで出力してください
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = input().split(" ")

for i in range(N):
    print(M[i])

# 1 行目で、整数 N と、続けて N 個の文字列 s_1, ... , s_N が半角スペース区切りで与えられます。
# s_1, ... , s_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
inputline = input().split()
N = int(inputline[0])

for i in range(N):
    M = inputline[1:]
    print(M[i])

# 1 行目に整数 N が与えられます。
# 2 行目に、N 個の文字列 s_1, ... , s_N が半角スペース区切りで与えられます。
# s_1, ... , s_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = input().split(" ")

for i in range(N):
    print(M[i])

# 1 行目に、整数 N と、続けて N 個の文字列 s_1, ... , s_N が半角スペース区切りで与えられます。
# s_1, ... , s_N を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
inputline = input().split()
N = int(inputline[0])

for i in range(N):
    M = inputline[1:]
    print(M[i])

# 1 行目に整数 N が与えられます。
# 2 行目以降に、N 個の実数 a_1, ... , a_N が N 行で与えられます。
# a_1, ... , a_N を改行区切りでそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = []

for i in range(N):
    M_i = input()
    M.append(M_i)
    print("{: >3}".format(M[i]))
# 小数点の問題のやつと組み合わせたらいけた。
# てか大筋はこれまでの問題から引っ張って一部修正的な感じでやってるけどやっぱ書いた方がいいかな

# 1 行目に整数 N が与えられます。
# 2 行目に、N 個の実数 a_1, ... , a_N が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りでそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = input().split(" ")

for i in range(N):
    print("{: >3}".format(M[i]))

# N = int(input())
# a = list(map(float, input().split(" ")))
# for i in range(N):
#     print(a[i]) 解答例はこっち


# 1 行目で、整数 N と、続けて N 個の実数 a_1, ... , a_N
# が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りでそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N_and_a = input().split(" ")
N = int(N_and_a[0])
a = list(map(float, N_and_a[1:]))
for i in range(N):
    print(a[i])

# 1 行目に整数 N が与えられます。
# 2 行目に、N 個の実数 a_1, ... , a_N が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りでそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = input().split(" ")

for i in range(N):
    print(M[i])

# 1 行目で、整数 N と、続けて N 個の実数 a_1, ... , a_N が半角スペース区切りで与えられます。
# a_1, ... , a_N を改行区切りでそのまま出力してください。
# coding: utf-8
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
NM = input().split()
N = int(NM[0])
M = NM[1:]

for i in range(N):
    print(M[i])

# 1 つの整数の組の入力
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A = input()
print(A)


# 1 行目に整数 N が与えられます。
# 2 行目以降に、N 組の整数 a_i と b_i が N 行で与えられます。(1 ≦ i ≦ N)
# N 組の a_i と b_i を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

for i in range(N):
    A,B = input().split()
    print("{} {}".format(A, B))


