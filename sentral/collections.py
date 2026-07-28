from dataclasses import dataclass

from . import Engine, SentralObject, instances, links, meta, objects, params


@dataclass(init=False, slots=True)
class ActivityCollection(SentralObject):
    data: list[objects.Activity]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Activity] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, params: params.ActivityCollectionParams | None = None):
        res = engine.query_json(
            endpoint="/v1/activities/activity", method="GET", params=params
        )

        return ActivityCollection(_data=res)


@dataclass(init=False, slots=True)
class CycleInstanceCollection(SentralObject):
    data: list[instances.CycleInstance]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[instances.CycleInstance] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AttendeeLinkCollection(SentralObject):
    data: list[objects.AttendeeLink]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.AttendeeLink] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityInstanceCollection(SentralObject):
    data: list[instances.ActivityInstance]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[instances.ActivityInstance] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, params: params.ActivityInstanceCollectionParams | None = None
    ):
        res = engine.query_json(
            endpoint="/v1/activities/activity-instance", method="GET", params=params
        )

        return ActivityInstanceCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivitySportEventCollection(SentralObject):
    data: list[objects.ActivitySportEvent]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivitySportEvent] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, params: params.ActivitySportEventCollectionParams | None = None
    ):
        res = engine.query_json(
            endpoint="/v1/activities/activity-sport-event", method="GET", params=params
        )

        return ActivitySportEventCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityCategoryCollection(SentralObject):
    data: list[objects.ActivityCategory]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityCategory] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, params: params.ActivityCategoryCollectionParams | None = None
    ):
        res = engine.query_json(
            endpoint="/v1/activities/activity-category", method="GET", params=params
        )

        return ActivityCategoryCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityGuardianLinkCollection(SentralObject):
    data: list[objects.ActivityGuardianLink]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityGuardianLink] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        params: params.ActivityGuardianLinkCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint="/v1/activities/activity-guardian-link",
            method="GET",
            params=params,
        )

        return ActivityGuardianLinkCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityResponseCollection(SentralObject):
    data: list[objects.ActivityResponse]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityResponse] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityRollCollection(SentralObject):
    data: list[objects.ActivityRoll]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityRoll] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityPositionCollection(SentralObject):
    data: list[objects.ActivityPosition]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityPosition] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, params: params.ActivityPositionCollectionParams | None = None
    ):
        res = engine.query_json(
            endpoint="/v1/activities/activity-position", method="GET", params=params
        )

        return ActivityPositionCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityPositionGroupCollection(SentralObject):
    data: list[objects.ActivityPositionGroup]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityPositionGroup] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        params: params.ActivityPositionGroupCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint="/v1/activities/activity-position-group",
            method="GET",
            params=params,
        )

        return ActivityPositionGroupCollection(_data=res)


@dataclass(init=False, slots=True)
class StaffCollection(SentralObject):
    data: list[objects.Staff]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Staff] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGroundsCollection(SentralObject):
    data: list[objects.VenueGrounds]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.VenueGrounds] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamCollection(SentralObject):
    data: list[objects.ActivityTeam]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityTeam] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTransportEventCollection(SentralObject):
    data: list[objects.ActivityTransportEvent]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityTransportEvent] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityVehicleCollection(SentralObject):
    data: list[objects.ActivityVehicle]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityVehicle] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueCollection(SentralObject):
    data: list[objects.Venue]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Venue] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffAbsenceCollection(SentralObject):
    data: list[objects.StaffAbsence]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StaffAbsence] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StaffQualificationCollection(SentralObject):
    data: list[objects.StaffQualification]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StaffQualification] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class TimetableLessonCollection(SentralObject):
    data: list[objects.TimetableLesson]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.TimetableLesson] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class ActivityTeamMemberCollection(SentralObject):
    data: list[objects.ActivityTeamMember]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.ActivityTeamMember] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AbsenceCollection(SentralObject):
    data: list[objects.Absence]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Absence] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentAcademicReportCollection(SentralObject):
    data: list[objects.StudentAcademicReport]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StudentAcademicReport] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentAwardLinkCollection(SentralObject):
    data: list[objects.StudentAwardLink]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StudentAwardLink] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class AwardCollection(SentralObject):
    data: list[objects.Award]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Award] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentDocumentCollection(SentralObject):
    data: list[objects.StudentDocument]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StudentDocument] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentAcademicReportEduProCollection(SentralObject):
    data: list[objects.StudentAcademicReportEduPro]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StudentAcademicReportEduPro] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class EnrolmentCollection(SentralObject):
    data: list[objects.Enrolment]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Enrolment] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentFlagLinkCollection(SentralObject):
    data: list[objects.StudentFlagLink]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StudentFlagLink] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class FlagCollection(SentralObject):
    data: list[objects.Flag]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Flag] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentHouseholdRelationCollection(SentralObject):
    data: list[objects.StudentHouseholdRelation]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.StudentHouseholdRelation] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class SpecialNeedsProgramCollection(SentralObject):
    data: list[objects.SpecialNeedsProgram]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.SpecialNeedsProgram] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class TenantCollection(SentralObject):
    data: list[objects.Tenant]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.Tenant] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CoreClassCollection(SentralObject):
    data: list[objects.CoreClass]
    meta: meta.CollectionMeta
    links: links.CollectionLinks

    def __init__(
        self,
        data: list[objects.CoreClass] | None = None,
        meta: meta.CollectionMeta | None = None,
        links: links.CollectionLinks | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)
