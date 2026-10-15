import tkinter as tk
import random
import sys

class TipApp:
    def __init__(self):
        self.batch_windows = []
        self.single_window = None

    def show_single_tip(self):
        self.single_window = tk.Tk()
        self.single_window.title("专属提示")

        screen_width = self.single_window.winfo_screenwidth()
        screen_height = self.single_window.winfo_screenheight()
        window_width = 280
        window_height = 100
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.single_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tip = "我想你啦"
        bg = "skyblue"

        tk.Label(
            self.single_window,
            text=tip,
            bg=bg,
            font=("微软雅黑", 14),
            width=30,
            height=3
        ).pack()

        self.single_window.bind('<space>', self.on_space_global)
        self.single_window.attributes('-topmost', True)

        # 修正这里：去掉 name= 关键字参数，按位置传递参数
        self.single_window.protocol("WM_DELETE_WINDOW", self.start_batch_tips)
        self.single_window.mainloop()

    def create_batch_window(self, count):
        if count <= 0:
            return

        window = tk.Toplevel()
        self.batch_windows.append(window)

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = 280
        window_height = 100
        x = random.randrange(0, screen_width - window_width)
        y = random.randrange(0, screen_height - window_height)

        window.title('温馨提示')
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tips = [
            '多喝永哦', '保持微笑呀', '每天都要元气满满',
            '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
            '梦想成真', '期待下一次见面', '全程匿名',
            '顺顺利利', '早点休息', '愿所有烦恼都消失',
            '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服', '晚安'
        ]
        tip = random.choice(tips)

        bg_colors = [
            'lightpink', 'skyblue', 'lightgreen', 'lavender',
            'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine'
        ]
        bg = random.choice(bg_colors)

        tk.Label(
            window,
            text=tip,
            bg=bg,
            font=("微软雅黑", 14),
            width=30,
            height=3
        ).pack()

        window.bind('<space>', self.on_space_global)
        window.attributes('-topmost', True)

        if count > 1:
            window.after(50, self.create_batch_window, count - 1)

    def start_batch_tips(self):
        if self.single_window:
            self.single_window.destroy()
            self.single_window = None

        self.create_batch_window(100)

    def on_space_global(self, event=None):
        if self.single_window:
            self.single_window.destroy()

        for window in self.batch_windows:
            try:
                window.destroy()
            except:
                pass

        sys.exit()

if __name__ == '__main__':
    app = TipApp()
    app.show_single_tip()