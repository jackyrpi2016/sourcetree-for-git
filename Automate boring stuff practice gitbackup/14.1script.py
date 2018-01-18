>>> # reading excel
>>> import openpyxl
>>> import os
>>> os.chdir('/Users/lichenglong/Desktop')
>>> 
>>> 
>>> # load into workbook
>>> workbook = openpyxl.load_workbook('example.xlsx')
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> # sheet in the workbook
>>> # that's when we know the sheet name
>>> sheet = workbook.get_sheet_by_name('Sheet1')
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> # when we don't know sheet name
>>> workbook.get_sheet_names()
['Sheet1', 'Sheet2', 'Sheet3']
>>> # get value of a cell, like A1
>>> sheet['A1']
<Cell Sheet1.A1>
>>> cell = sheet['A1']
>>> cell.value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> # it is date type in python
>>> # use str to get the normal look
>>> str(cell.value)
'2015-04-05 13:34:02'
>>> str(sheet['A1'].value)
'2015-04-05 13:34:02'
>>> # another way to read cell
>>> sheet.cell(row=1, column=2)
<Cell Sheet1.B1>
>>> sheet.cell(row=1, column=2).value
'Apples'
>>> # better to use second way of reading cells in for loop
>>> for i in range(1, 8):
	print(i, sheet.cell(row=i, column=2).value)

1 Apples
2 Cherries
3 Pears
4 Oranges
5 Apples
6 Bananas
7 Strawberries
>>> 
