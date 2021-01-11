# import requests module 
import requests 
import dns.resolver 

OUT = open('status.txt', 'w')
urls = ['https://www.google.com','https://www.127.0.0.1.com','https://www.udemy.com','https://www.microsoft.com','https://www.redhat.com','https://wikipedia.org','https://www.cloudflare.com','https://www.mozilla.org','https://wordpress.org','https://www.adobe.com','https://www.w3.org']
#urls = ['https://www.google.com','https://www.udemy.com']
# Making a get request 
for url in urls:
    try:
        response = requests.get(url)
        d_url=url[12:]
        dns_result = dns.resolver.resolve(d_url, 'A') 
        for val in dns_result:
            #print('A Record : ', val.to_text())
            dns_R=(val.to_text())
        print(response,response.url,dns_R)
        OUT_F=(response,response.url,dns_R)
        OUT.write(str(OUT_F) + '\n')
    except:
	     print('Error in url',' ',url)
OUT.close()
