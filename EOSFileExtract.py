import requests
import getpass

from pip._vendor.distlib.compat import raw_input

url = "page url"

uname=raw_input("Enter Username: ")
pswd=getpass.getpass(prompt='Enter Password: ', stream=None)

r=requests.get(url, auth=(uname, pswd))



if r.status_code==requests.codes.ok:
    print("Requests made a connection.\n")
    f=open(r'C:\\Test\dump.csv', 'wb')
    f.write(r.content)
    f.close()

else:
    print("\nAn error occured while establishing a connection.")
    print("Status code returned: ",r.status_code)

c=input("\nEnter a key to exit.\n")