# get all text from a docx to form a string

import docx, os

os.chdir('/Users/lichenglong/Desktop')

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    # fullText are elements of list, need join them together to get a string
    return '\n'.join(fullText)
    #return fullText

print(getText('demo.docx'))
