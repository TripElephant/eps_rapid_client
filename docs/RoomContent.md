# RoomContent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for a room type. | [optional] 
**name** | **str** | Room type name. | [optional] 
**descriptions** | [**RoomContentDescriptions**](RoomContentDescriptions.md) |  | [optional] 
**amenities** | [**dict(str, Amenity)**](Amenity.md) | Lists all of the amenities available in the room. See our [amenities reference](https://developer.expediapartnersolutions.com/reference/content-reference-lists-2-3/) for current known amenity ID and name values. | [optional] 
**images** | [**list[RoomContentImages]**](RoomContentImages.md) | The room&#39;s images. Contains all room images available. | [optional] 
**bed_groups** | [**dict(str, BedGroup)**](BedGroup.md) | A map of the room&#39;s bed groups. | [optional] 
**area** | [**RoomContentArea**](RoomContentArea.md) |  | [optional] 
**views** | [**dict(str, View)**](View.md) | A map of the room views. See our [view reference](https://developer.expediapartnersolutions.com/reference/content-reference-lists-2-3/) for current known room view ID and name values. | [optional] 
**occupancy** | [**RoomContentOccupancy**](RoomContentOccupancy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


