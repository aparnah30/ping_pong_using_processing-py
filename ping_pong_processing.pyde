ball = None
pad1 = None
pad2 = None

def setup():
    global ball, pad1, pad2
    size(800, 600)
    ball = Ball(400, 300, 20)
    pad1 = Paddle(30, 250)
    pad2 = Paddle(width - 50, 250)
    ball.speedX = 5
    ball.speedY = random(-3, 3)
    
def draw():
    background(0)
    ball.move()
    ball.checkCollision(pad1)
    ball.checkCollision(pad2)
    ball.display()
    pad1.move()
    pad2.move()
    pad1.display()
    pad2.display()
    # ball.scores()
    
class Ball:
    def __init__(self, tempX, tempY, tempDiameter):
        self.x = tempX
        self.y = tempY
        self.diameter = tempDiameter
        self.speedX = 0
        self.speedY = 0
        self.c = color(255)
        # self.score1 = 0
        # self.score2 = 0
        
    def move(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.y < 0 or self.y > height:
            self.speedY *= -1
            
    def checkCollision(self, paddle):
        if (self.right() > paddle.left() and
            self.left() < paddle.right() and
            self.bottom() > paddle.top() and
            self.top() < paddle.bottom()):
            self.speedX *= -1
            
    # def scores(self):
    #     textSize(32)
    #     textAlign(CENTER)
    #     text(self.score1, width/2-30, 30)
    #     text(self.score2, width/2+30, 30)
    #     if self.right > width:
    #         self.score1 += 1
    #     if self.left <0:
    #         self.score2 += 1
            
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def left(self):
        return self.x - self.diameter / 2
    
    def right(self):
        return self.x + self.diameter / 2
    
    def top(self):
        return self.y - self.diameter / 2
    
    def bottom(self):
        return self.y + self.diameter / 2

class Paddle:
    def __init__(self, tempX, tempY):
        self.x = tempX
        self.y = tempY
        self.w = 20
        self.h = 100
        self.speedY = 5
    
    def move(self):
        if self.x < width / 2:
            if keyPressed:
                if key == 'w' and self.y > 0:
                    self.y -= self.speedY
                elif key == 's' and self.y < height - self.h:
                    self.y += self.speedY
        else:
            if ball.y < self.y + self.h / 2 and self.y > 0:
                self.y -= self.speedY
            elif ball.y > self.y + self.h / 2 and self.y < height - self.h:
                self.y += self.speedY
 
    def display(self):
        fill(255)
        rect(self.x, self.y, self.w, self.h)
    
    def left(self):
        return self.x
    
    def right(self):
        return self.x + self.w
    
    def top(self):
        return self.y
    
    def bottom(self):
        return self.y + self.h
