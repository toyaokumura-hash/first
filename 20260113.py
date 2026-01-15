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

#こっちの方法もある。
# ; N = int(input())
# ; a = [] 空の変数を作って
# ; b = []
# ; for i in range(N):
# ;     a_i, b_i = map(int, input().split()) 2行目以降を整数のリストで受け取る
# ;     a.append(a_i) それを空の変数に合致させる
# ;     b.append(b_i)

# ; for i in range(N):
# ;     print(a[i], b[i]) 合致させたやつをプリントする
#一応こっちが模範解答っぽい。式短くするのもいいけど練習ならいろんな関数使うのがいいのかも
#あとボクのやつやとABが整数で受け取れてないからミスの可能性もある

# ; 1 行目に整数 N が与えられます。
# ; 2 行目以降に、N 組の整数 a_i と b_i が N 行で与えられます。(1 ≦ i ≦ N)
# ; 8 組目の a_i と b_i を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
a = []
b = []

for i in range(N):
    a_i,b_i = map(int,input().split())
    a.append(a_i)
    b.append(b_i)
print(a[7],b[7]) #今回は特定行なのでループはいらない。

# ; 1 行目に整数 N が与えられます。
# ; 2 行目以降に、N 組の文字列 s_i と整数 a_i が N 行で与えられます。(1 ≦ i ≦ N)
# ; N 組の s_i と a_i を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

for i in range(N):
    A,B = input().split()
    print("{} {}".format(A, B))


# ; 1 行目に整数 N が与えられます。
# ; 2 行目以降に、N 組の文字列 s_i と整数 a_i が N 行で与えられます。
# ; 8 組目の s_i と a_i を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
a = []
b = []

for i in range(N):
    a_i,b_i = input().split()
    a.append(a_i)
    b.append(b_i)
print(a[7],b[7])

# ; 3 行 3 列の行列が与えられます。上から i 番目、左から j 番目の整数は a_{i,j} です。
# ; 3 行 3 列の行列をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
arr = []
for i in range(3):
    value = list(map(int,input().split(" ")))
    arr.append(value)

for i in range(3):
    print(*arr[i]) #printに＊をつけるとリストを半角スペース入れて出力出来る


# ; ; 1 行目で整数 N が与えられます。
# ; ; 2 行目以降で N 行 3 列の行列が与えられます。上から i 番目、左から j 番目の整数は a_{i,j} です。
# ; N 行 3 列の行列をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
arr = []
for i in range(N):
    value = list(map(int,input().split(" ")))
    arr.append(value)

for i in range(N):
    print(*arr[i])

# ; ; 1 行目で整数 M が与えられます。
# ; 2 行目以降で 3 行 M 列の行列が与えられます。上から i 番目、左から j 番目の整数は a_{i,j} です。
# ; 3 行 M 列の行列をそのまま出力してください。
M = int(input())
a = []
for i in range(3):
    a_i = list(map(int, input().split()))
    a.append(a_i)

for i in range(3):
    print(*a[i])

# ; 1 行目で整数 N と整数 M が与えられます。
# ; 2 行目以降で N 行 M 列の行列が与えられます。上から i 番目、左から j 番目の整数は a_{i,j} です。
# ; N 行 M 列の行列をそのまま出力してください。

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N, M = map(int, input().split())
a = []
for i in range(N):
    a_i = list(map(int, input().split()))
    a.append(a_i)

for i in range(N):
    print(*a[i])



# ; 1 行目に整数 N が与えられます。
# ; 2 行目から (N + 1) 行目までの先頭に整数 M_i (1 ≦ i ≦ N) が与えられます。
# ; それに続いて M_i 個の整数 a_1, ..., a_{M_i} が与えられます。
# ; 上から i 番目、左から j 番目の整数は a_{i,j} です。
# ; N 行の a_1, ..., a_M をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
M = []
for i in range(N):
    M_i = list(map(int,input().split()))
    M.append(M_i[1:])


for i in range(N):
    print(*M[i])


# ; 自然数 N, M と N 個の自然数からなる数列 A と M 個の自然数からなる数列 B が与えられます。
# ; 1 行目には数列 A の最初の B_1 個の値を出力し、
# ; 2 行目にはその次から B_2 個の値を出力します。
# ; このように、i 行目には数列 A の 1 + B_1 + B_2 + ... + B_{i - 1} 番目の値から
# ; B_i 個の値を出力してください。
# ; 言い換えると、数列 A の値を B_1 個、B_2個、... B_M 個で分割し、
# ; それぞれの数列を改行区切りで出力してください。
values = input().split()
N = int(values[0])
M = int(values[1])

