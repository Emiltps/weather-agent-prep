from dataclasses import dataclass, field

# N.B Type hints aren't enforced when the code runs
@dataclass
class City:
    name: str
    lat: float
    lon: float
    tags: list[str] = field(default_factory=list)

berlin = City("Berlin", 52.52, 13.41 , ["Germany", "Europe", "Culture"])
print(berlin)                        # nice automatic __repr__
print(berlin == City("Berlin", 52.52, 13.41))   # automatic __eq__ -> True

broken = City("Paris", "not a number", 2.35)
print(broken.lat * 2)                # repeat sequence type because hints arnt enforced when the code runs