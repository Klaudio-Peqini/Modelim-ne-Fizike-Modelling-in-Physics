from dataclasses import dataclass

@dataclass
class CrankRodParameters:
    r: float = 0.05
    l: float = 0.18
    omega: float = 12.0
    duration: float = 2.0
    n_points: int = 800

    def validate(self) -> None:
        if self.r <= 0 or self.l <= 0:
            raise ValueError("Parametrat gjeometrikë duhet të jenë pozitivë.")
        if self.l <= self.r:
            raise ValueError("Duhet të vlejë l > r që mekanizmi të jetë i realizueshëm.")
        if self.duration <= 0:
            raise ValueError("Kohëzgjatja duhet të jetë pozitive.")
        if self.n_points < 10:
            raise ValueError("Numri i pikave duhet të jetë të paktën 10.")
