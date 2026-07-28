# pyright: reportArgumentType=false

import datetime
from dataclasses import dataclass

from . import (
    Engine,
    SentralObject,
    attributes,
    collections,
    instances,
    links,
    params,
    payloads,
    relationships,
)


@dataclass(init=False, slots=True)
class Activity(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityAttributes
    links: links.ActivityLinks
    relationships: relationships.ActivityRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityAttributes = None,
        links: links.ActivityLinks = None,
        relationships: relationships.ActivityRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.ActivityParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity/{id}",
            method="GET",
            params=params,
        )

        return Activity(res["data"])

    def get_cycle_instances(
        self, engine: Engine, params: params.CycleInstanceCollectionParams | None = None
    ):
        res = engine.query_json(endpoint=self.links.cycles, method="GET", params=params)

        return collections.CycleInstanceCollection(_data=res)

    def get_cycle_attendee_links(
        self,
        engine: Engine,
        cycle_instance: instances.CycleInstance,
        params: params.CycleInstanceAttendeeLinkCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.cycles + f"/{cycle_instance.id}/attendee-links",
            method="GET",
            params=params,
        )

        return collections.AttendeeLinkCollection(_data=res)

    def get_instances(
        self,
        engine: Engine,
        params: params.ActivityRelatedInstanceCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.instances, method="GET", params=params
        )

        return collections.ActivityInstanceCollection(_data=res)

    def get_sport_events(
        self,
        engine: Engine,
        params: params.ActivitySportEventCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/sport-events", method="GET", params=params
        )

        return collections.ActivitySportEventCollection(_data=res)


@dataclass(init=False, slots=True)
class AttendeeLink(SentralObject):
    type: str
    id: str
    attributes: attributes.AttendeeLinkAttributes
    links: links.AttendeeLinkLinks
    relationships: relationships.AttendeeLinkRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.AttendeeLinkAttributes = None,
        links: links.AttendeeLinkLinks = None,
        relationships: relationships.AttendeeLinkRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.AttendeeLinkParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/activities/attendee-link/{id}", method="GET", params=params
        )

        return AttendeeLink(_data=res)

    def get_student(
        self, engine: Engine, params: params.AttendeeLinkStudentParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.enrolmentAttendee, method="GET", params=params
        )

        return Student(_data=res)


@dataclass(init=False, slots=True)
class ActivitySportEvent(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivitySportEventAttributes
    links: links.ActivitySportEventLinks
    relationships: relationships.ActivitySportEventRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivitySportEventAttributes = None,
        links: links.ActivitySportEventLinks = None,
        relationships: relationships.ActivitySportEventRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        id: int,
        params: params.ActivitySportEventParams | None = None,
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-sport-event/{id}",
            method="GET",
            params=params,
        )

        return ActivitySportEvent(_data=res)

    def get_coaches(
        self,
        engine: Engine,
        params: params.ActivitySportEventCoachesParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/coaches", method="GET", params=params
        )

        return collections.StaffCollection(_data=res)

    def get_grounds(
        self,
        engine: Engine,
        params: params.ActivitySportEventGroundsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/grounds", method="GET", params=params
        )

        return collections.VenueGroundsCollection(_data=res)

    def get_teams(
        self, engine: Engine, params: params.ActivitySportEventTeamsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/teams", method="GET", params=params
        )

        return collections.ActivityTeamCollection(_data=res)

    def get_transport_events(
        self,
        engine: Engine,
        params: params.ActivitySportEventTransportEventsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/transport-events", method="GET", params=params
        )

        return collections.ActivityTransportEventCollection(_data=res)

    def get_vehicles(
        self,
        engine: Engine,
        params: params.ActivitySportEventVehiclesParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/vehicles", method="GET", params=params
        )

        return collections.ActivityVehicleCollection(_data=res)

    def get_venues(
        self,
        engine: Engine,
        params: params.ActivitySportEventVenuesParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/venues", method="GET", params=params
        )

        return collections.VenueCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityCategory(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityCategoryAttributes
    links: links.ActivityCategoryLinks

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityCategoryAttributes = None,
        links: links.ActivityCategoryLinks = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        id: int,
        params: params.ActivityCategoryParams | None = None,
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-category/{id}",
            method="GET",
            params=params,
        )

        return ActivityCategory(res["data"])


@dataclass(init=False, slots=True)
class ActivityGuardianLink(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityGuardianLinkAttributes
    links: links.ActivityGuardianLinkLinks
    relationships: relationships.ActivityGuardianLinkRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityGuardianLinkAttributes = None,
        links: links.ActivityGuardianLinkLinks = None,
        relationships: relationships.ActivityGuardianLinkRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        id: int,
        params: params.ActivityGuardianLinkParams | None = None,
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-guardian-link/{id}",
            method="GET",
            params=params,
        )

        return ActivityGuardianLink(_data=res)


