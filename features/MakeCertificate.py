from PIL import Image, ImageDraw, ImageFont
import random
import cv2

cfont = "public/SF-Pro.ttf"
eventfont = "public/SFPro.ttf"
color = (255,255,255)

def MakeCertificate(student, template, longestSpace, data, index):
    x1, y1, x2, y2 = longestSpace.values()
    templateImg = Image.open(template)
    cvImg = cv2.imread(template)
    cert = templateImg.copy()
    draw = ImageDraw.Draw(cert)
    height, width = cvImg.shape[:2]
    fontSize = int(((height/3)/50)*9.4)
    textFont = ImageFont.truetype(cfont, fontSize)

    #name
    nameTextLength = draw.textlength(student[2], textFont)
    namexpos = (x2+x1)/2 - nameTextLength/2
    # w, h = draw.textsize(student[0],font)
    # draw.text(xy = (960-w/2,535),text=student[0],fill=color,font=font)
    #rank
    if student[2] != "None":
        draw.text(xy = (namexpos,y1-80),text=student[2],fill=color,font=textFont )
    else:
        #rank holder
        draw.text(xy = (namexpos,y1-80),text=student[2],fill=color,font=textFont)
    # randm num for unique name
    ran = random.randint(1000,9999)
    # saving file in /output/ folder
    cert.save(str(f"output/{student[2]}{ran}.png"))

    # updating csv
    data.at[index, "isGenerated"] = True
    data.at[index, "certificateFile"] = str(f"output/{student[2]}{ran}.png")
    data.to_csv("js-list.csv", index=False)
    