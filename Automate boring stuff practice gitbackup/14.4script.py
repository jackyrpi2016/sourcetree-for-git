>>> # read and edit word
>>> import docx
>>> import os
>>> os.chdir('/Users/lichenglong/Desktop')
>>> # read the document
>>> d = docx.Document('demo.docx')
>>> # check the paragraphs
>>> d.paragraphs
[<docx.text.paragraph.Paragraph object at 0x103f90da0>, <docx.text.paragraph.Paragraph object at 0x103fa62b0>, <docx.text.paragraph.Paragraph object at 0x103fa65f8>, <docx.text.paragraph.Paragraph object at 0x103fa6668>, <docx.text.paragraph.Paragraph object at 0x103fa65c0>, <docx.text.paragraph.Paragraph object at 0x103fa6940>]
>>> d.paragraphs[0]
<docx.text.paragraph.Paragraph object at 0x103f50518>
>>> d.paragraphs[0].text
'Document Title'
>>> d.paragraphs[1].text
''
>>> d.paragraphs[2].text
'A plain paragraph having some bold and some italic'
>>> # sentence change styles, become a new run
>>> p = d.paragraphs[2]
>>> p.runs
[<docx.text.run.Run object at 0x103f90dd8>, <docx.text.run.Run object at 0x103fa6588>, <docx.text.run.Run object at 0x103fa62b0>, <docx.text.run.Run object at 0x103fa65c0>, <docx.text.run.Run object at 0x103fa6668>]
>>> p.runs[0].text
'A plain paragraph having some '
>>> p.runs[1].text
'bold'
>>> p.runs[2].text
' '
>>> p.runs[23.text
       
SyntaxError: invalid syntax
>>> p.runs[3].text
'and some '
>>> p.runs[4].text
'italic'
>>> # check if bold
>>> p.runs[1].bold
True
>>> p.runs[0].bold
>>> p.runs[0].bold == None
True
>>> p.runs[4].italic
True
>>> 
>>> # edit doc, underline
>>> p.runs[4].underline = True
>>> p.runs[4].text = 'italic and underlined'
>>> # save the changes
>>> d.save('demo2.docx')
>>> 
>>> # check paragraph style
>>> p.style
_ParagraphStyle('Normal') id: 4361710112
>>> p.style = 'Title'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    p.style = 'Title'
  File "/usr/local/lib/python3.6/site-packages/docx/text/paragraph.py", line 111, in style
    style_or_name, WD_STYLE_TYPE.PARAGRAPH
  File "/usr/local/lib/python3.6/site-packages/docx/parts/document.py", line 76, in get_style_id
    return self.styles.get_style_id(style_or_name, style_type)
  File "/usr/local/lib/python3.6/site-packages/docx/styles/styles.py", line 113, in get_style_id
    return self._get_style_id_from_name(style_or_name, style_type)
  File "/usr/local/lib/python3.6/site-packages/docx/styles/styles.py", line 143, in _get_style_id_from_name
    return self._get_style_id_from_style(self[style_name], style_type)
  File "/usr/local/lib/python3.6/site-packages/docx/styles/styles.py", line 57, in __getitem__
    raise KeyError("no style with name '%s'" % key)
KeyError: "no style with name 'Title'"
>>> # Mac and windows word are different, so cannot change paragraph from 'Normal' to 'Title'
>>> 
>>> 
>>> # create a new docx and edit
>>> d = docx.Document()
>>> d.add_paragraph('Hello this is a paragraph.')
<docx.text.paragraph.Paragraph object at 0x103fa6ba8>
>>> d.add_paragraph('This is another paragraph.')
<docx.text.paragraph.Paragraph object at 0x103fa6be0>
>>> p = d.paragraphs[0]
>>> # can only add new run at the end of paragraph
>>> p.add_run('This is a new run.')
<docx.text.run.Run object at 0x103fa6ba8>
>>> p.runs
[<docx.text.run.Run object at 0x103fba4e0>, <docx.text.run.Run object at 0x103fba208>]
>>> p.runs[1].bold = True
>>> d.save('demo4.docx')
>>> # use join
 RESTART: /Volumes/Extend/Automate boring stuff practice/getTextFromWordAsString.py 
Document Title

A plain paragraph having some bold and some italic

Heading, level 1

>>> # not use join
 RESTART: /Volumes/Extend/Automate boring stuff practice/getTextFromWordAsString.py 
['Document Title', '', 'A plain paragraph having some bold and some italic', '', 'Heading, level 1', '']
>>> 
