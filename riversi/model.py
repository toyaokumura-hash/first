class ReversiModel:

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
        self.board = [self.EMPTY] * 100

# 白黒の初期配置する
        self.board[44] = self.BLACK
        self.board[55] = self.BLACK
        self.board[54] = self.WHITE
        self.board[45] = self.WHITE

# 壁を設定する
        for i in range(10):
            self.board[i] = self.WALL
            self.board[90 + i] = self.WALL
            self.board[10 * i] = self.WALL
            self.board[10 * i + 9] = self.WALL

    def flip_list(self, i_board: int, top: int) -> list[int]:
        """
        盤面のi_boardにtop(BLACKorWHITE)を置いたときに
        ひっくり返るマスのリストを返す
        """


        if self.board[i_board] != self.EMPTY:
            return []

        enemy = self.BLACK if top == self.WHITE else self.WHITE

        tops = []

        UP,DOWN,LEFT,RIGHT =  -10,10,-1,1


        for v in (RIGHT,RIGHT+ UP,UP,LEFT + UP,LEFT,LEFT+DOWN,DOWN,RIGHT+DOWN):
            temp = []


            delta = v

            while self.board[i_board + delta] == enemy:

                temp.append(i_board + delta)
                delta += v
            if self.board[i_board + delta] == top:
                tops += temp

        return tops


    def put(self,i_board :int,top :int) -> bool:
        """
        盤面のi_boardにtop(BLACK or WHITE)を置き。
        同じ色で挟んでいるマスをひっくり返す
        ひっくり返したら
        """

        tops = self.flip_list(i_board, top)
        if tops :
            self.board[i_board] = top
            for i in tops:
                self.board[i] = top
            return True


        return False