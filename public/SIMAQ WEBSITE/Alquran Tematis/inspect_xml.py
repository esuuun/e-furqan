import zipfile

def list_docx_files():
    docx_path = 'Nabi Muhammad ﷺ.docx'
    try:
        with zipfile.ZipFile(docx_path, 'r') as docx_zip:
            for info in docx_zip.infolist():
                print(f"{info.filename} (Size: {info.file_size})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_docx_files()
