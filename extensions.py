def main ():
    filename = input("File Name:")
    if ('.' not in filename):
        filetype = "void"
    else:
        filetype = ("".join(filename.split())).split('.')[-1]


    extensions(filetype.casefold())

def extensions(filetype):
    match filetype:
        case "jpeg" | "jpg"| "png":
            print("image/"+ filetype)
        case "zip" | "pdf":
            print("application/"+ filetype)
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

main ()