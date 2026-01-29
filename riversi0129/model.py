class ReversiModel: #このコードには定義しか書いてないよ

# マスの状態を定義する。無、黒、白、盤外を表す壁。そこまで作っちゃったほうが楽らしい
    EMPTY = 0
    BLACK = 1
    WHITE = 2
    WALL = 3



    def __init__(self):
        """
        初期化
        """

#全て無でゲーム盤面を作成する
        self.board = [self.EMPTY] * 100 #空のリストを100回繋げてオセロ盤を作る

# 白黒の初期配置する
        self.board[44] = self.BLACK
        self.board[55] = self.BLACK
        self.board[54] = self.WHITE
        self.board[45] = self.WHITE

# 壁を設定する
        for i in range(10):
            self.board[i] = self.WALL #1〜１０
            self.board[90 + i] = self.WALL #９０〜１００
            self.board[10 * i] = self.WALL #１０ずつ
            self.board[10 * i + 9] = self.WALL #１９ずつ
# このi_boardやtopは定義されていない数値、定義されていないけどflip_listを実行するには必要
# この２つの数値は外部からの入力となってる。ここでは何マス目に何色を置いたってとこから持ってきている
# selfはclass（ReversiModel）のことで、class内の関数（flip_listも含めて）の情報を確認するのに必要
    def flip_list(self, i_board: int, top: int) -> list[int]:
        """
        盤面のi_boardにtop(BLACKorWHITE)を置いたときに
        ひっくり返るマスのリストを返す
        """

# board[i_board]が空じゃなければ[]のリストを返す。つまり他のコマがあるマスにはコマを置けないということ
        if self.board[i_board] != self.EMPTY:
            return []
# ここで相手の色を定義している。
# 三項演算子の解剖図
# = 結果A if 条件式 else 結果B
# なので、この文は、敵が黒になるのは自分が白の時、そうじゃないなら敵は白だ、的な意味になる
        enemy = self.BLACK if top == self.WHITE else self.WHITE
# あとで使う
        tops = []
# 上から順に盤面を作ってるから真上は−10、左は−1、となっていく
        UP,DOWN,LEFT,RIGHT =  -10,10,-1,1

# オセロで裏返るコマを探すために縦横斜めを定義している。temporalは一時的という意味であとで使う
        for vector in (RIGHT,RIGHT+ UP,UP,LEFT + UP,LEFT,LEFT+DOWN,DOWN,RIGHT+DOWN):
            temporal = []

# 裏返るコマを探すためにdeltaが必要。vectorは進む方向、deltaは進んだ距離として使う
            delta = vector
# このループで裏返るコマを探していく。コマ置いたマスのdelta方向にさっき定義したenemyがあれば
            while self.board[i_board + delta] == enemy:
                temporal.append(i_board + delta) #さっきの一時リストにマスを記録する
                delta += vector #deltaにvectorを足してさらにコマを探していく
            if self.board[i_board + delta] == top: #もしdeltaの先に自色があれば
                tops += temporal #さっき作ったリストに一時リストの中身を足す

# ここまでで壁や空白のことには触れていない。つまり『プログラムの指示されていないことはしない』というところが働いて
# 何もしないという処理になっている。また。while文でも『enemyがあれば続行すること』になっているので自色、壁、空白には
# 何もしないという処理になる。さらにdeltaの先に自色がなければ一時リストをtopsに足さないので、それ以外には何もしない
# ここで一時からtopsに足す処理がなければ、反対に白がなくても黒を裏返す処理になってくる
        return tops


    def put(self,i_board :int,top :int) -> bool:
        """
        盤面のi_boardにtop(BLACK or WHITE)を置き。
        同じ色で挟んでいるマスをひっくり返す
        """
# ここでflip_listにtopsを再計算させている。
# 違う関数内の変数は参照できない＋def put（）で呼び出したらどこに何を置いてtopsの数値を出すか計算しないといけないし情報が古い
# なので再計算させた方が楽だし最新の情報を使える
        tops = self.flip_list(i_board, top)
        if tops : #topsがあれば、なのでtopsが生まれなければこの処理はされない
            self.board[i_board] = top #コマ置いたマスと
            for i in tops: #tops内の数値をforで回した
                self.board[i] = top #各マスで『自分を置いたコマと同じ色にする』処理を行う
            return True


        return False