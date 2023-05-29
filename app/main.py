from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot():
    pass


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[list[int]] = None
    ) -> None:
        super().__init__(name, weight)
        self.coords = coords or [0, 0, 0]

    def go_up(self, steps: int = 1) -> None:
        self.go(2, 1, steps)

    def go_down(self, steps: int = 1) -> None:
        self.go(2, -1, steps)


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: Optional[list[int]] = None,
            current_load: Optional[int] = 0
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
