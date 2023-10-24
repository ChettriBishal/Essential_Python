"""
Flight Leg:
GLA -> LHR -> CAN

2 segments (GLA -> LHR, LHR-> CAN)
"""

from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """

        :return:string format of GLA -> LHR -> CAN
        """
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return '->'.join(stops)

    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        # self.segments[0].departure = val

        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)


flight = Flight([Segment('GLA', 'LHR')])
# print(flight.departure_point)

print(flight)
# flight.segments[0].departure = 'EDI'  # changing is very difficult
flight.departure_point = 'DEL'

# flight.segments.append(Flight(Segment('DEL','SIL')))

print(flight)
