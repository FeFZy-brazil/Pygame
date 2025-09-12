import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela
WIDTH, HEIGHT = 1000, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela com Imagem")

# Definindo a cor de fundo
BG_Color = (30, 30, 40) # Cor escura

# Carregar a imagem
imagem_file ="GAME\player.png" # Calma paê
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha() # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #Centralizar a imagem
else: 
    print("imagem não encontrada!")

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo
    screen.fill(BG_Color)

    # Desenhar a imagem na tela
    screen.blit(img, img_rect)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
