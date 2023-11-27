class Game_Stats:
    def __init__(self, sis):
        self.settings = sis.settings
        self.reset_ship()
        self.game_active = False
    
    def reset_ship(self):
        self.ships_left = self.settings.ship_limit

        
        