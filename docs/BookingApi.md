# eps_rapid.BookingApi

All URIs are relative to *https://api.ean.com/2.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**itineraries_itinerary_id_payment_sessions_put**](BookingApi.md#itineraries_itinerary_id_payment_sessions_put) | **PUT** /itineraries/{itinerary_id}/payment-sessions | Complete Payment Session
[**itineraries_itinerary_id_put**](BookingApi.md#itineraries_itinerary_id_put) | **PUT** /itineraries/{itinerary_id} | Resume Booking
[**itineraries_post**](BookingApi.md#itineraries_post) | **POST** /itineraries | Create Booking
[**payment_sessions_post**](BookingApi.md#payment_sessions_post) | **POST** /payment-sessions | Register Payments


# **itineraries_itinerary_id_payment_sessions_put**
> CompletePaymentSession itineraries_itinerary_id_payment_sessions_put(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, token, customer_session_id=customer_session_id, test=test)

Complete Payment Session

<b>This link only applies to transactions where EPS takes the customer's payment information. This includes both Expedia Collect and Property Collect transactions.</b><br> This link will be available in the booking response only if you've opted into Two-Factor Authentication to comply with the September 2019 EU Regulations for PSD2. It should be called after Two-Factor Authentication has been completed by the customer in order to finalize the payment and complete the booking or hold attempt. Learn more with our [PSD2 Overview](https://developer.expediapartnersolutions.com/reference/psd2-regulation/) 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.BookingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
itinerary_id = 'itinerary_id_example' # str | This parameter is used only to prefix the token value - no ID value is used.<br> Example: `8955599932111` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The payment-sessions call has a test header that can be used to return set responses with the following keywords:<br> * `standard` * `service_unavailable` * `internal_server_error`  (optional)

try:
    # Complete Payment Session
    api_response = api_instance.itineraries_itinerary_id_payment_sessions_put(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, token, customer_session_id=customer_session_id, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->itineraries_itinerary_id_payment_sessions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **itinerary_id** | **str**| This parameter is used only to prefix the token value - no ID value is used.&lt;br&gt; Example: &#x60;8955599932111&#x60;  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The payment-sessions call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60;  | [optional] 

### Return type

[**CompletePaymentSession**](CompletePaymentSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itineraries_itinerary_id_put**
> itineraries_itinerary_id_put(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, token, customer_session_id=customer_session_id, test=test)

Resume Booking

This link will be available in the booking response after creating a held booking. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.BookingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
itinerary_id = 'itinerary_id_example' # str | This parameter is used only to prefix the token value - no ID value is used.<br> Example: `8955599932111` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The resume call has a test header that can be used to return set responses with the following keywords:<br> * `standard` - Requires valid test held booking. * `service_unavailable` * `internal_server_error`  (optional)

try:
    # Resume Booking
    api_instance.itineraries_itinerary_id_put(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, token, customer_session_id=customer_session_id, test=test)
except ApiException as e:
    print("Exception when calling BookingApi->itineraries_itinerary_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **itinerary_id** | **str**| This parameter is used only to prefix the token value - no ID value is used.&lt;br&gt; Example: &#x60;8955599932111&#x60;  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The resume call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; - Requires valid test held booking. * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itineraries_post**
> CreateItinerary itineraries_post(accept, accept_encoding, authorization, content_type, customer_ip, user_agent, token, itinerary_request_body, customer_session_id=customer_session_id, test=test)

Create Booking

This link will be available in the Price Check response or in the register payments response when Two-Factor Authentication is used. It returns an itinerary id and links to retrieve reservation details, cancel a held booking, resume a held booking or complete payment session. Please note that depending on the state of the booking, the response will contain only the applicable link(s). 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.BookingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
content_type = 'content_type_example' # str | This parameter is to specify which format the partner wants their response to be in. The only supported value is application/json at the moment. Example: `application/json` 
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
itinerary_request_body = eps_rapid.CreateItineraryRequest() # CreateItineraryRequest | 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The book call has a test header that can be used to return set responses with the following keywords:<br> * `standard` * `complete_payment_session` * `service_unavailable` * `internal_server_error` * `price_mismatch` * `cc_declined` * `rooms_unavailable`  (optional)

try:
    # Create Booking
    api_response = api_instance.itineraries_post(accept, accept_encoding, authorization, content_type, customer_ip, user_agent, token, itinerary_request_body, customer_session_id=customer_session_id, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->itineraries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **content_type** | **str**| This parameter is to specify which format the partner wants their response to be in. The only supported value is application/json at the moment. Example: &#x60;application/json&#x60;  | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **itinerary_request_body** | [**CreateItineraryRequest**](CreateItineraryRequest.md)|  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The book call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; * &#x60;complete_payment_session&#x60; * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60; * &#x60;price_mismatch&#x60; * &#x60;cc_declined&#x60; * &#x60;rooms_unavailable&#x60;  | [optional] 

### Return type

[**CreateItinerary**](CreateItinerary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_sessions_post**
> PaymentSessions payment_sessions_post(accept, accept_encoding, authorization, content_type, customer_ip, user_agent, token, payment_sessions_request_body, customer_session_id=customer_session_id, test=test)

Register Payments

<b>This link only applies to transactions where EPS takes the customer's payment information. This includes both Expedia Collect and Property Collect transactions.</b><br> This link will be available in the Price Check response if payment registration is required. It returns a payment session ID and a link to create a booking. This will be the first step in the booking flow only if you've opted into Two-Factor Authentication to comply with the September 2019 EU Regulations for PSD2. Learn more with our [PSD2 Overview](https://developer.expediapartnersolutions.com/reference/psd2-regulation/) 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.BookingApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
content_type = 'content_type_example' # str | This parameter is to specify which format the partner wants their response to be in. The only supported value is application/json at the moment. Example: `application/json` 
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
payment_sessions_request_body = eps_rapid.PaymentSessionsRequest() # PaymentSessionsRequest | 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The book call has a test header that can be used to return set responses with the following keywords:<br> * `standard` * `service_unavailable` * `internal_server_error`  (optional)

try:
    # Register Payments
    api_response = api_instance.payment_sessions_post(accept, accept_encoding, authorization, content_type, customer_ip, user_agent, token, payment_sessions_request_body, customer_session_id=customer_session_id, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->payment_sessions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **content_type** | **str**| This parameter is to specify which format the partner wants their response to be in. The only supported value is application/json at the moment. Example: &#x60;application/json&#x60;  | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **payment_sessions_request_body** | [**PaymentSessionsRequest**](PaymentSessionsRequest.md)|  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The book call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60;  | [optional] 

### Return type

[**PaymentSessions**](PaymentSessions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

