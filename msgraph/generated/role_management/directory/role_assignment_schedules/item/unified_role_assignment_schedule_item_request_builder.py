from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
    from .activated_using.activated_using_request_builder import ActivatedUsingRequestBuilder
    from .app_scope.app_scope_request_builder import AppScopeRequestBuilder
    from .directory_scope.directory_scope_request_builder import DirectoryScopeRequestBuilder
    from .principal.principal_request_builder import PrincipalRequestBuilder
    from .role_definition.role_definition_request_builder import RoleDefinitionRequestBuilder

class UnifiedRoleAssignmentScheduleItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the roleAssignmentSchedules property of the microsoft.graph.rbacApplication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleAssignmentScheduleItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement/directory/roleAssignmentSchedules/{unifiedRoleAssignmentSchedule%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property roleAssignmentSchedules for roleManagement
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilderGetRequestConfiguration] = None) -> Optional[UnifiedRoleAssignmentSchedule]:
        """
        Retrieve the schedule for an active role assignment operation.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleAssignmentSchedule]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule

        return await self.request_adapter.send_async(request_info, UnifiedRoleAssignmentSchedule, error_mapping)
    
    async def patch(self,body: Optional[UnifiedRoleAssignmentSchedule] = None, request_configuration: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[UnifiedRoleAssignmentSchedule]:
        """
        Update the navigation property roleAssignmentSchedules in roleManagement
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleAssignmentSchedule]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule

        return await self.request_adapter.send_async(request_info, UnifiedRoleAssignmentSchedule, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleAssignmentSchedules for roleManagement
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the schedule for an active role assignment operation.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[UnifiedRoleAssignmentSchedule] = None, request_configuration: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleAssignmentSchedules in roleManagement
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def activated_using(self) -> ActivatedUsingRequestBuilder:
        """
        Provides operations to manage the activatedUsing property of the microsoft.graph.unifiedRoleAssignmentSchedule entity.
        """
        from .activated_using.activated_using_request_builder import ActivatedUsingRequestBuilder

        return ActivatedUsingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_scope(self) -> AppScopeRequestBuilder:
        """
        Provides operations to manage the appScope property of the microsoft.graph.unifiedRoleScheduleBase entity.
        """
        from .app_scope.app_scope_request_builder import AppScopeRequestBuilder

        return AppScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_scope(self) -> DirectoryScopeRequestBuilder:
        """
        Provides operations to manage the directoryScope property of the microsoft.graph.unifiedRoleScheduleBase entity.
        """
        from .directory_scope.directory_scope_request_builder import DirectoryScopeRequestBuilder

        return DirectoryScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def principal(self) -> PrincipalRequestBuilder:
        """
        Provides operations to manage the principal property of the microsoft.graph.unifiedRoleScheduleBase entity.
        """
        from .principal.principal_request_builder import PrincipalRequestBuilder

        return PrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definition(self) -> RoleDefinitionRequestBuilder:
        """
        Provides operations to manage the roleDefinition property of the microsoft.graph.unifiedRoleScheduleBase entity.
        """
        from .role_definition.role_definition_request_builder import RoleDefinitionRequestBuilder

        return RoleDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnifiedRoleAssignmentScheduleItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class UnifiedRoleAssignmentScheduleItemRequestBuilderGetQueryParameters():
        """
        Retrieve the schedule for an active role assignment operation.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnifiedRoleAssignmentScheduleItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[UnifiedRoleAssignmentScheduleItemRequestBuilder.UnifiedRoleAssignmentScheduleItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnifiedRoleAssignmentScheduleItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

