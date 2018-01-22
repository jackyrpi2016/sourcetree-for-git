
>>> # string formatting
>>> # often use + to concatenate several strings
>>> name = 'Jacky'
>>> place = 'Main street'
>>> time = '6 pm'
>>> food = 'turnips'
>>> 'Hello ' + name + '， you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'
'Hello Jacky， you are invited to a party at Main street at 6 pm. Please bring turnips.'
>>> 
>>> # a better way is to use %s
>>> 'Hello %s， you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
'Hello Jacky， you are invited to a party at Main street at 6 pm. Please bring turnips.'
>>> 
