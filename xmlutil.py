import xml.etree.ElementTree as ET
from idlelib.macosx import hideTkConsole

data = '''<person>
            <name>Chuck</name>
            <phone type='intl'>
            +1 7343034456
            </phone>
            <email hide='yes'/>
         </person>
            '''
xmlTree = ET.fromstring(data)
print('Name:',xmlTree.find('name').text )
print('Attr:',xmlTree.find('email').get('hide') )

input = '''
        <users>
            <user x='2'>
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x='7'>
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
        '''
xmlTree = ET.fromstring(input)
listOfUsers = xmlTree.findall('user')
print(len(listOfUsers))
for user in listOfUsers:
    print('Name:',user.find('name').text )
    print('Id:',user.find('id').text )
    print("Attr",user.get('x'))