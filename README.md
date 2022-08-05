# popen_wait_returncode

```shell
% docker compose up
[+] Running 1/0
 ⠿ Container popen_wait_returncode-app-1  Created                                                                                                                                                                           0.0s
Attaching to popen_wait_returncode-app-1
popen_wait_returncode-app-1  | Popen(ls -al)
popen_wait_returncode-app-1  | total 16
popen_wait_returncode-app-1  | drwxr-xr-x 6 root root  192 Aug  5 13:19 .
popen_wait_returncode-app-1  | drwxr-xr-x 1 root root 4096 Aug  5 13:08 ..
popen_wait_returncode-app-1  | -rw-r--r-- 1 root root   42 Aug  5 12:30 Dockerfile
popen_wait_returncode-app-1  | drwxr-xr-x 3 root root   96 Aug  5 13:09 __pycache__
popen_wait_returncode-app-1  | -rw-r--r-- 1 root root  212 Aug  5 13:09 logger.py
popen_wait_returncode-app-1  | -rw-r--r-- 1 root root  629 Aug  5 13:19 main.py
popen_wait_returncode-app-1  | process.returncode: 0
popen_wait_returncode-app-1  | Popen(curl http://localhost:3000)
popen_wait_returncode-app-1  | curl: (7) Failed to connect to localhost port 3000: Connection refused
popen_wait_returncode-app-1  | process.returncode: 7
popen_wait_returncode-app-1 exited with code 0
```

### 補足

curlコマンドのreturncode(7)について

```
CURLE_COULDNT_CONNECT (7)
Failed to connect() to host or proxy.
```
https://curl.se/libcurl/c/libcurl-errors.html
