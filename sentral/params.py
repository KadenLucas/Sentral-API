import datetime
from dataclasses import dataclass
from typing import Literal


@dataclass(init=False, slots=True)
class ParamList[T]:
    data: tuple[T, ...]

    def __init__(self, *args: T):
        self.data = args

    def __str__(self) -> str:
        return ",".join(str(i) for i in self.data if i)


class Params:
    __slots__ = []

    @property
    def __dict__(self):  # pyright: ignore[reportIncompatibleVariableOverride]
        output = {}

        for slot in self.__slots__:
            value = getattr(self, slot)

            if isinstance(value, ParamList):
                value = str(value)

            if value is not None:
                output[slot] = value

        return output


@dataclass(slots=True)
class ActivityParams(Params):
    include: ParamList[Literal["venue"]] | None = None


@dataclass(slots=True)
class ActivityCollectionParams(Params):
    include: ParamList[Literal["venue"]] | None = None
    limit: int | None = None
    offset: int | None = None
    ids: ParamList | None = None
    fromDate: str | None = None
    toDate: str | None = None


@dataclass(slots=True)
class CycleInstanceCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class CycleInstanceAttendeeLinkCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityRelatedInstanceCollectionParams(Params):
    include: ParamList[Literal["activity"]] | None = None


@dataclass(slots=True)
class ActivitySportEventCollectionParams(Params):
    include: ParamList[
        Literal["venues", "ground", "coaches", "vehicles", "teams"]
    ] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityCategoryCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None
    ids: ParamList | None = None


@dataclass(slots=True)
class ActivityCategoryParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityGuardianLinkParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityGuardianLinkCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None
    activityIds: ParamList | None = None


@dataclass(slots=True)
class ActivityInstanceCollectionParams(Params):
    include: ParamList[Literal["activity"]] | None = None
    limit: int | None = None
    offset: int | None = None
    ids: ParamList | None = None
    activityIds: ParamList | None = None
    fromDate: datetime.date | None = None
    toDate: datetime.date | None = None
    includeInactive: bool | None = None


@dataclass(slots=True)
class ActivityInstanceParams(Params):
    include: ParamList[Literal["activity"]] | None = None


@dataclass(slots=True)
class ActivityInstanceAttendeeLinkCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityInstanceActivityResponseCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None
    studentIds: ParamList | None = None


@dataclass(slots=True)
class ActivityInstanceActivityRollCollectionParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityPositionParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityPositionCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityPositionGroupParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityPositionGroupCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityPositionGroupPositionsParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivitySportEventParams(Params):
    include: ParamList[
        Literal["venues", "grounds", "coaches", "vehicles", "teams"]
    ] | None = None


@dataclass(slots=True)
class ActivitySportEventCoachesParams(Params):
    include: ParamList[
        Literal[
            "person", "emails", "phoneNumbers", "qualifications", "employments"
        ]
    ] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivitySportEventGroundsParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivitySportEventTeamsParams(Params):
    include: ParamList[Literal["teamMember", "teamMemberPositions"]] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivitySportEventTransportEventsParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivitySportEventVehiclesParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivitySportEventVenuesParams(Params):
    include: ParamList[Literal["grounds"]] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StaffParams(Params):
    include: ParamList[
        Literal[
            "person", "emails", "phoneNumbers", "qualifications", "employments"
        ]
    ] | None = None


@dataclass(slots=True)
class StaffStaffAbsencesParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StaffPersonParams(Params):
    include: ParamList[
        Literal[
            "primaryHousehold",
            "studentPrimaryEnrolment",
            "staff",
            "student",
            "contactDetails",
            "otherHouseholds",
            "studentContacts",
            "studentTenants",
            "prescribedMedication",
            "emails",
            "phoneNumbers",
            "givenConsents",
            "givenConsentLinks",
            "emergencyContactLinks",
            "abilities",
            "additionalFields",

        ]
    ] | None = None


