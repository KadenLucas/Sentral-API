from dataclasses import dataclass

from . import SentralObject, objects


class Payload:
    __slots__ = []

    @property
    def __dict__(self):  # pyright: ignore[reportIncompatibleVariableOverride]
        output = {}

        for slot in self.__slots__:
            value = getattr(self, slot)

            if isinstance(value, SentralObject):
                value = value.__dict__

            if value is not None:
                output[slot] = value

        return output


@dataclass(slots=True)
class ActivityInstanceAttendeeLinkPayload(Payload):
    data: objects.AttendeeLink | None = None


@dataclass(slots=True)
class ActivityInstanceActivityResponsePayload(Payload):
    data: objects.ActivityResponse | None = None


@dataclass(slots=True)
class StaffPayload(Payload):
    data: objects.Staff | None = None


@dataclass(slots=True)
class StudentPayload(Payload):
    data: objects.Student | None = None


@dataclass(slots=True)
class EnrolmentPayload(Payload):
    data: objects.Enrolment | None = None
