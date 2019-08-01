# TripAdvisor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Unique Expedia property ID. | [optional] 
**tripadvisor_id** | **str** | Unique TripAdvisor property ID. Can be used for mapping properties across suppliers. | [optional] 
**rating** | **str** | TripAdvisor rating for the property. Returns a value between 1.0 and 5.0. | [optional] 
**count** | **float** | Number of TripAdvisor guest reviews for the property. Only provided when greater than zero. | [optional] 
**links** | [**dict(str, Link)**](Link.md) | Link to the TripAdvisor rating image. Display of the rating image is required per TripAdvisor’s contract. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


