# PropertyContent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Unique Expedia property ID. | [optional] 
**name** | **str** | Property name. | [optional] 
**address** | [**PropertyContentAddress**](PropertyContentAddress.md) |  | [optional] 
**ratings** | [**PropertyContentRatings**](PropertyContentRatings.md) |  | [optional] 
**location** | [**PropertyContentLocation**](PropertyContentLocation.md) |  | [optional] 
**phone** | **str** | The property&#39;s phone number. | [optional] 
**fax** | **str** | The property&#39;s fax number. | [optional] 
**category** | [**PropertyContentCategory**](PropertyContentCategory.md) |  | [optional] 
**business_model** | [**PropertyContentBusinessModel**](PropertyContentBusinessModel.md) |  | [optional] 
**rank** | **float** | The property’s rank across all properties. This value sorts properties based on EPS transactional data and details about the property, with 1 indicating the best-performing property and others following in ascending numerical order. | [optional] 
**checkin** | [**PropertyContentCheckin**](PropertyContentCheckin.md) |  | [optional] 
**checkout** | [**PropertyContentCheckout**](PropertyContentCheckout.md) |  | [optional] 
**fees** | [**PropertyContentFees**](PropertyContentFees.md) |  | [optional] 
**policies** | [**PropertyContentPolicies**](PropertyContentPolicies.md) |  | [optional] 
**attributes** | [**PropertyContentAttributes**](PropertyContentAttributes.md) |  | [optional] 
**amenities** | [**dict(str, Amenity)**](Amenity.md) | Lists all of the amenities available for all guests at the property. See our [amenities reference](https://developer.expediapartnersolutions.com/reference/content-reference-lists-2-3/) for current known amenity ID and name values. | [optional] 
**images** | [**list[PropertyContentImages]**](PropertyContentImages.md) | Contains all property images available. | [optional] 
**onsite_payments** | [**PropertyContentOnsitePayments**](PropertyContentOnsitePayments.md) |  | [optional] 
**rooms** | [**dict(str, RoomContent)**](RoomContent.md) | Information about all of the rooms at the property. | [optional] 
**rates** | [**dict(str, RateContent)**](RateContent.md) | Additional information about the rates offered by the property. This should be used in conjunction with the pricing and other rate-related information in shopping. | [optional] 
**dates** | [**PropertyContentDates**](PropertyContentDates.md) |  | [optional] 
**descriptions** | [**PropertyContentDescriptions**](PropertyContentDescriptions.md) |  | [optional] 
**statistics** | [**dict(str, Statistic)**](Statistic.md) | Statistics of the property, such as number of floors. See our [statistics reference](https://developer.expediapartnersolutions.com/reference/content-reference-lists-2-3/) for current known statistics ID and name values. | [optional] 
**airports** | [**PropertyContentAirports**](PropertyContentAirports.md) |  | [optional] 
**registry_number** | **str** | The property&#39;s registry number required by some jurisdictions. | [optional] 
**themes** | [**dict(str, Theme)**](Theme.md) | Themes that describe the property. See our [themes reference](https://developer.expediapartnersolutions.com/reference/content-reference-lists-2-3/) for current known theme ID and name values. | [optional] 
**all_inclusive** | [**PropertyContentAllInclusive**](PropertyContentAllInclusive.md) |  | [optional] 
**tax_id** | **str** | Tax ID. | [optional] 
**chain** | [**Chain**](Chain.md) |  | [optional] 
**brand** | [**Brand**](Brand.md) |  | [optional] 
**spoken_languages** | [**dict(str, SpokenLanguage)**](SpokenLanguage.md) | Languages spoken at the property. | [optional] 
**multi_unit** | **bool** | Boolean value indicating if a property is a multi-unit property. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


