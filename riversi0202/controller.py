from model import ReversiModel
# modelからReversiModelを読み込んで参照する



class ReversiController: #新たにclassを定義している
    EMPTY = ReversiModel.EMPTY #ここでmodelから引用してEMPTYを定義しているのはあくまでcontrollerは橋渡しだから
    BLACK1 = ReversiModel.BLACK1 #何か変更したい時はmodelだけ変更すればいいようになっている。あと情報を統一することで
    WHITE2 = ReversiModel.WHITE2#ルールを一括管理してますよ的な感じにしている

    def __init__(self):
        """
        初期化
        """
        self.rm = ReversiModel() #インスタンスを変数に定義することで処理に組み込みやすくしてるし、情報を保持して処理できる
        self.turn = self.WHITE2 #model内でdelta＝vみたいな感じで初期値を設定している。
        self.e_turn = self.BLACK1


    def put(self, x: int,y: int)->None:
        print("コマを置いたプレーヤー",self.turn,self.e_turn)
        """
        (x,y)にコマを置く
        """
        x += 1
        y += 1
        if self.rm.put(5 * y + x,self.turn) and self.rm.flip_judge(self.e_turn): #この3行で0から数えるプログラムを1から数えるように認識合わせしている
# プログラムでは0から数えるけどこのあとのGUIとは位置ズレが発生するからそれを防ぐために必要
            self.turn = self.BLACK1 if self.turn == self.WHITE2 else self.WHITE2
            self.e_turn = self.WHITE2 if self.turn == self.BLACK1 else self.BLACK1
            return
# コマを置いたらターンが変わるようになっている。ターンで白を置いたら次は黒、それ以外なら黒だ。って文
# パス機能の実装でターンチェンジの判定が変わった。コマを置いた＆flip_judgeがtrueを返せばターンチェンジ、
# 当てはまらなければ（コマを置けなければ）パスとなる。
        if not self.rm.flip_judge(self.turn) and not self.rm.flip_judge(self.e_turn):
            # print("flip_judge2")
            self.rm.win_judge()
# flip_judge2はやってること一緒なのでflip_judgeの値だけ変えることにした。また、勝敗判定ということで
# どちらも置けないことを確認するために二重に判定した






    @property
#インスタンス変数をここで定義している。ここに書いておけば、データを変更されることを防げる。
# あとここに書くことでコードが多少見やすくできるboard()[x][y]じゃなくてboard[x][y]にできる
    def board(self) -> tuple[tuple[int]]:
        """
        盤面を渡す
        盤面には[X][Y]でアクセスする
        """
# ここでこのあと出てくるGUI側に盤面を８✖️８として渡せる用意をしている。range（✖️８として渡せる用意をしている。
# range（1、9）は０と９を含まないから、そこに入ってる壁の行を省いた形にしている。その左にあるboard（）の式で壁の列を省いている
        bd = [self.rm.board[5 * i + 1 : 5 * i + 4] for i in range(1, 4)]

        return tuple(zip(*bd))
# これでデータの並びをGUIにわかりやすい形に並び替えてるboard[23]みたいな表記をboard[行][列]みたいに直感的にしている

    # def __init__(self):
    #     self._pas = False
    #     self.callback = None

    # def pas(self):
    #     return self._pas
    
    # @pas.setter
    # def pas(self, value):
    #     self._pas = value
