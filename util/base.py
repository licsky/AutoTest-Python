import hashlib

def md5(string):
    if string:
        m = hashlib.md5()
        m.update(string.encode(encoding="utf-8"))
        return m.hexdigest()
    else:
        pass

def sha1(string):
    if string:
        return hashlib.sha1(string.encode(encoding="utf-8").hexdigest())
    else:
        pass