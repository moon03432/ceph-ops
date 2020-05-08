import boto.s3.connection

hostname = 'shoyb17plpcdp160.mcd.com.cn'
port = 8080
conn = boto.connect_s3(
        host=hostname, port=port,
        is_secure=False, calling_format=boto.s3.connection.OrdinaryCallingFormat(),
       )

for bucket in conn.get_all_buckets():
    print("{name} {created}".format(
        name=bucket.name,
        created=bucket.creation_date,
    ))

conn.close()
