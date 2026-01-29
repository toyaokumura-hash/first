import tkinter as tk
# pythonのGUIライブラリを呼び出している
from controller import ReversiController
# さっきと同じようにcontrollerからclassを呼び出している。
# controllerがviewとmodelを繋ぐという設計になってるから呼ぶ必要がないし、
# 呼んじゃうとせっかく省いた盤面の壁の情報とかが入ってややこしくなる。こういうのを依存関係を減らすと言う

class ReversiView:
# クラスの定義ここでは画面の要素のサイズ感がメイン
    EMPTY = ReversiController.EMPTY
    BLACK = ReversiController.BLACK
    WHITE = ReversiController.WHITE
    CELL_WIDTH = 50
    # マスの横幅
    CELL_HEIGHT = 50
    # マスの高さ
    TOP_MARGIN = 5
    # マスとコマの隙間
    MARGIN = 5
    # リバーシのウインドウと実線の隙間
    BD_WIDTH = CELL_WIDTH * 8 + MARGIN * 2
    # 盤面全体の横幅、８マス＋両橋ってこと
    BD_HEIGHT = CELL_HEIGHT * 8 + MARGIN * 2
    # 盤面の縦幅

    def __init__(self):
        """
        初期化
        """

        self.root = tk.Tk()
        # これまでclassを変数に代入してたのと一緒
        # これを書くことでPCのメモリ内にGUIのウインドウを作る準備が始まる
        self.root.title("リバーシ")
        # ウインドウのタイトルをリバーシにする
        self.canvas = tk.Canvas(
            self.root,
            bg = "green",
            width = self.BD_WIDTH,
            height = self.BD_HEIGHT
        )
        # 緑色でこの縦横の画面を出してと指示を出している

        self.canvas.pack()
        # canvasとrootを結びつけて一つの表示にしている
        # これをするまではまだcanvasはrootに表示されていない。表示のタイミングとか位置をいじれるのが
        # packのいいところ


        self.controller = ReversiController()
        # controllerを変数に代入している

        self.flash()
        # このあと出てくる盤面の描画関数を実行している。初期盤面を描いている


        self.canvas.bind("<ButtonPress>",self.click)
        # canvas内のbindメソッドで<ButtonPress>がマウスのボタンが押されたという指示、
        # そこにclick関数が指定してあるのでマウスのボタンが押されたらclick関数を実行するというもの
        # これがあれば盤面でshift押しながらドラッグみたいな操作も追加できそう

    def click(self,event) -> None:
        """
        盤面をクリックした時の処理
        """
# marginの中のマスの横幅のなかでイベント（クリック）が起きたら変数x、
# 同じ条件で縦幅をyとして
        x = (event.x - self.MARGIN) // self.CELL_WIDTH
        y = (event.y - self.MARGIN) // self.CELL_HEIGHT
        self.controller.put(x,y)
        self.flash()
        # xyの位置にcontrollerからコマを置く関数を実行させて描画してる
        # 最後にflashを描かないとデータ的にはコマ置かれてひっくり返ってても描画されない


    def draw_top(self,x: int,y: int,top: int) -> None:
        """
        canvasにコマを描画をする
        """

        top_color = "white" if top == self.WHITE else "black"
        # 色は白の番なら白、黒の番なら黒と描いてる


        self.canvas.create_oval(
            x * self.CELL_WIDTH + self.MARGIN + self.TOP_MARGIN,
            y * self.CELL_HEIGHT + self.MARGIN + self.TOP_MARGIN,
            (x + 1) * self.CELL_WIDTH + self.MARGIN - self.TOP_MARGIN,
            (y + 1) * self.CELL_HEIGHT + self.MARGIN - self.TOP_MARGIN,
            fill=top_color
        )
# 円を描くメソッドで、x×マスの横＋ウインドウの隙間＋マスの隙間って感じで４つ位置指定して
# そこに収まるように円を描いてその前に指定してたtop colorで塗りつぶすやつ
# 左端が X なら、右端は X+1って考えはグリッドを扱う上で結構大事らしい

    def flash(self) -> None:
        """
        盤面の状態をキャンバスに描画する
        """

        self.canvas.delete("all")
        # 一旦canvasを全消しする。まさかよね。でもこれ描くくらいわけないから目に見えないのよ
        # アニメで動いてるわけじゃないし、上から描き直すより消して描き直した方が処理も早いしコードも簡単になる


        for y in range(self.MARGIN,self.MARGIN + self.CELL_WIDTH * 8  + 1, self.CELL_WIDTH):
            self.canvas.create_line(self.MARGIN, y, self.MARGIN + self.CELL_WIDTH * 8, y)
        for x in range(self.MARGIN, self.MARGIN + self.CELL_HEIGHT * 8  + 1, self.CELL_HEIGHT):
            self.canvas.create_line(x, self.MARGIN, x, self.MARGIN + self.CELL_HEIGHT * 8)
# これは各マスごとに線を引いてるやつ、range(スタート, ゴール, ステップ)って感じになってる。rangeやから最後は＋１しようね


        for x in range(8):
            for y in range(8):
                match self.controller.board[x][y]:
                    case ReversiController.BLACK:
                        self.draw_top(x, y, ReversiController.BLACK)
                    case ReversiController.WHITE:
                        self.draw_top(x, y, ReversiController.WHITE)
# これはマスを描き直すやつ、８×８の中に色分けしてコマを描いてる。
# case _:を使えばどれにも当てはまらない時の処理が作れる
# if文よりもパターンごとにマッチさせるのが得意でコードが短くなる

    def run(self) -> None:
        """
        実行
        """
        self.root.mainloop()
# 何かイベントあった？って聞き続けて終わらない状態に入って、
# このリバーシのイベントはクリックしかないからそれを待ってクリックに反応する部分だけ繰り返されるってことね
# loopは普通上から下まで実行したら終わるコードを終わらせずに、
# OSにイベントの発生があるまで待機する状態にするメソッドってことね