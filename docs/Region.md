# Region

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Region Id. | [optional] 
**type** | **str** | Region type. | [optional] 
**name** | **str** | Region name. | [optional] 
**name_full** | **str** | Full region name. | [optional] 
**descriptor** | **str** | Specific information about the region e.g. whether it covers surrounding areas for a city. Only present when relevant for a region. See our [region descriptors reference](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/) for current known descriptor values. | [optional] 
**country_code** | **str** | Region country code (ISO-3166 ALPHA-2). | [optional] 
**coordinates** | [**RegionCoordinates**](RegionCoordinates.md) |  | [optional] 
**ancestors** | [**list[RegionAncestors]**](RegionAncestors.md) | An array of the region&#39;s ancestors. | [optional] 
**descendants** | **dict(str, list[str])** | A map of the region types that contain direct descendants of the region. | [optional] 
**property_ids** | **list[str]** | An array of associated property ids for the region. | [optional] 
**property_ids_expanded** | **list[str]** | An array of associated property ids within an expanded radius for the region. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