@dataclass(init=False, slots=True)
class ActivityResponse(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityResponseAttributes
    links: links.ActivityResponseLinks
    relationships: relationships.ActivityResponseRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityResponseAttributes = None,
        links: links.ActivityResponseLinks = None,
        relationships: relationships.ActivityResponseRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CompositeTime(SentralObject):
    timestamp: int
    iso8601: datetime.datetime

    def __init__(self, data: dict):
        super().__init__(data)


@dataclass(init=False, slots=True)
class ActivityRoll(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityRollAttributes
    links: links.ActivityRollLinks
    relationships.ActivityRollRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityRollAttributes = None,
        links: links.ActivityRollLinks = None,
        relationships: relationships.ActivityRollRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.ActivityRollParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/activities/roll/{id}", method="GET", params=params
        )

        return ActivityRoll(_data=res)

    def get_activity_instance(
        self,
        engine: Engine,
        params: params.ActivityRollActivityInstanceParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.activityInstance, method="GET", params=params
        )

        return instances.ActivityInstance(_data=res)


@dataclass(init=False, slots=True)
class ActivityPosition(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityPositionAttributes
    links: links.ActivityPositionLinks
    relationships.ActivityPositionRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityPositionAttributes = None,
        links: links.ActivityPositionLinks = None,
        relationships: relationships.ActivityPositionRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        id: int,
        params: params.ActivityPositionParams | None = None,
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-position/{id}",
            method="GET",
            params=params,
        )

        return ActivityPosition(_data=res)


@dataclass(init=False, slots=True)
class ActivityPositionGroup(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityPositionGroupAttributes
    links: links.ActivityPositionGroupLinks
    relationships: relationships.ActivityPositionGroupRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityPositionGroupAttributes = None,
        links: links.ActivityPositionGroupLinks = None,
        relationships: relationships.ActivityPositionGroupRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        id: int,
        params: params.ActivityPositionGroupParams | None = None,
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-position-group/{id}",
            method="GET",
            params=params,
        )

        return ActivityPositionGroup(_data=res)

    def get_positions(
        self,
        engine: Engine,
        params: params.ActivityPositionGroupPositionsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/positions", method="GET", params=params
        )

        return collections.ActivityPositionCollection(_data=res)


@dataclass(init=False, slots=True)
class Person(SentralObject):
    type: str
    id: str
    attributes: attributes.PersonAttributes
    links: links.PersonLinks
    relationships: relationships.PersonRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.PersonAttributes = None,
        links: links.PersonLinks = None,
        relationships: relationships.PersonRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class Staff(SentralObject):
    type: str
    id: str
    attributes: attributes.StaffAttributes
    links: links.StaffLinks
    relationships: relationships.StaffRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.StaffAttributes = None,
        links: links.StaffLinks = None,
        relationships: relationships.StaffRelationships = None,
        _data: dict | None | None = None,
    ):
        if _data is None:
            _data = locals()

        return super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.StaffParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/enrolments/staff/{id}", method="GET", params=params
        )

        return Staff(_data=res)

    @staticmethod
    def post(engine: Engine, payload: payloads.StaffPayload):
        res = engine.query_json(
            endpoint="/v1/enrolments/staff", method="POST", payload=payload
        )

        return Staff(_data=res)

    def delete(self, engine: Engine):
        res = engine.query_raw(endpoint=self.links.self_, method="DELETE")

        return res.ok

    def patch(self, engine: Engine):
        res = engine.query_json(
            endpoint=self.links.self_,
            method="PATCH",
            payload=payloads.StaffPayload(self),
        )

        return Staff(_data=res)

    def get_absences(
        self, engine: Engine, params: params.StaffStaffAbsencesParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.absences, method="GET", params=params
        )

        return collections.StaffAbsenceCollection(_data=res)

    def get_person(
        self, engine: Engine, params: params.StaffPersonParams | None = None
    ):
        res = engine.query_json(endpoint=self.links.person, method="GET", params=params)

        return Person(_data=res)

    def get_photo(
        self, engine: Engine, params: params.StaffPhotoParams | None = None
    ) -> bytes:
        res = engine.query_raw(
            endpoint=self.links.self_ + "/photo", method="GET", params=params
        )

        if res.ok:
            return res.content

        raise RuntimeError(res.text)

    def get_qualifications(
        self, engine: Engine, params: params.StaffQualificationsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/qualifications", method="GET", params=params
        )

        return collections.StaffQualificationCollection(_data=res)

    def get_timetable_lessons(
        self, engine: Engine, params: params.StaffTimetableLessonsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/timetable-lessons",
            method="GET",
            params=params,
        )

        return collections.TimetableLessonCollection(_data=res)


