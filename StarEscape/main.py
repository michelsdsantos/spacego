import sqlite3  # Importa o módulo para manipular o banco de dados
import pygame
import random
import time
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star Escape")

# Carregando a imagem da nave
player_img = pygame.image.load("assets/player.png").convert_alpha()
player_img = player_img.subsurface((1, 1, player_img.get_width() - 2, player_img.get_height() - 2))

# Se necessário, defina uma cor como transparente
player_img.set_colorkey((0, 0, 0))  # Substitua (0, 0, 0) pela cor exata do fundo, se houver

# Carregando imagens
enemy_img = pygame.image.load("assets/enemy.png").convert_alpha()

# Carregando e ajustando o fundo
background_img = pygame.image.load("assets/background.png").convert()

# Ajusta o fundo para respeitar a largura da tela, mantendo a proporção
background_width = SCREEN_WIDTH
background_height = int(background_img.get_height() * (SCREEN_WIDTH / background_img.get_width()))
background_img = pygame.transform.scale(background_img, (background_width, background_height))

# Variáveis para controlar o movimento do fundo
background_y1 = 0
background_y2 = -background_height  # Segunda cópia do fundo começa fora da tela


# Define uma cor como transparente, se necessário
enemy_img.set_colorkey((0, 0, 0))  # Substitua (0, 0, 0) pela cor exata do fundo, se houver

# Variável para controlar o movimento do fundo
background_y1 = 0
background_y2 = -SCREEN_HEIGHT  # Segunda cópia do fundo começa fora da tela

# Carregando sons
pygame.mixer.init()
pygame.mixer.music.load("assets/background_music.wav")  # Música de fundo
collision_sound = pygame.mixer.Sound("assets/collision_sound.wav")  # Som de colisão

# Fonte para exibir o score e o tempo
font = pygame.font.Font(None, 36)

# Classe do jogador
# Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Aumenta o tamanho da nave em 10%
        self.image = pygame.transform.scale(player_img, (55, 55))  # 10% maior que 50x50
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.speed = 5

        # Reduz a área de toque em 50% (25% de cada lado)
        self.rect = self.rect.inflate(-self.rect.width * 0.5, -self.rect.height * 0.5)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

# Classe do inimigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Aumenta o tamanho dos inimigos em 10%
        self.image = pygame.transform.scale(enemy_img, (55, 55))  # 10% maior que 50x50
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(3, 8)
            global score
            score += 1  # Incrementa o score ao desviar de um inimigo

# Função para exibir a tela final
def show_final_screen():
    pygame.mixer.music.stop()  # Garante que a música pare antes de exibir a tela final
    screen.fill(BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    final_time_text = font.render(f"Time Survived: {elapsed_time}", True, WHITE)
    continue_text = font.render("Press Y to play again or N to quit", True, WHITE)
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    screen.blit(final_time_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 10))
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 30))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # Reiniciar o jogo
                    waiting = False
                if event.key == pygame.K_n:  # Fechar o jogo
                    pygame.quit()
                    exit()

# Ajuste no loop principal do jogo
def main():
    global score, elapsed_time, background_y1, background_y2
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(8):  # Adiciona 8 inimigos
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Variáveis de pontuação e tempo
    score = 0
    start_time = time.time()

    # Inicia a música de fundo
    pygame.mixer.music.play(-1)  # -1 para tocar em loop

    # Loop principal do jogo
    clock = pygame.time.Clock()
    running = True

    while running:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualizações
        all_sprites.update()

        # Detecção de colisão
        if pygame.sprite.spritecollideany(player, enemies):
            pygame.mixer.music.stop()  # Para a música de fundo
            collision_sound.play()  # Toca o som de colisão

            # Solicita o nome do jogador
            name = ""
            waiting_for_name = True
            while waiting_for_name:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and len(name) > 0:
                            waiting_for_name = False
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        elif len(name) < 4 and event.unicode.isalnum():
                            name += event.unicode

                # Exibe a tela para inserir o nome
                screen.fill(BLACK)
                name_text = font.render(f"Enter your name (max 4 chars): {name}", True, WHITE)
                screen.blit(name_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
                pygame.display.flip()

            # Salva o jogador no banco de dados
            save_player_to_db(name, score, elapsed_time)

            # Exibe a tela final com o leaderboard
            show_final_screen_with_leaderboard()
            running = False

        # Calcula o tempo de jogo
        elapsed_time = int(time.time() - start_time)

        # Movimento do fundo
        background_y1 += 2  # Velocidade do fundo
        background_y2 += 2

        # Reposiciona o fundo quando ele sai da tela
        if background_y1 >= SCREEN_HEIGHT:
            background_y1 = background_y2 - background_height
        if background_y2 >= SCREEN_HEIGHT:
            background_y2 = background_y1 - background_height

        # Desenho na tela
        screen.blit(background_img, (0, background_y1))  # Primeira cópia do fundo
        screen.blit(background_img, (0, background_y2))  # Segunda cópia do fundo        
        
        all_sprites.draw(screen)  # Sprites

        # Exibir o score no canto superior esquerdo
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Exibir o tempo no canto superior direito
        time_text = font.render(f"Time: {elapsed_time}", True, WHITE)
        screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

        pygame.display.flip()  # Atualiza a tela

        # Controle de FPS
        clock.tick(FPS)

    # Tela de score final
    show_final_screen_with_leaderboard()


# Função para salvar o jogador no banco de dados
def save_player_to_db(name, score, elapsed_time):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO players (name, score, time)
        VALUES (?, ?, ?)
    """, (name, score, str(elapsed_time)))
    conn.commit()
    conn.close()

# Função para obter os top 3 jogadores
def get_top_players():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, score, time
        FROM players
        ORDER BY score DESC, time ASC
        LIMIT 3
    """)
    top_players = cursor.fetchall()
    conn.close()
    return top_players

# Função para exibir a tela final com os top 3 jogadores
def show_final_screen_with_leaderboard():
    screen.fill(BLACK)

    # Exibe os top 3 jogadores
    top_players = get_top_players()
    leaderboard_text = font.render("Top 3 Players:", True, WHITE)
    screen.blit(leaderboard_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))
    for i, player in enumerate(top_players):
        player_text = font.render(f"{i + 1}. {player[0]} - Score: {player[1]} - Time: {player[2]}", True, WHITE)
        screen.blit(player_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 70 + i * 30))

    # Exibe as opções para continuar ou sair
    continue_text = font.render("Press Y to play again or N to quit", True, WHITE)
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # Reiniciar o jogo
                    waiting = False
                if event.key == pygame.K_n:  # Fechar o jogo
                    pygame.quit()
                    exit()


# Loop principal para reiniciar o jogo
while True:
    main()