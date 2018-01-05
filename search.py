import shodan
import sys

with open('shodan_key') as inputfile:
    file = inputfile.read()
    API_KEY=file.split('\n',1)[0]
print API_KEY

# Configuration

# Input validation
if len(sys.argv) == 1:
        print 'Usage: %s <search query>' % sys.argv[0]
        sys.exit(1)

try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join(sys.argv[1:])
        result = api.search(query)

        print 'count :%s' % result['total']
        # Loop through the matches and print each IP
        #for service in result['matches']:
        #        print service['ip_str']
except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)
