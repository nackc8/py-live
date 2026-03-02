from abc import ABC, abstractmethod

# https://docs.python.org/3/library/abc.html


# Rubriker och stycken
# ABC gör klassen abstrakt = man får INTE göra instanser av den
class MiniGendoc(ABC):
    def __init__(self):
        self.parts = []

    def add_header(self, header):
        self.parts.append(("HEADER", header))

    def add_paragraph(self, paragraph):
        self.parts.append(("PARAGRAPH", paragraph))

    # Tvinga underklasserna att implementera render!
    @abstractmethod
    def render(self):
        pass


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


class Html(MiniGendoc):
    def render(self):
        result = ""
        for part in self.parts:
            # Som nedan fast kortare med unpacking: part_type, part_content = part
            part_type = part[0]
            part_content = part[1]
            if part_type == "HEADER":
                result += "<h1>" + part_content + "</h1>" + "\n" * 2
            else:
                result += "<p>" + part_content + "</p>" + "\n"

        return result


md = MiniGendoc()
md.add_header("Why Python?")
md.add_paragraph("Python is very very good")
rendered_result = md.render()

print("Rendered_result:")
print(rendered_result)
