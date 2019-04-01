from pymemcache.client.base import Client

def main():
    client = Client(('localhost', 11211))
    client.set('key', 'value')
    result = client.get('key')
    print("Got value: {}".format(result))


if __name__ == '__main__':
    main()