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
        """This function can override the topleft coordinates params from __init__()"""
        self.center = center
    
    def set_border_radius(self, border_radius: int) -> None:
        """This function sets border radius of the button"""
        self.border_radius = border_radius

    def change_color(self, color, default: bool = False) -> None:
        """This function changes background color of the button"""
        self.color = color
        if default:
            self.default_color = color

    def add_shadow(self, color, offset_x: int, offset_y: int, permanent: bool) -> None:
        """This function sets button's shadow"""
        self.shadow_color = color
        self.shadow_offset_x = offset_x
        self.shadow_offset_y = offset_y
        self.permanent_shadow = permanent

    def generate_shadow(self) -> pygame.rect.Rect:
        """This functions returns the button's shadow rectangle as an instance of the class Rect"""
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
        """This functions returns the button's rectangle as an instance of the class Rect"""
        result = pygame.rect.Rect(self.topleft_x, self.topleft_y, self.width, self.height)
        if self.center:
            result.center = self.center
        return result

class ButtonLabel:
    def __init__(self):
        self.font = None
        self.text = None
    
    def set_label(self, font: str, text: str, size: int, color, bold: bool = False) -> None:
        """This function sets text label of the button"""
        self.font = pygame.font.SysFont(font, size, bold)
        self.text = self.font.render(text, True, color)

class ButtonHover:
    def __init__(self):
        self.cursor = None
        self.color = None
    
    def set_effects(self, color, cursor=pygame.SYSTEM_CURSOR_HAND) -> None:
        """This function sets the hover effects of the button"""
        self.color = color
        self.cursor = cursor

    def effects(self, switch: bool, target: ButtonRect) -> None:
        """This function applies the hover effects of the button"""
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
        """This function renders the entire button into the page, without updating the screen."""
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

    def is_hovered(self) -> bool:
        """This function returns whether user is hovering over the button."""
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
        """This function returns whether user has clicked the button."""
        if self.is_hovered() and pygame.mouse.get_pressed()[0]:
            self.hover.effects(False, self.rect)
            return True
        else:
            return False

class Input:
    def __init__(self, surface, sizes: tuple((int, int)), topleft_coords: tuple((int, int)), background_color, focus_color, font_family: str, font_size: int, font_color, max_characters: int = -1, default_text: str = ""):
        self.surface = surface
        self.sizes = sizes
        self.topleft_coords = topleft_coords
        self.center_coords = None
        self.default_background_color = background_color
        self.background_color = background_color
        self.focus_color = focus_color
        self.font = pygame.font.SysFont(font_family, font_size)
        self.font_color = font_color
        self.max_characters = max_characters
        if max_characters > -1 and len(default_text) > max_characters:
            raise Exception("Chosen default_text has more characters then max_characters")
        else:
            self.default_text_value = default_text
            self.text_value = default_text
        self.is_focused = False

    def center_pos_override(self, center: tuple((int, int))) -> None:
        """This function can override the topleft_coords param from __init__()"""
        self.center_coords = center

    def generate_rect(self) -> pygame.rect.Rect:
        """This functions returns the input's rectangle as an instance of the class Rect"""
        result = pygame.rect.Rect(self.topleft_coords[0], self.topleft_coords[1], self.sizes[0], self.sizes[1])
        if self.center_coords:
            input_rect.center = self.center_coords 
        return result

    def render(self) -> None:
        """This function renders the entire input field into the page, without updating the screen."""
        input_rect = self.generate_rect()
        pygame.draw.rect(self.surface, self.background_color, input_rect)
        if self.text_value == self.default_text_value:
            input_text = self.font.render(self.text_value, True, (100, 100, 100))
        else:
            input_text = self.font.render(self.text_value, True, self.font_color)
        input_text_rect = input_text.get_rect()
        input_text_rect.center = input_rect.center
        self.surface.blit(input_text, input_text_rect)
 
    def watch_typing(self, event) -> None:
        """This function watches when user is focused to the input and typing and updates the input data.\nIt has to be used in a while loop within the for loop detecting events"""
        mouse_pos = pygame.mouse.get_pos()
        input_rect = self.generate_rect()
        if mouse_pos[0] >= input_rect.left and mouse_pos[0] <= input_rect.right and mouse_pos[1] >= input_rect.top and mouse_pos[1] <= input_rect.bottom and pygame.mouse.get_pressed()[0]:
            self.is_focused = True
            self.background_color = self.focus_color
        elif pygame.mouse.get_pressed()[0]:
            self.is_focused = False
            self.background_color = self.default_background_color
        if self.is_focused and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text_value = self.text_value[:-1]
            elif self.max_characters > -1 and len(self.text_value) < self.max_characters:
                if self.text_value == self.default_text_value:
                    self.text_value = ""
                self.text_value += event.unicode
