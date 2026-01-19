# N 個の要素からなる数列 A が与えられます。数列 A に対し、次の 3 つの操作を行うプログラムを作成してください。

# ・ push_back x : A の末尾に x を追加する
# ・ pop_back : A の末尾を削除する
# ・ print : A を半角スペース区切りで1行に出力する

# 例えば、入力例 1 において、数列 A は最初「1 2 3」です。最初の操作は「push_back 10」なので、
# 末尾に 10 を追加して「1 2 3 10」となります。 2 つ目の操作は「push_back 12」なので、
# 「1 2 3 10 12」となります。 3 つ目の操作は「print」なので「1 2 3 10 12」を出力します。
# 4 つ目の操作は「pop_back」なので末尾の「12」を削除して、「1 2 3 10」となります。
# 最後の操作は「print」なので「1 2 3 10」を出力します。

# NQ = input().split()
# N = int(NQ[0])
# Q = int(NQ[1])
# A = list(map(int,input().split()))
# q = [input() for _ in range(Q)]

# for i in range(Q):


N, Q = map(int, input().split())
A = [int(x) for x in input().split()]

for _ in range(Q):
    query = [int(x) for x in input().split()]

    cmd = query[0]
    if cmd == 0:
        # push_back
        A.append(query[1])
    elif cmd == 1:
        # pop_back
        A.pop()
    else:
        # print
        print(" ".join(map(str, A)))

# 配列を用意して、これに追加、削除、出力ができるようにします。普通の配列を用いてもよいのですが、
# 動的配列 (C++ における vector など) を用いると、バグを生みにくい実装が可能です。

# 縦 H マス、横 W マスの H × W マスからなる迷路 S があります。
# 上から i 行目、左から j 列目のマス は S_ij とあらわされ、 S_ij が
# 「#」のとき壁であり、「.」のとき道です。整数 r、c が与えられるので、S_rc が壁かどうか判定してください。


H,W,r,c = list(input().split())
S = [input() for _ in range(H)]


# H, W, r, c = map(int, input().split())
# maze = [input() for _ in range(H)]

# if maze[r-1][c-1] == "#":
#     print("Yes")
# else:
#     print("No")

# 文字が H 行 W 列 で与えられるので 2 次元配列などを用いれば正解できます。
# しかし、文字の配列は文字列とほぼ同義なので、配列の代わりに文字列を用いることで簡潔に実装することができます。



# N 個の文字列 S_1, ... , S_N と、Q 個の文字列 T_1, ... , T_Q が与えられます。各 T_i について、以下の処理を行ってください。

# ・ S_j == T_i を満たす最小の j を出力する。ただし、そのような j が存在しない場合は -1 を出力する。

N,Q = map(int,input().split())

S = {} # 文字列と順番を記録する辞書を作る。ちな辞書とリストとタプルは全部違う
for i in range(N): #ループして辞書への登録をする
    s = input()
    if s not in S: # 同じ文字列が何回出てきても最初の順番を守る
        S[s] = i+1 #辞書に最初にでたやつを登録する

for _ in range(Q):
    t = input()
    if t in S: # tが辞書にあれば順番出せるけど、
        print(S[t])
    else: # なければ−１を出す
        print(-1)

# N 個の要素からなる数列 A, B が与えられます。A または B に含まれる値をすべて列挙し、重複を取り除いて昇順に出力してください


N = int(input()) #入力されてるけど使ってない
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = set(A) | set(B) #AまたはBに含まれるやつを集合する
print(" ".join(map(str, sorted(C)))) # 整数にして昇順にして出力する

# N = int(input())
# A = [int(x) for x in input().split()]
# B = [int(x) for x in input().split()]

# c = set(A + B)

# print(" ".join(map(str, sorted(c))))

# 整数 A, B, C, D が与えられます。  を計算した結果を出力してください。ここで、X mod Dとは X を D で割った余りを指します。

N = input().split()
A = int(N[0])
B = int(N[1])
C = int(N[2])
D = int(N[3])

X = ((A+B)*C)**2%D #この**が累乗のやつね

print(X)

# a, b, c, d = map(int, input().split())

# print(((a + b) * c) ** 2 % d)

