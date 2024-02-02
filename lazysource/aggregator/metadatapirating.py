from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")

meta = reader.metadata

print(len(reader.pages))

# All of the following could be None!
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)

if __name__ == "__main__":
    reader = PdfReader("example.pdf")

    meta = reader.metadata

    print(len(reader.pages))

    # All of the following could be None!
    print(meta.author)
    print(meta.creator)
    print(meta.producer)
    print(meta.subject)
    print(meta.title)