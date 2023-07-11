from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_staff_member_base import BookingStaffMemberBase
    from .booking_staff_role import BookingStaffRole
    from .booking_work_hours import BookingWorkHours

from .booking_staff_member_base import BookingStaffMemberBase

@dataclass
class BookingStaffMember(BookingStaffMemberBase):
    """
    Represents a staff member who provides services in a business.
    """
    odata_type = "#microsoft.graph.bookingStaffMember"
    # True means that if the staff member is a Microsoft 365 user, the Bookings API would verify the staff member's availability in their personal calendar in Microsoft 365, before making a booking.
    availability_is_affected_by_personal_calendar: Optional[bool] = None
    # The name of the staff member, as displayed to customers. Required.
    display_name: Optional[str] = None
    # The email address of the staff member. This can be in the same Microsoft 365 tenant as the business, or in a different email domain. This email address can be used if the sendConfirmationsToOwner property is set to true in the scheduling policy of the business. Required.
    email_address: Optional[str] = None
    # True indicates that a staff member will be notified via email when a booking assigned to them is created or changed.
    is_email_notification_enabled: Optional[bool] = None
    # The role property
    role: Optional[BookingStaffRole] = None
    # The time zone of the staff member. For a list of possible values, see dateTimeTimeZone.
    time_zone: Optional[str] = None
    # True means the staff member's availability is as specified in the businessHours property of the business. False means the availability is determined by the staff member's workingHours property setting.
    use_business_hours: Optional[bool] = None
    # The range of hours each day of the week that the staff member is available for booking. By default, they are initialized to be the same as the businessHours property of the business.
    working_hours: Optional[List[BookingWorkHours]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingStaffMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingStaffMember
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingStaffMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_staff_member_base import BookingStaffMemberBase
        from .booking_staff_role import BookingStaffRole
        from .booking_work_hours import BookingWorkHours

        from .booking_staff_member_base import BookingStaffMemberBase
        from .booking_staff_role import BookingStaffRole
        from .booking_work_hours import BookingWorkHours

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityIsAffectedByPersonalCalendar": lambda n : setattr(self, 'availability_is_affected_by_personal_calendar', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "isEmailNotificationEnabled": lambda n : setattr(self, 'is_email_notification_enabled', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(BookingStaffRole)),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "useBusinessHours": lambda n : setattr(self, 'use_business_hours', n.get_bool_value()),
            "workingHours": lambda n : setattr(self, 'working_hours', n.get_collection_of_object_values(BookingWorkHours)),
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
        writer.write_bool_value("availabilityIsAffectedByPersonalCalendar", self.availability_is_affected_by_personal_calendar)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_bool_value("isEmailNotificationEnabled", self.is_email_notification_enabled)
        writer.write_enum_value("role", self.role)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_bool_value("useBusinessHours", self.use_business_hours)
        writer.write_collection_of_object_values("workingHours", self.working_hours)
    

