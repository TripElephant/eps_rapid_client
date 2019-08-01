# RetrieveRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the rate. | 
**merchant_of_record** | **str** | The merchant responsible for collecting payment. | 
**refundable** | **bool** | Indicates whether the itinerary is refundable or not. | 
**cancel_refund** | [**RetrieveRateCancelRefund**](RetrieveRateCancelRefund.md) |  | [optional] 
**amenities** | **list[float]** |  | [optional] 
**promotions** | [**RetrieveRatePromotions**](RetrieveRatePromotions.md) |  | [optional] 
**nightly** | **list[list[object]]** |  | 
**stay** | [**list[RetrieveRateStay]**](RetrieveRateStay.md) |  | [optional] 
**cancel_penalties** | [**list[RetrieveRateCancelPenalties]**](RetrieveRateCancelPenalties.md) |  | [optional] 
**deposit_policies** | [**list[RetrieveRateDepositPolicies]**](RetrieveRateDepositPolicies.md) |  | [optional] 
**fees** | [**list[RetrieveRateFees]**](RetrieveRateFees.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


