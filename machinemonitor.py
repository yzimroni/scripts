"""A simple script to log the machine resources usage to a database"""
import json
import psutil
import MySQLdb

config = json.load(open('config.json'))

cpu_usage = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
ram_used = ram.total - ram.available
ram_cache = ram.used
swap_used = psutil.swap_memory().used
disk_usage = psutil.disk_usage('/').used

db = MySQLdb.connect(host=config['database']['host'], user=config['database']['username'], passwd=config['database']['password'], db=config['database']['database'])
cur = db.cursor()
query = "INSERT INTO logs (cpu_usage,ram_used,ram_cache,swap_used,disk_usage) VALUES(%s,%s,%s,%s,%s)"
cur.execute(query, (cpu_usage, ram_used, ram_cache, swap_used, disk_usage))
db.commit()

db.close()
