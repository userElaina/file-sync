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
