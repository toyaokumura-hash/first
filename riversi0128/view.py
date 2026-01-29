import tkinter as tk
from controller import ReversiController


class ReversiView:
    EMPTY = ReversiController.EMPTY
    BLACK = ReversiController.BLACK
    WHITE = ReversiController.WHITE
    CELL_WIDTH = 50
    CELL_HEIGHT = 50
    TOP_MARGIN = 5
    MARGIN = 5
    BD_WIDTH = CELL_WIDTH * 8 + MARGIN * 2
    BD_HEIGHT = CELL_HEIGHT * 8 + MARGIN * 2


    def __init__(self):
        """
        初期化
        """

        self.root = tk.Tk()
        self.root.title("リバーシ")
        self.canvas = tk.Canvas(
            self.root,
            bg = "green",
            width = self.BD_WIDTH,
            height = self.BD_HEIGHT
        )

        self.controller = ReversiController()


        self.flash()


        self.canvas.bind("<ButtonPress>",self.click)


        self.canvas.pack()


    def click(self,event) -> None:
        """
        盤面をクリックした時の処理
        """

        x = (event.x - self.MARGIN) // self.CELL_WIDTH
        y = (event.y - self.MARGIN) // self.CELL_HEIGHT
        self.controller.put(x,y)
        self.flash()


    def draw_top(self,x: int,y: int,top: int) -> None:
        """
        canvasにコマを描画をする
        """

        top_color = "white" if top == self.WHITE else "black"


        self.canvas.create_oval(
            x * self.CELL_WIDTH + self.MARGIN + self.TOP_MARGIN,
            y * self.CELL_HEIGHT + self.MARGIN + self.TOP_MARGIN,
            (x + 1) * self.CELL_WIDTH + self.MARGIN - self.TOP_MARGIN,
            (y + 1) * self.CELL_HEIGHT + self.MARGIN - self.TOP_MARGIN,
            fill=top_color
        )



    def flash(self) -> None:
        """
        盤面の状態をキャンバスに描画する
        """

        self.canvas.delete("all")


        for y in range(self.MARGIN,self.MARGIN + self.CELL_WIDTH * 8  + 1, self.CELL_WIDTH):
            self.canvas.create_line(self.MARGIN, y, self.MARGIN + self.CELL_WIDTH * 8, y)
        for x in range(self.MARGIN, self.MARGIN + self.CELL_HEIGHT * 8  + 1, self.CELL_HEIGHT):
            self.canvas.create_line(x, self.MARGIN, x, self.MARGIN + self.CELL_HEIGHT * 8)

        for x in range(8):
            for y in range(8):
                match self.controller.board[x][y]:
                    case ReversiController.BLACK:
                        self.draw_top(x, y, ReversiController.BLACK)
                    case ReversiController.WHITE:
                        self.draw_top(x, y, ReversiController.WHITE)


    def run(self) -> None:
        """
        実行
        """
        self.root.mainloop()
