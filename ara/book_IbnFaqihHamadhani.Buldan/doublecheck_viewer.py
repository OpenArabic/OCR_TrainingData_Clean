import os, shutil

folder = "./ara/book_IbnFaqihHamadhani.Buldan/5_goldStandard/"

htmlTop = """

<!DOCTYPE html>
<html>

<head>
  <title>fileName</title>

  <meta charset="UTF-8">
  <meta name="description" content="Reviewing OCR Training/Testing Data">
  <meta name="keywords" content="HTML">
  <meta name="author" content="Open ITI Corpus Team">

  <link href='http://fonts.googleapis.com/earlyaccess/amiri.css' rel='stylesheet' type='text/css'>
  
    <style>
      body {background-color: white;}
      p {color: red; direction: rtl; font-size: 38pt; text-align: center; font-family: "Geeza Pro",  "Amiri"}
      h1 {color: darkgreen; font-size: 20pt; text-align: left; font-family: "Baskerville",  "Garamond"}
      img {height: 50pt; text-align: center}
      #download_button {
      position: fixed;
      padding: 0;
      text-align: left;
      width: 15%;
      bottom: 10px;
      right: 20px;
      font-size: 16pt;
      color: #8B0000;
      font-weight: bold;
      }
      
    </style>

</head>

<body>

<table style="width:100%" align="center">
"""

htmlBot = """

</table>

<a id="download_button" href="#" download>SAVE CORRECTIONS</a>

</body>

</html>


"""

def getText(fileName):
    with open(fileName[:-4]+'.gt.txt', "r", encoding="utf8") as f1:
        text = f1.read()
        text = text.replace('"', "«»")
        #print(text)
        #text = list(text)
        #print(text)
        #text.reverse()
        #print(text)
        #text = "".join(text)
        #print(text)
        #input()
        return(text)

import math
def roundup(x, par):
    newX = int(math.ceil(int(x) / float(par)) * par)
    return(newX)

def createHTMLs(lines):
    files = os.listdir(folder)

    counter = 0
    table = []

    for f in files:
        if f.endswith(".png"):
            # <a href="file://C:/path/to/file/file.html">Link Anchor</a>
            href = '<h1>File: %s (if the image is defective, simply delete all Arabic text and the line will be excluded)</h1>'
            head = href % (f[:-4]+'.gt.txt')
            tags = head + '<p><img src="%s"></p>' % (folder+f)
            text = tags+"<p contenteditable=\"true\" fileNameId=\"%s\">%s</p>" % ((f[:-4]+'.gt.txt'), getText(folder+f))
            table.append('<tr align="center">%s</tr><hr>' % text)
            counter += 1
            if counter % lines == 0:
                fileName = "%s%06d.html" % (pref, counter)
                newHTML = htmlTop.replace(">fileName<", ">"+fileName[:-5]+"_corrected<")
                with open(fileName, "w", encoding="utf8") as f9:
                    f9.write(newHTML + "\n\n".join(table) + htmlBot)
                table = []
                print("%s%06d.html" % (pref, counter))
                #input("Check!")

    newCount = roundup(counter, lines)
    fileName = "%s%06d.html" % (pref, newCount)
    newHTML = htmlTop.replace(">fileName<", ">"+fileName[:-5]+"_corrected<")
    with open(fileName, "w", encoding="utf8") as f9:
        f9.write(newHTML + "\n\n".join(table) + htmlBot)    

        

folder = "./5_goldStandard/"
pref = (os.path.abspath(folder)).split("/")[-2].replace(".","_")
pref = "gs_"+pref[5:]+"_"

print(pref)
print()

createHTMLs(30)    

        
        
