# # coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
t = input()
print("{}@{}".format(s,t))

# あなたは休暇をとり旅行の予定を立てています。

# n 日間の休暇を取り移動に m 日間かけます。 何日分の宿を取れば良いかを出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
m = int(input())

print(n-m)

# あなたは散歩をするために水筒を用意しようとしています。

# 散歩をするときの水分補給の目安として 15 分あたり 200 ml を飲む必要があります。

# n 分間散歩する時に必要な水筒の容量を出力してください
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
print((n//15)*200)

# 手始めに文字列の最後の 1 文字を出力するプログラムを作成することにしました。

# 文字列 S が与えられるので最後の 1 文字を出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
print(s[-1])


# 与えられた10進数の整数Nを2進数に変換したときの1の個数を答えて下さい。

# 整数の10進数を2進数に変換するには、変換したい10進数を商が0になるまで2で割り続け求めた余りの部分を逆順に並べます。
N = int(input())
ans = 0
bitMask = 1
while bitMask <= N:
    if bitMask & N != 0:
        ans += 1
    bitMask *= 2

print(ans)

# 10 進数の整数 N が与えられます。
# 入力を整数型で受け取り、出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = input()
print(N)

# 2 進数の整数 S が与えられます。
# 与えられる 2 進数の 1 の個数を数え、出力してください。

S = input()

ans = 0
for i in range(len(S)):
    if S[i] == "1":
        ans += 1
print(ans)

# 与えられた 10 進数の整数 N を 2 進数に変換したときの 1 の個数を答えて下さい。

# 整数の 10 進数を 2 進数に変換するには、変換したい 10 進数を商が 0 になるまで 2 で割り続け求めた余りの部分を逆順に並べます。

# 例えば、10 進数の 11 を 2 進数に変換するとき

# N が 0 になるまで繰り返す

# 毎回 N % 2 が 1 ならカウントを増やす

# N //= 2 で次へ進む

# Python3コード
N = int(input())

binaryNumber = list() #空のリスト作成。ここに2で割ったあまりを入れる
while N // 2 > 0: #N//2が0より大きければループする。Nが２以上の間くり返す。
    binaryNumber.append(N % 2) #Nを２で割ったあまり、これをリストの末尾に追加する
    N //= 2 #Nを2で割り、次の桁へ進む
binaryNumber.append(N) # ループを抜けた後に最後に残った1をリストに追加
reversed(binaryNumber)  # 逆順にする

ans = 0 # 2進数の1を数えるための変数
for i in range(len(binaryNumber)): # binarynumberの長さだけループする
    if binaryNumber[i] == 1: # リストのI番目の値が1か判定する
        ans += 1 # 1があればカウントを増やす
print(ans)

# 10 進数の整数 N が与えられます。
# N を 2 進数にしたとき、最下位の桁が 1 かどうか判定してください。

# 今回の問題では N を 2 進数に変換することなく、AND 演算(論理積)を使って判定してください
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

if N & 1: # &演算子は２つの数字を合わせて2進数で表示してくれるやつ。今回は末尾1を探したいからこの形になった
    print("Yes")
else:
    print("No")
# # こんな簡単な式でいいんや
# 与えられた 10 進数の整数 N を 2 進数に変換したときの 1 の個数を答えて下さい。

# ただし、今回の問題では AND 演算を使って解いてみましょう
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
count = 0
while N > 0:
    if N & 1:
        count += 1
    N >>= 1

print(count)
# N = int(input())
# ans = 0
# bitMask = 1 ビットマスク用の変数、今回は１
# while bitMask <= N: ビットマスクがN以下ならループする
#     if bitMask & N != 0: ビットが０じゃなければ（１なら）
#         ans += 1 カウントを１進める
#     bitMask *= 2

# print(ans)

# 長さ M の 2 つの異なったタグの組で囲まれた部分を、ある長さ N のテキストデータから抽出しようとしています。

# 1 行目に < と > で囲まれた半角英数字のタグがスペース区切りで開始、終了タグの順で入力されます。

# 2 行目に抽出を行う対象のテキストデータが入力されます。テキストデータは半角英数字とタグのみで構成されています。

# 抽出の手順は

# 1.テキストデータの先頭から、開始タグを見つけます。
# 2.開始タグ末尾から終了タグを探します。
# 3.開始タグから終了タグまでの間の文字列を出力します。もし、文字列が存在しない場合は<blank>と出力します。
# 4.終了タグの末尾を先頭として 1. から再度繰り返します。
# 5.テキストデータの末尾に到達したら終了します。
# tag1,tag2 = input().split()
# text = input()

# pos = 0 #検索開始位置
# while pos < len(text): #開始タグを探す
#         start_idx = N.find(tag1,pos)
#         if start_idx == -1:
#             break

#         end_idx = N.find(tag2, start_idx + len(tag1))
#         if end_idx == -1:
#             break

#         content = N[start_idx + len(tag1):end_idx]
#         if content == "":
#             print("<blank>")
#         else:
#             print(content)

#         N = end_idx + len(tag2)

def solve(): #関数作るよ！
    tag_a, tag_b = input().split()
    search_str = input()
    p = 0
    s = 0
    while True:
        s = search_str[p::].find(tag_a)
        p += s + len(tag_a)
        e = search_str[p::].find(tag_b) + p
        if s == -1:
            break
        elif p == e:
            print('<blank>')
        elif p < e:
            print(search_str[p:e:])
        p = e
if __name__ == "__main__":
    solve()

# <abc> <xyz>
# hoge<abc>piyo<xyz>
#鬼むずい、正直あんまり理解できんかった

# 文字列 S が与えられます。
# これを、改行区切りで 2 回出力してください。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
print("{}\n{}".format(s,s))

# def solve():
#     S1 = input()
#     S2 = list(S1)
#     print(S1)
#     print("".join(S2))
# if __name__ == "__main__":
#     solve()

# ある長さ N のテキストデータのうち長さ M の開始タグと終了タグで囲まれている部分を出力してみましょう。
# ・ テキストデータは必ず開始タグと終了タグがこの順で丁度 1 つずつ存在し、それぞれの開始位置が与えられます。
def solve():
    tag_a, tag_b = input().split()
    search_str = input()
    m = len(tag_a)
    a_index,b_index = map(int,input().split())
    if a_index+m == b_index:
        print('<blank>')
    else:
        print(search_str[a_index+m-1:b_index-1])
if __name__ == "__main__":
    solve()

# ある長さNのテキストデータのうち開始タグと終了タグがどこにあるかを出力してみましょう。
# ・ テキストデータは必ず開始タグと終了タグがこの順で丁度1つずつ存在します。
def solve():
    tag_a, tag_b = input().split()
    search_str = input()

    a_pos = search_str.find(tag_a)
    b_pos = search_str.find(tag_b)

    print(a_pos+1, b_pos+1)

if __name__ == "__main__":
    solve()
# find関数は探したい元の文字列そのものにつける

# ・ 開始タグと終了タグの開始位置 (s_i,g_i) を全て求めてみましょう。
# ・ テキストデータは必ず 1 組以上のタグが含まれ、タグは片方のみ出現することはありません。
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def solve(): #関数作るよ！
    tag_a, tag_b = input().split() #　変数だよ！
    search_str = input()

    pos = 0 #変数だよ！これは検索開始位置だよ！
    while True: #ループして検索
        a_idx = search_str.find(tag_a, pos) #　search_strのpos文字目からtag_aを探すやつだよ
        if a_idx == -1: #なかったらループやめるよ
            break

        b_idx = search_str.find(tag_b, a_idx + len(tag_a)) #tag_bをtag_aの最後から探すよ
        if b_idx == -1:
            break

        # < の位置同士をスペース区切りで出力
        print(a_idx+1, b_idx+1) #見つかったやつを出力するよ

        # 次は終了タグの後ろから探す
        pos = b_idx + len(tag_b)

if __name__ == "__main__": #このファイルが直で叩かれたときに作った関数発動するよ！課題の処理には直接関係ないよ！
    solve()


# 長さ M の 2 つの異なったタグの組で囲まれた部分を、ある長さ N のテキストデータから抽出しようとしています。

# 1 行目に < と > で囲まれた半角英数字のタグがスペース区切りで開始,終了タグの順で入力されます。

# 2 行目に抽出を行う対象のテキストデータが入力されます。テキストデータは半角英数字とタグのみで構成されています。

# 抽出の手順は

# 1.テキストデータの先頭から、開始タグを見つけます。
# 2.開始タグ末尾から終了タグを探します。
# 3.開始タグから終了タグまでの間の文字列を出力します。もし、文字列が存在しない場合は<blank>と出力します。
# 4.終了タグの末尾を先頭として1.から再度繰り返します。
# 5.テキストデータの末尾に到達したら終了します。
def solve(): #関数作るよ！
    tag_a, tag_b = input().split() #　変数だよ！
    search_str = input()
    p = 0 #変数だよ！これは検索開始位置だよ！
    s = 0 #変数だよ！これは検索方法だよ！二つとも最初だから０だよ！
    while True: #ループで検索開始
        s = search_str[p::].find(tag_a) #開始されたからさっきの二つに属性追加されたよ！
        p += s + len(tag_a) #sはpから１文字ずつ最後までtag_aを探すよ、pは次の開始位置を探した結果に移動させるよ
        e = search_str[p::].find(tag_b) + #ほぼsだよ！
        if s == -1:
            break
        elif p == e:
            print('<blank>')
        elif p < e:
            print(search_str[p:e:])
        p = e
if __name__ == "__main__":
    solve()