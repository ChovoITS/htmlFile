import fileOpenTkinter


def extractBody(lines: list):
    for line in lines:
        if "<body" in line:
            start = lines.index(line)
        elif "</body>" in line:
            end = lines.index(line)
    return lines[start:end]

def countKeywords(body: list, keywords: str):
    lines = list(filter(lambda x: keywords in x, body))
    return sum(list(map(lambda x: x.count(keywords), lines)))

def textGenerator(keywords: str, countKeyword: int, input: str):
    return input + "\n" + keywords + ": " + str(countKeyword)

def htmlFileGenerator(keywordList : list):
    bodyHtml = extractBody(fileOpenTkinter.importFile("html", "r"))
    text = ""
    for keyword in keywordList:
        text = textGenerator(keyword, countKeywords(bodyHtml, keyword), text)
    fileOpenTkinter.importFile("txt", "w", text)

def htmlFileGenerator(keyword : str):
    bodyHtml = extractBody(fileOpenTkinter.importFile("html", "r"))
    text = ""
    text = textGenerator(keyword, countKeywords(bodyHtml, keyword), text)
    fileOpenTkinter.importFile("txt", "w", text)