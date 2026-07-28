import datetime
from dataclasses import dataclass

from . import SentralObject, objects


@dataclass(init=False, slots=True)
class ActivityAttributes(SentralObject):
    name: str
    reportName: str
    description: str
    startDate: datetime.date
    endDate: datetime.date
    startTime: datetime.time
    endTime: datetime.time
    permissionFormDueDate: datetime.date
    isRestrictedByTerm: bool
    isRestrictedByYear: bool
    showReports: bool
    showAttendance: bool
    showPortal: bool
    selfRegistration: bool
    approvalRequired: bool
    maximumPlaces: int
    waitingListPlaces: int
    archived: datetime.date
    riskAssessment: bool
    registrationType: str
    portalDescription: str
    availableTerms: list[int]
    availableYears: list[str]
    isActive: bool

    def __init__(
        self,
        name: str | None = None,
        reportName: str | None = None,
        description: str | None = None,
        startDate: datetime.date | None = None,
        endDate: datetime.date | None = None,
        startTime: datetime.time | None = None,
        endTime: datetime.time | None = None,
        permissionFormDueDate: datetime.date | None = None,
        isRestrictedByTerm: bool | None = None,
        isRestrictedByYear: bool | None = None,
        showReports: bool | None = None,
        showAttendance: bool | None = None,
        showPortal: bool | None = None,
        selfRegistration: bool | None = None,
        approvalRequired: bool | None = None,
        maximumPlaces: int | None = None,
        waitingListPlaces: int | None = None,
        archived: datetime.date | None = None,
        riskAssessment: bool | None = None,
        registrationType: str | None = None,
        portalDescription: str | None = None,
        availableTerms: list[int] | None = None,
        availableYears: list[str] | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CycleInstanceAttributes(SentralObject):
    name: str
    year: int
    cycle: str
    period: str

    def __init__(
        self,
        name: str | None = None,
        year: int | None = None,
        cycle: str | None = None,
        period: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AttendeeLinkAttributes(SentralObject):
    attendeeType: str
    showInReports: bool
    points: int
    permissionGiven: bool
    paid: bool
    paidAmount: str

    def __init__(
        self,
        attendeeType: str | None = None,
        showInReports: bool | None = None,
        points: int | None = None,
        permissionGiven: bool | None = None,
        paid: bool | None = None,
        paidAmount: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityInstanceAttributes(SentralObject):
    status: str
    year: int
    name: str
    startDate: datetime.date
    endDate: datetime.date
    startTime: datetime.time
    endTime: datetime.time
    isPublishedToPortal: bool
    isPaymentRequired: bool
    isPermissionRequired: bool
    isActive: bool

    def __init__(
        self,
        status: str | None = None,
        year: int | None = None,
        name: str | None = None,
        startDate: datetime.date | None = None,
        endDate: datetime.date | None = None,
        startTime: datetime.time | None = None,
        endTime: datetime.time | None = None,
        isPublishedToPortal: bool | None = None,
        isPaymentRequired: bool | None = None,
        isPermissionRequired: bool | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivitySportEventAttributes(SentralObject):
    name: str
    description: str
    startDateTime: datetime.datetime
    endDateTime: datetime.datetime
    placeType: str
    opposition: str
    playersType: str
    type: str
    isActive: bool

    def __init__(
        self,
        name: str | None = None,
        description: str | None = None,
        startDateTime: datetime.datetime | None = None,
        endDateTime: datetime.datetime | None = None,
        placeType: str | None = None,
        opposition: str | None = None,
        playersType: str | None = None,
        type: str | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityCategoryAttributes(SentralObject):
    name: str
    type: str

    def __init__(self, name: str | None = None, type: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityGuardianLinkAttributes(SentralObject):
    startTime: datetime.time
    endTime: datetime.time

    def __init__(
        self,
        startTime: datetime.time | None = None,
        endTime: datetime.time | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityResponseAttributes(SentralObject):
    additionalNotes: str
    medicalDetails: str
    emergencyContactDetails: str
    consentedAt: objects.CompositeTime
    consentedBy: str
    permissionGiven: str
    isPaid: bool

    def __init__(
        self,
        additionalNotes: str | None = None,
        medicalDetails: str | None = None,
        emergencyContactDetails: str | None = None,
        consentedAt: objects.CompositeTime | None = None,
        consentedBy: str | None = None,
        permissionGiven: str | None = None,
        isPaid: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityRollAttributes(SentralObject):
    name: str
    rollDate: str
    isSubmitted: bool

    def __init__(
        self,
        name: str | None = None,
        rollDate: str | None = None,
        isSubmitted: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionAttributes(SentralObject):
    name: str

    def __init__(self, name: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionGroupAttributes(SentralObject):
    name: str

    def __init__(self, name: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffAttributes(SentralObject):
    staffCode: str
    timetableCode: str
    barcode: str
    createdAt: objects.CompositeTime
    updatedAt: objects.CompositeTime
    isActive: bool

    def __init__(
        self,
        staffCode: str | None = None,
        timetableCode: str | None = None,
        barcode: str | None = None,
        createdAt: objects.CompositeTime | None = None,
        updatedAt: objects.CompositeTime | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffAbsenceAttributes(SentralObject):
    type: str
    startDate: datetime.date
    endDate: datetime.date
    startTime: datetime.time
    endTime: datetime.time
    reason: str
    notes: str
    hasReceivedMedicalCertificate: bool
    externalSource: str
    externalId: str
    isApproved: bool

    def __init__(
        self,
        type: str | None = None,
        startDate: datetime.date | None = None,
        endDate: datetime.date | None = None,
        startTime: datetime.time | None = None,
        endTime: datetime.time | None = None,
        reason: str | None = None,
        notes: str | None = None,
        hasReceivedMedicalCertificate: bool | None = None,
        externalSource: str | None = None,
        externalId: str | None = None,
        isApproved: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class PersonAttributes(SentralObject):
    externalId: str
    refId: str
    contactCode: str
    firstName: str
    middleNames: str
    lastName: str
    legalLastName: str
    title: str
    preferredName: str
    gender: str
    genderDescription: str
    genderCode: str
    dateOfBirth: datetime.date
    dateOfDeath: datetime.date
    crn: str
    otherLanguage: str
    otherLanguageCode: str
    languageSpokenAtHome: str
    languageSpokenAtHomeCode: str
    indigenousStatus: str
    indigenousStatusCode: str
    nationality: str
    nationalityCode: str
    countryOfCitizenship: str
    countryOfCitizenshipCode: str
    religion: str
    religionCode: str
    countryOfBirth: str
    countryOfBirthCode: str
    ethnicGroup: str
    ethnicGroupCode: str
    placeOfBirth: str
    residentialStatus: str
    residentialStatusCode: str
    isDeceased: bool
    createdAt: objects.CompositeTime
    updatedAt: objects.CompositeTime
    isActive: bool

    def __init__(
        self,
        externalId: str | None = None,
        refId: str | None = None,
        contactCode: str | None = None,
        firstName: str | None = None,
        middleNames: str | None = None,
        lastName: str | None = None,
        legalLastName: str | None = None,
        title: str | None = None,
        preferredName: str | None = None,
        gender: str | None = None,
        genderDescription: str | None = None,
        genderCode: str | None = None,
        dateOfBirth: datetime.date | None = None,
        dateOfDeath: datetime.date | None = None,
        crn: str | None = None,
        otherLanguage: str | None = None,
        otherLanguageCode: str | None = None,
        languageSpokenAtHome: str | None = None,
        languageSpokenAtHomeCode: str | None = None,
        indigenousStatus: str | None = None,
        indigenousStatusCode: str | None = None,
        nationality: str | None = None,
        nationalityCode: str | None = None,
        countryOfCitizenship: str | None = None,
        countryOfCitizenshipCode: str | None = None,
        religion: str | None = None,
        religionCode: str | None = None,
        countryOfBirth: str | None = None,
        countryOfBirthCode: str | None = None,
        ethnicGroup: str | None = None,
        ethnicGroupCode: str | None = None,
        placeOfBirth: str | None = None,
        residentialStatus: str | None = None,
        residentialStatusCode: str | None = None,
        isDeceased: bool | None = None,
        createdAt: objects.CompositeTime | None = None,
        updatedAt: objects.CompositeTime | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsAttributes(SentralObject):
    name: str

    def __init__(self, name: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTransportEventAttributes(SentralObject):
    date: datetime.date
    time: datetime.time
    type: str

    def __init__(
        self,
        date: datetime.date | None = None,
        time: datetime.time | None = None,
        type: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamAttributes(SentralObject):
    name: str

    def __init__(self, name: str | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityVehicleAttributes(SentralObject):
    name: str
    description: str
    useDate: datetime.date
    vehicleIdentifier: str
    capacity: int
    type: str

    def __init__(
        self,
        name: str | None = None,
        description: str | None = None,
        useDate: datetime.date | None = None,
        vehicleIdentifier: str | None = None,
        capacity: int | None = None,
        type: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffQualificationAttributes(SentralObject):
    qualification: str
    type: str
    from_: str
    aitsTeacherAccreditationLevel: str
    nextAitsTeacherAccreditationLevel: str
    dateAchieved: datetime.date
    isActive: bool

    def __init__(
        self,
        qualification: str | None = None,
        type: str | None = None,
        from_: str | None = None,
        aitsTeacherAccreditationLevel: str | None = None,
        nextAitsTeacherAccreditationLevel: str | None = None,
        dateAchieved: datetime.date | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class TimetableLessonAttributes(SentralObject):
    className: str
    subject: str
    roomName: str
    teacherName: str
    teacherIds: list[int]
    date: datetime.date
    dayName: str
    dayOrder: str
    periodName: str
    periodOrder: int
    startTime: datetime.time
    endTime: datetime.time
    colour: str
    classType: str
    rollMarkingUrl: str

    def __init__(
        self,
        className: str | None = None,
        subject: str | None = None,
        roomName: str | None = None,
        teacherName: str | None = None,
        teacherIds: list[int] | None = None,
        date: datetime.date | None = None,
        dayName: str | None = None,
        dayOrder: str | None = None,
        periodName: str | None = None,
        periodOrder: int | None = None,
        startTime: datetime.time | None = None,
        endTime: datetime.time | None = None,
        colour: str | None = None,
        classType: str | None = None,
        rollMarkingUrl: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueAttributes(SentralObject):
    name: str
    address: str
    mapUrl: str

    def __init__(
        self,
        name: str | None = None,
        address: str | None = None,
        mapUrl: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamMemberAttributes(SentralObject):
    is_active: bool

    def __init__(self, is_active: bool | None = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentAttributes(SentralObject):
    studentCode: str
    barcode: str
    isEligibleForDiscount: bool
    permissionToPhotograph: bool
    examNumber: str
    usiId: str
    acaraId: str
    systemStudentId: str
    username: str
    ealStage: str
    ealIsReceivingSupport: bool
    ealLastAssessmentAt: str
    isSubjectToCourtOrders: bool
    courtOrderInformation: str
    studentFirstLanguage: str
    studentFirstLanguageDesc: str
    languageOtherThanEnglishSpokenAtHome: bool
    studentMainlySpeaksEnglishAtHome: bool
    loteBackground: str
    isPayingInternationalFee: bool
    cpsfIsInCare: bool
    cpsfCaseManager: str
    cpsfDistrict: str
    cpsfContactNumber: str
    createdAt: objects.CompositeTime
    updatedAt: objects.CompositeTime
    isActive: bool

    def __init__(
        self,
        studentCode: str | None = None,
        barcode: str | None = None,
        isEligibleForDiscount: bool | None = None,
        permissionToPhotograph: bool | None = None,
        examNumber: str | None = None,
        usiId: str | None = None,
        acaraId: str | None = None,
        systemStudentId: str | None = None,
        username: str | None = None,
        ealStage: str | None = None,
        ealIsReceivingSupport: bool | None = None,
        ealLastAssessmentAt: str | None = None,
        isSubjectToCourtOrders: bool | None = None,
        courtOrderInformation: str | None = None,
        studentFirstLanguage: str | None = None,
        studentFirstLanguageDesc: str | None = None,
        languageOtherThanEnglishSpokenAtHome: bool | None = None,
        studentMainlySpeaksEnglishAtHome: bool | None = None,
        loteBackground: str | None = None,
        isPayingInternationalFee: bool | None = None,
        cpsfIsInCare: bool | None = None,
        cpsfCaseManager: str | None = None,
        cpsfDistrict: str | None = None,
        cpsfContactNumber: str | None = None,
        createdAt: objects.CompositeTime | None = None,
        updatedAt: objects.CompositeTime | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentDocumentAttributes(SentralObject):
    fileName: str
    isConfidential: bool

    def __init__(
        self,
        fileName: str | None = None,
        isConfidential: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CoreStudentAttributes(SentralObject):
    firstName: str
    lastName: str
    preferredName: str
    gender: str
    barcode: str
    examId: str
    schoolYear: str
    dateOfBirth: datetime.date
    allergies: list[str]
    medicalConditions: list[str]
    externalId: str
    externalSource: str
    username: str
    email: str
    mobile: str
    refId: str
    eslSupportNeeded: bool
    eslDateAssessed: datetime.date
    isEslSupportReceived: bool
    enrolDate: datetime.date
    createdAt: objects.CompositeTime
    updatedAt: objects.CompositeTime
    isActive: bool
    indigenousStatus: str

    def __init__(
        self,
        firstName: str | None = None,
        lastName: str | None = None,
        preferredName: str | None = None,
        gender: str | None = None,
        barcode: str | None = None,
        examId: str | None = None,
        schoolYear: str | None = None,
        dateOfBirth: datetime.date | None = None,
        allergies: list[str] | None = None,
        medicalConditions: list[str] | None = None,
        externalId: str | None = None,
        externalSource: str | None = None,
        username: str | None = None,
        email: str | None = None,
        mobile: str | None = None,
        refId: str | None = None,
        eslSupportNeeded: bool | None = None,
        eslDateAssessed: datetime.date | None = None,
        isEslSupportReceived: bool | None = None,
        enrolDate: datetime.date | None = None,
        createdAt: objects.CompositeTime | None = None,
        updatedAt: objects.CompositeTime | None = None,
        isActive: bool | None = None,
        indigenousStatus: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class EnrolmentAttributes(SentralObject):
    startDate: datetime.date
    endDate: datetime.date
    status: str
    school: str
    schoolYear: str
    rollClass: str
    isBoarding: bool
    boardingHouse: str
    tutorGroup: str
    fteAmount: float
    createdAt: objects.CompositeTime
    updatedAt: objects.CompositeTime
    isActive: bool

    def __init__(
        self,
        startDate: datetime.date | None = None,
        endDate: datetime.date | None = None,
        status: str | None = None,
        school: str | None = None,
        schoolYear: str | None = None,
        rollClass: str | None = None,
        isBoarding: bool | None = None,
        boardingHouse: str | None = None,
        tutorGroup: str | None = None,
        fteAmount: float | None = None,
        createdAt: objects.CompositeTime | None = None,
        updatedAt: objects.CompositeTime | None = None,
        isActive: bool | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class HouseAttributes(SentralObject):
    name: str
    sequence: int

    def __init__(
        self, name: str | None = None, sequence: int | None = None, _data: dict | None = None
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AbsenceAttributes(SentralObject):
    type: str
    date: str
    start: str
    end: str
    comment: str
    explainer: str
    explainerSource: str
    letterSent: bool
    bulkAbsenceId: bool  # Should be a string?
    submitted: bool
    externalSource: str

    def __init__(
        self,
        type: str | None = None,
        date: str | None = None,
        start: str | None = None,
        end: str | None = None,
        comment: str | None = None,
        explainer: str | None = None,
        explainerSource: str | None = None,
        letterSent: bool | None = None,
        bulkAbsenceId: bool | None = None,
        submitted: bool | None = None,
        externalSource: str | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
