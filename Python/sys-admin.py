import os
import subprocess

print(os.getcwd())
print(os.listdir())
print(os.mkdir("tes-dir3"))
print(os.rmdir("tes-dir3"))
print(os.getlogin())

os.system("ls -1;touch myfile")

output = subprocess.run(["touch","myfile4"], capture_output=True)
print(output)
