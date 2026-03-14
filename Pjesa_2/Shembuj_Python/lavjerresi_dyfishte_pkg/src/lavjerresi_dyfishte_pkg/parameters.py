from dataclasses import dataclass

@dataclass
class DoublePendulumParameters:
    m1: float = 1.0
    m2: float = 1.0
    l1: float = 1.0
    l2: float = 1.0
    g: float = 9.81
    theta1: float = 0.6
    theta2: float = 0.2
    omega1: float = 0.0
    omega2: float = 0.0
    duration: float = 10.0
    n_points: int = 1500

    def validate(self) -> None:
        for value in (self.m1, self.m2, self.l1, self.l2, self.g, self.duration):
            if value <= 0:
                raise ValueError("Masat, gjatësitë, g dhe kohëzgjatja duhet të jenë pozitive.")
        if self.n_points < 50:
            raise ValueError("Numri i pikave duhet të jetë të paktën 50.")
