from dataclasses import dataclass

from . import SentralObject


@dataclass(init=False, slots=True)
class RelatedModel(SentralObject):
    id: str
    type: str

    def __init__(self, id: str | None = None, type: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class SingleRelationship(SentralObject):
    data: RelatedModel

    def __init__(self, data: RelatedModel | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CollectionRelationship(SentralObject):
    data: list[RelatedModel]

    def __init__(self, data: list[RelatedModel] | None = None, _data: dict | None = None):
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
        cycles: CollectionRelationship | None = None,
        instances: CollectionRelationship | None = None,
        organisers: CollectionRelationship | None = None,
        venue: SingleRelationship | None = None,
        category: SingleRelationship | None = None,
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
        student: SingleRelationship | None = None,
        activityInstance: SingleRelationship | None = None,
        activity: SingleRelationship | None = None,
        cycleInstance: SingleRelationship | None = None,
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
        activity: SingleRelationship | None = None,
        rolls: CollectionRelationship | None = None,
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
        activity: SingleRelationship | None = None,
        venues: CollectionRelationship | None = None,
        grounds: CollectionRelationship | None = None,
        coaches: CollectionRelationship | None = None,
        vehicles: CollectionRelationship | None = None,
        teams: CollectionRelationship | None = None,
        transportEvents: CollectionRelationship | None = None,
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
        activityInstance: SingleRelationship | None = None,
        staff: SingleRelationship | None = None,
        persion: SingleRelationship | None = None,
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
        attendeeStudent: SingleRelationship | None = None,
        coreConsentor: SingleRelationship | None = None,
        enrolmentConsentor: SingleRelationship | None = None,
        activityInstance: SingleRelationship | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityRollRelationships(SentralObject):
    activityInstance: SingleRelationship

    def __init__(
        self, activityInstance: SingleRelationship | None = None, _data: dict | None = None
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionRelationships(SentralObject):
    group: SingleRelationship

    def __init__(self, group: SingleRelationship | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionGroupRelationships(SentralObject):
    positions: CollectionRelationship

    def __init__(
        self, positions: CollectionRelationship | None = None, _data: dict | None = None
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
        person: SingleRelationship | None = None,
        emails: CollectionRelationship | None = None,
        phoneNumbers: CollectionRelationship | None = None,
        absences: SingleRelationship | None = None,
        qualifications: CollectionRelationship | None = None,
        employments: CollectionRelationship | None = None,
        staff: SingleRelationship | None = None,
        leaveType: SingleRelationship | None = None,
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
        primaryHousehold: SingleRelationship | None = None,
        studentPrimaryEnrolment: SingleRelationship | None = None,
        staff: SingleRelationship | None = None,
        student: SingleRelationship | None = None,
        contactDetails: SingleRelationship | None = None,
        otherHouseholds: SingleRelationship | None = None,
        studentContacts: SingleRelationship | None = None,
        studentTenants: SingleRelationship | None = None,
        prescribedMedication: CollectionRelationship | None = None,
        doctors: CollectionRelationship | None = None,
        associatedStudents: CollectionRelationship | None = None,
        emails: SingleRelationship | None = None,
        phoneNumbers: SingleRelationship | None = None,
        givenConsents: SingleRelationship | None = None,
        givenConsentLinks: SingleRelationship | None = None,
        emergencyContactLinks: SingleRelationship | None = None,
        abilities: SingleRelationship | None = None,
        additionalFields: CollectionRelationship | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsRelationships(SentralObject):
    venue: SingleRelationship

    def __init__(self, venue: SingleRelationship | None = None, _data: dict | None = None):
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
        activity: SingleRelationship | None = None,
        vehicle: SingleRelationship | None = None,
        sportEvent: SingleRelationship | None = None,
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
        activity: SingleRelationship | None = None,
        coaches: CollectionRelationship | None = None,
        teamMembers: CollectionRelationship | None = None,
        teamMemberPositions: CollectionRelationship | None = None,
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
        activity: SingleRelationship | None = None,
        transportEvents: CollectionRelationship | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffQualificationRelationships(SentralObject):
    staff: SingleRelationship

    def __init__(self, staff: SingleRelationship | None = None, _data: dict | None = None):
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
        relatedStudent: SingleRelationship | None = None,
        relatedStaff: SingleRelationship | None = None,
        relatedCoreStudent: SingleRelationship | None = None,
        relatedCoreStaff: SingleRelationship | None = None,
        relatedTimetableClass: SingleRelationship | None = None,
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
        group: SingleRelationship | None = None,
        grounds: CollectionRelationship | None = None,
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
        attendeeLink: SingleRelationship | None = None,
        team: SingleRelationship | None = None,
        position: SingleRelationship | None = None,
        cycleInstance: SingleRelationship | None = None,
        student: SingleRelationship | None = None,
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
        primaryEnrolment: SingleRelationship | None = None,
        person: SingleRelationship | None = None,
        emails: CollectionRelationship | None = None,
        phoneNumbers: CollectionRelationship | None = None,
        activities: CollectionRelationship | None = None,
        activityInstances: CollectionRelationship | None = None,
        activityLinks: CollectionRelationship | None = None,
        documents: CollectionRelationship | None = None,
        tenants: CollectionRelationship | None = None,
        flags: CollectionRelationship | None = None,
        flagLinks: CollectionRelationship | None = None,
        awards: CollectionRelationship | None = None,
        awardLinks: CollectionRelationship | None = None,
        contacts: CollectionRelationship | None = None,
        holidays: CollectionRelationship | None = None,
        specialNeedsPrograms: CollectionRelationship | None = None,
        schoolHistory: CollectionRelationship | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentDocumentRelationships(SentralObject):
    category: SingleRelationship

    def __init__(self, category: SingleRelationship | None = None, _data: dict | None = None):
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
        enrolmentStudent: SingleRelationship | None = None,
        additionalDetails: SingleRelationship | None = None,
        coreRollclass: SingleRelationship | None = None,
        attendedClasses: CollectionRelationship | None = None,
        holidays: CollectionRelationship | None = None,
        studentRelationships: CollectionRelationship | None = None,
        coreHouse: SingleRelationship | None = None,
        family: SingleRelationship | None = None,
        nonResidentialFamily: SingleRelationship | None = None,
        contacts: CollectionRelationship | None = None,
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
        student: SingleRelationship | None = None,
        house: SingleRelationship | None = None,
        rollclass: SingleRelationship | None = None,
        classes: CollectionRelationship | None = None,
        school: SingleRelationship | None = None,
        yearLevel: SingleRelationship | None = None,
        academicPeriod: SingleRelationship | None = None,
        campus: SingleRelationship | None = None,
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
        reaseon: SingleRelationship | None = None,
        enrolmentStudent: SingleRelationship | None = None,
        coreStudent: SingleRelationship | None = None,
        matchingFutureAbsence: SingleRelationship | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
