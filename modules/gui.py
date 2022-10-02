import pygame

class ButtonRect:
    def __init__(self, topleft_x: int, topleft_y: int, width: int, height: int, color):
        self.topleft_x = topleft_x
        self.topleft_y = topleft_y
        self.width = width
        self.height = height
        self.default_color = color
        self.color = color
        self.border_radius = -1
        self.center = None
        self.shadow_color = None
        self.shadow_offset_x = None
        self.shadow_offset_y = None
        self.permanent_shadow = None

    def center_pos_override(self, center: tuple((int, int))) -> None:
        self.center = center
    
    def set_border_radius(self, border_radius: int) -> None:
        self.border_radius = border_radius

    def change_color(self, color, default: bool = False) -> None:
        self.color = color
        if default:
            self.default_color = color

    def add_shadow(self, color, offset_x: int, offset_y: int, permanent: bool) -> None:
        self.shadow_color = color
        self.shadow_offset_x = offset_x
        self.shadow_offset_y = offset_y
        self.permanent_shadow = permanent

    def generate_shadow(self) -> pygame.rect.Rect:
        if self.shadow_color:
            result = pygame.rect.Rect(self.topleft_x+self.shadow_offset_x, self.topleft_y+self.shadow_offset_y, self.width, self.height)
            if self.center:
                result.center = self.center
                result.x += self.shadow_offset_x
                result.y += self.shadow_offset_y
            return result
        else:
            raise Exception("Called generate_shadow() without using the add_shadow() method")
    
    def generate_rect(self) -> pygame.rect.Rect:
        result = pygame.rect.Rect(self.topleft_x, self.topleft_y, self.width, self.height)
        if self.center:
            result.center = self.center
        return result

class ButtonLabel:
    def __init__(self):
        self.font = None
        self.text = None
    
    def set_label(self, font: str, text: str, size: int, color, bold: bool = False) -> None:
        self.font = pygame.font.SysFont(font, size, bold)
        self.text = self.font.render(text, True, color)

class ButtonHover:
    def __init__(self):
        self.cursor = None
        self.color = None
    
    def set_effects(self, color, cursor=pygame.SYSTEM_CURSOR_HAND) -> None:
        self.color = color
        self.cursor = cursor

    def effects(self, switch: bool, target: ButtonRect) -> None:
        if switch:
            if self.color:
                target.change_color(self.color)
                pygame.mouse.set_cursor(self.cursor)
            else:
                raise Exception("Called effects() with switch=True without using the set_effects() method")
        else:
            target.change_color(target.default_color)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

class Button:
    def __init__(self, surface, topleft_x: int, topleft_y: int, width: int, height: int, rect_color):
        self.surface = surface
        self.rect = ButtonRect(topleft_x, topleft_y, width, height, rect_color)
        self.label = ButtonLabel()
        self.hover = ButtonHover()

    def render(self, with_shadow:bool=False) -> None:
        if with_shadow and not self.rect.shadow_color:
            raise Exception("Called render() with with_shadow=True without declaring the shadow using the add_shadow() method")
        elif self.rect.permanent_shadow or (with_shadow and self.rect.shadow_color):
            shadow = self.rect.generate_shadow()
            pygame.draw.rect(self.surface, self.rect.shadow_color, shadow, 0, self.rect.border_radius)
        rect_to_render = self.rect.generate_rect()
        pygame.draw.rect(self.surface, self.rect.color, rect_to_render, 0, self.rect.border_radius)
        if self.label.text:
            text_rect = self.label.text.get_rect()
            text_rect.center = rect_to_render.center
            self.surface.blit(self.label.text, text_rect)
        # pygame.display.update()

    def is_hovered(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        rect_to_check = self.rect.generate_rect()
        if mouse_pos[0] >= rect_to_check.left and mouse_pos[0] <= rect_to_check.right and mouse_pos[1] >= rect_to_check.top and mouse_pos[1] <= rect_to_check.bottom:
            if self.hover.color:
                self.hover.effects(True, self.rect)
            if self.rect.permanent_shadow == False and self.rect.permanent_shadow != None:
                self.render(True)
            else:
                self.render()
            return True
        else:
            self.hover.effects(False, self.rect)
            self.render()
            return False
    
    def is_clicked(self) -> bool:
        if self.is_hovered() and pygame.mouse.get_pressed()[0]:
            self.hover.effects(False, self.rect)
            return True
        else:
            return False
