# -*- encoding: utf-8 -*-

import logging
import sh
import random
from bakthat.helper import BakHelper

logging.basicConfig(level=logging.INFO)

# Backup settings
DESTINATION = "glacier"
BACKUP_NAME = "full_backup"
BACKUP_PASS = "your_password"
MYSQL_DB    = "foo_db"

# Creates a temporary folder at /tmp to store the packed backup
TMP = "/tmp/{0}/{1}".format(random.getrandbits(32), BACKUP_NAME)
sh.mkdir("-p", TMP)

# Copy your backup files to the TMP
sh.cp("-R", "/var/www/website/uploads", TMP)

# Execute a MySQL dump and store at TMP
sh.mysqldump("--defaults-extra-file=/root/.database.cnf",
             MYSQL_DB,
             _out=TMP+"/dump.sql")

# The conf=bakthat_conf will not be specified. We'll use the settings on 
# ~/.bakthat.yml (which can be configured with $ bakthat configure).
with BakHelper(BACKUP_NAME,
               destination=DESTINATION,
               password=BACKUP_PASS,
               tags=["public-uploads", "public-ipad", "mysql"]) as bh:
  bh.backup(TMP)
  bh.rotate()

# Removes the temporary folder
sh.rm("-r", TMP)
