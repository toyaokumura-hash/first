from model import ReversiModel


class ReversiController:
    EMPTY = ReversiModel.EMPTY
    BLACK = ReversiModel.BLACK
    WHITE = ReversiModel.WHITE

    def __init__(self):
        """
        初期化
        """
        self.rm = ReversiModel()
        self.turn = self.WHITE


    def put(self, x: int,y: int)->None:
        """
        (x,y)にコマを置く
        """
        x += 1
        y += 1
        if self.rm.put(10 * y + x,self.turn):
            self.turn = self.WHITE if self.BLACK else self.BLACK



    def board(self) -> tuple[tuple[int]]:
        """
        盤面を渡す
        盤面には[X][Y]でアクセスする
        """

        bd = [self.rm.board[10 * i + 1:10 * i + 9] for i in range(1,9)]
        return tuple(zip(*bd))