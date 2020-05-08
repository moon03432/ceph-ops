#### create realm, zonegroup, zone
``` sh
radosgw-admin realm create --rgw-realm=<realm-name> --default
radosgw-admin zonegroup create --rgw-zonegroup=<zonegroup-name>  --master --default
radosgw-admin zone create --rgw-zonegroup=<zonegroup-name> --rgw-zone=<zone-name> --master --default
```

#### deploy radosgw daemons for a particular realm and zone
``` sh
ceph orch apply rgw <realm> <zone> --placement=2
```

#### configure (stored in monitor configuration database)
``` sh
ceph config get client.rgw.test-realm.test-zone
ceph config set client.rgw.test-realm.test-zone
ceph orch restart/rm rgw.test-realm.test-zone
```

#### create user
``` sh
radosgw-admin user create --uid=<id> --display-name=<name>
radosgw-admin user list
radosgw-admin user info --uid=<id>
```

#### enable radosgw in dashboard
``` sh
radosgw-admin user create --uid=<id> --display-name=<name> --system
ceph dashboard set-rgw-api-access-key <access_key>
ceph dashboard set-rgw-api-secret-key <secret_key>
ceph dashboard set-rgw-api-ssl-verify False
ceph mgr module disable dashboard
ceph mgr module enable dashboard
```
