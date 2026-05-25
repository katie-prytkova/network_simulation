from network_device.models import Router, Switch


router1 = Router("Router1", "192.168.1.1")
router2 = Router("Router2", "192.168.1.2")

switch1 = Switch("Switch1", "192.168.1.3")
switch2 = Switch("Switch2", "192.168.1.4")


router1.power_on()
router1.add_route("192.168.2.0", "192.168.1.254")

switch1.power_on()
switch1.create_vlan(10)

router2.power_on()
switch2.power_on()


print()
print(router1.get_info(), end="\n\n")
print(router2.get_info(), end="\n\n")

print(switch1.get_info(), end="\n\n")
print(switch2.get_info(), end="\n\n")


router1.remove_route("192.168.2.0")
switch1.delete_vlan(10)

router1.power_off()
router2.power_off()

switch1.power_off()
switch2.power_off()
