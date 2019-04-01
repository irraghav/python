from getPageDOM import getRequests
from getPageList import getList

tree = getRequests("https://www.bmo.com/main/personal")
ids = tree.xpath('//a/@data-ana')

for id in ids:
    print(id)
