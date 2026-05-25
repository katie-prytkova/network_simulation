class NetworkDeviceError(Exception):
    """Базовое исключение для сетевых устройств."""
    pass


class RouteNotFoundError(NetworkDeviceError):
    """Вызывается при попытке удалить несуществующий маршрут."""
    pass


class VlanNotFoundError(NetworkDeviceError):
    """Вызывается при попытке удалить несуществующий VLAN."""
    pass
