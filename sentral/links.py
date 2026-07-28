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
        first: str | None = None,
        last: str | None = None,
        prev: str | None = None,
        next: str | None = None,
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
        self_: str | None = None,
        cycles: str | None = None,
        instances: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CycleInstanceLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AttendeeLinkLinks(SentralObject):
    self_: str
    enrolmentAttendee: str

    def __init__(
        self,
        self_: str | None = None,
        enrolmentAttendee: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityInstanceLinks(SentralObject):
    self_: str
    rolls: str

    def __init__(self, self_: str | None = None, rolls: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivitySportEventLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityCategoryLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityGuardianLinkLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityResponseLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
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
        self_: str | None = None,
        activityInstance: str | None = None,
        uiMarkRolls: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionGroupLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
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
        self_: str | None = None,
        person: str | None = None,
        absences: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffAbsenceLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
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
        self_: str | None = None,
        primaryHousehold: str | None = None,
        otherHouseholds: str | None = None,
        staff: str | None = None,
        student: str | None = None,
        studentContacts: str | None = None,
        medicalSummary: str | None = None,
        medicalConditions: str | None = None,
        prescribedMedications: str | None = None,
        doctors: str | None = None,
        associatedStudents: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTransportEventLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityVehicleLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffQualificationLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamMemberLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
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
        self_: str | None = None,
        primaryEnrolment: str | None = None,
        person: str | None = None,
        activities: str | None = None,
        activityLinks: str | None = None,
        photo: str | None = None,
        documents: str | None = None,
        tenants: str | None = None,
        flags: str | None = None,
        flagLinks: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentDocumentLinks(SentralObject):
    self_: str
    file: str

    def __init__(self, self_: str | None = None, file: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CoreStudentLinks(SentralObject):
    self_: str

    def __init__(self, self_: str | None = None, _data: dict | None = None):
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
        self_: str | None = None,
        house: str | None = None,
        classes: str | None = None,
        rollclass: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
