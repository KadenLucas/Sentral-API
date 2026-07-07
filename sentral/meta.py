from dataclasses import dataclass
from typing import get_args, get_type_hints


class SentralObject:
    __slots__ = []

    def __init__(self, data: dict):
        type_hints = get_type_hints(self.__class__)

        for slot in self.__slots__:
            slot_type = type_hints[slot]
            slot_value = data.get(slot.replace("_", ""))

            if hasattr(slot_type, "__iter__") and slot_type is not str:
                if args := get_args(slot_type):
                    (sub_type,) = args

                    if slot_value:
                        slot_value = [
                            self.convert_value(value, sub_type) for value in slot_value
                        ]
                    else:
                        slot_value = None
                else:
                    slot_value = None

            setattr(self, slot, self.convert_value(slot_value, slot_type))

    @staticmethod
    def convert_value(value, type):
        if isinstance(value, type):
            return value

        elif isinstance(value, SentralObject):
            return type(_data=value)

        return (
            type.fromisoformat(value)
            if hasattr(type, "fromisoformat") and value is not None
            else type(value)
            if value is not None
            else value
        )

    @property
    def __dict__(self):  # pyright: ignore[reportIncompatibleVariableOverride]
        output = dict()

        for slot in self.__slots__:
            value = getattr(self, slot)

            if isinstance(value, SentralObject):
                value = value.__dict__

            if value is not None:
                output[slot.replace("_", "")] = value

        return output


@dataclass(init=False, slots=True)
class CollectionMeta(SentralObject):
    count: int

    def __init__(self, data: dict):
        super().__init__(data)
