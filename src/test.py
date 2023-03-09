import asyncio
import searchKeyword

asyncio.run(searchKeyword.htmlURLGeneratorList(
    ["https://www.repubblica.it", "https://www.corriere.it"], ["class=", "img", "<a"]))
