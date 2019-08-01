# RoomRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nightly** | **list[list[object]]** | Array of arrays of amount objects. Each sub-array of amount objects represents a single night&#39;s charges | 
**stay** | [**list[RoomRateStay]**](RoomRateStay.md) | Array of amount objects. Details any charges that apply to the entire stay (not divided per-night). Any per-room adjustments are applied to the &#x60;base_rate&#x60; amount within this object. | 
**totals** | [**RoomRateTotals**](RoomRateTotals.md) |  | 
**fees** | [**RoomRateFees**](RoomRateFees.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