# 整数 A, B が与えられます。以下のアルゴリズムを実行してください。
# 変数 N を 10,000 で初期化する
# N を A で割った商を N へ代入する
# N を B で割った余りを N へ代入する
# N を出力する
def solve():
    AB = input().split()
    A = int(AB[0])
    B = int(AB[1])
    N = 10000
    N = N//A
    N = N%B
    print(N)

if __name__ == "__main__":
    solve()


# 1 行目に整数 N と整数 K が与えられます。
# 2 行目に N 個の整数 a_i (1 ≤ i ≤ N) が半角スペース区切りで与えられます。
# K 番目の整数 a_K を出力してください。

N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

print(A[K-1])


# 1 行目に整数 N, M, K, L が与えられます。
# 2 行目以降に N 行 M 列の二次元配列が与えられます。
# 配列の K 行目 L 列目の要素を出力してください。
# 上から i 番目、左から j 番目の整数は a_ij です。


N,M,K,L = map(int,input().split())
k = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(i*j)
    k.append(row)

print(k[K-1][L-1])

# 1 行目に整数 N, M が与えられます。
# 2 行目に M 個の整数 a_1, a_2, ..., a_M が与えられます。
# M 個の整数に N が何個あるか数え、出力してください。
# また、N は M 個の整数の中に 1 個以上含まれるものとします。

N,M = list(map(int,input().split()))

for i in range(N):
    A = list(map(int,input().split()))
    a = A.count(N)
    print(a)

# values = input().split()
# N = int(values[0])
# M = int(values[1])

# A = [0] * M
# values = input().split()
# for i in range(M):
#     A[i] = int(values[i])

# ans = 0
# for a in A:
#     if a == N:
#         ans += 1

# print(ans)


# 5枚のカードが配られます。それぞれのカードには、1以上13以下のいずれかの整数が書かれています。
# カードに書かれている整数の組み合わせによって役が決まります。

# 配られた5枚のカードが、以下のいずれの役に該当するかを調べてください。
# 複数の役に該当する場合は、以下で先に記述した方の役に該当するものとします。

# FULL HOUSE
# ある数をちょうど3つと、別の数をちょうど2つ含む。
# THREE CARD
# ある数をちょうど3つ含む。
# TWO PAIR
# ある数をちょうど2つと、別の数をちょうど2つ含む。
# ONE PAIR
# ある数をちょうど2つ含む。

A = input().split()

a = {} # 値を数えたい時に便利な辞書
for i in A: # 標準入力をカウントしている
    if i in a: # 同じ数があれば辞書内のカウンターを回していく
        a[i] += 1
    else: # 違う数ならカウンター回さない
        a[i] = 1

cnt = list(a.values()) #　.values() → 辞書の「値だけ」を取得
if 3 in cnt and 2 in cnt:
    print("FULL HOUSE")
elif 3 in cnt:
    print("THREE CARD")
elif cnt.count(2) == 2:
    print("TWO PAIR")
elif 2 in cnt:
    print("ONE PAIR")
else:
    print("NO HAND")

# 自分だけなら正解できなかった。if構文を作るところはできるが、辞書やlist２までは辿り着けなかっ
# dict.keys() → 辞書の「キーだけ」を取得
# dict.items() → 辞書の「キーと値の両方」を取得

# 両親の血液型に関する遺伝情報が、 A, B, O からなる
# 2 つの長さ
# 2 の文字列
# S,T として与えられます。 子の血液型は、以下のルールによって決定します。

# S,T の中からそれぞれ
# 1 文字ずつ独立かつ一様ランダムに取り出し、それぞれ
# s,t とする。

# {s,t} の中に A が含まれ、なおかつ B が含まれないならば、血液型はA型となる。
# {s,t} の中に B が含まれ、なおかつ A が含まれないならば、血液型はB型となる。
# {s,t} の中に A と B がともに含まれるならば、血液型はAB型となる。
# 上記のいずれにも当てはまらない場合、血液型はO型となる。
# 子が各血液型になる確率を百分率表記 [%] でそれぞれ求めてください。ただし、求める答えは全て整数であることが保証されます

S = input()
T = input()
ST = {S,T}

cnt = list(ST.keys())
if "A" in cnt and "B" in cnt:
    print()
# 途中