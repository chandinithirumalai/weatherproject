
# from datetime import datetime 
iso_string="2010-01-27T07:00:00+08:00"
# iso_string = datetime.now()
    
import datetime

# x = datetime.datetime(iso_string)

x= datetime.fromisoformat(iso_string)

print(x.year)
print(x.strftime("%A %d %B %Y"))

# newdate= datetime.strptime(iso_string)

# print(newdate)