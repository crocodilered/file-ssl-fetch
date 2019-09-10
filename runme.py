import requests
import shutil
import os


def x_filename(url):
    if url and len(url) > 0:
        filename = url.split['https://ftp.egrul.nalog.ru/'].pop()
        return filename.lower().replace('/', '__')
    return None


file_url = 'https://ftp.egrul.nalog.ru/EGRUL/01.01.2019_FULL'

r = requests.get(
    file_url,
    cert=('cert/newfile.crt.pem', 'cert/newfile.key.pem'),
    verify=False,
    stream=True
)

if r.status_code == 200:
    out_file = os.path.join('downloads', x_filename(file_url))
    with open(out_file, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
