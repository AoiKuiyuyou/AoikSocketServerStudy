# AoikSocketServerStudy
Python 2 **SocketServer** library and Python 3 **socketserver** library study.

Tested working with:
- Python 2.7 and 3.5

Trace call using [AoikTraceCall](https://github.com/AoiKuiyuyou/AoikTraceCall):
- [StreamRequestHandlerTraceCall.py](/src/StreamRequestHandlerTraceCall.py)
- [StreamRequestHandlerTraceCallLogPy2.txt](/src/StreamRequestHandlerTraceCallLogPy2.txt?raw=True)
- [StreamRequestHandlerTraceCallLogPy3.txt](/src/StreamRequestHandlerTraceCallLogPy3.txt?raw=True)
- [StreamRequestHandlerTraceCallNotesPy2.txt](/src/StreamRequestHandlerTraceCallNotesPy2.txt?raw=True)
- [StreamRequestHandlerTraceCallNotesPy3.txt](/src/StreamRequestHandlerTraceCallNotesPy3.txt?raw=True)

## Table of Contents
- [Set up AoikTraceCall](#set-up-aoiktracecall)
  - [Setup via pip](#setup-via-pip)
  - [Setup via git](#setup-via-git)
- [Usage](#usage)
  - [Start server](#start-server)
  - [Send request](#send-request)

## Set up AoikTraceCall
- [Setup via pip](#setup-via-pip)
- [Setup via git](#setup-via-git)

### Setup via pip
Run:
```
pip install git+https://github.com/AoiKuiyuyou/AoikTraceCall
```

### Setup via git
Run:
```
git clone https://github.com/AoiKuiyuyou/AoikTraceCall

cd AoikTraceCall

python setup.py install
```

## Usage
- [Start server](#start-server)
- [Send request](#send-request)

### Start server
Run:
```
python "AoikSocketServerStudy/src/StreamRequestHandlerTraceCall.py" > Log.txt 2>&1
```

### Send request
Run:
```
echo hello| nc 127.0.0.1 8000
```
