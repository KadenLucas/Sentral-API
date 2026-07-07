# pyright: reportAssignmentType=false

from dataclasses import dataclass
from typing import TYPE_CHECKING

from . import SentralObject

if TYPE_CHECKING:
    from . import objects


class Payload:
    __slots__ = []

    @property
    def __dict__(self):  # pyright: ignore[reportIncompatibleVariableOverride]
        output = dict()

        for slot in self.__slots__:
            value = getattr(self, slot)

            if isinstance(value, SentralObject):
                value = value.__dict__

            if value is not None:
                output[slot] = value

        return output


@dataclass(slots=True)
class ActivityInstanceAttendeeLinkPayload(Payload):
    data: objects.AttendeeLink = None


@dataclass(slots=True)
class ActivityInstanceActivityResponsePayload(Payload):
    data: objects.ActivityResponse = None


@dataclass(slots=True)
class StaffPayload(Payload):
    data: objects.Staff = None


@dataclass(slots=True)
class StudentPayload(Payload):
    data: objects.Student = None


@dataclass(slots=True)
class EnrolmentPayload(Payload):
    data: objects.Enrolment = None
