import socket

def netcat1(content):
    hostname = 'crypto.chal.csaw.io'
    port=1578
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.send(content)
    s.shutdown(socket.SHUT_WR)
    equal = False
    while 1:
        data = s.recv(1024)
        split1 = data.split("\n")
        split2 = split1[0].split(" ")
        cookie = split2[-1]
        if cookie[:32] == cookie[-32:] and cookie != '':
            equal = True
        if data == "":
            break
    s.close()
    if equal:
        return True
    return False

    
#print('}' + '0' * 15 + 'a')
#last 16 bytes of flag
def break_aes1():
    flag = '}'
    for y in range(2, 17):
        for x in range(0,255):
            if netcat1(chr(x) + flag + (16-y)*'0' + y*'a'):
                flag = chr(x) + flag
                break
    print flag
#0_h@rd_t0_d0...}

def netcat2(content):
    hostname = 'crypto.chal.csaw.io'
    port=1578
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.send(content)
    s.shutdown(socket.SHUT_WR)
    equal = False
    while 1:
        data = s.recv(1024)
        split1 = data.split("\n")
        split2 = split1[0].split(" ")
        cookie = split2[-1]
        #not sure why but when you send chr(10), it encrypts to 32 bytes, ensure that it's > 32 bytes
        if cookie[:32] == cookie[-64:-32] and cookie != '' and len(cookie) > 64:
            equal = True
        if data == "":
            break
    s.close()
    if equal:
        return True
    return False

#last 16 are 0_h@rd_t0_d0...}
# | a + 15 bytes | + | 16th byte + 0_h@rd_t0_d0... | + | } + 15*'0' |
def break_aes2():
    flag = "0_h@rd_t0_d0..."
    realflag = ""
    for y in range(1,17): #guess 16 characters
        for x in range(0,255):
            if netcat2(chr(x) + flag + y*'a'):
                flag = chr(x) + flag[:-1]
                realflag = chr(x) + realflag
                break
    print flag
break_aes1()
#0_h@rd_t0_d0...}
break_aes2()
#flag{Crypt0_is_s