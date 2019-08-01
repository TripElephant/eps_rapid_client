# PropertyAvailabilityWithoutScoreRates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier for a rate. | 
**available_rooms** | **float** | The number of bookable rooms remaining with this rate in EPS inventory. Use this value to create rules for urgency messaging to alert users to low availability on busy travel dates or at popular properties. If the value returns as 2147483647 (max int value), the actual value could not be determined. Ensure your urgency messaging ignores such instances when returned. | 
**refundable** | **bool** | Indicates if the rate is fully refundable at the time of booking. Cancel penalties may still apply. Please refer to the cancel penalties section for reference. | 
**fenced_deal** | **bool** | Indicates that a \&quot;Member Only Deal\&quot; discount has been applied to the rate. Partners must be enabled to receive \&quot;Member Only Deals\&quot; to benefit from this parameter. If interested, partners should speak to their account representatives. This parameter can be used to merchandise if a \&quot;Member Only Deal\&quot; has been applied which will help partners to drive loyalty. In addition, it can be used by OTA&#39;s to create an opaque but public shopping experience. | 
**fenced_deal_available** | **bool** | Indicates if a \&quot;Member Only Deal\&quot; is available for this rate. | 
**deposit_required** | **bool** | If a deposit is required for the rate, this value will be &#x60;true&#x60;. A \&quot;deposit_policies\&quot; link will be included in this response to retrieve more information about the deposit, including amounts and timing. | 
**merchant_of_record** | **str** | * &#x60;expedia&#x60; - Payment is taken by Expedia. The payment options avaliable can be discovered using the \&quot;payment-options\&quot; link in the response. This includes AFFILIATE_COLLECT payments. * &#x60;property&#x60; - Payment is taken by the property.  | 
**amenities** | [**dict(str, Amenity)**](Amenity.md) | Room amenities. | [optional] 
**links** | [**dict(str, Link)**](Link.md) | A map of links, including links to request payment options and deposit policies. | 
**bed_groups** | [**dict(str, BedGroupAvailability)**](BedGroupAvailability.md) | A map of the room&#39;s bed groups. | [optional] 
**cancel_penalties** | [**list[PropertyAvailabilityWithoutScoreCancelPenalties]**](PropertyAvailabilityWithoutScoreCancelPenalties.md) | Array of &#x60;cancel_penalty&#x60; objects containing cancel penalty information. Will not be populated on non refundable. | [optional] 
**occupancy_pricing** | [**RoomRates**](RoomRates.md) |  | 
**promotions** | [**PropertyAvailabilityWithoutScorePromotions**](PropertyAvailabilityWithoutScorePromotions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


