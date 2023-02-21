import tkinter.filedialog

def importFile(fileType : str, fileOpenType : str, writeText=""):
    if fileType != "html" and fileType != "txt":
        raise TypeError("Devi inserire come tipo di file 'html' o 'txt'")
    elif fileOpenType != "r" and fileOpenType != "w":
        raise TypeError("Devi inserire come apertura del file 'r' o 'w'")
    pathFile = tkinter.filedialog.askopenfilename(title=f"Chose {fileType.upper()} file", filetypes=[(f"{fileType.upper()} files", f"*.{fileType.lower()}")])
    return openFile(pathFile, fileOpenType, writeText)

def openFile(pathFile : str, fileOpenType : str, writeText=""):
    if fileOpenType != "r" and fileOpenType != "w":
        raise TypeError("Devi inserire come apertura del file 'r' o 'w'")
    try:
        open(pathFile, fileOpenType, encoding="utf-8", errors="ignore")
    except FileExistsError:
        raise TypeError("File non esistente")
    except:
        raise TypeError("Errore generico")
    finally:
        if fileOpenType == "r":
            with open(pathFile, fileOpenType, encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
            return lines
        else:
            f = open(pathFile, fileOpenType, encoding="utf-8", errors="ignore")
            f.write(writeText)
            return