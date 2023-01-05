import sys
import hashlib

def calc_passwd(sn):
    passwd = sn + '6d2df50a-250f-4a30-a5e6-d44fb0960aa0'
    md5_value = hashlib.md5(passwd.encode())
    return md5_value.hexdigest()[:8]

if __name__ == "__main__":
    serial = ''  # you can input your SN here.
    if serial != '':
        print(calc_passwd(serial))
    else:
        serial = input('input your SN eg: 12345/A1BC23456 \n')
        print(calc_passwd(serial))