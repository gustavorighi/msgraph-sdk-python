from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .web_part import WebPart

from .entity import Entity

@dataclass
class HorizontalSectionColumn(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The webparts property
    webparts: Optional[List[WebPart]] = None
    # The width property
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HorizontalSectionColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HorizontalSectionColumn
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HorizontalSectionColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .web_part import WebPart

        from .entity import Entity
        from .web_part import WebPart

        fields: Dict[str, Callable[[Any], None]] = {
            "webparts": lambda n : setattr(self, 'webparts', n.get_collection_of_object_values(WebPart)),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("webparts", self.webparts)
        writer.write_int_value("width", self.width)
    