@dataclass(slots=True)
class StaffPhotoParams(Params):
    width: int | None = None
    height: int | None = None


@dataclass(slots=True)
class StaffQualificationsParams(Params):
    include: None = None


@dataclass(slots=True)
class StaffTimetableLessonsParams(Params):
    include: None = None
    fromDate: datetime.date | None = None
    toDate: datetime.date | None = None


@dataclass(slots=True)
class ActivityTeamParams(Params):
    include: ParamList[Literal["teamMembers", "teamMemberPositions"]] | None = None


@dataclass(slots=True)
class ActivityTeamCoachesParams(Params):
    include: ParamList[
        Literal[
            "person", "emails", "phoneNumbers", "qualifications", "emplyoments"
        ]
    ] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityTeamRelatedMembersParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class ActivityTeamMemberParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityTransportEventParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityVehicleParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityRollParams(Params):
    include: None = None


@dataclass(slots=True)
class ActivityRollActivityInstanceParams(Params):
    include: ParamList[Literal["acitvity"]] | None = None


@dataclass(slots=True)
class VenueGroundsParams(Params):
    include: None = None


@dataclass(slots=True)
class VenueParams(Params):
    include: ParamList[Literal["grounds"]] | None = None


@dataclass(slots=True)
class VenueRelatedGroundsParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class AttendeeLinkParams(Params):
    include: None = None


@dataclass(slots=True)
class AttendeeLinkStudentParams(Params):
    include: ParamList[
        Literal[
            "primaryEnrolment",
            "person",
            "emails",
            "phoneNumbers",
            "activities",
            "activityInstances",
            "tenants",
            "flags",
            "flagLinks",
            "contacts",
            "holidays",
            "specialNeedsPrograms",
            "schoolHistory",

        ]
    ] | None = None


@dataclass(slots=True)
class StudentParams(Params):
    include: ParamList[
        Literal[
            "primaryEnrolment",
            "person",
            "emails",
            "phoneNumbers",
            "activities",
            "activityInstances",
            "tenants",
            "flags",
            "flagLinks",
            "contacts",
            "holidays",
            "specialNeedsPrograms",
            "schoolHistory",

        ]
    ] | None = None


@dataclass(slots=True)
class StudentAbsencesParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StudentRelatedAcademicReportsParams(Params):
    include: ParamList[Literal["period"]] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StudentActivitiesParams(Params):
    include: ParamList[Literal["venue"]] | None = None
    limit: int | None = None
    offset: int | None = None
    fromDate: datetime.date | None = None
    toDate: datetime.date | None = None


@dataclass(slots=True)
class StudentActivityLinksParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StudentRelatedAwardLinksParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StudentAwardsParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StudentRelatedStudentDocumentParams(Params):
    isConfidential: bool | None = None
    studentEnrolmentDraftId: int | None = None
    categoryId: int | None = None


@dataclass(slots=True)
class StudentStudentDocumentsParams(Params):
    include: None = None


@dataclass(slots=True)
class StudentRelatedEduProReportsParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class StudentEnrolmentsParams(Params):
    include: ParamList[
        Literal["student", "house", "rollclass", "classes", "campus"]
    ] | None = None
    statuses: ParamList[Literal["active", "active_pending", "active_leaving"]] | None = (
        None
    )


@dataclass(slots=True)
class StudentStudentFlagLinksParams(Params):
    include: ParamList[Literal["student", "flag"]] | None = None


@dataclass(slots=True)
class StudentFlagsParams(Params):
    include: ParamList[Literal["school"]] | None = None


@dataclass(slots=True)
class StudentHouseholdRelationsParams(Params):
    include: ParamList[Literal["student", "household"]] | None = None
    residentialHouseholdTypes: ParamList | None = None


