import os, shutil, re

# filenames from the folder
# parse out values from html
# copy/save into a new folder
# create a manifesto


sFolder = "./6_DoubleChecked/"
tFolder = "./7_final/"

def parsing():
    lof = os.listdir(sFolder)

    for f in lof:
        if f.endswith(".html"):
            print(f)
            picFolder = f[:-5]+"_files/"
            with open(sFolder+f, "r", encoding="utf8") as ft:
                text = ft.read()
                for l in re.findall("<p filenameid=.*?</p>", text):
                    l = re.sub("<br>", "", l)
                    #print(l)
                    fn = l[15:28]
                    val = re.search(">(.*?)</p>", l).group(1)
                    if val == "":
                        pass
                    else:
                        with open(tFolder+fn, "w", encoding="utf8") as ft2:
                            ft2.write(val)
                        imName = fn[:-7]+".png"
                        shutil.copy2(sFolder+picFolder+imName, tFolder+imName)
    # create a manifest
    man = os.listdir(tFolder)
    manNew = []
    for i in man:
        if i.endswith(".png"):
            manNew.append(i)
    with open(tFolder+"manifest.txt", "w", encoding="utf8") as f9:
        f9.write("\n".join(manNew))


parsing()
print("Done!")


        
        
