import fitz

def make_text(words):
    """Return textstring output of getText("words").
    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
    line_dict = {}  # key: vertical coordinate, value: list of words
    words.sort(key=lambda w: w[0])  # sort by horizontal coordinate
    for w in words:  # fill the line dictionary
        y1 = round(w[3], 1)  # bottom of a word: don't be too picky!
        word = w[4]  # the text of the word
        line = line_dict.get(y1, [])  # read current line content
        line.append(word)  # append new word
        line_dict[y1] = line  # write back to dict
    lines = list(line_dict.items())
    lines.sort()  # sort vertically
    return "\n".join([" ".join(line[1]) for line in lines])

def main():
    srcpath=input("please enter source pdf path")
    destpath=input("please enter destination pdf path")
    src = fitz.open(srcpath)
    dest = fitz.open(destpath)
    start,end = input("enter start & ending page numbers both inclusive:").split()
    for i in range(start-1,end+1):#pages start from 0
        pagesrc = src[i]
        pagedes = dest[i]
        words = pagesrc.getText("words")
        annot = pagesrc.firstAnnot
        while annot:
            if annot.type[0] in (8, 9, 10, 11): # one of the 4 types above
                i=0
                j=4
                while j<=len(annot.vertices):
                    rect = fitz.Quad(annot.vertices[i:j]).rect
                    mywords = [w for w in words if fitz.Rect(w[:4]).intersect(rect)]
                    search = make_text(mywords)
                    print(search)
                    quads = pagedes.search_for(search, quads=True)
                    pagedes.addHighlightAnnot(quads)
                    i=i+4
                    j=j+4
            annot=annot.next
        #dest.saveIncr() #to save in original file
        dest.save("output.pdf") #to save in new file
if __name__=="__main__":
    main()