from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ip_range import IpRange

from .ip_range import IpRange

@dataclass
class IPv6CidrRange(IpRange):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iPv6CidrRange"
    # IPv6 address in CIDR notation. Not nullable.
    cidr_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IPv6CidrRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IPv6CidrRange
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IPv6CidrRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ip_range import IpRange

        from .ip_range import IpRange

        fields: Dict[str, Callable[[Any], None]] = {
            "cidrAddress": lambda n : setattr(self, 'cidr_address', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("cidrAddress", self.cidr_address)
    

