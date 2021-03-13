htimport json
import jsonpath
import urllib.request as req

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
header = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"}

request = req.Request(url, headers = header)
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

unicodestr = json.loads(data)

name = jsonpath.jsonpath(unicodestr,"$..stitle")
longitude = jsonpath.jsonpath(unicodestr, "$..longitude")
latitude = jsonpath.jsonpath(unicodestr, "$..latitude")
pic = jsonpath.jsonpath(unicodestr, "$..file")

for idx in range(len(pic)):
    pic[idx] = 'http:' + pic[idx].split('http:')[1]

result = open('data.txt', mode="w", encoding="utf-8")
for n, lo, la, p in zip(name, longitude, latitude, pic):
    ans = ','.join([n, lo, la, p])
    result.write(ans)
    result.write('\n')

result.close()