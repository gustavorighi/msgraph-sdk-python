from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_information_protection_app import WindowsInformationProtectionApp

from .windows_information_protection_app import WindowsInformationProtectionApp

@dataclass
class WindowsInformationProtectionStoreApp(WindowsInformationProtectionApp):
    """
    Store App for Windows information protection
    """
    odata_type = "#microsoft.graph.windowsInformationProtectionStoreApp"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionStoreApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_information_protection_app import WindowsInformationProtectionApp

        from .windows_information_protection_app import WindowsInformationProtectionApp

        fields: Dict[str, Callable[[Any], None]] = {
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
    

