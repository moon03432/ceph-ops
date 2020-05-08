#### initialize storage pool
rbd pool init <pool>

#### create pool/image (4G)
rbd create <image> --size 4096 --image-feature layering -p <pool>

#### map image to the kernel's block device
rbd map <image> --name client.admin -p <pool>
