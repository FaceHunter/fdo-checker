import hashlib
import urllib
from glob import glob

hashlist = "http://facehunter.tk/fdo/iw4m.json"
a = urllib.urlopen(hashlist)
b = a.read()
hashdict = eval(b)
exceptlist = ["list.json","iw4m.ini","iw4mp.cfg"

def check(file, hash):
	try:
		if hashdict[file] == hash:
			print "true"
		else:
			print "false "+file
	except:
		pass
	
def md5Checksum(filePath):
    fh = open(filePath, 'r+')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()
	
for x in glob("*"):
	if "." in x:
		# print "writing: "+x+" "+md5Checksum(x)+"\n"
		check(x,md5Checksum(x))
		pass
	else:
		# print "folder: "+x
		for y in glob(""+x+"\\*"):
			if "." in y:
				try:
					check(y,md5Checksum(y))
				except IOError:
					print "Error on file: "+y
					# write(y+" ERROR\n")
			else:
				# print "folder: "+y
				for z in glob(y+"\\*"):
					if "." in z:
						try:
							check(z,md5Checksum(z))
						except IOError:
							print "Error on file: "+z
							# write(z+" ERROR\n")
					else:
						# print "folder: "+z
						for a in glob(z+"\\*"):
							if "." in a:
								try:
									check(a,md5Checksum(a))
								except IOError:
									print "Error on file: "+a
									# write(a+" ERROR\n")
							else:
								# print "folder: "+a
								for b in glob(a+"\\*"):
									if "." in b:
										try:
											check(b,md5Checksum(b))
										except IOError:
											print "Error on file: "+b
											# write(b+" ERROR\n")