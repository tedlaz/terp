import os


from PyQt5.QtCore import QDir

VERSION = '0.1.0'
DATE = '20190916000000'
NAME = 'TERP'
PRODUCT_NAME = 'Ted ERP'
GPL_VERSION = '3'
DECRIPTION = 'Mini ERP system caontaining Accounting and Payroll'
COMPANY_NAME = 'TedSoft'
ORG_DOMAIN = 'tedlaz'
COPYRIGHT = "Copyright (c) 2008-2018 %s" % COMPANY_NAME
CWD = os.getcwd()
PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
HOME_PATH = os.path.join(os.path.expanduser("~"))
USER_PATH = os.path.join(HOME_PATH, ".qterp")
BACKUP_PATH = os.path.join(USER_PATH, 'backup')
ASSETS_PATH = os.path.join(USER_PATH, "assets")

for folder in [USER_PATH, BACKUP_PATH, ASSETS_PATH]:
    if not os.path.exists(folder.encode("UTF-8")):
        os.makedirs(folder, exist_ok=True)
