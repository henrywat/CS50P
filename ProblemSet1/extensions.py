def get_media_type(file_extension):

    if file_extension.endswith("gif"):
        return 'image/gif'
    elif file_extension.endswith("jpg"):
        return 'image/jpeg'
    elif file_extension.endswith("jpeg"):
        return 'image/jpeg'
    elif file_extension.endswith("png"):
        return 'image/png'
    elif file_extension.endswith("pdf"):
        return 'application/pdf'
    elif file_extension.endswith("txt"):
        return 'text/plain'
    elif file_extension.endswith("zip"):
        return 'application/zip'
    else:
        return 'application/octet-stream'

filename = input("File name: ").lower().strip()
print(get_media_type(filename))