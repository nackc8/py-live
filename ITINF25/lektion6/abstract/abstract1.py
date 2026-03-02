# Rubriker och stycken
class MiniGendoc:
    def __init__(self):
        self.parts = []

    def add_header(self, header):
        self.parts.append(("HEADER", header))

    def add_paragraph(self, paragraph):
        self.parts.append(("PARAGRAPH", paragraph))

    def __str__(self):
        lst = [part_content for part_type, part_content in self.parts]
        return " ".join(lst)


doc = MiniGendoc()
doc.add_header("Why Python?")
doc.add_paragraph("Python is very very good")
print(doc)
