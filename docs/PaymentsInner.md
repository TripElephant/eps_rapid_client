# PaymentsInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifier for the type of payment. If affiliate_collect, cardholder information is not required as EPS will not be processing the payment. | 
**card_type** | **str** | The type of credit card that is being used. Obtain possible values from the Payment Options call. Required for credit card transactions. | [optional] 
**number** | **str** | Card number. Required for credit card transactions. | [optional] 
**security_code** | **str** | CVV/CSV code from the back of the customer&#39;s card. Required for credit card transactions. | [optional] 
**expiration_month** | **str** | Two-digit month the credit card will expire. Required for credit card transactions. | [optional] 
**expiration_year** | **str** | Year the credit card will expire. Required for credit card transactions. | [optional] 
**billing_contact** | [**BillingContact**](BillingContact.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


