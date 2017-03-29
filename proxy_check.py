import urllib.request
import socket

socket.setdefaulttimeout(180)

# read the list of proxy IPs in proxyList
proxyList = ['103.255.30.249:80', '202.5.17.76:8080',"77.241.235.52:80"] # there are two sample proxy ip

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://www.google.com')  # change the url address here
        sock=urllib.request.urlopen(req)

    except urllib.request.HTTPError as e:
        print('Error code: ',e)
        return 1
    except Exception as detail:
        print("ERROR:", detail)
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print("Bad Proxy", item)
    else:
        print(item, "is working")
