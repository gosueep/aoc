import requests
import sys

YEAR = 2022

if len(sys.argv) == 2:
    DAY = sys.argv[1]
else:
    print('In directory of day:')
    print('py ../getInput.py DAY')
    sys.exit()

print(f'{YEAR}, Day {DAY}')

tokens = {
    'session': '53616c7465645f5f237b5baf4b135686d23c2e2b4292fe0283c3315094335f6430b00e0487e8d93256efb702b24838a6d729e0aa2f6810bbfa0ac38accf49bdb '
}

r = requests.get(f'https://adventofcode.com/{YEAR}/day/{DAY}/input', cookies=tokens)
open(f'input.txt', 'wb').write(r.content)

print(r)
if r.status_code == 200:
    print(f'Day {DAY} successfully downloaded :)')
elif r.status_code == 500:
    print('Maybe Session cookie is expired')
elif r.status_code == 404:
    print('Link Wrong or unavailable?')
