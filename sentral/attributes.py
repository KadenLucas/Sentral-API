# pyright: reportArgumentType=false

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
        name: str = None,
        reportName: str = None,
        description: str = None,
        startDate: datetime.date = None,
        endDate: datetime.date = None,
        startTime: datetime.time = None,
        endTime: datetime.time = None,
        permissionFormDueDate: datetime.date = None,
        isRestrictedByTerm: bool = None,
        isRestrictedByYear: bool = None,
        showReports: bool = None,
        showAttendance: bool = None,
        showPortal: bool = None,
        selfRegistration: bool = None,
        approvalRequired: bool = None,
        maximumPlaces: int = None,
        waitingListPlaces: int = None,
        archived: datetime.date = None,
        riskAssessment: bool = None,
        registrationType: str = None,
        portalDescription: str = None,
        availableTerms: list[int] = None,
        availableYears: list[str] = None,
        isActive: bool = None,
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
        name: str = None,
        year: int = None,
        cycle: str = None,
        period: str = None,
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
        attendeeType: str = None,
        showInReports: bool = None,
        points: int = None,
        permissionGiven: bool = None,
        paid: bool = None,
        paidAmount: str = None,
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
        status: str = None,
        year: int = None,
        name: str = None,
        startDate: datetime.date = None,
        endDate: datetime.date = None,
        startTime: datetime.time = None,
        endTime: datetime.time = None,
        isPublishedToPortal: bool = None,
        isPaymentRequired: bool = None,
        isPermissionRequired: bool = None,
        isActive: bool = None,
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
        name: str = None,
        description: str = None,
        startDateTime: datetime.datetime = None,
        endDateTime: datetime.datetime = None,
        placeType: str = None,
        opposition: str = None,
        playersType: str = None,
        type: str = None,
        isActive: bool = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityCategoryAttributes(SentralObject):
    name: str
    type: str

    def __init__(self, name: str = None, type: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityGuardianLinkAttributes(SentralObject):
    startTime: datetime.time
    endTime: datetime.time

    def __init__(
        self,
        startTime: datetime.time = None,
        endTime: datetime.time = None,
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
        additionalNotes: str = None,
        medicalDetails: str = None,
        emergencyContactDetails: str = None,
        consentedAt: objects.CompositeTime = None,
        consentedBy: str = None,
        permissionGiven: str = None,
        isPaid: bool = None,
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
        name: str = None,
        rollDate: str = None,
        isSubmitted: bool = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionAttributes(SentralObject):
    name: str

    def __init__(self, name: str = None, _data: dict | None = None):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionGroupAttributes(SentralObject):
    name: str

    def __init__(self, name: str = None, _data: dict | None = None):
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
        staffCode: str = None,
        timetableCode: str = None,
        barcode: str = None,
        createdAt: objects.CompositeTime = None,
        updatedAt: objects.CompositeTime = None,
        isActive: bool = None,
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
        type: str = None,
        startDate: datetime.date = None,
        endDate: datetime.date = None,
        startTime: datetime.time = None,
        endTime: datetime.time = None,
        reason: str = None,
        notes: str = None,
        hasReceivedMedicalCertificate: bool = None,
        externalSource: str = None,
        externalId: str = None,
        isApproved: bool = None,
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
        externalId: str = None,
        refId: str = None,
        contactCode: str = None,
        firstName: str = None,
        middleNames: str = None,
        lastName: str = None,
        legalLastName: str = None,
        title: str = None,
        preferredName: str = None,
        gender: str = None,
        genderDescription: str = None,
        genderCode: str = None,
        dateOfBirth: datetime.date = None,
        dateOfDeath: datetime.date = None,
        crn: str = None,
        otherLanguage: str = None,
        otherLanguageCode: str = None,
        languageSpokenAtHome: str = None,
        languageSpokenAtHomeCode: str = None,
        indigenousStatus: str = None,
        indigenousStatusCode: str = None,
        nationality: str = None,
        nationalityCode: str = None,
        countryOfCitizenship: str = None,
        countryOfCitizenshipCode: str = None,
        religion: str = None,
        religionCode: str = None,
        countryOfBirth: str = None,
        countryOfBirthCode: str = None,
        ethnicGroup: str = None,
        ethnicGroupCode: str = None,
        placeOfBirth: str = None,
        residentialStatus: str = None,
        residentialStatusCode: str = None,
        isDeceased: bool = None,
        createdAt: objects.CompositeTime = None,
        updatedAt: objects.CompositeTime = None,
        isActive: bool = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsAttributes(SentralObject):
    name: str

    def __init__(self, name: str = None, _data: dict | None = None):
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
        date: datetime.date = None,
        time: datetime.time = None,
        type: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamAttributes(SentralObject):
    name: str

    def __init__(self, name: str = None, _data: dict | None = None):
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
        name: str = None,
        description: str = None,
        useDate: datetime.date = None,
        vehicleIdentifier: str = None,
        capacity: int = None,
        type: str = None,
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
        qualification: str = None,
        type: str = None,
        from_: str = None,
        aitsTeacherAccreditationLevel: str = None,
        nextAitsTeacherAccreditationLevel: str = None,
        dateAchieved: datetime.date = None,
        isActive: bool = None,
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
        className: str = None,
        subject: str = None,
        roomName: str = None,
        teacherName: str = None,
        teacherIds: list[int] = None,
        date: datetime.date = None,
        dayName: str = None,
        dayOrder: str = None,
        periodName: str = None,
        periodOrder: int = None,
        startTime: datetime.time = None,
        endTime: datetime.time = None,
        colour: str = None,
        classType: str = None,
        rollMarkingUrl: str = None,
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
        name: str = None,
        address: str = None,
        mapUrl: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamMemberAttributes(SentralObject):
    is_active: bool

    def __init__(self, is_active: bool = None, _data: dict | None = None):
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
        studentCode: str = None,
        barcode: str = None,
        isEligibleForDiscount: bool = None,
        permissionToPhotograph: bool = None,
        examNumber: str = None,
        usiId: str = None,
        acaraId: str = None,
        systemStudentId: str = None,
        username: str = None,
        ealStage: str = None,
        ealIsReceivingSupport: bool = None,
        ealLastAssessmentAt: str = None,
        isSubjectToCourtOrders: bool = None,
        courtOrderInformation: str = None,
        studentFirstLanguage: str = None,
        studentFirstLanguageDesc: str = None,
        languageOtherThanEnglishSpokenAtHome: bool = None,
        studentMainlySpeaksEnglishAtHome: bool = None,
        loteBackground: str = None,
        isPayingInternationalFee: bool = None,
        cpsfIsInCare: bool = None,
        cpsfCaseManager: str = None,
        cpsfDistrict: str = None,
        cpsfContactNumber: str = None,
        createdAt: objects.CompositeTime = None,
        updatedAt: objects.CompositeTime = None,
        isActive: bool = None,
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
        fileName: str = None,
        isConfidential: bool = None,
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
        firstName: str = None,
        lastName: str = None,
        preferredName: str = None,
        gender: str = None,
        barcode: str = None,
        examId: str = None,
        schoolYear: str = None,
        dateOfBirth: datetime.date = None,
        allergies: list[str] = None,
        medicalConditions: list[str] = None,
        externalId: str = None,
        externalSource: str = None,
        username: str = None,
        email: str = None,
        mobile: str = None,
        refId: str = None,
        eslSupportNeeded: bool = None,
        eslDateAssessed: datetime.date = None,
        isEslSupportReceived: bool = None,
        enrolDate: datetime.date = None,
        createdAt: objects.CompositeTime = None,
        updatedAt: objects.CompositeTime = None,
        isActive: bool = None,
        indigenousStatus: str = None,
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
        startDate: datetime.date = None,
        endDate: datetime.date = None,
        status: str = None,
        school: str = None,
        schoolYear: str = None,
        rollClass: str = None,
        isBoarding: bool = None,
        boardingHouse: str = None,
        tutorGroup: str = None,
        fteAmount: float = None,
        createdAt: objects.CompositeTime = None,
        updatedAt: objects.CompositeTime = None,
        isActive: bool = None,
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
        self, name: str = None, sequence: int = None, _data: dict | None = None
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
        type: str = None,
        date: str = None,
        start: str = None,
        end: str = None,
        comment: str = None,
        explainer: str = None,
        explainerSource: str = None,
        letterSent: bool = None,
        bulkAbsenceId: bool = None,
        submitted: bool = None,
        externalSource: str = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
