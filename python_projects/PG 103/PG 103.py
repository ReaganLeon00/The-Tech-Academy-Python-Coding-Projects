import sqlite3


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_textFile TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    count = 0
    print("These are the files that end in .txt:")
    for file in fileList:
        if file.endswith ('.txt'):
            count += 1
            print("{}) {}".format(count,file))
            cur.execute("INSERT INTO tbl_fileList(col_textFile) VALUES(?)",(file,))
    conn.commit()
conn.close()
