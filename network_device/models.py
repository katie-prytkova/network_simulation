from typing import Dict, Optional

from network_device.exceptions import VlanNotFoundError, RouteNotFoundError


class NetworkDevice:
    """Базовый класс для всех сетевых устройств."""

    def __init__(self, name: str, ip_address: str):
        self.name = name
        self.ip_address = ip_address
        self._status = "Inactive"

    @property
    def status(self) -> str:
        return self._status

    def power_on(self) -> None:
        """Включить устройство."""
        if self._status == "Active":
            print(f"{self.name} уже включён")
            return
        self._status = "Active"
        print(f"{self.name} включён")

    def power_off(self) -> None:
        """Выключить устройство."""
        if self._status == "Inactive":
            print(f"{self.name} уже выключен")
            return
        self._status = "Inactive"
        print(f"{self.name} выключен")

    def get_info(self) -> str:
        """Возвращает базовую информацию об устройстве."""
        return (
            f"{self.__class__.__name__}: {self.name}\n"
            f"IP Address: {self.ip_address}\n"
            f"Status: {self.status}"
        )


class Router(NetworkDevice):
    """Маршрутизатор."""

    def __init__(self, name: str, ip_address: str):
        super().__init__(name, ip_address)
        self.routing_table: Dict[str, str] = {}

    def add_route(self, destination: str, gateway: str) -> None:
        """Добавляет маршрут в таблицу маршрутизации."""
        self.routing_table[destination] = gateway
        print(f"Маршрут {destination}: {gateway} добавлен")

    def remove_route(self, destination: str) -> None:
        """Удаляет маршрут из таблицы."""
        if destination not in self.routing_table:
            raise RouteNotFoundError(f"Route to {destination} not found")

        del self.routing_table[destination]
        print(f"Маршрут {destination} удалён")

    def get_info(self) -> str:
        """Переопределённый метод с информацией о маршрутах."""
        base_info = super().get_info()
        return (
            f"{base_info}\n"
            f"Routing Table: {self.routing_table if self.routing_table else 'No routes'}"
        )


class Switch(NetworkDevice):
    """Коммутатор."""

    def __init__(self, name: str, ip_address: str):
        super().__init__(name, ip_address)
        self.vlan: Optional[int] = None

    def create_vlan(self, vlan_id: int) -> None:
        """Создаёт VLAN."""
        self.vlan = vlan_id
        print(f"VLAN {vlan_id} создан")

    def delete_vlan(self, vlan_id: int) -> None:
        """Удаляет VLAN."""
        if self.vlan != vlan_id:
            raise VlanNotFoundError(f"VLAN {vlan_id} not found")
        self.vlan = None
        print(f"VLAN {vlan_id} удалён")

    def get_info(self) -> str:
        """Переопределённый метод с информацией о VLAN."""
        base_info = super().get_info()
        return (
            f"{base_info}\n"
            f"VLAN: {self.vlan if self.vlan is not None else 'No VLAN'}"
        )
