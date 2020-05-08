#### bootstrap
cephadm bootstrap --mon-ip 10.126.146.150 --allow-fqdn-hostname --skip-pull --skip-monitoring-stack --allow-overwrite --dashboard-key /home/cdp_user/ceph-install/certs/shoya17plpcdp150.mcd.com.cn.key --dashboard-crt /home/cdp_user/ceph-install/certs/shoya17plpcdp150.mcd.com.cn.crt

#### add hosts
for host in {shoya17plpcdp151.mcd.com.cn,shoya17plpcdp152.mcd.com.cn,shoya18plpcdp153.mcd.com.cn,shoya18plpcdp154.mcd.com.cn,shoya18plpcdp155.mcd.com.cn,shoya19plpcdp156.mcd.com.cn,shoya19plpcdp157.mcd.com.cn,shoya19plpcdp158.mcd.com.cn,shoyb17plpcdp159.mcd.com.cn,shoyb17plpcdp160.mcd.com.cn}; do ceph orch host add $host; done

#### add osd
for host in {shoya17plpcdp150.mcd.com.cn,shoya17plpcdp151.mcd.com.cn,shoya17plpcdp152.mcd.com.cn,shoya18plpcdp153.mcd.com.cn,shoya18plpcdp154.mcd.com.cn,shoya18plpcdp155.mcd.com.cn,shoya19plpcdp156.mcd.com.cn,shoya19plpcdp157.mcd.com.cn,shoya19plpcdp158.mcd.com.cn,shoyb17plpcdp159.mcd.com.cn,shoyb17plpcdp160.mcd.com.cn}; do for device in {sda,sdb,sdc};do ceph orch daemon add osd $host:/dev/$device; done; done

#### get public key
ceph cephadm get-pub-key
