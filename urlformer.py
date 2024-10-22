urltemplate = """https://portal.mpsd.ca/Lists/LISTNAME/AllItems.aspx#/=\",
\t\"https://portal.mpsd.ca/LISTNAME/AllItems.aspx#/="""
with open("yuh.txt", "w") as clear:
    clear.write("")
with open("yuh.txt", "a") as write:
    write.write("[")
    with open("urllistnames.txt","r") as read:
        for line in read.readlines():
            write.write("\t\"" + urltemplate.replace("LISTNAME", line.replace("\n", "")) + "\",\n")
    write.write("""].forEach(url=>{
    window.open(url);
});""")