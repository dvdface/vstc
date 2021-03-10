import base64
files = ['Virtual Spirent TestCenter.png', 'VSTC Class Diagram.png' ]
for file in files:
    f1 = open(file, 'rb')
    data = base64.b64encode(f1.read())
    f1.close()
    f2 = open(file + '.txt', 'wb')
    f2.write(data)
    f2.close()