import random
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)


class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("asteroid_small.bmp"),
              MEDIUM: games.load_image("asteroid_med.bmp"),
              LARGE: games.load_image("asteroid_big.bmp")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size

    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width


def main():
    nebula_image = games.load_image("nebula.jpg")
    games.screen.background = nebula_image

    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    games.screen.mainloop()


main()
