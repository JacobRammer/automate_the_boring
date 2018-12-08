import requests  # does not handle sites requesting passwords 

res = requests.get("http://automatetheboringstuff.com/files/rj.txt")

print(res.status_code)

# bad_request = requests.get("http://automatetheboringstuff.com/khjsdfiffd")
# bad_request.raise_for_status()  # will stop program execution

play_file = open("request_module.txt", "wb")  # need wb (write binary) to keep unicode
for chunk in res.iter_content(100000):  # 100,000 byte chunk
    play_file.write(chunk)
print(res.status_code)  # 200 for OK
play_file.close()
