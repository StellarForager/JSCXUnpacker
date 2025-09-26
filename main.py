from hashlib import md5
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import base64
def get_aes_key(file_name: str):
    s0 = "chaoxing_" + md5((file_name + '_chenxi').encode()).hexdigest()
    k0 = md5(s0.encode()).hexdigest()
    k = k0[1:5] + '.' + s0[16:19] + '*' + k0[12:19]
    return k.encode()


def find_jscx_files(directory):
    result = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jscx'):
                result.append(os.path.join(root, file))
    return result
target_directory = r"C:\Users\Administrator\AppData\Local\cxstudy\1.3.8\resources\app\electron"
files = find_jscx_files(target_directory)

for file in files:
    objName = file[file.rfind('\\') + 1:]
    pureName = objName[:objName.rfind('.')]
    _dir = file[:file.rfind('\\')] # no \\
    aeskey = get_aes_key(objName)
    content = open(file, 'r', encoding='utf-8').read()
    enc = base64.b64decode(content)
    aes = AES.new(aeskey, AES.MODE_ECB)
    decoded = unpad(aes.decrypt(enc), 16).decode('utf-8')
    target = _dir + '\\' + pureName + '.js'
    open(target, 'w').write(decoded)
    os.remove(file)
