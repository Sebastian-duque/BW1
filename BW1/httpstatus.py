import http.client

host = input("Inserire host/IP del sistema target: ")
port = input("Insert la porta del sistema target (default:80):")

if(port == ""):
    port = 80

try:

    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', 'http://192.168.50.101/phpMyAdmin/phpMyAdmin.html%27)
    response=connection.getresponse()
    print("I metodi abilitati sono:")
    print(response.getheader('allow'))
    connection.close()

except ConnectionRefusedError:
    print("Errore")