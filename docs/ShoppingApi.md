# eps_rapid.ShoppingApi

All URIs are relative to *https://api.ean.com/2.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**properties_availability_get**](ShoppingApi.md#properties_availability_get) | **GET** /properties/availability | Get property room rates and availability
[**properties_property_id_deposit_policies_get**](ShoppingApi.md#properties_property_id_deposit_policies_get) | **GET** /properties/{property_id}/deposit-policies | Get Deposit Policy
[**properties_property_id_payment_options_get**](ShoppingApi.md#properties_property_id_payment_options_get) | **GET** /properties/{property_id}/payment-options | Get Accepted Payment Types - EPS MOR Only
[**properties_property_id_rooms_room_id_rates_rate_id_price_check_get**](ShoppingApi.md#properties_property_id_rooms_room_id_rates_rate_id_price_check_get) | **GET** /properties/{property_id}/rooms/{room_id}/rates/{rate_id}/price-check | Get Current Price for Pre-Booking


# **properties_availability_get**
> PropertyAvailabilities properties_availability_get(accept, accept_encoding, authorization, user_agent, checkin, checkout, currency, language, country_code, occupancy, property_id, sales_channel, sales_environment, sort_type, rate_plan_count, customer_ip=customer_ip, customer_session_id=customer_session_id, test=test, filter=filter, rate_option=rate_option, billing_terms=billing_terms, payment_terms=payment_terms, partner_point_of_sale=partner_point_of_sale, platform_name=platform_name)

Get property room rates and availability

Returns rates and availability on all room types for specified properties (maximum of 250 properties per request).  The response includes rate details such as promos, whether the rate is refundable, cancellation penalties and a full price breakdown to meet the price display requirements for your market. * Multiple rooms of the same type may be requested by including multiple instances of the `occupancy` parameter. * The `nightly` array includes each individual night's charges. When the total price includes fees, charges, or adjustments that are not divided by night, these amounts will be included in the `stay` rate array, which details charges applied to the entire stay (each check-in). 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ShoppingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
checkin = 'checkin_example' # str | Check-in date, in ISO 8601 format (YYYY-MM-DD) Example: `2018-09-15`. 
checkout = 'checkout_example' # str | Check-out date, in ISO 8601 format (YYYY-MM-DD). Availability can be searched up to 500 days in advance of this date. Total length of stay cannot exceed 28 nights.  Example: `2018-09-17`. 
currency = 'currency_example' # str | Requested currency for the rates, in ISO 4217 format<br> Example: `USD`.<br> Currency Options: [https://developer.expediapartnersolutions.com/reference/currency-options/](https://developer.expediapartnersolutions.com/reference/currency-options/) 
language = 'language_example' # str | Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: `language=en-US`  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/) 
country_code = 'country_code_example' # str | Integrations that use multiple points of sale (POS) must pass the country code that matches the point of sale being used for each specific request. For Example: .co.mx would pass in MX or .co.uk would pass in UK. For primary root (.com, .net, .biz, etc) domains, pass the country in which the majority of business occurs.<br> For more information see: [https://www.iso.org/obp/ui/#search/code/](https://www.iso.org/obp/ui/#search/code/)<br> 
occupancy = ['occupancy_example'] # list[str] | Defines the requested occupancy for a single room. Each room must have at least 1 adult occupant.<br> Format: `numberOfAdults[-firstChildAge[,nextChildAge]]`<br> To request multiple rooms (of the same type), include one instance of occupancy for each room requested. Up to 8 rooms may be requested or booked at once.<br> Examples: * 2 adults, one 9-year-old and one 4-year-old would be represented by `occupancy=2-9,4`.<br> * A multi-room request to lodge an additional 2 adults would be represented by `occupancy=2-9,4&occupancy=2` 
property_id = ['property_id_example'] # list[str] | The ID of the property you want to search for. You can provide 1 to 250 property_id parameters.  Example: `property_id=19248&property_id=20321` 
sales_channel = 'sales_channel_example' # str | You must provide the sales channel for the display of rates. EPS dynamically provides the best content for optimal conversion on each sales channel. If you have a sales channel that is not currently supported in this list, please contact our support team.<br> * `website` - Standard website accessed from the customer's computer * `agent_tool` - Your own agent tool used by your call center or retail store agent * `mobile_app` - An application installed on a phone or tablet device * `mobile_web` - A web browser application on a phone or tablet device * `meta` - Rates will be passed to and displayed on a 3rd party comparison website * `cache` - Rates will be used to populate a local cache 
sales_environment = 'sales_environment_example' # str | You must provide the sales environment in which rates will be sold. EPS dynamically provides the best content for optimal conversion. If you have a sales environment that is not currently supported in this list, please contact our support team.<br> * `hotel_package` - Use when selling the hotel with a transport product, e.g. flight & hotel. * `hotel_only` - Use when selling the hotel as an individual product. * `loyalty` - Use when you are selling the hotel as part of a loyalty program and the price is converted to points. 
sort_type = 'preferred' # str | Order properties should be returned in. If the requested sort type cannot be applied, the response will include a Warning header indicating the results are unsorted.<br> * `preferred` - Sort optimised for profitability.  (default to preferred)
rate_plan_count = 8.14 # float | The number of rates to return per property. This will return the lowest rate first, on up to the highest rate. The lowest rate has been proven to provide the best conversion rate and so a value of 1 is recommended.  The value must be greater than 0. 
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics.  (optional)
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | Shop calls have a test header that can be used to return set responses with the following keywords:<br> * `standard` * `service_unavailable` * `unknown_internal_error`  (optional)
filter = ['filter_example'] # list[str] | Single filter type. Send multiple instances of this parameter to request multiple filters.<br> * `refundable` - Filters results to only show fully refundable rates. * `expedia_collect` - Filters results to only show rates where payment is collected by Expedia at the time of booking. These properties can be eligible for payments via Expedia Affiliate Collect(EAC). * `property_collect` - Filters results to only show rates where payment is collected by the property after booking. This can include rates that require a deposit by the property, dependent upon the deposit policies.  Example: `filter=refundable&filter=expedia_collect`  (optional)
rate_option = ['rate_option_example'] # list[str] | Request specific rate options for each property. Send multiple instances of this parameter to request multiple rate options. Accepted values:<br> * `closed_user_group` - Return closed user group rates for each property. This feature must be enabled and requires a user to be logged in to request these rates. * `net_rates` - Return net rates for each property. This feature must be enabled to request these rates. * `cross_sell` - Identify if the traffic is coming from a cross sell booking. Where the traveler has booked another service (flight, car, activities...) before hotel.  Example: `rate_option=closed_user_group&rate_option=net_rates`  (optional)
billing_terms = 'billing_terms_example' # str | This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  (optional)
payment_terms = 'payment_terms_example' # str | This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  (optional)
partner_point_of_sale = 'partner_point_of_sale_example' # str | This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)
platform_name = 'platform_name_example' # str | This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)

try:
    # Get property room rates and availability
    api_response = api_instance.properties_availability_get(accept, accept_encoding, authorization, user_agent, checkin, checkout, currency, language, country_code, occupancy, property_id, sales_channel, sales_environment, sort_type, rate_plan_count, customer_ip=customer_ip, customer_session_id=customer_session_id, test=test, filter=filter, rate_option=rate_option, billing_terms=billing_terms, payment_terms=payment_terms, partner_point_of_sale=partner_point_of_sale, platform_name=platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingApi->properties_availability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **checkin** | **str**| Check-in date, in ISO 8601 format (YYYY-MM-DD) Example: &#x60;2018-09-15&#x60;.  | 
 **checkout** | **str**| Check-out date, in ISO 8601 format (YYYY-MM-DD). Availability can be searched up to 500 days in advance of this date. Total length of stay cannot exceed 28 nights.  Example: &#x60;2018-09-17&#x60;.  | 
 **currency** | **str**| Requested currency for the rates, in ISO 4217 format&lt;br&gt; Example: &#x60;USD&#x60;.&lt;br&gt; Currency Options: [https://developer.expediapartnersolutions.com/reference/currency-options/](https://developer.expediapartnersolutions.com/reference/currency-options/)  | 
 **language** | **str**| Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: &#x60;language&#x3D;en-US&#x60;  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/)  | 
 **country_code** | **str**| Integrations that use multiple points of sale (POS) must pass the country code that matches the point of sale being used for each specific request. For Example: .co.mx would pass in MX or .co.uk would pass in UK. For primary root (.com, .net, .biz, etc) domains, pass the country in which the majority of business occurs.&lt;br&gt; For more information see: [https://www.iso.org/obp/ui/#search/code/](https://www.iso.org/obp/ui/#search/code/)&lt;br&gt;  | 
 **occupancy** | [**list[str]**](str.md)| Defines the requested occupancy for a single room. Each room must have at least 1 adult occupant.&lt;br&gt; Format: &#x60;numberOfAdults[-firstChildAge[,nextChildAge]]&#x60;&lt;br&gt; To request multiple rooms (of the same type), include one instance of occupancy for each room requested. Up to 8 rooms may be requested or booked at once.&lt;br&gt; Examples: * 2 adults, one 9-year-old and one 4-year-old would be represented by &#x60;occupancy&#x3D;2-9,4&#x60;.&lt;br&gt; * A multi-room request to lodge an additional 2 adults would be represented by &#x60;occupancy&#x3D;2-9,4&amp;occupancy&#x3D;2&#x60;  | 
 **property_id** | [**list[str]**](str.md)| The ID of the property you want to search for. You can provide 1 to 250 property_id parameters.  Example: &#x60;property_id&#x3D;19248&amp;property_id&#x3D;20321&#x60;  | 
 **sales_channel** | **str**| You must provide the sales channel for the display of rates. EPS dynamically provides the best content for optimal conversion on each sales channel. If you have a sales channel that is not currently supported in this list, please contact our support team.&lt;br&gt; * &#x60;website&#x60; - Standard website accessed from the customer&#39;s computer * &#x60;agent_tool&#x60; - Your own agent tool used by your call center or retail store agent * &#x60;mobile_app&#x60; - An application installed on a phone or tablet device * &#x60;mobile_web&#x60; - A web browser application on a phone or tablet device * &#x60;meta&#x60; - Rates will be passed to and displayed on a 3rd party comparison website * &#x60;cache&#x60; - Rates will be used to populate a local cache  | 
 **sales_environment** | **str**| You must provide the sales environment in which rates will be sold. EPS dynamically provides the best content for optimal conversion. If you have a sales environment that is not currently supported in this list, please contact our support team.&lt;br&gt; * &#x60;hotel_package&#x60; - Use when selling the hotel with a transport product, e.g. flight &amp; hotel. * &#x60;hotel_only&#x60; - Use when selling the hotel as an individual product. * &#x60;loyalty&#x60; - Use when you are selling the hotel as part of a loyalty program and the price is converted to points.  | 
 **sort_type** | **str**| Order properties should be returned in. If the requested sort type cannot be applied, the response will include a Warning header indicating the results are unsorted.&lt;br&gt; * &#x60;preferred&#x60; - Sort optimised for profitability.  | [default to preferred]
 **rate_plan_count** | **float**| The number of rates to return per property. This will return the lowest rate first, on up to the highest rate. The lowest rate has been proven to provide the best conversion rate and so a value of 1 is recommended.  The value must be greater than 0.  | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | [optional] 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| Shop calls have a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; * &#x60;service_unavailable&#x60; * &#x60;unknown_internal_error&#x60;  | [optional] 
 **filter** | [**list[str]**](str.md)| Single filter type. Send multiple instances of this parameter to request multiple filters.&lt;br&gt; * &#x60;refundable&#x60; - Filters results to only show fully refundable rates. * &#x60;expedia_collect&#x60; - Filters results to only show rates where payment is collected by Expedia at the time of booking. These properties can be eligible for payments via Expedia Affiliate Collect(EAC). * &#x60;property_collect&#x60; - Filters results to only show rates where payment is collected by the property after booking. This can include rates that require a deposit by the property, dependent upon the deposit policies.  Example: &#x60;filter&#x3D;refundable&amp;filter&#x3D;expedia_collect&#x60;  | [optional] 
 **rate_option** | [**list[str]**](str.md)| Request specific rate options for each property. Send multiple instances of this parameter to request multiple rate options. Accepted values:&lt;br&gt; * &#x60;closed_user_group&#x60; - Return closed user group rates for each property. This feature must be enabled and requires a user to be logged in to request these rates. * &#x60;net_rates&#x60; - Return net rates for each property. This feature must be enabled to request these rates. * &#x60;cross_sell&#x60; - Identify if the traffic is coming from a cross sell booking. Where the traveler has booked another service (flight, car, activities...) before hotel.  Example: &#x60;rate_option&#x3D;closed_user_group&amp;rate_option&#x3D;net_rates&#x60;  | [optional] 
 **billing_terms** | **str**| This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **payment_terms** | **str**| This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **partner_point_of_sale** | **str**| This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **platform_name** | **str**| This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 

### Return type

[**PropertyAvailabilities**](PropertyAvailabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_property_id_deposit_policies_get**
> DepositPolicies properties_property_id_deposit_policies_get(accept, accept_encoding, authorization, user_agent, property_id, token, customer_ip=customer_ip, customer_session_id=customer_session_id, test=test)

Get Deposit Policy

This link will be available in the shop response when rates require a deposit. It returns the amounts and dates for when any deposits are due. Deposit information is obtained by making a deposit-policies API call using this link. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ShoppingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
property_id = 'property_id_example' # str | Expedia Property ID.<br> Example: `19248` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics.  (optional)
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | Deposit policies calls have a test header that can be used to return set responses with the following keywords: * `all` * `nights` * `amount` * `percent` * `remainder` * `service_unavailable` * `unknown_internal_error`  (optional)

try:
    # Get Deposit Policy
    api_response = api_instance.properties_property_id_deposit_policies_get(accept, accept_encoding, authorization, user_agent, property_id, token, customer_ip=customer_ip, customer_session_id=customer_session_id, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingApi->properties_property_id_deposit_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **property_id** | **str**| Expedia Property ID.&lt;br&gt; Example: &#x60;19248&#x60;  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | [optional] 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| Deposit policies calls have a test header that can be used to return set responses with the following keywords: * &#x60;all&#x60; * &#x60;nights&#x60; * &#x60;amount&#x60; * &#x60;percent&#x60; * &#x60;remainder&#x60; * &#x60;service_unavailable&#x60; * &#x60;unknown_internal_error&#x60;  | [optional] 

### Return type

[**DepositPolicies**](DepositPolicies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_property_id_payment_options_get**
> PaymentOption properties_property_id_payment_options_get(accept, accept_encoding, authorization, property_id, token, user_agent, customer_ip=customer_ip, customer_session_id=customer_session_id)

Get Accepted Payment Types - EPS MOR Only

Returns the accepted payment options.  Use this API to power your checkout page and display valid forms of payment, ensuring a smooth booking. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ShoppingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
property_id = 'property_id_example' # str | Expedia Property ID.<br> Example: `19248` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics.  (optional)
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)

try:
    # Get Accepted Payment Types - EPS MOR Only
    api_response = api_instance.properties_property_id_payment_options_get(accept, accept_encoding, authorization, property_id, token, user_agent, customer_ip=customer_ip, customer_session_id=customer_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingApi->properties_property_id_payment_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **property_id** | **str**| Expedia Property ID.&lt;br&gt; Example: &#x60;19248&#x60;  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | [optional] 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 

### Return type

[**PaymentOption**](PaymentOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_property_id_rooms_room_id_rates_rate_id_price_check_get**
> RoomPriceCheck properties_property_id_rooms_room_id_rates_rate_id_price_check_get(accept, accept_encoding, authorization, user_agent, property_id, room_id, rate_id, token, customer_ip=customer_ip, customer_session_id=customer_session_id, test=test)

Get Current Price for Pre-Booking

Confirms the price returned by the Property Availability response. Use this API to verify a previously-selected rate is still valid before booking. If the price is matched, the response returns a link to request a booking. If the price has changed, the response returns new price details and a booking link for the new price. If the rate is no longer available, the response will return a new Property Availability request link to search again for different rates. In the event of a price change, go back to Property Availability and book the property at the new price or return to additional rates for the property. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ShoppingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
property_id = 'property_id_example' # str | Expedia Property ID.<br> Example: `19248` 
room_id = 'room_id_example' # str | Room ID of a property.<br> Example: `123abc`. 
rate_id = 'rate_id_example' # str | Rate ID of a room.<br> Example: `123abc` 
token = 'token_example' # str | A hashed collection of query parameters. Used to maintain state across calls. This token is provided as part of the price check link from the shop response.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics.  (optional)
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | Price check calls have a test header that can be used to return set responses with the following keywords:   * `matched`   * `price_changed`   * `sold_out`   * `service_unavailable`   * `unknown_internal_error`  (optional)

try:
    # Get Current Price for Pre-Booking
    api_response = api_instance.properties_property_id_rooms_room_id_rates_rate_id_price_check_get(accept, accept_encoding, authorization, user_agent, property_id, room_id, rate_id, token, customer_ip=customer_ip, customer_session_id=customer_session_id, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShoppingApi->properties_property_id_rooms_room_id_rates_rate_id_price_check_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **property_id** | **str**| Expedia Property ID.&lt;br&gt; Example: &#x60;19248&#x60;  | 
 **room_id** | **str**| Room ID of a property.&lt;br&gt; Example: &#x60;123abc&#x60;.  | 
 **rate_id** | **str**| Rate ID of a room.&lt;br&gt; Example: &#x60;123abc&#x60;  | 
 **token** | **str**| A hashed collection of query parameters. Used to maintain state across calls. This token is provided as part of the price check link from the shop response. | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | [optional] 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| Price check calls have a test header that can be used to return set responses with the following keywords:   * &#x60;matched&#x60;   * &#x60;price_changed&#x60;   * &#x60;sold_out&#x60;   * &#x60;service_unavailable&#x60;   * &#x60;unknown_internal_error&#x60;  | [optional] 

### Return type

[**RoomPriceCheck**](RoomPriceCheck.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

