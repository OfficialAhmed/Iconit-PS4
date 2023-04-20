from Module.Constant.Constants import Constants as Constant

class Html:
    def __init__(self) -> None:
        self.__start = "<html><head/><body>"
        self.__end = "</p></body></html>"
        self.__constant = Constant()


    def p_tag(self, cstm_style, txt=None) -> str:
        """  generate Paragraph """
        return f'<p align="center" style="{cstm_style}">{txt}</p>'


    def a_tag(self, href:str, txt:str, color:str, size:int, cstm_style: str = "", align: str = "center", font="Arial") -> str:
        """  generate Link """
        return f'{self.__start}<p align="{align}"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}; font-family: {font}">{txt}</span></a>{self.__end}'
        

    def span_tag(self, txt:str, color:str, size:int, align:str = "center", weight = 700, font="Arial") -> str:
        """  generate Text """
        return f'{self.__start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color}; font-family: {font}">{txt}</span>{self.__end}'


    def tooltip_tag(self, txt:str) -> str:
        return f"<p style='color:Black'>{txt}</p>"


    def bg_image(self, url:str) -> str:
        return f"background-image: url({url});"


    def border_image(self, url:str) -> str:
        return f"border-image: url({url});"


    def internal_log_msg(self, state, msg, size=10, custome_style="") -> str:
        """ generate a logging line as <p> tag"""
        color = {
            "error":self.__constant.get_color("red"),
            "warning":self.__constant.get_color("orange"),
            "success":self.__constant.get_color("green"),
            "ps4":self.__constant.get_color("white")
        }

        style = f"margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:{size}pt; color:{color[state]}; {custome_style}"
        return self.p_tag(style, f"[{state.upper()}] : {msg}")
    
    
    def caution_p_tag(self, clr):
        return f"<p align='center' style=' margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;'><span style=' font-size:9pt; font-weight:600; color:{clr};'>"

    def caution_msg_2(self, clr):
        return f"<p align='center' style='-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:{clr};'>"