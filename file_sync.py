_os='linux'
EXT='.sync_old'
LL=r'/root/log/from/'
RR=r'/root/log/to/'

import os
from downs import *

import hashlib
def md5(pth:str)->str:
	return hashlib.md5(open(pth,'rb').read()).hexdigest()

print('Files that have changed paths will not deduplicated.')
exit() if input('(y/n)? ')!='y' else print('begin')
_os=_os[:3]
if _os=='win':
	_cp='copy'
if _os=='lin':
	_cp='cp'
_lg=list()
t=nThread(1)

def mkp2(p:str)->str:
	return p.replace(LL,RR)

def mkp3(p2:str)->str:
	for i in range(0x100):
		p3=p2+'.'+hex(i)[2:].zfill(2)+EXT
		if not os.path.exists(p3):
			return p3
	for i in range(0x10000):
		p3=p2+'.'+hex(i)[2:].zfill(4)+EXT
		if not os.path.exists(p3):
			return p3
	for i in range(0x100000000):
		p3=p2+'.'+hex(i)[2:].zfill(8)+EXT
		if not os.path.exists(p3):
			return p3
	raise MemoryError('Too many old versions... B00000000M!')
	
def mkmv(p2:str,p3:str=None)->str:
	if not p3:
		p3=mkp3(p2)
	return _cp+' "'+p2+'" "'+p3+'"'

def mkcp(p:str,p2:str=None)->str:
	if not p2:
		p2=mkp2(p)
	return _cp+' "'+p+'" "'+p2+'"'

def _sh(x:str):
	_lg.append(x)
	# t.th(sh,x)
	
def g(p,p2,s):
	if not os.path.exists(p2):
		return 'c'
	s2=os.stat(p2)

	if s.st_size!=s2.st_size:
		return 'mc'
	if s.st_mtime==s2.st_mtime:
		return ''
	if md5(p)==md5(p2):
		return ''
	return 'mc'


def f(x):
	x2=mkp2(x)
	if not os.path.exists(x2):
		if _os=='win':
			_sh('echo D | xcopy "'+x+'" "'+x2+'" /E /V /F')
		if _os=='lin':
			_sh('cp -r "'+x+'" "'+x2+'"')
		return

	execute=list()
	for i in os.scandir(x):
		if i.is_file():
			p=i.path
			p2=mkp2(p)
			_=g(p,p2,i.stat())
			execute.append(p2)
			if 'm' in _:
				_sh(mkmv(p2))
			if 'c' in _:
				_sh(mkcp(p,p2))
		else:
			f(i.path)
	
	for i in os.scandir(x2):
		if not i.is_file():
			continue
		p2=i.path
		if p2.endswith(EXT):
			continue
		if p2 in execute:
			continue
		od='#'+p2
		if od not in _lg:
			_lg.append(od)

f(LL)
open('file_sync.sh','w').write('\n'.join(_lg)+'\n')
t.join()


