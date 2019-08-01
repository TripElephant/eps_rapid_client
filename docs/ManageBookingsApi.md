# eps_rapid.ManageBookingsApi

All URIs are relative to *https://api.ean.com/2.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**itineraries_get**](ManageBookingsApi.md#itineraries_get) | **GET** /itineraries | Retrieve Booking with Affiliate Reference Id
[**itineraries_itinerary_id_delete**](ManageBookingsApi.md#itineraries_itinerary_id_delete) | **DELETE** /itineraries/{itinerary_id} | Cancel Held Booking
[**itineraries_itinerary_id_get**](ManageBookingsApi.md#itineraries_itinerary_id_get) | **GET** /itineraries/{itinerary_id} | Retrieve Booking
[**itineraries_itinerary_id_rooms_room_id_delete**](ManageBookingsApi.md#itineraries_itinerary_id_rooms_room_id_delete) | **DELETE** /itineraries/{itinerary_id}/rooms/{room_id} | Cancel a room.
[**itineraries_itinerary_id_rooms_room_id_put**](ManageBookingsApi.md#itineraries_itinerary_id_rooms_room_id_put) | **PUT** /itineraries/{itinerary_id}/rooms/{room_id} | Change details of a room.


# **itineraries_get**
> Retrieve itineraries_get(accept, accept_encoding, authorization, customer_ip, user_agent, affiliate_reference_id, email, customer_session_id=customer_session_id, test=test)

Retrieve Booking with Affiliate Reference Id

This can be called directly without a token when an affiliate reference id is provided. It returns details about a booking associated with the affiliate reference id along with cancel links to cancel the booking. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ManageBookingsApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
affiliate_reference_id = 'affiliate_reference_id_example' # str | The affilliate reference id value. Example: `111A222BB33344CC5555` 
email = 'email_example' # str | Email associated with the booking.<br> Example: `test@example.com`. 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The retrieve call has a test header that can be used to return set responses with the following keywords:<br> * `standard` - Requires valid test booking. * `service_unavailable` * `internal_server_error`  (optional)

try:
    # Retrieve Booking with Affiliate Reference Id
    api_response = api_instance.itineraries_get(accept, accept_encoding, authorization, customer_ip, user_agent, affiliate_reference_id, email, customer_session_id=customer_session_id, test=test)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageBookingsApi->itineraries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **customer_ip** | **str**| IP address of the customer, as captured by your integration. Send IPV4 addresses only.&lt;br&gt; Ensure your integration passes the customer&#39;s IP, not your own. This value helps determine their location and assign the correct payment gateway.&lt;br&gt; Also used for fraud recovery and other important analytics.  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **affiliate_reference_id** | **str**| The affilliate reference id value. Example: &#x60;111A222BB33344CC5555&#x60;  | 
 **email** | **str**| Email associated with the booking.&lt;br&gt; Example: &#x60;test@example.com&#x60;.  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The retrieve call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; - Requires valid test booking. * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60;  | [optional] 

### Return type

[**Retrieve**](Retrieve.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itineraries_itinerary_id_delete**
> itineraries_itinerary_id_delete(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, token, customer_session_id=customer_session_id, test=test)

Cancel Held Booking

This link will be available in a held booking response. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ManageBookingsApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
itinerary_id = 'itinerary_id_example' # str | This parameter is used only to prefix the token value - no ID value is used.<br> Example: `8955599932111` 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The cancel call has a test header that can be used to return set responses with the following keywords:<br> * `standard` - Requires valid test held booking. * `service_unavailable` * `internal_server_error` * `post_stay_cancel`  (optional)

try:
    # Cancel Held Booking
    api_instance.itineraries_itinerary_id_delete(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, token, customer_session_id=customer_session_id, test=test)
except ApiException as e:
    print("Exception when calling ManageBookingsApi->itineraries_itinerary_id_delete: %s\n" % e)
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
 **test** | **str**| The cancel call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; - Requires valid test held booking. * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60; * &#x60;post_stay_cancel&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itineraries_itinerary_id_get**
> Retrieve itineraries_itinerary_id_get(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, customer_session_id=customer_session_id, test=test, token=token, email=email)

Retrieve Booking

This API call returns itinerary details and links to resume or cancel the booking. There are two methods to retrieve a booking: * Using the link included in the original Book response, example: https://api.ean.com/2.3/itineraries/8955599932111?token=QldfCGlcUA4GXVlSAQ4W * Using the email of the booking, example: https://api.ean.com/2.3/itineraries/8955599932111?email=customer@email.com 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ManageBookingsApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
itinerary_id = 'itinerary_id_example' # str | This parameter is used only to prefix the token value - no ID value is used.<br> Example: `8955599932111` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The retrieve call has a test header that can be used to return set responses. Passing standard in the Test header will retrieve a test booking, and passing any of the errors listed below will return a stubbed error response that you can use to test your error handling code. Additionally, refer to the Test Request documentation for more details on how these header values are used. * `standard` - Requires valid test booking. * `service_unavailable` * `internal_server_error`  (optional)
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m`  (optional)
email = 'email_example' # str | Email associated with the booking. (Email is required if the token is not provided the request) <br> Example: `test@example.com`.  (optional)

try:
    # Retrieve Booking
    api_response = api_instance.itineraries_itinerary_id_get(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, customer_session_id=customer_session_id, test=test, token=token, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManageBookingsApi->itineraries_itinerary_id_get: %s\n" % e)
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
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The retrieve call has a test header that can be used to return set responses. Passing standard in the Test header will retrieve a test booking, and passing any of the errors listed below will return a stubbed error response that you can use to test your error handling code. Additionally, refer to the Test Request documentation for more details on how these header values are used. * &#x60;standard&#x60; - Requires valid test booking. * &#x60;service_unavailable&#x60; * &#x60;internal_server_error&#x60;  | [optional] 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | [optional] 
 **email** | **str**| Email associated with the booking. (Email is required if the token is not provided the request) &lt;br&gt; Example: &#x60;test@example.com&#x60;.  | [optional] 

### Return type

[**Retrieve**](Retrieve.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itineraries_itinerary_id_rooms_room_id_delete**
> itineraries_itinerary_id_rooms_room_id_delete(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, room_id, token, customer_session_id=customer_session_id, test=test)

Cancel a room.

This link will be available in the retrieve response. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ManageBookingsApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
itinerary_id = 'itinerary_id_example' # str | This parameter is used only to prefix the token value - no ID value is used.<br> Example: `8955599932111` 
room_id = 'room_id_example' # str | Room ID of a property.<br> Example: `123abc`. 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The cancel call has a test header that can be used to return set responses with the following keywords:<br> * `standard` - Requires valid test booking. * `service_unavailable` * `unknown_internal_error` * `post_stay_cancel`  (optional)

try:
    # Cancel a room.
    api_instance.itineraries_itinerary_id_rooms_room_id_delete(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, room_id, token, customer_session_id=customer_session_id, test=test)
except ApiException as e:
    print("Exception when calling ManageBookingsApi->itineraries_itinerary_id_rooms_room_id_delete: %s\n" % e)
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
 **room_id** | **str**| Room ID of a property.&lt;br&gt; Example: &#x60;123abc&#x60;.  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The cancel call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; - Requires valid test booking. * &#x60;service_unavailable&#x60; * &#x60;unknown_internal_error&#x60; * &#x60;post_stay_cancel&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itineraries_itinerary_id_rooms_room_id_put**
> itineraries_itinerary_id_rooms_room_id_put(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, room_id, token, room_details_request_body, customer_session_id=customer_session_id, test=test)

Change details of a room.

This link will be available in the retrieve response. Changes in smoking preference and special request will be passed along to the property and are not guaranteed. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.ManageBookingsApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
customer_ip = 'customer_ip_example' # str | IP address of the customer, as captured by your integration. Send IPV4 addresses only.<br> Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br> Also used for fraud recovery and other important analytics. 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
itinerary_id = 'itinerary_id_example' # str | This parameter is used only to prefix the token value - no ID value is used.<br> Example: `8955599932111` 
room_id = 'room_id_example' # str | Room ID of a property.<br> Example: `123abc`. 
token = 'token_example' # str | Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: `MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m` 
room_details_request_body = eps_rapid.ChangeRoomDetailsRequest() # ChangeRoomDetailsRequest | The request body is required, but only the fields that are being changed need to be passed in. Fields that are not being changed should not be included in the request body.
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
test = 'test_example' # str | The change call has a test header that can be used to return set responses with the following keywords:<br> * `standard` - Requires valid test booking. * `service_unavailable` * `unknown_internal_error`  (optional)

try:
    # Change details of a room.
    api_instance.itineraries_itinerary_id_rooms_room_id_put(accept, accept_encoding, authorization, customer_ip, user_agent, itinerary_id, room_id, token, room_details_request_body, customer_session_id=customer_session_id, test=test)
except ApiException as e:
    print("Exception when calling ManageBookingsApi->itineraries_itinerary_id_rooms_room_id_put: %s\n" % e)
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
 **room_id** | **str**| Room ID of a property.&lt;br&gt; Example: &#x60;123abc&#x60;.  | 
 **token** | **str**| Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed. Example: &#x60;MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m&#x60;  | 
 **room_details_request_body** | [**ChangeRoomDetailsRequest**](ChangeRoomDetailsRequest.md)| The request body is required, but only the fields that are being changed need to be passed in. Fields that are not being changed should not be included in the request body. | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **test** | **str**| The change call has a test header that can be used to return set responses with the following keywords:&lt;br&gt; * &#x60;standard&#x60; - Requires valid test booking. * &#x60;service_unavailable&#x60; * &#x60;unknown_internal_error&#x60;  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

