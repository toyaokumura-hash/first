from view import ReversiView


if __name__ == "__main__":
    view = ReversiView()
    view.run()

# mainを分けてるのもmodelとかを分けるのと同じであとの変更がしやすい、何を司るファイルか理解しやすいようになってる
# 今回はmodel、controller、view、（main）で理解していったけど
# 実際は（main）、view、controller、modelって感じで動くのね〜。
# でもmodel自体は定義しかないから何かをするというよりはcontrollerにそこ置けるよここは壁だよって言うやつか