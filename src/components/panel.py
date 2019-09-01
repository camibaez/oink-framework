import component

class Panel(component.Component):
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        super(Panel, self).__init__((x, y), (width, height))
        Panel.graphicInit(self)
        
    def graphicInit(self):
        self.__opaque = True
        self.__layout = None
        self.__color = (0, 0, 0)
        self.__imagen = None
        
        self.fill(self.color)

    
    def get_opaque(self):
        return self.__opaque
    def get_layout(self):
        return self.__layout
    def get_color(self):
        return self.__color
    def get_imagen(self):
        return self.__imagen

    def set_opaque(self, value):
        self.__opaque = value
        color = self.color if value else (0, 0 ,0 ,0)
        self.fill(color)
        if value:
            self.blit(self.imagen, (0, 0))
    def set_layout(self, value):
        self.__layout = value
        value.parent = self
    def set_color(self, c):
        self.__color = c
        if self.opaque:
            self.fill(c)
    def set_imagen(self, i):
        self.blit(i, (0,0))
        self.__imagen = i

    opaque = property(get_opaque, set_opaque)
    layout = property(get_layout, set_layout)
    color = property(get_color, set_color)
    imagen = property(get_imagen, set_imagen)
        