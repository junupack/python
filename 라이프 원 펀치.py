import tkinter as tk

CELL_SIZE = 15
GRID_WIDTH = 40
GRID_HEIGHT = 30

class LifeGame:
    def __init__(self, master):
        self.master = master
        self.is_running = False

        self.grid = [[0]*GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.canvas = tk.Canvas(master, width=GRID_WIDTH*CELL_SIZE, height=GRID_HEIGHT*CELL_SIZE, bg='white')
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.toggle_cell)

        frame = tk.Frame(master)
        frame.pack()

        self.start_button = tk.Button(frame, text="시작", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(frame, text="멈춤", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(frame, text="초기화", command=self.clear)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = "black" if self.grid[y][x] == 1 else "white"
                self.canvas.create_rectangle(
                    x*CELL_SIZE, y*CELL_SIZE,
                    (x+1)*CELL_SIZE, (y+1)*CELL_SIZE,
                    fill=color, outline="gray"
                )

    def toggle_cell(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            if self.grid[y][x] == 0:
                # 빈 칸 클릭하면 무조건 살림
                self.grid[y][x] = 1
            else:
                # 살아있는 셀 클릭하면 죽음(토글)
                self.grid[y][x] = 0
            self.draw_grid()

    def count_neighbors(self, x, y):
        count = 0
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                nx, ny = x + dx, y + dy
                if (dx != 0 or dy != 0) and 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                    count += self.grid[ny][nx]
        return count

    def next_generation(self):
        new_grid = [[0]*GRID_WIDTH for _ in range(GRID_HEIGHT)]
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                neighbors = self.count_neighbors(x, y)
                if self.grid[y][x] == 1 and neighbors in [2,3]:
                    new_grid[y][x] = 1
                elif self.grid[y][x] == 0 and neighbors == 3:
                    new_grid[y][x] = 1
        self.grid = new_grid

    def update(self):
        if self.is_running:
            self.next_generation()
            self.draw_grid()
        self.master.after(150, self.update)

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def clear(self):
        if not self.is_running:
            self.grid = [[0]*GRID_WIDTH for _ in range(GRID_HEIGHT)]
            self.draw_grid()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("생명 게임 (클릭 가능, 시작 후 클릭 가능, 멈춤 가능)")
    game = LifeGame(root)
    game.update()
    root.mainloop()