#######################
#                     # 
# Name: Jaayanth SK   #
# Roll No.: ED21B029  #
# Question: Bonus 1   #
#                     #
#######################


import pygame
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()


class points(pygame.sprite.Sprite):
    def __init__(self, color, height, width, degree):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos_x, self.pos_y = screen_width / 2, screen_height / 2
        self.rect.center = (self.pos_x, self.pos_y)
        self.degree = degree

    def update(self):
        global lengths
        vel = 4
        self.pos_x += vel * np.cos(0.0174533 * self.degree)
        self.pos_y += vel * np.sin(0.0174533 * self.degree)
        self.rect.center = (self.pos_x, self.pos_y)

        if (
            pygame.sprite.spritecollideany(self, bg_list, pygame.sprite.collide_mask)
            or self.rect.x < 0
            or self.rect.x > screen_width
            or self.rect.y < 0
            or self.rect.y > screen_height
        ):
            distance = np.sqrt(
                (self.rect.x - screen_width / 2) ** 2
                + (self.rect.y - screen_height / 2) ** 2
            )
            data = [self.degree, distance]
            lengths.append(data)
            print(data)
            self.kill()


class bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Scenario.png").convert() #Load the different images here
        self.rect = self.image.get_rect()


pygame.init()

screen_width, screen_height = 683, 384
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bonus Q1")

point_list = pygame.sprite.Group()
bg_list = pygame.sprite.Group()

for deg in range(1, 361):
    point = points((255, 0, 0), 2, 2, deg)
    point_list.add(point)

bg1 = bg()
bg_list.add(bg1)

for sprite in bg_list:
    sprite.mask = pygame.mask.from_threshold(
        sprite.image, pygame.Color("black"), (1, 1, 1, 255)
    )

Running = True
clock = pygame.time.Clock()
lengths = []

while Running:
    bg_list.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    if len(lengths) == 360:
        Running = False
        x, y = [], []

        for i in lengths:
            x.append(i[0])
            y.append(i[1])

        plt.scatter(x, y, label="LiDar", color="blue")

        plt.xlabel("Beam Serial Number")
        plt.ylabel("Normalized Length")
        plt.title("Bonus")
        plt.legend()
        print("--- %s seconds ---" % (time.time() - start_time))
        plt.show()

    point_list.update()
    point_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
