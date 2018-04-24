
import telnetlib

hostname = input ('Insira o Hostname ou IP: ')
usuario  = input ('Insira o Usuario.......: ')
password = input ('Insira a Senha.........: ')

print ('Conectando no host {} com o usuário {} e senha {}'.format(hostname, usuario, password))

connexion = telnetlib.Telnet(HOST)

connexion.read_until(b"login: ")
connexion.write(usuario.encode('ascii') + b"\n")
if password:
    connexion.read_until(b"Password: ")
    connexion.write(password.encode('ascii') + b"\n")

#################################
# COMANDOS    NO    EQUIPAMENTO
# DEVERA  CHAMAR  UM  DIFERENTE
# PARA CADA EQUIPAMENTO DE REDE
#################################

connexion.write(b"ls\n")
connexion.write(b"exit\n")

print(connexion.read_all().decode('ascii'))