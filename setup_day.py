# setup_day.py
import os
import requests

day = input('Enter day: ')

try:
    day = int(day)
except ValueError:
    print('ERROR: Entered day is not an integer.')
    quit()

script_path = 'src/day_{0:d}.py'.format(day)
online_input_path = 'https://adventofcode.com/2022/day/{0:d}/input'.format(day)
local_input_path = 'input/day_{0:d}_full.txt'.format(day)

# Exit with error if preqrequisites are not met
if os.path.exists(script_path):
    print('ERROR: Script for this day already exists.')
    quit()
elif not os.path.exists('.session_cookie'):
    print('ERROR: .session_cookie file does not exist.')
    quit()
elif os.path.exists(local_input_path):
    print('ERROR: Input file for this day already exists.')
    quit()

# To get session cookie, go to input file in browser, and do the following:
# right-click/inspect/network/refresh/input/cookies/session
# Put this string in a file called '.session_cookie', in the top directory
# We now read the cookie
with open('.session_cookie') as f:
    cookies_dict = {'session': f.read()}

req = requests.get(online_input_path, cookies=cookies_dict)

# Check if request has succeeded, otherwise exit
if not req.ok:
    print('ERROR: Input could not be downloaded.')
    quit()
# Now all checks have succeeded, so continue

# Create and write input file
with open(local_input_path, 'w', newline='\n') as f:
    # remove trailing empty line and write to file
    # f.write(req.text.rstrip('\n'))
    f.write(req.text)

# Create python solution script
with open(script_path, 'w', newline='\n') as f:
    f.write("# day_{0:d}.py\n\n".format(day))
    f.write("def parse_input(input):\n")
    f.write("    with open(input) as f:\n\n\n\n")
    f.write("def main(input, part):\n\n\n\n")
    f.write("    if part == 0:\n")
    f.write("        return 0\n")
    f.write("    elif part == 1:\n")
    f.write("        return 0\n")
    f.write("    elif part == 2:\n")
    f.write("        return 0\n\n\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    input = 'input/day_{0:d}_test.txt'\n".format(day))
    f.write("    part = 1\n")
    f.write("    print(main(input, part))\n")
