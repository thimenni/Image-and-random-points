import random
import pygame
from image import Image
from point import Point


class Game:
    def __init__(self, image: Image) -> None:
        pygame.init()
        self.image = image
        monitor_w, monitor_h = 600, 600
        self.image.padding(monitor_w, monitor_h)
        self.surface = pygame.display.set_mode((monitor_w, monitor_h))
        self.surface.fill((255, 255, 255))
        pygame.display.set_caption('Image and Random Point.')
        self.clock = pygame.time.Clock()
        self.move_points_tl = pygame.sprite.Group()
        self.move_points_tr = pygame.sprite.Group()
        self.move_points_bl = pygame.sprite.Group()
        self.move_points_br = pygame.sprite.Group()
        color = (255, 0, 0)
        nb_random_point = self.image.width * self.image.height//16
        for _ in range(nb_random_point):
            y = random.randint(0, monitor_h // 2)
            x = random.randint(0, monitor_w // 2)
            p = Point((x, y), self.image, (1, 1), color)
            self.move_points_tl.add(p)

            y = random.randint(0, monitor_h // 2)
            x = random.randint(monitor_w // 2, monitor_w)
            p = Point((x, y), self.image, (-1, 1), color)
            self.move_points_tr.add(p)

            y = random.randint(monitor_h // 2, monitor_h)
            x = random.randint(0, monitor_w // 2)
            p = Point((x, y), self.image, (1, -1), color)
            self.move_points_bl.add(p)

            y = random.randint(monitor_h // 2, monitor_h)
            x = random.randint(monitor_w // 2, monitor_w)
            p = Point((x, y), self.image, (-1, -1), color)
            self.move_points_br.add(p)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
            self.move_points_tl.update()
            self.move_points_tr.update()
            self.move_points_bl.update()
            self.move_points_br.update()

            self.surface.fill((255, 255, 255))
            self.move_points_tl.draw(surface=self.surface)
            self.move_points_tr.draw(surface=self.surface)
            self.move_points_bl.draw(surface=self.surface)
            self.move_points_br.draw(surface=self.surface)

            pygame.display.flip()
            self.clock.tick(60)


def main():
    img = Image()
    game = Game(img)
    game.run()
    return 0


if __name__ == '__main__':
    exit(main())
