import xml.etree.ElementTree as ET

with open("lists.asmx.xml", "r") as read:
    text = '\n'.join(read.readlines())
    begins = text.split("DefaultViewUrl=\"")
    urls = []
    for begin in begins:
        t = begin.split("\" ID")[0].replace(" Mobile", "").replace("\"","").replace("\n","")
        if len(t) > 0:
            urls.append(f"https://portal.mpsd.ca{t}")

    print('\n'.join(urls))