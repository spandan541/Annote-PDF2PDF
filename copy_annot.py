import fitz

def main():
    srcpath=input("please enter source pdf path")
    destpath=input("please enter destination pdf path")
    src = fitz.open(srcpath)
    dest = fitz.open(destpath)
    start,end = input("enter start & ending page numbers both inclusive:").split()
    for i in range(start-1,end+1):#pages start from 0
        pagesrc = src[i]
        pagedes = dest[i]
        # print(pagesrc.rect)
        # print(pagedes.rect)
        scaleX=pagedes.rect[2]/pagesrc.rect[2]
        scaleY=pagedes.rect[3]/pagesrc.rect[3]
        m = fitz.Matrix(scaleX,0,0,scaleY,0,0)
        annot = pagesrc.firstAnnot
        while annot:
            if annot.type[0] in (8, 9, 10, 11): # one of the 4 types above
                i=0
                j=4
                while j<=len(annot.vertices):
                    rect = fitz.Quad(annot.vertices[i:j])
                    rect.transform(m)#transforming quad using matrix m
                    pagedes.addHighlightAnnot(rect)
                    i=i+4
                    j=j+4
            annot=annot.next
        #dest.saveIncr() #to save in original file
        dest.save("output.pdf") #to save in new file
if __name__=="__main__":
    main()