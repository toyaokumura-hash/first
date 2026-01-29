from model import ReversiModel
# modelからReversiModelを読み込んで参照する

class ReversiController: #新たにclassを定義している
    EMPTY = ReversiModel.EMPTY #ここでmodelから引用してEMPTYを定義しているのはあくまでcontrollerは橋渡しだから
    BLACK = ReversiModel.BLACK #何か変更したい時はmodelだけ変更すればいいようになっている。あと情報を統一することで
    WHITE = ReversiModel.WHITE #ルールを一括管理してますよ的な感じにしている

    def __init__(self):
        """
        初期化
        """
        self.rm = ReversiModel() #インスタンスを変数に定義することで処理に組み込みやすくしてるし、情報を保持して処理できる
        self.turn = self.WHITE #model内でdelta＝vみたいな感じで初期値を設定している。


    def put(self, x: int,y: int)->None:
        """
        (x,y)にコマを置く
        """
        x += 1
        y += 1
        if self.rm.put(10 * y + x,self.turn): #この3行で0から数えるプログラムを1から数えるように認識合わせしている
# プログラムでは0から数えるけどこのあとのGUIとは位置ズレが発生するからそれを防ぐために必要
            self.turn = self.BLACK if self.turn == self.WHITE else self.WHITE
# コマを置いたらターンが変わるようになっている。ターンで白を置いたら次は黒、それ以外なら黒だ。って文


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
        bd = [self.rm.board[10 * i + 1:10 * i + 9] for i in range(1,9)]
        return tuple(zip(*bd))
# これでデータの並びをGUIにわかりやすい形に並び替えてるboard[23]みたいな表記をboard[行][列]みたいに直感的にしている