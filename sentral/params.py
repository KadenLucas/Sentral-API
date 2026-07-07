# pyright: reportAssignmentType=false

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
        output = dict()

        for slot in self.__slots__:
            value = getattr(self, slot)

            if isinstance(value, ParamList) or isinstance(value, ParamList):
                value = str(value)

            if value is not None:
                output[slot] = value

        return output


@dataclass(slots=True)
class ActivityParams(Params):
    include: ParamList[Literal["venue", None]] = None


@dataclass(slots=True)
class ActivityCollectionParams(Params):
    include: ParamList[Literal["venue", None]] = None
    limit: int = None
    offset: int = None
    ids: ParamList = None
    fromDate: str = None
    toDate: str = None


@dataclass(slots=True)
class CycleInstanceCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class CycleInstanceAttendeeLinkCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityRelatedInstanceCollectionParams(Params):
    include: ParamList[Literal["activity", None]] = None


@dataclass(slots=True)
class ActivitySportEventCollectionParams(Params):
    include: ParamList[
        Literal["venues", "ground", "coaches", "vehicles", "teams", None]
    ] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityCategoryCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None
    ids: ParamList = None


@dataclass(slots=True)
class ActivityCategoryParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityGuardianLinkParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityGuardianLinkCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None
    activityIds: ParamList = None


@dataclass(slots=True)
class ActivityInstanceCollectionParams(Params):
    include: ParamList[Literal["activity", None]] = None
    limit: int = None
    offset: int = None
    ids: ParamList = None
    activityIds: ParamList = None
    fromDate: datetime.date = None
    toDate: datetime.date = None
    includeInactive: bool = None


@dataclass(slots=True)
class ActivityInstanceParams(Params):
    include: ParamList[Literal["activity", None]] = None


@dataclass(slots=True)
class ActivityInstanceAttendeeLinkCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityInstanceActivityResponseCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None
    studentIds: ParamList = None


@dataclass(slots=True)
class ActivityInstanceActivityRollCollectionParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityPositionParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityPositionCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityPositionGroupParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityPositionGroupCollectionParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityPositionGroupPositionsParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivitySportEventParams(Params):
    include: ParamList[
        Literal["venues", "grounds", "coaches", "vehicles", "teams", None]
    ] = None


@dataclass(slots=True)
class ActivitySportEventCoachesParams(Params):
    include: ParamList[
        Literal[
            "person", "emails", "phoneNumbers", "qualifications", "employments", None
        ]
    ] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivitySportEventGroundsParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivitySportEventTeamsParams(Params):
    include: ParamList[Literal["teamMember", "teamMemberPositions", None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivitySportEventTransportEventsParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivitySportEventVehiclesParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivitySportEventVenuesParams(Params):
    include: ParamList[Literal["grounds", None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StaffParams(Params):
    include: ParamList[
        Literal[
            "person", "emails", "phoneNumbers", "qualifications", "employments", None
        ]
    ] = None


@dataclass(slots=True)
class StaffStaffAbsencesParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


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
            None,
        ]
    ] = None


@dataclass(slots=True)
class StaffPhotoParams(Params):
    width: int = None
    height: int = None


@dataclass(slots=True)
class StaffQualificationsParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class StaffTimetableLessonsParams(Params):
    include: ParamList[Literal[None]] = None
    fromDate: datetime.date = None
    toDate: datetime.date = None


@dataclass(slots=True)
class ActivityTeamParams(Params):
    include: ParamList[Literal["teamMembers", "teamMemberPositions", None]] = None


@dataclass(slots=True)
class ActivityTeamCoachesParams(Params):
    include: ParamList[
        Literal[
            "person", "emails", "phoneNumbers", "qualifications", "emplyoments", None
        ]
    ] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityTeamRelatedMembersParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class ActivityTeamMemberParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityTransportEventParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityVehicleParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityRollParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class ActivityRollActivityInstanceParams(Params):
    include: ParamList[Literal["acitvity", None]] = None


@dataclass(slots=True)
class VenueGroundsParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class VenueParams(Params):
    include: ParamList[Literal["grounds", None]] = None


@dataclass(slots=True)
class VenueRelatedGroundsParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class AttendeeLinkParams(Params):
    include: ParamList[Literal[None]] = None


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
            None,
        ]
    ] = None


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
            None,
        ]
    ] = None


@dataclass(slots=True)
class StudentAbsencesParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StudentRelatedAcademicReportsParams(Params):
    include: ParamList[Literal["period", None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StudentActivitiesParams(Params):
    include: ParamList[Literal["venue", None]] = None
    limit: int = None
    offset: int = None
    fromDate: datetime.date = None
    toDate: datetime.date = None


@dataclass(slots=True)
class StudentActivityLinksParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StudentRelatedAwardLinksParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StudentAwardsParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StudentRelatedStudentDocumentParams(Params):
    isConfidential: bool = None
    studentEnrolmentDraftId: int = None
    categoryId: int = None


@dataclass(slots=True)
class StudentStudentDocumentsParams(Params):
    include: ParamList[Literal[None]] = None


@dataclass(slots=True)
class StudentRelatedEduProReportsParams(Params):
    include: ParamList[Literal[None]] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class StudentEnrolmentsParams(Params):
    include: ParamList[
        Literal["student", "house", "rollclass", "classes", "campus", None]
    ] = None
    statuses: ParamList[Literal["active", "active_pending", "active_leaving", None]] = (
        None
    )


@dataclass(slots=True)
class StudentStudentFlagLinksParams(Params):
    include: ParamList[Literal["student", "flag", None]] = None


@dataclass(slots=True)
class StudentFlagsParams(Params):
    include: ParamList[Literal["school", None]] = None


@dataclass(slots=True)
class StudentHouseholdRelationsParams(Params):
    include: ParamList[Literal["student", "household", None]] = None
    residentialHouseholdTypes: ParamList = None


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
            None,
        ]
    ] = None


@dataclass(slots=True)
class StudentPhotoParams(Params):
    width: int = None
    height: int = None
    avoidReturningMissingPhoto: str = None


@dataclass(slots=True)
class StudentPrimaryEnrolmentParams(Params):
    forYear: int = None


@dataclass(slots=True)
class StudentSpecialNeedsProgramsParams(Params):
    include: ParamList[Literal["student", None]] = None


@dataclass(slots=True)
class StudentTenantsParams(Params):
    include: ParamList[Literal["schools", None]] = None


@dataclass(slots=True)
class StudentTimetableLessonsParams(Params):
    include: ParamList[Literal[None]] = None
    fromDate: datetime.date = None
    toDate: datetime.date = None
    classTypes: ParamList = None
    excludeClassTypes: ParamList = None


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
            None,
        ]
    ] = None


@dataclass(slots=True)
class CoreStudentAttendedClassesParams(Params):
    include: ParamList[
        Literal[
            "assignedStudents", "assignedStaff", "coreSubject", "timetableClass", None
        ]
    ] = None
    limit: int = None
    offset: int = None


@dataclass(slots=True)
class EnrolmentParams(Params):
    include: ParamList[
        Literal["student", "house", "rollclass", "classes", "campus", None]
    ] = None
    limit: int = None
    offset: int = None
    ids: ParamList = None
    academicPeriodIds: ParamList = None
    studentIds: ParamList = None
    rollclassIds: ParamList = None
    yearLevelIds: ParamList = None
    houseIds: ParamList = None
    statuses: ParamList = None
    startDateFrom: datetime.date = None
    startDateTo: datetime.date = None
    endDateFrom: datetime.date = None
    endDateTo: datetime.date = None
    includeInactive: bool = None
