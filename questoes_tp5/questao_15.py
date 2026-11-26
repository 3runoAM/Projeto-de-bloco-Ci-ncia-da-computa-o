import subprocess

nslookup_response = subprocess.run(["nslookup", "google.com"], capture_output=True, text=True)
print(nslookup_response.stdout)

curl_response = subprocess.run(["curl", "-I", "https://google.com"], capture_output=True, text=True).stdout
print(curl_response)