# pyright: reportArgumentType=false

from dataclasses import dataclass

from . import SentralObject


@dataclass(init=False, slots=True)
class CollectionLinks(SentralObject):
    first: str
    last: str
    prev: str
    next: str

    def __init__(
        self,
        first: str = None,
        last: str = None,
        prev: str = None,
        next: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityLinks(SentralObject):
    self_: str
    cycles: str
    instances: str

    def __init__(
        self,
        self_: str = None,
        cycles: str = None,
        instances: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CycleInstanceLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AttendeeLinkLinks(SentralObject):
    self_: str
    enrolmentAttendee: str

    def __init__(
        self,
        self_: str = None,
        enrolmentAttendee: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityInstanceLinks(SentralObject):
    self_: str
    rolls: str

    def __init__(self, self_: str = None, rolls: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivitySportEventLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityCategoryLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityGuardianLinkLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityResponseLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityRollLinks(SentralObject):
    self_: str
    activityInstance: str
    uiMarkRolls: str

    def __init__(
        self,
        self_: str = None,
        activityInstance: str = None,
        uiMarkRolls: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionGroupLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffLinks(SentralObject):
    self_: str
    person: str
    absences: str

    def __init__(
        self,
        self_: str = None,
        person: str = None,
        absences: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffAbsenceLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class PersonLinks(SentralObject):
    self_: str
    primaryHousehold: str
    otherHouseholds: str
    staff: str
    student: str
    studentContacts: str
    medicalSummary: str
    medicalConditions: str
    prescribedMedications: str
    doctors: str
    associatedStudents: str

    def __init__(
        self,
        self_: str = None,
        primaryHousehold: str = None,
        otherHouseholds: str = None,
        staff: str = None,
        student: str = None,
        studentContacts: str = None,
        medicalSummary: str = None,
        medicalConditions: str = None,
        prescribedMedications: str = None,
        doctors: str = None,
        associatedStudents: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTransportEventLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityVehicleLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffQualificationLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamMemberLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentLinks(SentralObject):
    self_: str
    primaryEnrolment: str
    person: str
    activities: str
    activityLinks: str
    photo: str
    documents: str
    tenants: str
    flags: str
    flagLinks: str

    def __init__(
        self,
        self_: str = None,
        primaryEnrolment: str = None,
        person: str = None,
        activities: str = None,
        activityLinks: str = None,
        photo: str = None,
        documents: str = None,
        tenants: str = None,
        flags: str = None,
        flagLinks: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentDocumentLinks(SentralObject):
    self_: str
    file: str

    def __init__(self, self_: str = None, file: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CoreStudentLinks(SentralObject):
    self_: str

    def __init__(self, self_: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class EnrolmentLinks(SentralObject):
    self_: str
    house: str
    classes: str
    rollclass: str

    def __init__(
        self,
        self_: str = None,
        house: str = None,
        classes: str = None,
        rollclass: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
