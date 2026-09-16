import mammoth
import sys

def convert_to_html():
    with open("NabiMuhammad.docx", "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
        messages = result.messages
        with open("mammoth_out.html", "w", encoding="utf-8") as f:
            f.write(html)
        if messages:
            print("Messages:")
            for msg in messages:
                print(msg)
        print("Done!")

if __name__ == "__main__":
    convert_to_html()
