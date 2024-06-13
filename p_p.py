ball = None
pad1 = None
pad2 = None

def setup():
    global ball, pad1, pad2
    size(800,600)
    ball = Ball(400, 300, 20)
    pad1 = Paddle(30, 250)
    pad2 = Paddle(width-50, 250)
    ball.speedX = 5
    ball.speedY = random(-3, 3)
    
def draw():
    
    
class Ball:
    def __init__(self, X, Y, Dia):
        self.c = color(255)
        self.x = X
        self.y = Y
        self.d = Dia
        self.speedX = 0
        self.speedY = 0
        self.score1 = 0
        self.score2 = 0
        
    def display(self):
        fill(self.c)
        circle(self.x, self.y, self.d)
        
    def move(self):
        self.x = speedX
        self.y = speedY
        if(self.y > height and self.y < 0):
            self.speedY *= -1
    
    def checkCollision(self, paddle):
        if(self.right() > paddle.left() and self.left() < paddle.right() and self.top() < paddle.bottom() and self.bottom > paddle.top():
               self.speedX *= -1
               
    def right():
        return self.x + 
               
    def scores(self):
        textSize(32)
        textAlign(CENTER)
        if(self.right > width):
            score1 += 1
            self.reset()
        if(self.left < 0):
            score2 += 1
            self.reset()
    
    def reset(self):
        self.x = 400
        self.y = 300
        self.speedX *= -1
        self.speedY = random(-3, 3)
    
class Paddle:
        
