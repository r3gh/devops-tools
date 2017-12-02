import shade

cloud = shade.openstack_cloud(cloud='envvars')

print("Listando sabores...")
flavors = cloud.list_flavors()
for flavor in flavors:
    print("{}\t{} vcpus \t{} MB  \t{}".format(flavor.id, flavor.vcpus, flavor.ram, flavor.name))
