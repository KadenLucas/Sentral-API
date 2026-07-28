# pyright: reportArgumentType=false

from dataclasses import dataclass

from . import SentralObject


@dataclass(init=False, slots=True)
class RelatedModel(SentralObject):
    id: str
    type: str

    def __init__(self, id: str = None, type: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class SingleRelationship(SentralObject):
    data: RelatedModel

    def __init__(self, data: RelatedModel = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CollectionRelationship(SentralObject):
    data: list[RelatedModel]

    def __init__(self, data: list[RelatedModel] = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityRelationships(SentralObject):
    cycles: CollectionRelationship
    instances: CollectionRelationship
    organisers: CollectionRelationship
    venue: SingleRelationship
    category: SingleRelationship

    def __init__(
        self,
        cycles: CollectionRelationship = None,
        instances: CollectionRelationship = None,
        organisers: CollectionRelationship = None,
        venue: SingleRelationship = None,
        category: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AttendeeLinkRelationships(SentralObject):
    student: SingleRelationship
    activityInstance: SingleRelationship
    activity: SingleRelationship
    cycleInstance: SingleRelationship

    def __init__(
        self,
        student: SingleRelationship = None,
        activityInstance: SingleRelationship = None,
        activity: SingleRelationship = None,
        cycleInstance: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityInstanceRelationships(SentralObject):
    activity: SingleRelationship
    rolls: CollectionRelationship

    def __init__(
        self,
        activity: SingleRelationship = None,
        rolls: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivitySportEventRelationships(SentralObject):
    activity: SingleRelationship
    venues: CollectionRelationship
    grounds: CollectionRelationship
    coaches: CollectionRelationship
    vehicles: CollectionRelationship
    teams: CollectionRelationship
    transportEvents: CollectionRelationship

    def __init__(
        self,
        activity: SingleRelationship = None,
        venues: CollectionRelationship = None,
        grounds: CollectionRelationship = None,
        coaches: CollectionRelationship = None,
        vehicles: CollectionRelationship = None,
        teams: CollectionRelationship = None,
        transportEvents: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityGuardianLinkRelationships(SentralObject):
    activityInstance: SingleRelationship
    staff: SingleRelationship
    persion: SingleRelationship

    def __init__(
        self,
        activityInstance: SingleRelationship = None,
        staff: SingleRelationship = None,
        persion: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityResponseRelationships(SentralObject):
    attendeeStudent: SingleRelationship
    coreConsentor: SingleRelationship
    enrolmentConsentor: SingleRelationship
    activityInstance: SingleRelationship

    def __init__(
        self,
        attendeeStudent: SingleRelationship = None,
        coreConsentor: SingleRelationship = None,
        enrolmentConsentor: SingleRelationship = None,
        activityInstance: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityRollRelationships(SentralObject):
    activityInstance: SingleRelationship

    def __init__(
        self, activityInstance: SingleRelationship = None, _data: dict | None = None
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionRelationships(SentralObject):
    group: SingleRelationship

    def __init__(self, group: SingleRelationship = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionGroupRelationships(SentralObject):
    positions: CollectionRelationship

    def __init__(
        self, positions: CollectionRelationship = None, _data: dict | None = None
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffRelationships(SentralObject):
    person: SingleRelationship
    emails: CollectionRelationship
    phoneNumbers: CollectionRelationship
    absences: SingleRelationship
    qualifications: CollectionRelationship
    employments: CollectionRelationship


@dataclass(init=False, slots=True)
class StaffAbsenceRelationships(SentralObject):
    staff: SingleRelationship
    leaveType: SingleRelationship

    def __init__(
        self,
        person: SingleRelationship = None,
        emails: CollectionRelationship = None,
        phoneNumbers: CollectionRelationship = None,
        absences: SingleRelationship = None,
        qualifications: CollectionRelationship = None,
        employments: CollectionRelationship = None,
        staff: SingleRelationship = None,
        leaveType: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class PersonRelationships(SentralObject):
    primaryHousehold: SingleRelationship
    studentPrimaryEnrolment: SingleRelationship
    staff: SingleRelationship
    student: SingleRelationship
    contactDetails: SingleRelationship
    otherHouseholds: SingleRelationship
    studentContacts: SingleRelationship
    studentTenants: SingleRelationship
    prescribedMedication: CollectionRelationship
    doctors: CollectionRelationship
    associatedStudents: CollectionRelationship
    emails: SingleRelationship
    phoneNumbers: SingleRelationship
    givenConsents: SingleRelationship
    givenConsentLinks: SingleRelationship
    emergencyContactLinks: SingleRelationship
    abilities: SingleRelationship
    additionalFields: CollectionRelationship

    def __init__(
        self,
        primaryHousehold: SingleRelationship = None,
        studentPrimaryEnrolment: SingleRelationship = None,
        staff: SingleRelationship = None,
        student: SingleRelationship = None,
        contactDetails: SingleRelationship = None,
        otherHouseholds: SingleRelationship = None,
        studentContacts: SingleRelationship = None,
        studentTenants: SingleRelationship = None,
        prescribedMedication: CollectionRelationship = None,
        doctors: CollectionRelationship = None,
        associatedStudents: CollectionRelationship = None,
        emails: SingleRelationship = None,
        phoneNumbers: SingleRelationship = None,
        givenConsents: SingleRelationship = None,
        givenConsentLinks: SingleRelationship = None,
        emergencyContactLinks: SingleRelationship = None,
        abilities: SingleRelationship = None,
        additionalFields: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsRelationships(SentralObject):
    venue: SingleRelationship

    def __init__(self, venue: SingleRelationship = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTransportEventRelationships(SentralObject):
    activity: SingleRelationship
    vehicle: SingleRelationship
    sportEvent: SingleRelationship

    def __init__(
        self,
        activity: SingleRelationship = None,
        vehicle: SingleRelationship = None,
        sportEvent: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamRelationships(SentralObject):
    activity: SingleRelationship
    coaches: CollectionRelationship
    teamMembers: CollectionRelationship
    teamMemberPositions: CollectionRelationship

    def __init__(
        self,
        activity: SingleRelationship = None,
        coaches: CollectionRelationship = None,
        teamMembers: CollectionRelationship = None,
        teamMemberPositions: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityVehicleRelationships(SentralObject):
    activity: SingleRelationship
    transportEvents: CollectionRelationship

    def __init__(
        self,
        activity: SingleRelationship = None,
        transportEvents: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffQualificationRelationships(SentralObject):
    staff: SingleRelationship

    def __init__(self, staff: SingleRelationship = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class TimetableLessonRelationships(SentralObject):
    relatedStudent: SingleRelationship
    relatedStaff: SingleRelationship
    relatedCoreStudent: SingleRelationship
    relatedCoreStaff: SingleRelationship
    relatedTimetableClass: SingleRelationship

    def __init__(
        self,
        relatedStudent: SingleRelationship = None,
        relatedStaff: SingleRelationship = None,
        relatedCoreStudent: SingleRelationship = None,
        relatedCoreStaff: SingleRelationship = None,
        relatedTimetableClass: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueRelationships(SentralObject):
    group: SingleRelationship
    grounds: CollectionRelationship

    def __init__(
        self,
        group: SingleRelationship = None,
        grounds: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamMemberRelationships(SentralObject):
    attendeeLink: SingleRelationship
    team: SingleRelationship
    position: SingleRelationship
    cycleInstance: SingleRelationship
    student: SingleRelationship

    def __init__(
        self,
        attendeeLink: SingleRelationship = None,
        team: SingleRelationship = None,
        position: SingleRelationship = None,
        cycleInstance: SingleRelationship = None,
        student: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentRelationships(SentralObject):
    primaryEnrolment: SingleRelationship
    person: SingleRelationship
    emails: CollectionRelationship
    phoneNumbers: CollectionRelationship
    activities: CollectionRelationship
    activityInstances: CollectionRelationship
    activityLinks: CollectionRelationship
    documents: CollectionRelationship
    tenants: CollectionRelationship
    flags: CollectionRelationship
    flagLinks: CollectionRelationship
    awards: CollectionRelationship
    awardLinks: CollectionRelationship
    contacts: CollectionRelationship
    holidays: CollectionRelationship
    specialNeedsPrograms: CollectionRelationship
    schoolHistory: CollectionRelationship

    def __init__(
        self,
        primaryEnrolment: SingleRelationship = None,
        person: SingleRelationship = None,
        emails: CollectionRelationship = None,
        phoneNumbers: CollectionRelationship = None,
        activities: CollectionRelationship = None,
        activityInstances: CollectionRelationship = None,
        activityLinks: CollectionRelationship = None,
        documents: CollectionRelationship = None,
        tenants: CollectionRelationship = None,
        flags: CollectionRelationship = None,
        flagLinks: CollectionRelationship = None,
        awards: CollectionRelationship = None,
        awardLinks: CollectionRelationship = None,
        contacts: CollectionRelationship = None,
        holidays: CollectionRelationship = None,
        specialNeedsPrograms: CollectionRelationship = None,
        schoolHistory: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentDocumentRelationships(SentralObject):
    category: SingleRelationship

    def __init__(self, category: SingleRelationship = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CoreStudentRelationships(SentralObject):
    enrolmentStudent: SingleRelationship
    additionalDetails: SingleRelationship
    coreRollclass: SingleRelationship
    attendedClasses: CollectionRelationship
    holidays: CollectionRelationship
    studentRelationships: CollectionRelationship
    coreHouse: SingleRelationship
    family: SingleRelationship
    nonResidentialFamily: SingleRelationship
    contacts: CollectionRelationship

    def __init__(
        self,
        enrolmentStudent: SingleRelationship = None,
        additionalDetails: SingleRelationship = None,
        coreRollclass: SingleRelationship = None,
        attendedClasses: CollectionRelationship = None,
        holidays: CollectionRelationship = None,
        studentRelationships: CollectionRelationship = None,
        coreHouse: SingleRelationship = None,
        family: SingleRelationship = None,
        nonResidentialFamily: SingleRelationship = None,
        contacts: CollectionRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class EnrolmentRelationships(SentralObject):
    student: SingleRelationship
    house: SingleRelationship
    rollclass: SingleRelationship
    classes: CollectionRelationship
    school: SingleRelationship
    yearLevel: SingleRelationship
    academicPeriod: SingleRelationship
    campus: SingleRelationship

    def __init__(
        self,
        student: SingleRelationship = None,
        house: SingleRelationship = None,
        rollclass: SingleRelationship = None,
        classes: CollectionRelationship = None,
        school: SingleRelationship = None,
        yearLevel: SingleRelationship = None,
        academicPeriod: SingleRelationship = None,
        campus: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class HouseRelationships(SentralObject):
    students: CollectionRelationship
    school: SingleRelationship

    def __init__(
        self,
        students: CollectionRelationship,
        school: SingleRelationship,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AbsenceRelationships(SentralObject):
    reaseon: SingleRelationship
    enrolmentStudent: SingleRelationship
    coreStudent: SingleRelationship
    matchingFutureAbsence: SingleRelationship

    def __init__(
        self,
        reaseon: SingleRelationship = None,
        enrolmentStudent: SingleRelationship = None,
        coreStudent: SingleRelationship = None,
        matchingFutureAbsence: SingleRelationship = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
