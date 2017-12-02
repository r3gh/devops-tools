import shade

cloud = shade.openstack_cloud(cloud='envvars')

print("\nListando imagens...")
images = cloud.list_images()
for image in images:
    print(image.id + '\t' + image.name)

print("\nListando sabores...")
flavors = cloud.list_flavors()
for flavor in flavors:
    print("{}\t{} vcpus \t{} MB  \t{}".format(flavor.id, flavor.vcpus, flavor.ram, flavor.name))