@dataclass(init=False, slots=True)
class StaffAbsence(SentralObject):
    type: str
    id: str
    attributes: attributes.StaffAbsenceAttributes
    links: links.StaffAbsenceLinks
    relationships: relationships.StaffAbsenceRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.StaffAbsenceAttributes = None,
        links: links.StaffAbsenceLinks = None,
        relationships: relationships.StaffAbsenceRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class VenueGrounds(SentralObject):
    type: str
    id: str
    attributes: attributes.VenueGroundsAttributes
    links: links.VenueGroundsLinks
    relationships: relationships.VenueGroundsRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.VenueGroundsAttributes = None,
        links: links.VenueGroundsLinks = None,
        relationships: relationships.VenueGroundsRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.VenueGroundsParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/activities/venue-grounds/{id}", method="GET", params=params
        )

        return VenueGrounds(_data=res)


@dataclass(init=False, slots=True)
class ActivityTransportEvent(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityTransportEventAttributes
    links: links.ActivityTransportEventLinks
    relationships: relationships.ActivityTransportEventRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityTransportEventAttributes = None,
        links: links.ActivityTransportEventLinks = None,
        relationships: relationships.ActivityTransportEventRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine,
        id: int,
        params: params.ActivityTransportEventParams | None = None,
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-transport-event/{id}",
            method="GET",
            params=params,
        )

        return ActivityTransportEvent(_data=res)


@dataclass(init=False, slots=True)
class ActivityTeam(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityTeamAttributes
    links: links.ActivityTeamLinks
    relationships: relationships.ActivityTeamRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityTeamAttributes = None,
        links: links.ActivityTeamLinks = None,
        relationships: relationships.ActivityTeamRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.ActivityTeamParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-team/{id}", method="GET", params=params
        )

        return ActivityTeam(_data=res)

    def get_coaches(
        self, engine: Engine, params: params.ActivityTeamCoachesParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/coaches", method="GET", params=params
        )

        return collections.StaffCollection(_data=res)

    def get_members(
        self,
        engine: Engine,
        params: params.ActivityTeamRelatedMembersParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/team-members", method="GET", params=params
        )

        return collections.ActivityTeamMemberCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityVehicle(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityVehicleAttributes
    links: links.ActivityVehicleLinks
    relationships: relationships.ActivityVehicleRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityVehicleAttributes = None,
        links: links.ActivityVehicleLinks = None,
        relationships: relationships.ActivityVehicleRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, id: int, params: params.ActivityVehicleParams | None = None
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activty-vehicle/{id}", method="GET", params=params
        )

        return ActivityVehicle(_data=res)


@dataclass(init=False, slots=True)
class StaffQualification(SentralObject):
    type: str
    id: str
    attributes: attributes.StaffQualificationAttributes
    links: links.StaffQualificationLinks
    relationships: relationships.StaffQualificationRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.StaffQualificationAttributes = None,
        links: links.StaffQualificationLinks = None,
        relationships: relationships.StaffQualificationRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class TimetableLesson(SentralObject):
    type: str
    id: str
    attributes: attributes.TimetableLessonAttributes
    relationships: relationships.TimetableLessonRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.TimetableLessonAttributes = None,
        relationships: relationships.TimetableLessonRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class Venue(SentralObject):
    type: str
    id: str
    attributes: attributes.VenueAttributes
    links: links.VenueLinks
    relationships: relationships.VenueRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.VenueAttributes = None,
        links: links.VenueLinks = None,
        relationships: relationships.VenueRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.VenueParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/activities/venue/{id}", method="GET", params=params
        )

        return Venue(_data=res)

    def get_grounds(
        self, engine: Engine, params: params.VenueRelatedGroundsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/grounds", method="GET", params=params
        )

        return collections.VenueGroundsCollection(_data=res)


@dataclass(init=False, slots=True)
class ActivityTeamMember(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityTeamMemberAttributes
    links: links.ActivityTeamMemberLinks
    relationships: relationships.ActivityTeamMemberRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.ActivityTeamMemberAttributes = None,
        links: links.ActivityTeamMemberLinks = None,
        relationships: relationships.ActivityTeamMemberRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, id: int, params: params.ActivityTeamMemberParams | None = None
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-team-member/{id}",
            method="GET",
            params=params,
        )

        return ActivityTeamMember(_data=res)


