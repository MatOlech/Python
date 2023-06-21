def files():
    ext = input("File:").split(".")
    exte = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }
    if ext[1] in exte:
        print(exte[ext[1]])
    else:
        print("application/octet-stream")

def main():
    files()

main()


