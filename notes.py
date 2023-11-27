    # def _check_rects_edges(self):
    #     while not self.rectangle.rect.x:
    #         if self.rectangle.rect.y == 0 or self.rectangle.rect.y == self.settings.screen_height:
    #             self.rectangle.rect.x -= self.settings.rects_drop_speed
    #             self.settings.rects_direction *= -1
    #             break
    #     # self.rectangle.update()
    #     # else:
    #         # self.rectangle.update()
    # # def _change_rects_direction(self):
        

    def _check_rects_edges(self):
        while not self.rectangle.rect.x:
            # if self.rectangle.rect.y == 0 or self.rectangle.rect.y == self.settings.screen_height:
            if self.rectangle._check_edges():
                self._change_rects_direction()
            else:
                self.rectangle.update()

        # self.rectangle.update()
        # else:
            # self.rectangle.update()

    
    def _change_rects_direction(self):
                self.rectangle.rect.x -= self.settings.rects_drop_speed
                self.settings.rects_direction *= -1
        