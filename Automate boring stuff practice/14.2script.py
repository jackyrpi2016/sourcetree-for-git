>>> # edit excel
>>> import openpyxl
>>> # create a blank workbook
>>> wb = openpyxl.Workbook()
>>> wb
<openpyxl.workbook.workbook.Workbook object at 0x10c0c56d8>
>>> # the default sheet name is Sheet
>>> wb.get_sheet_names()
['Sheet']
>>> # edit cell value
>>> sheet = wb.get_sheet_by_name('Sheet')
>>> sheet
<Worksheet "Sheet">
>>> sheet['A1'].value
>>> sheet['A1'].value == None
True
>>> # default cell value is None
>>> sheet['A1'] = 42
>>> sheet['A2'] = 'Hello'
>>> 
>>> import os
>>> os.chdir('/Users/lichenglong/Desktop')
>>> # save the worksheet
>>> wb.save('creatework.xlsx')
>>> # save as another worksheet
>>> # the existed values for A1 and A2 is still there
>>> sheet2 = wb.create_sheet()
>>> wb.get_sheet_names()
['Sheet', 'Sheet1']
>>> # change Sheet1 to mySheet
>>> sheet2.title
'Sheet1'
>>> sheet2.title = 'mySheet'
>>> wb.get_sheet_names()
['Sheet', 'mySheet']
>>> wb.save('creatwork2.xlsx')
>>> # create a sheet in specified index of sheet list
>>> # index starts from 0
>>> wb.create_sheet(index=0, title='myOtherSheet')
<Worksheet "myOtherSheet">
>>> wb.save('creatwork3.xlsx')
>>> 
