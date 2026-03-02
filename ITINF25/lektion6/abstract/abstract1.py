# Rubriker och stycken
class MiniGendoc:
    def __init__(self):
        self.parts = []

    def add_header(self, header):
        self.parts.append(("HEADER", header))

    def add_paragraph(self, paragraph):
        self.parts.append(("PARAGRAPH", paragraph))


class Markdown(MiniGendoc):
    def render():
        result = ""
        for part in self.parts:
            result += part + "\n"

        return result


md = Markdown()
md.add_header("Why Python?")
md.add_paragraph("Python is very very good")
