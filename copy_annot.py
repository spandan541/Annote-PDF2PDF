import fitz
red = (1, 0, 0)
def print_descr(annot):
    """Print a short description to the right of each annot rect."""
    annot.parent.insert_text(
        annot.rect.br + (10, -5), "%s annotation" % annot.type[1], color=red
    )

def main():
    src = fitz.open("input.pdf")
    dest = fitz.open("output.pdf")
    pagesrc = src[0]
    pagedes = dest[0]
    annot = pagesrc.firstAnnot

    while annot:
        if annot.type[0] in (8, 9, 10, 11): # one of the 4 types above
            print(len(annot.vertices))
            i=0
            j=4
            while j<=len(annot.vertices):
                rect = fitz.Quad(annot.vertices[i:j])
                print(rect)
                pagedes.addHighlightAnnot(rect)
                i=i+4
                j=j+4
        annot=annot.next
    #dest.saveIncr() #to save in original file
    dest.save("output1.pdf") #to save in new file
if __name__=="__main__":
    main()