@dataclass(slots=True)
class StudentPersonParams(Params):
    include: ParamList[
        Literal[
            "primaryHousehold",
            "studentPrimaryEnrolment",
            "staff",
            "student",
            "contactDetails",
            "otherHouseholds",
            "studentContacts",
            "studentTenants",
            "prescribedMedication",
            "emails",
            "phoneNumbers",
            "givenConsents",
            "givenConsentLinks",
            "emergencyContactLinks",
            "abilities",
            "additionalFields",

        ]
    ] | None = None


@dataclass(slots=True)
class StudentPhotoParams(Params):
    width: int | None = None
    height: int | None = None
    avoidReturningMissingPhoto: str | None = None


@dataclass(slots=True)
class StudentPrimaryEnrolmentParams(Params):
    forYear: int | None = None


@dataclass(slots=True)
class StudentSpecialNeedsProgramsParams(Params):
    include: ParamList[Literal["student"]] | None = None


@dataclass(slots=True)
class StudentTenantsParams(Params):
    include: ParamList[Literal["schools"]] | None = None


@dataclass(slots=True)
class StudentTimetableLessonsParams(Params):
    include: None = None
    fromDate: datetime.date | None = None
    toDate: datetime.date | None = None
    classTypes: ParamList | None = None
    excludeClassTypes: ParamList | None = None


@dataclass(slots=True)
class CoreStudentParams(Params):
    include: ParamList[
        Literal[
            "additionalDetails",
            "coreRollclass",
            "attendedClasses",
            "holidays",
            "studentRelationships",
            "coreHouse",
            "contacts",

        ]
    ] | None = None


@dataclass(slots=True)
class CoreStudentAttendedClassesParams(Params):
    include: ParamList[
        Literal[
            "assignedStudents", "assignedStaff", "coreSubject", "timetableClass"
        ]
    ] | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class EnrolmentParams(Params):
    include: ParamList[
        Literal["student", "house", "rollclass", "classes", "campus"]
    ] | None = None
    limit: int | None = None
    offset: int | None = None
    ids: ParamList | None = None
    academicPeriodIds: ParamList | None = None
    studentIds: ParamList | None = None
    rollclassIds: ParamList | None = None
    yearLevelIds: ParamList | None = None
    houseIds: ParamList | None = None
    statuses: ParamList | None = None
    startDateFrom: datetime.date | None = None
    startDateTo: datetime.date | None = None
    endDateFrom: datetime.date | None = None
    endDateTo: datetime.date | None = None
    includeInactive: bool | None = None


@dataclass(slots=True)
class EnrolmentCollectionParams(Params):
    include: ParamList[
        Literal["student", "house", "rollclass", "classes", "campus"]
    ] | None = None
    limit: int | None = None
    offset: int | None = None
    ids: ParamList | None = None
    academicPeriodIds: ParamList | None = None
    studentIds: ParamList | None = None
    rollclassIds: ParamList | None = None
    yearLevelIds: ParamList | None = None
    houseIds: ParamList | None = None
    statuses: ParamList | None = None
    startDateFrom: datetime.date | None = None
    startDateTo: datetime.date | None = None
    endDateFrom: datetime.date | None = None
    endDateTo: datetime.date | None = None
    includeInactive: bool | None = None


@dataclass(slots=True)
class EnrolmentClassesParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None


@dataclass(slots=True)
class EnrolmentHouseParams(Params):
    include: None = None


@dataclass(slots=True)
class EnrolmentRollclassParams(Params):
    include: None = None


@dataclass(slots=True)
class HouseCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None
    ids: ParamList | None = None
    schoolIds: ParamList | None = None


@dataclass(slots=True)
class AbsenceCollectionParams(Params):
    include: None = None
    limit: int | None = None
    offset: int | None = None
    studentId: ParamList | None = (
        None  # Check for potential error - should presumably be "studentIds"
    )
    year: ParamList | None = None  # Check for potential error - should presumably be "years"
    coreStudentIds: ParamList | None = None
    dates: ParamList | None = None
