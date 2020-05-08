import argparse
import boto.s3.connection

parser = argparse.ArgumentParser()
parser.add_argument("bucket", default=None)
args = parser.parse_args()

bucketname = args.bucket

hostname = 'shoyb17plpcdp160.mcd.com.cn'
port = 8080
conn = boto.connect_s3(
        host=hostname, port=port,
        is_secure=False, calling_format=boto.s3.connection.OrdinaryCallingFormat(),
       )

bucket = conn.get_bucket(bucketname)
for key in bucket.list():
    print("{name}\t{size}\t{modified}".format(
        name=key.name,
        size=key.size,
        modified=key.last_modified,
    ))

conn.close()
