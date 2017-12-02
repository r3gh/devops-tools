import shade

cloud = shade.openstack_cloud(cloud='envvars')

print("Listando imagens...")
images = cloud.list_images()
for image in images:
    print(image.id + '\t' + image.name)
