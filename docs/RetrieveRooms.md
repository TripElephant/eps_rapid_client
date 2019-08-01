# RetrieveRooms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The room id. | 
**confirmation_id** | [**RetrieveConfirmationId**](RetrieveConfirmationId.md) |  | [optional] 
**bed_group_id** | **str** | Unique identifier for a bed type. | [optional] 
**checkin** | **str** | The check-in date of the itinerary. | 
**checkout** | **str** | The check-out date of the itinerary. | 
**number_of_adults** | **float** | The number of adults staying in the room. | 
**child_ages** | **list[float]** | The ages of children for the room. | [optional] 
**given_name** | **str** | The first name of the main guest staying in the room. | 
**family_name** | **str** | The last name of the main guest staying in the room. | 
**status** | **str** | The booking status of the room. | 
**special_request** | **str** | Any special request info associated with the room. | [optional] 
**smoking** | **bool** | Indicates if the room is smoking or non-smoking. | 
**rate** | [**RetrieveRate**](RetrieveRate.md) |  | [optional] 
**links** | [**RetrieveLinks1**](RetrieveLinks1.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


