from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .oma_setting import OmaSetting

from .oma_setting import OmaSetting

@dataclass
class OmaSettingDateTime(OmaSetting):
    """
    OMA Settings DateTime definition.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.omaSettingDateTime"
    # Value.
    value: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSettingDateTime:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OmaSettingDateTime
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OmaSettingDateTime()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .oma_setting import OmaSetting

        from .oma_setting import OmaSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_datetime_value()),
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
        writer.write_datetime_value("value", self.value)
    

