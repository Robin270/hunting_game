import math, pygame

class Button:
    def __init__(self, label: str, label_color, font: str, surface, rect_color, topleft_x: int, topleft_y: int, width: int, height: int, border_radius: int=-1):
        self.label = label
        self.label_color = label_color
        self.font = pygame.font.SysFont(font, math.floor(height-(height/100*35)))
        self.surface = surface
        self.default_rect_color = rect_color
        self.rect_color = rect_color
        self.rect = pygame.Rect(topleft_x, topleft_y, width, height)
        self.border_radius = border_radius
    
    def render(self):
        pygame.draw.rect(self.surface, self.rect_color, self.rect, 0, self.border_radius)
        text = self.font.render(self.label, True, self.label_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        self.surface.blit(text, text_rect)
    
    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] >= self.rect.left and mouse_pos[0] <= self.rect.right and mouse_pos[1] >= self.rect.top and mouse_pos[1] <= self.rect.bottom:
            return True
        else:
            return False
    
    # def hover_effect(self, color, cursor=pygame.SYSTEM_CURSOR_HAND):
    #     if self.is_hovered():
    #         pygame.mouse.set_cursor(cursor)
    #         self.rect_color = color
    #     else:
    #         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    #         self.rect_color = self.default_rect_color
    #     self.render()
