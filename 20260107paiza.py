# 3つの文字列がカンマ区切りで1行で与えられます。
# 3行での出力
# すべてのテストケースにおいて、以下の条件をみたします。

# ・入力される各文字列は1文字以上100文字以下の文字列
# ・入力される各文字列の各文字は英小文字または大文字または数字

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input().split(",")
for i in input_line:
    print(i)

# 1行目でNが与えらます。
# 2行目でN個の文字列がカンマ区切りで与えれます。
# N行での出力
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 <= N <= 10
# ・入力される各文字列は1文字以上100文字以下の文字列
# ・入力される各文字列の各文字は英小文字または大文字または数字

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

N = int(input().rstrip())
for i in input().split(","):

    print(i)

    # coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print("813")

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print(8)
print(13)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print(8)
print(1)
print(3)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for i in range(1, 1001):
    print(i)

    # coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print("1 1")

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print("8 1 3")
# print("{} {} {}".format(8, 1, 3))これもあり

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for i in range(10):
    print(i + 1, end=" ")

print()


# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！

for i in range(10):
    if i != 9:
        print(i + 1, end=" ")
    else :
        print(i + 1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# 1000までの整数を半角スペースを入れながら１行で出力する￥gb
for i in range(1000):
    if i != 999:
        print(i + 1, end=" ")
    else:
        print(i + 1)


# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print("paiza")

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print("paiza" + " " + "learning")

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

S = input()
T = input()

print(S)
print(T)

# S_1
# S_2
# S_3
# ...
# S_10　入力
# S_1 S_2 S_3 ... S_10　出力
# * S_i の長さは 1 以上 10 以下
# * S_i は英小文字列
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
strings = []
for i in range(10):
    strings.append(input())

for i in range(10):
    if i != 9:
        print(strings[i], end=" ")
    else:
        print(strings[i])

# S_1 S_2 S_3 ... S_10　入力
# S_1
# S_2
# S_3
# ...
# S_10　出力
# * S_i の長さは 1 以上 1,000 以下
# * S_i は英小文字列

N = input()
M = N.split()

for i in M:
    print(i)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

if N == 1:
    print(1)
else:
    print(1)
    print(2)


# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

if N >= 1:
    print(1)
if N >= 2:
    print(2)
if N >= 3:
    print(3)
if N >= 4:
    print(4)
if N == 5:
    print(5)

    # coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

N = int(input())

for i in range(N):
    print(i + 1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

N = int(input())

for i in range(N):
    print(i + 1)


# 2 つの数値が半角スペース区切りで与えられます。これらの数値をカンマ区切りで出力してください。
# N M　入力
# N,M　出力
# 1 ≦ N, M ≦ 10
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
S = input().rsplit()
print(",".join(S))

# バーティカルライン区切りで 3 つの文字列を出力
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
S1 = input()
S2 = input()
S3 = input()
print("{}|{}|{}".format(S1, S2, S3)) #formatを使うと{}で分けたとこに割り振れる

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
S = input().split() #入力を分割する
for N in S : #分割した入力を繰り返し出力する
    print(N,end=",") #endを付けると、分割した分に任意の区切りがつく


# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
S = input().rsplit() 
print(",".join(S))