import fileOpenTkinter
import asyncio
import urllib.request

# Estrarre il body del file HTMl per togliere tutte le informazioni inutili
def extractBody(lines: list):
    for line in lines:
        if "<body" in line:
            start = lines.index(line)
        elif "</body>" in line:
            end = lines.index(line)
    return lines[start:end]

#Conteggio della parola chiave all'interno di ogni riga
def countKeywords(body: list, keywords: str):
    lines = list(filter(lambda x: keywords in x, body))
    return sum(list(map(lambda x: x.count(keywords), lines)))

#Generatore del testo che verrà scritto nel file di output
def textGenerator(keywords: str, countKeyword: int, input: str):
    return input + "\n" + keywords + ": " + str(countKeyword)

#Funzione finale per chiedere più parole chiavi
def htmlFileGenerator(keywordList : list):
    bodyHtml = extractBody(fileOpenTkinter.importFile("html", "r"))
    text = ""
    for keyword in keywordList:
        text = textGenerator(keyword, countKeywords(bodyHtml, keyword), text)
    fileOpenTkinter.importFile("txt", "w", text)

#Funzione finale per chiedere una parola chiavi
def htmlFileGenerator(keyword : str):
    bodyHtml = extractBody(fileOpenTkinter.importFile("html", "r"))
    text = ""
    text = textGenerator(keyword, countKeywords(bodyHtml, keyword), text)
    fileOpenTkinter.importFile("txt", "w", text)

async def htmlURLGenerator(url : str, keywords):
    req = urllib.request.urlopen(url)
    html = req.read().decode(req.headers.get_content_charset())
    text = ""
    if type(keywords) == list:
        for keyword in keywords:
            text = textGenerator(keyword, html.count(keyword), text)
    else:
        text = textGenerator(keywords, html.count(keywords), text)
    fileOpenTkinter.importFile("txt", "w", text)

async def htmlURLGeneratorList(urls : list, keywords):
    tasks = [asyncio.create_task(htmlURLGenerator(url, keywords))for url in urls]
    result = asyncio.gather(*tasks)