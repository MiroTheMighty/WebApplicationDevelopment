import socket, time

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print (e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       
    
    return s

def get_source(s, ip, page):

    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    return response

def get_links(response):
    beg = 0
    links=['0']
    while True:
        if int(links[0]) >=50 or len(links) >=50:
            return links
        
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return links
        
        end_str = response.find('"', beg_str + 6) 
        if (response.find("200 OK")):
            
            link = response[beg_str + 6:end_str]
            if link[-5:] == ".html":
                put_together = 1 +int(links[0])
                links[0]=str(put_together)
                if link not in links:
                    links.append(link)
        beg = end_str + 1


def get_all_links(links):
    for check_links in links[1:]:
        check_links="1280/"+check_links
        print(check_links, "provjera")
        s = connect_to_server(ip,port)
        response = get_source(s,ip,check_links)
        all_links_variable =get_links(response)
        for link in all_links_variable[1:]:
            put_together = 1 +int(links[0])
            links[0]=str(put_together)
            if link not in links:
                links.append(link)
    return links[1:]


ip = 'www.optimazadar.hr'
port = 80
page = '1280/djelatnost1280.html'

s = connect_to_server(ip, port)
response = get_source(s, ip, page)
first_page_links = get_links(response)
print(get_all_links(first_page_links))

s.close()