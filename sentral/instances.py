from dataclasses import dataclass

from . import (
    Engine,
    SentralObject,
    attributes,
    collections,
    links,
    objects,
    params,
    payloads,
    relationships,
)


@dataclass(init=False, slots=True)
class CycleInstance(SentralObject):
    type: str
    id: int
    attributes: attributes.CycleInstanceAttributes
    links: links.CycleInstanceLinks

    def __init__(self, data: dict):
        super().__init__(data)


@dataclass(init=False, slots=True)
class ActivityInstance(SentralObject):
    type: str
    id: str
    attributes: attributes.ActivityInstanceAttributes
    links: links.ActivityInstanceLinks
    relationships: relationships.ActivityInstanceRelationships

    def __init__(
        self,
        type: str | None = None,
        id: str | None = None,
        attributes: attributes.ActivityInstanceAttributes | None = None,
        links: links.ActivityInstanceLinks | None = None,
        relationships: relationships.ActivityInstanceRelationships | None = None,
        _data: dict | None = None,
    ):
        if _data is None:
            _data = locals()

        super().__init__(_data)

    @staticmethod
    def get(
        engine: Engine, activity_instance_id: int, params: params.ActivityInstanceParams
    ):
        res = engine.query_json(
            endpoint=f"/v1/activities/activity-instance/{activity_instance_id}",
            method="GET",
            params=params,
        )

        return ActivityInstance(_data=res)

    def get_attendee_links(
        self,
        engine: Engine,
        params: params.ActivityInstanceAttendeeLinkCollectionParams,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/attendee-links", method="GET", params=params
        )

        return collections.ActivityInstanceCollection(_data=res)

    def post_attendee_link(
        self, engine: Engine, payload: payloads.ActivityInstanceAttendeeLinkPayload
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/attendee-links",
            method="POST",
            payload=payload,
        )

        return ActivityInstance(_data=res)

    def get_guardian_links(
        self,
        engine: Engine,
        params: params.ActivityGuardianLinkCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/guardian-links", method="GET", params=params
        )

        return collections.ActivityGuardianLinkCollection(_data=res)

    def get_activity_responses(
        self,
        engine: Engine,
        params: params.ActivityInstanceActivityResponseCollectionParams | None = None,
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/responses", method="GET", params=params
        )

        return collections.ActivityResponseCollection(_data=res)

    def post_activity_responses(
        self, engine: Engine, payload: payloads.ActivityInstanceActivityResponsePayload
    ):
        res = engine.query_json(
            endpoint=self.links.self_ + "/responses", method="POST", payload=payload
        )

        return objects.ActivityResponse(_data=res)

    def get_activity_rolls(
        self,
        engine: Engine,
        params: params.ActivityInstanceActivityRollCollectionParams | None = None,
    ):
        res = engine.query_json(endpoint=self.links.rolls, method="GET", params=params)

        return collections.ActivityRollCollection(_data=res)
