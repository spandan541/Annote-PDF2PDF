import fitz

def main():
    src = fitz.open("KuroseCh1-2.pdf")
    dest = fitz.open("James-Kurose-Keith-Ross-Computer-Networking_-A-Top-Down-Approach-7th-Edition.pdf")
    for i in range(176,177):#pages start from 0
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
                    rect.transform(m)
                    pagedes.addHighlightAnnot(rect)
                    i=i+4
                    j=j+4
            annot=annot.next
        #dest.saveIncr() #to save in original file
        dest.save("output1.pdf") #to save in new file
if __name__=="__main__":
    main()