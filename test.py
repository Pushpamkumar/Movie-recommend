# import requests, certifi
# url = "https://api.themoviedb.org/3/movie/550?api_key=f52e52ebb7825b9dff966c9c1e38696e&language=en-US"

# try:
#     response = requests.get(url, verify=certifi.where(), timeout=10)
#     response.raise_for_status()
#     print("✅ API connected successfully!")
#     print("Poster Path:", response.json().get("poster_path"))
# except Exception as e:
#     print("❌ Error:", e)
import requests, certifi

url = "https://api.themoviedb.org/3/movie/550?api_key=f52e52ebb7825b9dff966c9c1e38696e"
resp = requests.get(url, verify=certifi.where())
print(resp.status_code, resp.json().get("title"))
