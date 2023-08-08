# Document Interface
class Document:
    def __init__(self):
        self.content = ""

    def set_title(self, title):
        pass

    def add_heading(self, heading):
        pass

    def add_paragraph(self, paragraph):
        pass

    def get_document(self):
        return self.content

# Concrete Document: PDF Document
class PDFDocument(Document):
    def set_title(self, title):
        self.content += f"PDF Title: {title}\n"

    def add_heading(self, heading):
        self.content += f"PDF Heading: {heading}\n"

    def add_paragraph(self, paragraph):
        self.content += f"PDF Paragraph: {paragraph}\n"

# Concrete Document: HTML Document
class HTMLDocument(Document):
    def set_title(self, title):
        self.content += f"<h1>{title}</h1>\n"

    def add_heading(self, heading):
        self.content += f"<h2>{heading}</h2>\n"

    def add_paragraph(self, paragraph):
        self.content += f"<p>{paragraph}</p>\n"

# Concrete Document: Plain Text Document
class PlainTextDocument(Document):
    def set_title(self, title):
        self.content += f"PLAIN TEXT Title: {title}\n"

    def add_heading(self, heading):
        self.content += f"PLAIN TEXT Heading: {heading}\n"

    def add_paragraph(self, paragraph):
        self.content += f"PLAIN TEXT Paragraph: {paragraph}\n"

# Document Builder
class DocumentBuilder:
    def __init__(self):
        self.document = None

    def create_document(self):
        self.document = Document()

    def set_title(self, title):
        self.document.set_title(title)

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document.get_document()

# Example usage
if __name__ == "__main__":
    builder = DocumentBuilder()

    # Create PDF Document
    builder.create_document()
    builder.set_title("Sample PDF Document")
    builder.add_heading("Introduction")
    builder.add_paragraph("This is a sample PDF document.")
    pdf_document = builder.get_document()

    # Create HTML Document
    builder.create_document()
    builder.set_title("Sample HTML Document")
    builder.add_heading("Introduction")
    builder.add_paragraph("This is a sample HTML document.")
    html_document = builder.get_document()

    # Create Plain Text Document
    builder.create_document()
    builder.set_title("Sample Plain Text Document")
    builder.add_heading("Introduction")
    builder.add_paragraph("This is a sample plain text document.")
    plain_text_document = builder.get_document()

    print("PDF Document:")
    print(pdf_document)
    print("HTML Document:")
    print(html_document)
    print("Plain Text Document:")
    print(plain_text_document)
