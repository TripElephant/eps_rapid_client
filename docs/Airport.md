# Airport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iata_airport_code** | **str** | 3-character IATA airport code. | [optional] 
**name** | **str** | Airport name. | [optional] 
**name_full** | **str** | Full airport name. | [optional] 
**descriptor** | **str** | Specific information about the region e.g. whether it covers surrounding areas for a city. See our [region descriptors reference](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/) for current known descriptor values. | [optional] 
**country_code** | **str** | Airport’s country code (ISO-3166 ALPHA-2). | [optional] 
**iata_airport_metro_code** | **str** | 3-character IATA airport metropolitan code of the metropolitan airport area. | [optional] 
**coordinates** | [**AirportCoordinates**](AirportCoordinates.md) |  | [optional] 
**property_ids** | **list[str]** | An array of property ids within a 20 km radius of the airport. | [optional] 
**associated_region** | [**AirportAssociatedRegion**](AirportAssociatedRegion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


