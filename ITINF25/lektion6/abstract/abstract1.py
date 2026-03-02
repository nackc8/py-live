# Rubriker och stycken
class MiniGendoc:
    def __init__(self):
        self.parts = []

    def add_header(self, header):
        self.parts.append(("HEADER", header))

    def add_paragraph(self, paragraph):
        self.parts.append(("PARAGRAPH", paragraph))


class Markdown(MiniGendoc):
    def render(self):
        result = ""
        for part in self.parts:
            # Som nedan fast kortare med unpacking: part_type, part_content = part
            part_type = part[0]
            part_content = part[1]
            if part_type == "HEADER":
                result += "# " + part_content + "\n" * 2
            else:
                result += part_content + "\n"

        return result


md = Markdown()
md.add_header("Why Python?")
md.add_paragraph("Python is very very good")
rendered_result = md.render()

print("rendered_result")
print(rendered_result)
