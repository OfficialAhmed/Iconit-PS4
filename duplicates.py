
'''
    Repeated code will be stored here as functions
    To minimize code structure

'''
class html:
    def __init__(self) -> None:
        self.start = "<html><head/><body>"
        self.end = "</p></body></html>"

    def a_tag(self, href: str, txt: str, color: str, size: int, align="center") -> str:
        ##############################################
        ####             HTML link
        ##############################################
        return f'{self.start}<p align="{align};"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color};">{txt}</span></a>{self.end}'

    def span_tag(self, txt: str, color: str, size: int, align="center", weight=700) -> str:
        ##############################################
        ####             HTML Text
        ##############################################
        return f'{self.start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color};">{txt}</span>{self.end}'