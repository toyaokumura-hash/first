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

# 昨日のポーカーのやつを拡張してみよう。本当のポーカーみたいにできたらめっちゃいい感じやんな

# 開始したらランダムな数字が配られて、確認して、入力したら数字が入れ替わって、役が作られて、対戦ができるってとこが最終目標？
# 詳しく考えると、ファイルを実行したらまず、『ポーカースタート、Press Enter』と表示されて、
# エンター押すと1〜13のランダムな数字が最大４つまでの５つ配られて、それと現状の役が半角スペース区切りで表示される。
# その下に『手札を入れ替える？左から1〜5、入れ替えないならN』と表示されて、
# Nなら改めて役を表示、数字なら入力した位置のカードが交換されて、役を表示される。
# その下に『また遊んでね』と表示して終了って感じ？？

import random

def deal_hand() -> list[int]:
    """1~13のカードを5枚配る（各数字4枚ずつある想定）"""
    deck = [i for i in range(1,14)] * 4 # 1〜13のカードが4枚ずつあるデッキ
    hand = random.sample(deck,5) # デッキから重複なしでランダムに5枚配って手札とする。重複しないが、
    # 同じ数字のカードは4枚あるので最大4枚被りあり
    return hand #これをつけて返すことで他の関数でhandが使える（ローカルスコープとグローバルスコープ）

def judge_hand(hand):
    """数字のみの役判定（スートなし）"""
    # 役判定しやすくするためにソート

    # 各数字が何枚あるかカウント
    counts = {} # 空のリスト
    for num in hand:
        counts[num] = counts.get(num,0) + 1
            # ↑手札を数えるやつ
    unique_numbers = sorted(counts.keys())
    #数えたやつをキーごとに見やすく並べ替え。カードの数字で判定
    cnt_list = list(counts.values())
    #数えたやつを値ごとにリストにする。出た回数で判定
    # ストレート判定
    is_straight = False # 初期値を0にしてフラグを立てておく
    if len(unique_numbers) == 5: #並べ替えたやつが5枚連続してたら
        # 連続した数字の場合（３４５６７）
        if max(unique_numbers) - min(unique_numbers) == 4:
            is_straight = True #連番の最大と最小の差が4ならストレート判定。連番なら差は4になるはずやから
        #1,10,11,12,13の場合
        elif unique_numbers == [1,10,11,12,13]:
            is_straight = True #unique_numbersがロイヤルストレートのパターンならストレート判定

    #役の判定、ここもreturnで返すようになってる。別のとこでprintするから
    if is_straight and unique_numbers == [1, 10, 11, 12, 13]:
        return "ROYAL STRAIGHT !"
    # ストレート判定を両方満たしていたらこっち
    # 通常のストレート
    if is_straight:
        return "STRAIGHT !"

    # フォーカード
    if 4 in cnt_list:
        return "FOUR CARD !"

    # フルハウス
    if 3 in cnt_list and 2 in cnt_list:
        return "FULL HOUSE !"

    # スリーカード
    if 3 in cnt_list:
        return "THREE CARD !"

    # ツーペア (2枚組が2つある)
    if cnt_list.count(2) == 2: # ここだけちょっと違うフルハウスのような判定だとミスる
        return "TWO PAIR !"

    # ワンペア
    if 2 in cnt_list:
        return "ONE PAIR !"

    return "NO HAND"

def change_hand(hand: list[int]) -> list[int]: # 入力された手札を捨てて、新しく手札を追加したい
    s = list(map(int,input().split()))
    S = len(s) #ここで入力された数値の個数を出したい
    deck: list[int] = [i for i in range(1,14)] * 4
    # for _ in range(S):
    popped_hand = [i for i in hand if i not in s] #半角スペースで入力された数値をちゃんと判定できてない？
    new_hand: list[int] = random.sample(deck,S)
    #ここは入力された数値じゃなくて数値の個数で判定したい
    new_hand1 = popped_hand + new_hand
    # 減らした手札に新しい手札を追加したい
    return new_hand1

# メイン処理。プレイヤーに見えてる部分。裏の処理や定義を作ってからじゃないと
# 処理が止まるからここは最後の方に書く
print("ポーカースタート (Press Enter)")
input() # エンター待ち

start_hand = deal_hand()
#ここで最初に定義した関数が動いて、その結果を変数に代入している。
# deal_handの中でもhandが定義されているけどここは関数の外なので、
# スコープというルールで別物となっていて、関数の中と外では干渉し合わないしお互いが見えない
# なので、関数の外では今0から新しくhandが定義された
# ここで変数に代入したのは次とかでまたdeal_handを使うと手札が変わって大変だから

display_hand = sorted(start_hand) #プレイヤーに見やすくするために並べ替え

role = judge_hand(start_hand) # 上で作った役の判定を表示する。
# ここでreturnが活きる。関数の中と外では見えないけど。returnを使えば見える。
# 今までprintで表示させてたけど今回はそれじゃ分からない

print(f"配られた手札: {display_hand}")
print(f"役: {role}")

print("手札を入れ替える？")
print("入れ替えたい手札を半角スペースを入れて選んでね")
print("入れ替えない時はNを押してね")

new_hand = change_hand(start_hand)
display_hand1 = sorted(new_hand)
role = judge_hand(new_hand)

print(f"新しい手札: {display_hand1}")
print(f"新しい役: {role}")
print("また遊んでね !")
# 数字を入力したら対応した位置の手札が交換される（その位置にあった数字が削除され、新しい数字が表示され、また並べ替えられ、役が表示される）