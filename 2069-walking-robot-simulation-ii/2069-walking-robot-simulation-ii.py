class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dirs = {
            0:['East',(1,0)],
            1:['North',(0,1)],
            2:['West',(-1,0)],
            3:['South',(0,-1)]
        }
        self.x=0
        self.y=0
        self.curr_dir = 0
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        num %= self.perimeter
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.curr_dir = 3   # South
            return

        while num:
            dx, dy = self.dirs[self.curr_dir][1]
            nx, ny = self.x + dx, self.y + dy

            if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                self.curr_dir = (self.curr_dir + 1) % 4
                continue

            self.x, self.y = nx, ny
            num -= 1

    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.dirs[self.curr_dir][0]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()