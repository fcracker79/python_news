# PEP 615 – Support for the IANA Time Zone Database in the Standard Library
import datetime
import zoneinfo

if __name__ == '__main__':
    now = datetime.datetime.now(zoneinfo.ZoneInfo('Europe/Rome'))
    print(now)  # 2022-10-28 12:30:50.665090+02:00
