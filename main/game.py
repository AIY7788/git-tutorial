
import pygame
import random
import sys

# ----- SETTINGS -----
WIDTH, HEIGHT = 800, 600
FPS = 80
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (255, 255, 255)
ENEMY_COLOR = [(255, 0, 255),(255, 0, 0),(0, 255, 255),(50, 250, 50),(255,255,0)]

# ----- INIT -----
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")
clock = pygame.time.Clock()

# ----- CLASS PLAYER -----
class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 6
        

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, self.width, self.height))

# ----- CLASS ENEMY -----
class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(3, 6)
        self.l = random.choice(ENEMY_COLOR)

    def update(self):
        self.y += self.speed

    def draw(self):
        
        pygame.draw.rect(screen, self.l, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y > HEIGHT

    def collide_with(self, player):
        return (
            self.x < player.x + player.width and
            self.x + self.width > player.x and
            self.y < player.y + player.height and
            self.y + self.height > player.y
        )

# ----- MAIN GAME LOOP -----
def main():
    player = Player()
    enemies = []
    score = 0
    font = pygame.font.SysFont(None, 36)
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # --- EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- MOVE PLAYER ---
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw()

        # --- SPAWN ENEMIES ---
        if random.randint(1, 30) == 5:
            enemies.append(Enemy())

        # --- UPDATE ENEMIES ---
        for enemy in enemies[:]:
            enemy.update()
            enemy.draw()

            if enemy.collide_with(player):
                print("Game Over!")
                running = False

            if enemy.off_screen():
                enemies.remove(enemy)
                score += 1
        if score >=100 and score < 200:
            enemy.speed = random.randint(4, 7)

        elif score >=200 and score < 300:
            enemy.speed = random.randint(5, 8)

        elif score >=300 and score < 400:
            enemy.speed = random.randint(6, 9)

        elif score >=400 :
            enemy.speed = random.randint(10 ,14)

        # --- DRAW SCORE ---
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (360, 10))

        # --- UPDATE DISPLAY ---
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()