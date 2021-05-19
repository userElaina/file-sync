# file-sync
\*\*\*@\*\*\*:~/log# ls -R from
```
from:
bigfile  exist  existe  nexist  nexiste  only_time.txt

from/bigfile:
'bingo - 副本 (2).txt'  'bingo - 副本 (3).txt'  'bingo - 副本.txt'   bingo.txt

from/exist:
edit.txt  nexist.txt  same.txt

from/existe:

from/nexist:
'新建 文本文档.txt'

from/nexiste:
```
\*\*\*@\*\*\*:~/log# ls -R to
```
to:
exist  existe  more.txt  only_time.txt

to/exist:
edit.txt  same.txt

to/existe:
```
\*\*\*@\*\*\*:~/log#cat file_sync.sh
```sh
cp -r "/root/log/from/bigfile" "/root/log/to/bigfile"
cp "/root/log/to/exist/edit.txt" "/root/log/to/exist/edit.txt.00.sync_old"
cp "/root/log/from/exist/edit.txt" "/root/log/to/exist/edit.txt"
cp "/root/log/from/exist/nexist.txt" "/root/log/to/exist/nexist.txt"
cp -r "/root/log/from/nexist" "/root/log/to/nexist"
cp -r "/root/log/from/nexiste" "/root/log/to/nexiste"
#/root/log/to/more.txt
```
\*\*\*@\*\*\*:~/log#
