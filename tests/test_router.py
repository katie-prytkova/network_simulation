from pyats import aetest

from network_device.exceptions import RouteNotFoundError
from network_device.models import Router, NetworkDevice


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def setup_router(self):
        self.parent.parameters['router'] = Router("Router1", "192.168.1.1")


class TestRouter(aetest.Testcase):

    @aetest.test
    def test_inheritance(self, router):
        assert isinstance(router, NetworkDevice)

    @aetest.test
    def test_add_route(self, router):
        router.add_route("192.168.2.0", "192.168.1.254")
        assert "192.168.2.0" in router.routing_table

    @aetest.test
    def test_get_info(self, router):
        router.add_route("192.168.2.0", "192.168.1.254")
        info = router.get_info()
        assert "Routing Table" in info

    @aetest.test
    def test_remove_route(self, router):
        router.add_route("10.0.0.0", "192.168.1.1")
        router.remove_route("10.0.0.0")
        assert "10.0.0.0" not in router.routing_table

    @aetest.test
    def test_remove_nonexistent_route(self, router):
        try:
            router.remove_route("10.0.0.0")
            assert False, "Должен быть RouteNotFoundError"
        except RouteNotFoundError:
            pass  # ожидаемое поведение
        except Exception as e:
            assert False, f"Ожидание: RouteNotFoundError, реальность: {type(e).__name__}"
