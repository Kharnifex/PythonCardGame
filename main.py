import pygame
pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("testing this atm")

black = 0, 0, 0

card = pygame.image.load("assets//cardlol.png")
cardrect = card.get_rect()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(black)
        WIN.blit(card, cardrect)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
