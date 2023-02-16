import pygame, sys, time, random
from pygame.locals import QUIT


pygame.init()
play_surface = pygame.display.set_mode((500, 500))    # pantalla

fps = pygame.time.Clock()    # frames por segundo
font = pygame.font.Font(None, 30)    # fuente de la letra para mostrar el score

def food():
    random_pos = random.randint(0,49)*10    # posicion aletorio
    food_pos = [random_pos, random_pos]    # coordenadas de la posición de la comida
    return food_pos


def game():
    
    snake_pos = [100, 50]    # posicion inicial
    snake_body = [[100, 50], [90, 50], [80, 50]]    # posiciones de los pixeles del cuerpo

    run = True
    motion = 'RIGHT'
    food_pos = food()
    score = 0
    speed = 10
    
    while run:

        for event in pygame.event.get():    # para cada evento que se obtine de los eventos que transcurren en la pantalla
            if event.type == pygame.QUIT:    # click en X se cierra el juego
                run = False
            if event.type == pygame.KEYDOWN:    # si usamos las felchas
                if event.key == pygame.K_RIGHT:    # si es la flecha de la derecha
                    motion = 'RIGHT'    # mover a la derecha
                if event.key == pygame.K_LEFT:
                    motion = 'LEFT'    # mover a la izquierda
                if event.key == pygame.K_UP:
                    motion = 'UP'    # mover a arriba
                if event.key == pygame.K_DOWN:
                    motion = 'DOWN'    # mover a abajo
        
        if motion == 'RIGHT':
            snake_pos[0] += 10
        if motion == 'LEFT':
            snake_pos[0] -= 10
        if motion == 'UP':
            snake_pos[1] -= 10
        if motion == 'DOWN':
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))    # inserta un pixel en indice 0, desplaza las otras posiciones, con list(snake_pos) creamos una copia de la lista snake_pos original

        # puntaje
        if snake_pos == food_pos:
            food_pos = food()
            score += 1
        else:
            snake_body.pop()    # eliminia en ultimo elemento de la lista
                
        play_surface.fill((0,0,128))    # pantalla negra

        # dibujamos la serpiente
        for pos in snake_body:
            pygame.draw.rect(play_surface, (255,255,0), pygame.Rect(pos[0], pos[1], 10, 10))    # dibuja el cuerpo de la serpiente
        pygame.draw.rect(play_surface, (255,0,0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        text = font.render(str(score),0, (255,255,0))
        play_surface.blit(text, (480,20))
        pygame.display.flip()    # actualiza lo que hacemos

        # dificultad
        if score == 0:
            fps.tick(speed)    # velocidad inicial
        if score > 0 and score % 5 == 0:
            speed += 5
        fps.tick(speed)    

        # salir de la pantalla
        if snake_pos[0] <= 0 or snake_pos[0] >= 500:
            run = False
            print('Game over')
        if snake_pos[1] <= 0 or snake_pos[1] >= 500:
            run = False
            print('Game over')
            
if __name__ == '__main__':
    game()
    pygame.quit()

