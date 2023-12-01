import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

YEAR = os.getenv('year')

if len(sys.argv) == 2:
    DAY = sys.argv[1]
else:
    print('In directory of day:')
    print('py ../getInput.py DAY')
    sys.exit()

print(f'{YEAR}, Day {DAY}')

r = requests.get(f'https://adventofcode.com/{YEAR}/day/{DAY}/input', 
                 cookies={
                    'session': os.getenv('session')}
                 )
open(f'input.txt', 'wb').write(r.content)

print(r)
if r.status_code == 200:
    print(f'Day {DAY} successfully downloaded :)')
elif r.status_code == 500:
    print('Maybe Session cookie is expired')
elif r.status_code == 404:
    print('Link Wrong or unavailable?')
