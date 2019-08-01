# CreateItineraryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_reference_id** | **str** | Your unique reference value. This field supports a maximum of 28 characters and is required to be unique (if provided). | [optional] 
**hold** | **bool** | Flag for placing a booking on hold. The booking will be released if the resume link is not followed within the hold period. Please refer to our Hold and Resume documentation. | [optional] 
**rooms** | [**list[CreateItineraryRequestRooms]**](CreateItineraryRequestRooms.md) |  | 
**payments** | **object** |  | [optional] 
**affiliate_metadata** | **str** | Field that stores up to 256 characters of additional metadata with the itinerary. Will be returned on all retrieve responses for this itinerary. The data must be in the format &#39;key1:value|key2:value|key3:value&#39;. | [optional] 
**tax_registration_number** | **str** | The customer&#39;s taxpayer identification number that is provided by the government to nationals or resident aliens. This number should be collected from individuals that pay taxes or participate in activities that provide revenue for one or more tax types.  Note: This value is only needed from Brazilian customers. | [optional] 
**traveler_handling_instructions** | **str** | Custom traveler handling instructions for the hotel. Do not include PCI sensitive data, such as credit card numbers, in this field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


