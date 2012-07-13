import tiledtmxloader, pygame

class Enemy(tiledtmxloader.helperspygame.SpriteLayer.Sprite):

    class Waypoints():
        def __init__(self):
            self.waypoints = []
            self.current_waypoint = 0

        def add_waypoint(self, x, y, nr):
            self.waypoints.append((x, y, nr))
            
        def next_waypoint(self):
            self.current_waypoint += 1
            if(len(self.waypoints) == self.current_waypoint):
               self.current_waypoint = 0

        def get_mission_possition(self, position):
            (waypoint_x, waypoint_y, nr) = self.waypoints[self.current_waypoint]
            (position_x, position_y) = position
            if(position_x == waypoint_x and position_y == waypoint_y):
                self.next_waypoint()    
            return self.waypoints[self.current_waypoint]

        def init(self):
            self.waypoints = sorted(self.waypoints, key=lambda waypoint: waypoint[2])


    def __init__(self, screen):
        self.waypoints = self.Waypoints()
        self.position = (0, 0)
        self.speed = 4
        self.screen = screen

    def set_sprite(self, image_location):
        image = pygame.image.load(image_location)
        tiledtmxloader.helperspygame.SpriteLayer.Sprite.__init__(self, image, image.get_rect())

    def add_waypoint(self, (x, y, nr)):
        self.waypoints.add_waypoint(x, y, nr)

    def update(self, deltat):
        (waypoint_x, waypoint_y, nr) = self.waypoints.get_mission_possition(self.position)
        (position_x, position_y) = self.position
        if(position_x != waypoint_x):
            if(position_x < waypoint_x):
                position_x += self.speed
            else :
                position_x -= self.speed
        if(position_y != waypoint_y):
            if(position_y < waypoint_y):
                position_y += self.speed
            else:
                position_y -= self.speed
        self.position = (position_x, position_y)
        
    def draw(self):
        (x, y) = self.position
        self.screen.blit(self.image, (x, y))

    def init(self):
        self.waypoints.init()
        (x, y, nr) = self.waypoints.get_mission_possition((0, 0))
        self.position = (x, y)