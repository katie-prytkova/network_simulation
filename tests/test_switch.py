from pyats import aetest

from network_device.exceptions import VlanNotFoundError
from network_device.models import Switch, NetworkDevice


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def setup_switch(self):
        self.parent.parameters['switch'] = Switch("Switch1", "192.168.1.2")


class TestSwitch(aetest.Testcase):

    @aetest.test
    def test_inheritance(self, switch):
        assert isinstance(switch, NetworkDevice)

    @aetest.test
    def test_create_vlan(self, switch):
        switch.create_vlan(10)
        assert switch.vlan == 10

    @aetest.test
    def test_get_info(self, switch):
        switch.create_vlan(20)
        info = switch.get_info()
        assert "VLAN:" in info

    @aetest.test
    def test_delete_vlan(self, switch):
        switch.create_vlan(10)
        switch.delete_vlan(10)

        assert switch.vlan is None

    @aetest.test
    def test_delete_nonexistent_vlan(self, switch):
        try:
            switch.delete_vlan(999)
            assert False, "Должен быть VlanNotFoundError"
        except VlanNotFoundError:
            pass  # ожидаемое поведение
        except Exception as e:
            assert False, f"Ожидание: VlanNotFoundError, реальность: {type(e).__name__}"
