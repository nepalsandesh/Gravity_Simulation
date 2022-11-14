import pygame

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)


class Simulation:
    
    def __init__(self):
        pygame.init()
        self.width = 1920
        self.height = 1080
        self.resolution = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Gravity Simulation")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
    def draw(self):
        self.screen.fill(black)
        
    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    

        
        
    def run(self): 
        
        ball = pygame.Rect(self.width/2, self.height/2, 80, 80)
        ground = pygame.Rect(0, self.height/1.1, self.width, 50)
        
        ball_velocity = 0
        gravity = 1
                
        while True:
            self.draw()
            self.inputs()
            
            pygame.draw.ellipse(self.screen, yellow, ball)
            pygame.draw.rect(self.screen, white, ground)
            

            if ball.colliderect(ground):
                ball_velocity *= -1
                # print(ball_velocity)
                # ball_velocity = 35
                
            ball.y += ball_velocity
            ball_velocity += gravity
            
                               
        
            print("ball.y: {}, ball_velocity: {}, gravity: {}".format(ball.y, ball_velocity, gravity))
        
            pygame.display.flip()
            self.clock.tick(self.FPS)
            

                
                
                

            
if __name__ == "__main__":
    app = Simulation()
    app.run()