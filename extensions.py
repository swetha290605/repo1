file_name=input("File name: ")
file_name=file_name.split(".")
ext=file_name[1]
ext=ext.lower()
if ext=="jpg" or ext=="jpeg" or ext=="gif" or ext=="png":
    print("image/"+ext)
elif ext=="pdf" or ext=="zip":
    print("application/"+ext)
elif ext=="txt":
    print("text/plain")
else:
    print("application/octet-stream")
