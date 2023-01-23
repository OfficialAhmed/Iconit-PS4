class Widget:
    """ Sharable pointers for ui widgets, to access them anywhere """
    ip_label = None
    ip_input = None
    CacheBar = None
    port_input = None
    port_label = None
    mode_label = None
    cache_label = None
    StatusLabel = None
    GameIconsRadio = None

    def __init__(self) -> None:
        pass
    
    def set_cache_bar(self, ptr):
        Widget.CacheBar = ptr

    def get_cache_bar(self):
        return Widget.CacheBar

    def set_ip_label(self, ptr):
        Widget.ip_label = ptr

    def get_ip_label(self):
        return Widget.ip_label

    def set_port_label(self, ptr):
        Widget.port_label = ptr

    def get_port_label(self):
        return Widget.port_label

    def set_mode_label(self, ptr):
        Widget.mode_label = ptr

    def get_mode_label(self):
        return Widget.mode_label

    def set_cache_label(self, ptr):
        Widget.cache_label = ptr

    def get_cache_label(self):
        return Widget.cache_label

    def set_ip_input(self, ptr):
        Widget.ip_input = ptr
        
    def get_ip_input(self):
        return Widget.ip_input

    def set_port_input(self, ptr):
        Widget.port_input = ptr

    def get_port_input(self):
        return Widget.port_input

    def set_status_label(self, ptr):
        Widget.StatusLabel = ptr

    def get_status_label(self):
        return Widget.StatusLabel

    def set_game_icon_radio(self, ptr):
        Widget.GameIconsRadio = ptr

    def get_game_icon_radio(self):
        return Widget.GameIconsRadio