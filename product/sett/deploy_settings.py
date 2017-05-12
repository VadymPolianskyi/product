from product.settings import *

DEBUG=False
#settings of db to depoloy server
DATABASES['default']['OPTIONS'] = {'read_default_file': 'product/sett/mysql.cnf',}
