from product.settings import *

DEBUG=True
#settings of db to develop server
DATABASES['default']['OPTIONS'] = {'read_default_file': 'product/sett/dev_mysql.cnf',}