from getPageDOM import getRequests
from getPageList import getList

getURLlist = getList('./validation_sheet.xlsx')

for url in getURLlist:
    tree = getRequests(url)
    anas = tree.xpath('//a/@data-ana')
    print(f"\n\n Tracking the following URL: {url} \n\n")
    for ana in anas:
        print(ana)
