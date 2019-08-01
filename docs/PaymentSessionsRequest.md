# PaymentSessionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the EgPayments.js library. | 
**browser_accept_header** | **str** | The customer&#39;s browser accept header that was used in the booking request. | 
**encoded_browser_metadata** | **str** | Encoded browser metadata, provided by the EgPayments.js library. | 
**preferred_challenge_window_size** | **str** | The preferred window size that needs to be displayed to the customer. Following are the possible values of this field:   * &#x60;extra_small&#x60;: 250 x 400   * &#x60;small&#x60;: 390 x 400   * &#x60;medium&#x60;: 600 x 400   * &#x60;large&#x60;: 500 x 600   * &#x60;full_screen&#x60;: Full screen  | 
**merchant_url** | **str** | Fully qualified URL of merchant website or customer care site. | 
**customer_account_details** | [**PaymentSessionsRequestCustomerAccountDetails**](PaymentSessionsRequestCustomerAccountDetails.md) |  | 
**payments** | **object** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


