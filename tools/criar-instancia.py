import shade

cloud = shade.openstack_cloud(cloud='envvars')

print("\nAdicionando chave SSH...")
keypair_name = 'r3gh-sshkey'
pub_key = open('.ssh/id_rsa.pub', 'r').read().strip()
if not cloud.search_keypairs(keypair_name):
    cloud.create_keypair(keypair_name, pub_key)
print("A chave \'{}\' foi adicionada!".format(keypair_name))

print("\nAbrindo portas...")
sec_group_name = 'r3gh-group'
ports = [22, 80, 5432, 8080]
if not cloud.search_security_groups(sec_group_name):
    cloud.create_security_group(sec_group_name, 'Grupo de acesso a network')
    for port in ports:
        cloud.create_security_group_rule(sec_group_name, port, port, 'TCP')
print("As portas [{}] foram abertas no grupo \'{}\'!".format(', '.join(str(p) for p in ports),
                                                             sec_group_name))

print("\nCriando rede privada...")
network_name = 'r3gh-network'
if not cloud.search_networks(network_name):
    cloud.create_network(network_name)
print("Rede privada '{}' criada!".format(network_name))

print("\nCriando sub-rede...")
subnet_name = 'r3gh-subnet'
if not cloud.search_subnets(subnet_name):
    cloud.create_subnet(network_name,
                        subnet_name=subnet_name,
                        enable_dhcp=True,
                        cidr='192.168.0.0/24',
                        gateway_ip='192.168.0.1',
                        dns_nameservers=['9.9.9.9'])
print("Sub-rede '{}' criada!".format(subnet_name))

print("\nCriando roteador...")
router_name = 'r3gh-router'
public_network_id = cloud.get_network('public_network').id
if not cloud.search_routers(router_name):
    cloud.create_router(name=router_name,
                        enable_snat=True,
                        ext_gateway_net_id=public_network_id)
print("Roteador '{}' criado!".format(router_name))

print("\nCriando interface do roteador...")
router_dict = cloud.get_router(router_name)
subnet_id = cloud.get_subnet(subnet_name).id
if not cloud.list_router_interfaces(router_dict):
    cloud.add_router_interface(router_dict, subnet_id=subnet_id)
print("Interface criada para o roteador '{}'!".format(router_name))

print("Levantando uma instância...")
image_name = 'Ubuntu 16.04 LTS Xenial'
flavor_name = 'm1.large'
instance_name = 'hackathonRioHeatMap'
image = cloud.get_image(image_name)
flavor = cloud.get_flavor(flavor_name)
network = cloud.get_network(network_name)
ex_userdata = open('./scripts/run.sh', 'r').read()

cloud.create_server(instance_name,
                    image=image_name,
                    flavor=flavor_name,
                    wait=True,
                    auto_ip=True,
                    key_name=keypair_name,
                    security_groups=[sec_group_name],
                    network=network_name,
                    userdata=ex_userdata)
print("Imagem '{}' de '{}' com {} vcpus e {} MB de RAM na rede '{}'!".format(instance_name,
                                                                             image.name,
                                                                             flavor.vcpus,
                                                                             flavor.ram,
                                                                             network.name))
