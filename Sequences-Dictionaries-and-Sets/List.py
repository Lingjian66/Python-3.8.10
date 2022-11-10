#编码与解码 encode()、decode()
my_string="人生苦短，我用python"
my_encode=my_string.encode('utf-8')
print(my_encode)
my_decode=my_encode.decode('utf-8')
print(my_decode)