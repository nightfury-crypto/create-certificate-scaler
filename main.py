from pandas import read_csv
from features.CheckBlankSpace import Detectfield
from features.MakeCertificate import MakeCertificate

def start():
    # update csv path
    data = read_csv("js-list.csv")

    # Update the template path
    template = "template/testFormat.jpg"

    longestSpace = Detectfield(template)
    if (longestSpace != None):
        index = 0
        for student in data.values.tolist():
            if student[4] == True:
                print("already updated! want to overwrite -> manually remove the certificateFile field and update isGenerated to False")
                continue
            MakeCertificate(student, template, longestSpace, data, index)
            index +=1
        print("All Certificates are generated.")
    else:
        print("No Blank Space is detected. Give the correct certificate format")

if __name__ == "__main__":
    start()