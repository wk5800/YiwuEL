from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("C://Users//Administrator//Desktop//label//yl.1.xml")
collection = DOMTree.documentElement
names = collection.getElementsByTagName("object")
labels = []
for i in names:
    format = i.getElementsByTagName('name')[0].firstChild.data
    labels.append(format)
print(set(labels))