@dataclass(init=False, slots=True)
class Student(SentralObject):
    type: str
    id: str
    attributes: attributes.StudentAttributes
    links: links.StudentLinks
    relationships: relationships.StudentRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.StudentAttributes = None,
        links: links.StudentLinks = None,
        relationships: relationships.StudentRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.StudentParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/enrolments/students/{id}", method="GET", params=params
        )

        return Student(_data=res)

    def patch(self, engine: Engine):
        res = engine.query_json(
            endpoint=self.links.self_,
            method="PATCH",
            payload=payloads.StudentPayload(self),
        )

        return Student(_data=res)

    def get_absences(
        self, engine: Engine, params: params.StudentAbsencesParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/absences", method="GET", params=params
        )

        return collections.AbsenceCollection(_data=res)

    def get_academic_reports(
        self,
        engine: Engine,
        params: params.StudentRelatedAcademicReportsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/academic-reports", method="GET", params=params
        )

        return collections.StudentAcademicReportCollection(_data=res)

    def get_activities(
        self, engine: Engine, params: params.StudentActivitiesParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.activities, method="GET", params=params
        )

        return collections.ActivityCollection(_data=res)

    def get_activity_links(
        self, engine: Engine, params: params.StudentActivityLinksParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.activityLinks, method="GET", params=params
        )

        return collections.AttendeeLinkCollection(_data=res)

    def get_award_links(
        self,
        engine: Engine,
        params: params.StudentRelatedAwardLinksParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/award-links", method="GET", params=params
        )

        return collections.StudentAwardLinkCollection(_data=res)

    def get_awards(
        self, engine: Engine, params: params.StudentAwardsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/awards", method="GET", params=params
        )

        return collections.AwardCollection(_data=res)

    def post_data_sync(self, engine: Engine):
        res = engine.query_json(endpoint=self.links.self_ + "/data-sync", method="POST")

        return CoreStudent(_data=res)

    def post_document(
        self,
        engine: Engine,
        document: bytes | str,
        params: params.StudentRelatedStudentDocumentParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/document",
            method="POST",
            params=params,
            payload={"document": document},
        )

        return StudentDocument(_data=res)

    def get_documents(
        self, engine: Engine, params: params.StudentStudentDocumentsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.documents, method="GET", params=params
        )

        return collections.StudentDocumentCollection(_data=res)

    def get_edupro_academic_reports(
        self,
        engine: Engine,
        params: params.StudentRelatedEduProReportsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/edupro-academic-reports",
            method="GET",
            params=params,
        )

        return collections.StudentAcademicReportEduProCollection(_data=res)

    def get_enrolments(
        self, engine: Engine, params: params.StudentEnrolmentsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/enrolments", method="GET", params=params
        )

        return collections.EnrolmentCollection(_data=res)

    def get_flag_links(
        self, engine: Engine, params: params.StudentStudentFlagLinksParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.flagLinks, method="GET", params=params
        )

        return collections.StudentFlagLinkCollection(_data=res)

    def get_flags(
        self, engine: Engine, params: params.StudentFlagsParams | None = None
    ):
        res = engine.query_json(endpoint=self.links.flags, method="GET", params=params)

        return collections.FlagCollection(_data=res)

    def get_households(
        self,
        engine: Engine,
        params: params.StudentHouseholdRelationsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/households", method="GET", params=params
        )

        return collections.StudentHouseholdRelationCollection(_data=res)

    def get_person(
        self, engine: Engine, params: params.StudentPersonParams | None = None
    ):
        res = engine.query_json(endpoint=self.links.person, method="GET", params=params)

        return Person(_data=res)

    def get_photo(
        self, engine: Engine, params: params.StudentPhotoParams | None = None
    ):
        res = engine.query_raw(endpoint=self.links.photo, method="GET", params=params)

        return res.content

    def get_primary_enrolment(
        self, engine: Engine, params: params.StudentPrimaryEnrolmentParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.primaryEnrolment, method="GET", params=params
        )

        return Enrolment(_data=res)

    def get_special_needs_programs(
        self,
        engine: Engine,
        params: params.StudentSpecialNeedsProgramsParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/special-needs-programs",
            method="GET",
            params=params,
        )

        return collections.SpecialNeedsProgramCollection(_data=res)

    def get_tenants(
        self, engine: Engine, params: params.StudentTenantsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.tenants, method="GET", params=params
        )

        return collections.TenantCollection(_data=res)

    def get_timetable_lessons(
        self, engine: Engine, params: params.StudentTimetableLessonsParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/timetable-lessons",
            method="GET",
            params=params,
        )

        return collections.TimetableLessonCollection(_data=res)


