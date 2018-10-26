import datetime
import random
import argparse

ProductCode = {
    'Xmanager': 0,
    'Xshell': 1,
    'Xlpd': 2,
    'Xfile': 3,
    'Xftp': 4,
    'Xmanager 3D': 5,
    'Xmanager Enterprise': 6,
    'Xshell Plus': 7
}

ProductPublishList = (
    {'ProductName': 'Xmanager', 'Version': 2, 'PublishDate': datetime.date(2003, 1, 1)},
    {'ProductName': 'Xshell', 'Version': 2, 'PublishDate': datetime.date(2004, 10, 1)},

    {'ProductName': 'Xmanager', 'Version': 3, 'PublishDate': datetime.date(2007, 1, 1)},
    {'ProductName': 'Xshell', 'Version': 3, 'PublishDate': datetime.date(2007, 1, 1)},
    {'ProductName': 'Xlpd', 'Version': 3, 'PublishDate': datetime.date(2007, 1, 1)},
    {'ProductName': 'Xftp', 'Version': 3, 'PublishDate': datetime.date(2007, 1, 1)},
    {'ProductName': 'Xmanager Enterprise', 'Version': 3, 'PublishDate': datetime.date(2007, 1, 1)},

    {'ProductName': 'Xmanager', 'Version': 4, 'PublishDate': datetime.date(2010, 8, 1)},
    {'ProductName': 'Xshell', 'Version': 4, 'PublishDate': datetime.date(2010, 8, 1)},
    {'ProductName': 'Xlpd', 'Version': 4, 'PublishDate': datetime.date(2010, 8, 1)},
    {'ProductName': 'Xftp', 'Version': 4, 'PublishDate': datetime.date(2010, 8, 1)},
    {'ProductName': 'Xmanager Enterprise', 'Version': 4, 'PublishDate': datetime.date(2010, 8, 1)},
    {'ProductName': 'Xmanager', 'Version': 5, 'PublishDate': datetime.date(2014, 4, 28)},
    {'ProductName': 'Xshell', 'Version': 5, 'PublishDate': datetime.date(2014, 4, 28)},
    {'ProductName': 'Xlpd', 'Version': 5, 'PublishDate': datetime.date(2014, 4, 28)},
    {'ProductName': 'Xftp', 'Version': 5, 'PublishDate': datetime.date(2014, 4, 28)},
    {'ProductName': 'Xmanager Enterprise', 'Version': 5, 'PublishDate': datetime.date(2014, 4, 28)},
    {'ProductName': 'Xmanager', 'Version': 6, 'PublishDate': datetime.date(2018, 4, 29)},
    {'ProductName': 'Xshell', 'Version': 6, 'PublishDate': datetime.date(2018, 4, 29)},
    {'ProductName': 'Xshell Plus', 'Version': 6, 'PublishDate': datetime.date(2018, 4, 29)},
    {'ProductName': 'Xlpd', 'Version': 6, 'PublishDate': datetime.date(2018, 4, 29)},
    {'ProductName': 'Xftp', 'Version': 6, 'PublishDate': datetime.date(2018, 4, 29)},
    {'ProductName': 'Xmanager Enterprise', 'Version': 6, 'PublishDate': datetime.date(2018, 4, 29)}
)


def GetChecksum(preProductKey: str):
    Checksum = 1
    for i in range(0, len(preProductKey)):
        if preProductKey[i] != '-' and preProductKey[i] != '8' and preProductKey[i] != '9':
            place = int(preProductKey[i])
            Checksum = (9 - place) * Checksum % -1000
    Checksum = (Checksum + int(preProductKey[9])) % 1000
    return Checksum


def GenerateProductKey(IssueDate: datetime.date,
                       ProductName: str,
                       ProductVersion: int,
                       NumberOfLicense: int):
    if IssueDate.year < 2002:
        raise ValueError('IssueDate cannot be earlier than 2002.')
    if IssueDate > datetime.date.today() + datetime.timedelta(days=7):
        raise ValueError('IssueDate cannot be later than today after a week.')
    if NumberOfLicense < 0 or NumberOfLicense > 999:
        raise ValueError('NumberOfLicense must vary from 0 to 999.')

    for item in ProductPublishList:
        if item['ProductName'] == ProductName and item['Version'] == ProductVersion:
            if item['PublishDate'] > IssueDate:
                raise ValueError('IssueDate cannot be earlier than the publish date.')
            break
        if item == ProductPublishList[-1]:
            raise ValueError('Invalid product.')

    preProductKey = '%02d%02d%02d-%02d%d%03d-%03d' % (IssueDate.year - 2000,
                                                      IssueDate.month,
                                                      IssueDate.day,
                                                      0x0B,
                                                      ProductCode[ProductName],
                                                      random.randint(0, 999),
                                                      NumberOfLicense)
    Checksum = GetChecksum(preProductKey)
    ProductKey = preProductKey + '%03d' % Checksum
    return ProductKey

ProductNameDict = {
    0:'Xmanager',
    1:'Xshell',
    2:'Xlpd',
    3:'Xfile',
    4:'Xftp',
    5:'Xmanager 3D',
    6:'Xmanager Enterprise',
    7:'Xshell Plus'
}
config = {}


def main():
    print("Welcome to use this tool .\n This is a python tool for Xmanager series product. You can use -h show the way to use.\n Let's begin.......Enjoy it.")
    parser = argparse.ArgumentParser(description='Xmanager series keygen . Modified by meter . Just for study . Do not commercial!',
                                     epilog="version: xkeygen V1.0 Date:2018-10-24 ")
    parser.add_argument("-p", "--ProductName", dest="name", default=6,
                        help="You can input a int number to specify the product type;Default is 6;The possible num :['Xmanager' : 0,  'Xshell' : 1, 'Xlpd' : 2, 'Xfile' : 3, 'Xftp' : 4,  'Xmanager 3D' : 5, 'Xmanager Enterprise' : 6; 'Xshell Plus' : 7]",
                        type=int)
    parser.add_argument("-v", "--ProductVersion", dest="version", default=6,
                        help='Use this flag to specify the current product version,Default is 6..', type=int)
    parser.add_argument("-n", "--NumberOfLicense", dest="number", default=999,
                        help='Use this flag to specify the number of the product license,default is 999.', type=int)
    config.update(vars(parser.parse_args()));
    key = GenerateProductKey(datetime.date(2018, 10, 26), ProductNameDict[config['name']], config['version'],
                             config['number']);
    print("The product [",ProductNameDict[config['name']], "] key is :", key);
    print("End");


if __name__ == "__main__":
    main();
