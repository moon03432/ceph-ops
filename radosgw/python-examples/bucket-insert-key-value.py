import argparse
import boto.s3.connection

parser = argparse.ArgumentParser()
parser.add_argument("bucket", default=None)
parser.add_argument("key", default=None)
parser.add_argument("value", default=None)
args = parser.parse_args()

bucketname = args.bucket
keyname = args.key
value = args.value

hostname = 'shoyb17plpcdp160.mcd.com.cn'
port = 8080
conn = boto.connect_s3(
        host=hostname, port=port,
        is_secure=False, calling_format=boto.s3.connection.OrdinaryCallingFormat(),
       )

bucket = conn.get_bucket(bucketname)
key = bucket.new_key(keyname)
key.set_contents_from_string(value)

conn.close()