A = [0] * N #Aを定義しよう。AはNの
values = input().split()
for i in range(N):
    A[i] = int(values[i])

B = [0] * M
values = input().split()
for i in range(M):
    B[i] = int(values[i])

head = 0
for i in B:
    for j in range(i):
        if j == i - 1:
            print(A[head])
        else:
            print(A[head],end=" ")

        head += 1

# ; イメージとしては 数列A を M 個に分割するというものです。
# ; 1 行目は数列のここからここまでを出力、2 行目は数列のここからここまでを出力...
# ; ということがわかれば前問と同じように解くことができます。
# ; さて、各行で出力する区間なのですが、始点(begin)がわかれば終点(end)は
# ; end = begin + B[i] - 1 と、容易に求まります。
# ; 注意点として、end = begin + B[i] とすると、
# ; 最後の要素は範囲外なので出力してはいけません
# ; (今回は数学の言葉で「閉区間」として考えます。)。
# ; 次に始点について考えてみます。最初に出力する数列の始点は 0 です
# ; (問題文では 1 - indexed でしたが、解説では 0 -indexed です)。
# ; i番目に出力する数列の始点について考えてみます。
# ; これは、(i - 1 番目に出力する数列の終点) + 1 であることがわかります。
# ; よって、すべての数列の始点と終点がわかりました。

#鬼むずい。なんで何回もValues定義するの？[0] * Nって何？

# ; 文字列 paiza を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
print("paiza")

# ; 文字列 paiza と learning を半角スペース区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print("paiza learning")

# ; 1 行で整数 813 を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

print(813)

# ; 整数 8, 1, 3 をこの順に改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
print(8)
print(1)
print(3)

# ; 2 つの 1 を半角スペース区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
print("1 1")

# ; 1,231 と 5,178 の和を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
print(1231 + 5178)

# ; 整数 A = 437,326、 B = 9,085 とします。以下の二つの演算の結果を半角スペース区切りで出力してください。

# ; 1. A を B で割った商
# ; 2. A を B で割った余り
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
X = 437326 // 9085
Y = 437326 % 9085

print("{} {}".format(X,Y))

# ; 整数 A = 202、B = 134、C = 107 とします。
#((A+B)*C)2を計算した結果を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A = 202
B = 134
C = 107
N = ((A+B)*C)
print(N*N)

# ; 変数 N を 0 で初期化する
# ; N に 3,286 を足した値を N へ代入する
# ; N に 4,736 をかけた値を N へ代入する
# ; N を 12,312 で割った余りを N へ代入する
# ; N を出力する
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = 0
n = n + 3286
n = n * 4736
n = n % 12312
print(n)

# ; 文字列 s が 1 行で与えられるので s をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
print(input_line)

# ; 文字列 s と t が 2 行で与えられるので、s と t の 2 行をそのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
t = input()
print(s)
print(t)

# ; 半角スペースを含まない文字列 s が 1 行で与えられるので、そのまま出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
print(input_line)

# ; 文字列 s_1, s_2 が半角スペースで区切られて 1 行で与えられます。
# ; 各文字列を出力するごとに改行し 2 行で出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s_1,s_2 = input().split(" ")
print(s_1)
print(s_2)

# ; 2 つの文字列 S, T が入力されます。S, T を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
t = input()
print(s)
print(t)

# ; 整数 A, B が与えられます。A と B の差 D と積 P を半角スペース区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A,B = list(map(int,input().split()))

D = A - B
P = A * B
print("{} {}".format(D,P))

# ; 変数 N を 0 で初期化する
# ; N に A を足した値を N へ代入する
# ; N に B をかけた値を N へ代入する
# ; N を C で割ったあまりを N へ代入する
# ; N を出力する
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A,B,C = map(int,input().split())
N = 0
N = N+ A
N = N* B
N = N% C
print(N)

# ; ある電車に a 人が乗っています。
# ; 駅に到着した時に b 人が降りて新たに c 人が乗車する時、
# ; 電車に乗っている乗客人数を求めてください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A,B,C = map(int,input().split())
N = A-B+C
print(N)

# ; 文字列Sが与えられます。
# ; Sがpaizaと一致する場合はYESを、一致しない場合はNOを出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
S = input()

if S == ("paiza"):
    print("YES")
else:
    print("NO")

