# PropertyAvailability

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Expedia property ID. | 
**rooms** | [**list[PropertyAvailabilityWithoutScoreRooms]**](PropertyAvailabilityWithoutScoreRooms.md) | Array of objects containing room information. | 
**links** | [**dict(str, Link)**](Link.md) | A map of links, including links to request additional rates and recommendations. | [optional] 
**score** | **float** | A score to sort properties where the higher the value the better. It can be used to:&lt;br&gt; * Sort the properties on the response&lt;br&gt; * Sort properties across multiple responses in parallel searches for large regions&lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


