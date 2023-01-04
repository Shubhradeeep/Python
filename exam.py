def countline():
    file=open('test1.txt','r')
    line=file.readline()
    c=0
    for i in line:
        c=c+1
    print("total number of line",c)
    flie.close()
countline()
