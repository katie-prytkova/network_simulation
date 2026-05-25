from pyats import aetest
from network_device.models import NetworkDevice


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def setup_device(self):
        self.parent.parameters['device'] = NetworkDevice("TestDevice", "192.168.1.100")


class TestNetworkDevice(aetest.Testcase):

    @aetest.test
    def test_creation(self, device):
        assert device.name == "TestDevice"
        assert device.ip_address == "192.168.1.100"
        assert device.status == "Inactive"

    @aetest.test
    def test_power_on_off(self, device):
        device.power_on()
        assert device.status == "Active"

        device.power_off()
        assert device.status == "Inactive"

    @aetest.test
    def test_get_info(self, device):
        info = device.get_info()

        assert "TestDevice" in info
        assert "192.168.1.100" in info