# ; 整数Nが与えられます。Nが 100 以下の場合はYESを、
# ; そうではない場合はNOを出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
if N <= 100:
    print("YES")
else:
    print("NO")

# ; 整数 A, B, C が与えられます。式 A × B ≦ C が成立している場合はYESを、
# ; そうではない場合はNOを出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A,B,C = map(int,input().split())
if A*B<=C:
    print("YES")
else:
    print("NO")


# ; ある占いでは、箱の中に 1~9 までのいずれかの数字が書かれている玉を取り出し、
# ; その玉に書かれている数字から運勢を占います。玉に書かれている数字が 7 の時は大吉となります。
# ; 占いで取り出した玉に書かれている数字が 1 つ与えられます。大吉かどうかを判定してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
if n == 7:
    print("Yes")
else:
    print("No")

# ; 正の整数 N が与えられます。
# ; 1 ~ N の整数を 1 から順に改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

for i in range(1,N+1):
    print(i)

# ; 1 ~ 100 の整数に対して、3 と 5 の両方で割り切れるなら FizzBuzz を、
# ; 3 でのみ割り切れるなら Fizz 、5 でのみ割り切れるなら Buzz を改行区切りで出力してください。
# ; また、どちらでも割り切れない場合は、その数字を改行区切りで出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
for i in range(1,101):
    if i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

# ; ２つの正の整数 a, b が半角スペース区切りで入力されるので
# ; a と b を足した数を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
a,b = map(int,input().split())
print(a+b)

# ; 5 つの正の整数が入力されるので、最も小さい数字を出力して下さい。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = [int(input()) for _ in range(5)]
print(min(n))

# ; 2 つの文字列 a, b が入力されます。
# ; 文字列が一致していれば "OK" 、異なっていれば "NG" と出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
a = input()
b = input()
if a == b :
    print("OK")
else:
    print("NG")

# ; 整数 N が入力として与えられます。

# ; 1からNまでの整数を1から順に表示してください。

# ; ただし、表示しようとしている数値が、

# ; ・3の倍数かつ5の倍数のときには、"Fizz Buzz"
# ; ・3の倍数のときには、"Fizz"
# ; ・5の倍数のときには、"Buzz"

# ; を数値の代わりに表示してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
for i in range(1,N+1):
    if i % 3 == i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ; パイザ宝くじ券には 100000 以上 199999 以下の 6 桁の番号がついています。毎年1つ当選番号 (100000 以上 199999 以下)が発表され、当たりクジの番号が以下のように決まります。

# ; 1等：当選番号と一致する番号
# ; 前後賞：当選番号の ±1 の番号（当選番号が 100000 または 199999 の場合，前後賞は一つしかありません）
# ; 2等：当選番号と下 4 桁が一致する番号（1等に該当する番号を除く）
# ; 3等：当選番号と下 3 桁が一致する番号（1等および2等に該当する番号を除く）
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
b = int(input())
n = int(input())

for _ in range(1,n+1):
    a = int(input())
    if a == b:
        print("first")
    elif a == b + 1 or a == b -1:
        print("adjacent")
    elif a % 10000 == b % 10000:
        print("second")
    elif a % 1000 == b % 1000:
        print("third")
    else:
        print("blank")

# ; # こいつ苦戦した〜〜〜。
# ; あなたはストライクとボールを判定してコールする審判です。
# ; その場の状況に合わせて適切なコールを出しましょう。

# ; 【コール一覧】
# ; ストライクが 1 〜 2 つたまったとき → "strike!"
# ; ストライクが 3 つたまったとき → "out!"
# ; ボールが 1 〜 3 つたまったとき → "ball!"
# ; ボールが 4 つたまったとき → "fourball!"
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
strikes = 0
balls = 0

for i in range(1,N+1):
    pitch = input().strip().lower()

    if pitch == "strike":
        strikes += 1
        if strikes == 3:
            print("out!")
            break # Exit the loop because the batter is out
        else:
            print("strike!")

    elif pitch == "ball":
        balls += 1
        if balls == 4:
            print("fourball!")
            break # Exit the loop because the batter walks
        else:
            print("ball!")
# geminiに聞いてみた。ストライクとボールを数えるカウンターを作って
# 結果によってカウントアップ、一定回数になったら違う結果を出力するやつを
# ストライクとボール両方で作った。っぽい
# ボクが書いたやつはカウンターとかじゃなくてif構文にしてたから、
# アウトとかフォアボールを出すのがうまくいかんかった
#