

# ver1.0 不支持嵌套

class Structer(object):
    def __init__(self, src_string):
        self.src_str = src_string

    def start_analy(self):
        lines = self.src_str.split('\n|\r');
        for s_line in lines:
            s_line