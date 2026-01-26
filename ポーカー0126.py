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

def deal_hand() -> list:
    """1~13のカードを5枚配る（各スート数字4枚ずつある想定）"""
    suit = ['♠︎','❤︎','♦︎','♣︎']
    deck = [(s,r) for s in suit for r in range(1,14)] * 4 # 1〜13のカードが4枚ずつあるデッキ
    hand:list = random.sample(deck,5) # デッキから重複なしでランダムに5枚配って手札とする。重複しないが、
    # 同じ数字のカードは4枚あるので最大4枚被りあり
    return hand #これをつけて返すことで他の関数でhandが使える（ローカルスコープとグローバルスコープ）

def judge_hand(hand):
    """数字のみの役判定（スートなし）"""
    # 役判定しやすくするためにソート
    # hand.sort()

    # 各数字が何枚あるかカウント
    cnt = {}
    cnt1 = {} # 空のリスト
    for _,i in (hand):
        (hsu,hnu) = _,i
        cnt[hnu] = cnt.get(hnu,0) + 1
        cnt1[hsu] = cnt1.get(hsu,0) + 1
            # ↑手札を数えるやつ
    hand_sort = sorted(cnt.keys())
    #数えたやつをキーごとに見やすく並べ替え。カードの数字で判定
    cnt_list = list(cnt.values())
    #数えたやつを値ごとにリストにする。出た回数で判定
    # ストレート判定
    straight = False # 初期値を0にしてフラグを立てておく
    if len(hand_sort) == 5: #並べ替えたやつが5枚連続してたら
        # 連続した数字の場合（３４５６７）
        if max(hand_sort) - min(hand_sort) == 4:
            straight = True #連番の最大と最小の差が4ならストレート判定。連番なら差は4になるはずやから
    #1,10,11,12,13の場合
    elif hand_sort == [1,10,11,12,13]:
        straight = True #unique_numbersがロイヤルストレートのパターンならストレート判定

    Flush = False
    if cnt1 == 5:
        Flush = True


    if straight and Flush and hand_sort == [1, 10, 11, 12, 13]:
        return "ROYAL STRAIGHT FLUSH !"
    #役の判定、ここもreturnで返すようになってる。別のとこでprintするから
    if straight and hand_sort == [1, 10, 11, 12, 13]:
        return "ROYAL STRAIGHT !"
        # ストレート判定を両方満たしていたらこっち
        # 通常のストレート
    if straight and Flush:
        return "STRAIGHT FLUSH !"
    if straight:
        return "STRAIGHT !"
    if Flush:
        return "FLUSH !"


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

def change_hand(hand: list) -> list: # 入力された手札を捨てて、新しく手札を追加したい
        change_list = list(map(int,change_num.split()))
        change_cnt = len(change_list) #ここで入力された数値の個数を出したい
        change_reverse = sorted(change_list, reverse=True)

        suit = ['♠︎','❤︎','♦︎','♣︎']
        deck = [(s,r) for s in suit for r in range(1,14)] * 4 # 1〜13のカードが4枚ずつあるデッキ
        new_hand: list = random.sample(deck,change_cnt)
        for pos,new_card in enumerate(new_hand): #enumerateを使うと、リストの位置と数値を取り出せる
            for pos1,reverse_cnt in enumerate(change_reverse):
                if pos == pos1 :
                    hand.insert(reverse_cnt,new_card) #handのiの位置にcardの数値を挿入する
                    hand.pop(reverse_cnt-1) #handのiの位置の数値を消す
            # 減らした手札に新しい手札を追加したい
        return hand

# メイン処理。プレイヤーに見えてる部分。裏の処理や定義を作ってからじゃないと
# 処理が止まるからここは最後の方に書く
print("ポーカースタート")
input( "Press Enter >> ") # エンター待ち

start_hand = deal_hand()
#ここで最初に定義した関数が動いて、その結果を変数に代入している。
# deal_handの中でもhandが定義されているけどここは関数の外なので、
# スコープというルールで別物となっていて、関数の中と外では干渉し合わないしお互いが見えない
# なので、関数の外では今0から新しくhandが定義された
# ここで変数に代入したのは次とかでまたdeal_handを使うと手札が変わって大変だから

# display_hand = sorted(start_hand) #プレイヤーに見やすくするために並べ替え
role = judge_hand(start_hand) # 上で作った役の判定を表示する。
# ここでreturnが活きる。関数の中と外では見えないけど。returnを使えば見える。
# 今までprintで表示させてたけど今回はそれじゃ分からない
deal = (f"手札: {start_hand}")
role1 = (f"役: {role}")

print(f"配られた{deal}")
print(role1)

print("手札を入れ替える？")
change_num = input("入れ替えたい手札を1〜5で半角スペースを入れて選んでね\n入れ替えない時はEnterを押してね >> ")

while True:
    if not change_num:
        print(deal)
        print(role1)
        print("また遊んでね !")
        break

    # print()
    new_hand = change_hand(start_hand)
    # display_hand1 = sorted(new_hand)
    role = judge_hand(new_hand)

    print(f"新しい手札: {new_hand}")
    print(f"新しい役: {role}")
    print("また遊んでね !")
    break
# 数字を入力したら対応した位置の手札が交換される（その位置にあった数字が削除され、新しい数字が表示され、また並べ替えられ、役が表示される）