@dataclass(init=False, slots=True)
class StudentDocument(SentralObject):
    type: str
    id: str
    attributes: attributes.StudentDocumentAttributes
    links: links.StudentDocumentLinks
    relationships: relationships.StudentDocumentRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.StudentDocumentAttributes = None,
        links: links.StudentDocumentLinks = None,
        relationships: relationships.StudentDocumentRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class CoreStudent(SentralObject):
    type: str
    id: str
    attributes: attributes.CoreStudentAttributes
    links: links.CoreStudentLinks
    relationships: relationships.CoreStudentRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.CoreStudentAttributes = None,
        links: links.CoreStudentLinks = None,
        relationships: relationships.CoreStudentRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.CoreStudentParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/core/core-student/{id}", method="GET", params=params
        )

        return CoreStudent(_data=res)

    def get_attended_classes(
        self,
        engine: Engine,
        params: params.CoreStudentAttendedClassesParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/attended-classes", method="GET", params=params
        )

        return collections.CoreClassCollection(_data=res)


@dataclass(init=False, slots=True)
class Enrolment(SentralObject):
    type: str
    id: str
    attributes: attributes.EnrolmentAttributes
    links: links.EnrolmentLinks
    relationships: relationships.EnrolmentRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.EnrolmentAttributes = None,
        links: links.EnrolmentLinks = None,
        relationships: relationships.EnrolmentRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(engine: Engine, id: int, params: params.EnrolmentParams | None = None):
        res = engine.query_json(
            endpoint=f"/v1/enrolments/enrolment/{id}", method="GET", params=params
        )

        return Enrolment(_data=res)

    def post(self, engine: Engine):
        res = engine.query_json(
            endpoint="/v1/enrolments/enrolment",
            method="POST",
            payload=payloads.EnrolmentPayload(self),
        )

        return Enrolment(_data=res)

    def delete(self, engine: Engine):
        res = engine.query_raw(endpoint=self.links.self_, method="DELETE")

        return res.ok

    def patch(self, engine: Engine):
        res = engine.query_json(
            endpoint=self.links.self_,
            method="PATCH",
            payload=payloads.EnrolmentPayload(self),
        )

        return Enrolment(_data=res)

    def get_classes(
        self, engine: Engine, params: params.EnrolmentClassesParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.classes, method="GET", params=params
        )

        return collections.ClassCollection(_data=res)

    def get_house(
        self, engine: Engine, params: params.EnrolmentHouseParams | None = None
    ):
        res = engine.query_json(endpoint=self.links.house, method="GET", params=params)

        return House(_data=res)

    def get_rollclass(
        self, engine: Engine, params: params.EnrolmentRollclassParams | None = None
    ):
        res = engine.query_json(
            endpoint=self.links.rollclass, method="GET", params=params
        )

        return Rollclass(_data=res)


@dataclass(init=False, slots=True)
class House(SentralObject):
    type: str
    id: str
    attributes: attributes.HouseAttributes
    links: links.HouseLinks
    relationships: relationships.HouseRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.HouseAttributes = None,
        links: links.HouseLinks = None,
        relationships: relationships.HouseRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class Absence(SentralObject):
    type: str
    id: str
    attributes: attributes.AbsenceAttributes
    links: links.AbsenceLinks
    relationships: relationships.AbsenceRelationships

    def __init__(
        self,
        type: str = None,
        id: str = None,
        attributes: attributes.AbsenceAttributes = None,
        links: links.AbsenceLinks = None,
        relationships: relationships.AbsenceRelationships = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)


@dataclass(init=False, slots=True)
class StudentAcademicReport(SentralObject):
    pass


@dataclass(init=False, slots=True)
class StudentAwardLink(SentralObject):
    pass


@dataclass(init=False, slots=True)
class Award(SentralObject):
    pass


@dataclass(init=False, slots=True)
class StudentAcademicReportEduPro(SentralObject):
    pass


@dataclass(init=False, slots=True)
class StudentFlagLink(SentralObject):
    pass


@dataclass(init=False, slots=True)
class Flag(SentralObject):
    pass


@dataclass(init=False, slots=True)
class StudentHouseholdRelation(SentralObject):
    pass


@dataclass(init=False, slots=True)
class SpecialNeedsProgram(SentralObject):
    pass


@dataclass(init=False, slots=True)
class Tenant(SentralObject):
    pass


@dataclass(init=False, slots=True)
class CoreClass(SentralObject):
    pass


@dataclass(init=False, slots=True)
class Rollclass(SentralObject):
    pass


@dataclass(init=False, slots=True)
class Class(SentralObject):
    pass
