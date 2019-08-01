# eps_rapid.GeographyApi

All URIs are relative to *https://api.ean.com/2.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airports_get**](GeographyApi.md#airports_get) | **GET** /airports | Airports
[**airports_iata_airport_code_get**](GeographyApi.md#airports_iata_airport_code_get) | **GET** /airports/{iata_airport_code} | Airport
[**properties_geography_post**](GeographyApi.md#properties_geography_post) | **POST** /properties/geography | Properties within Polygon
[**regions_get**](GeographyApi.md#regions_get) | **GET** /regions | Regions
[**regions_region_id_get**](GeographyApi.md#regions_region_id_get) | **GET** /regions/{region_id} | Region


# **airports_get**
> Airports airports_get(accept, accept_encoding, authorization, user_agent, language, include, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)

Airports

Returns the geographic definition and property mappings of all airports in our geography system. The response is a map in JSON format, where the key is the IATA airport code and the airport object is the value. The map has no order. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.GeographyApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
language = 'language_example' # str | Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: `language=en-US`  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/) 
include = ['include_example'] # list[str] | Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.   * details - Include the metadata, coordinates and associated region of the airport.   * property_ids - Include the list of the property IDs within a 20km radius of the airport.   * associated_region_property_ids - Include the list of property IDs within the polygon of the associated region. The associated region is the city or multi-city most commonly associated with the airport.  Example: `include=details&include=property_ids` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
billing_terms = 'billing_terms_example' # str | This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  (optional)
partner_point_of_sale = 'partner_point_of_sale_example' # str | This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)
payment_terms = 'payment_terms_example' # str | This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  (optional)
platform_name = 'platform_name_example' # str | This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)

try:
    # Airports
    api_response = api_instance.airports_get(accept, accept_encoding, authorization, user_agent, language, include, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographyApi->airports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **language** | **str**| Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: &#x60;language&#x3D;en-US&#x60;  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/)  | 
 **include** | [**list[str]**](str.md)| Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.   * details - Include the metadata, coordinates and associated region of the airport.   * property_ids - Include the list of the property IDs within a 20km radius of the airport.   * associated_region_property_ids - Include the list of property IDs within the polygon of the associated region. The associated region is the city or multi-city most commonly associated with the airport.  Example: &#x60;include&#x3D;details&amp;include&#x3D;property_ids&#x60;  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **billing_terms** | **str**| This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **partner_point_of_sale** | **str**| This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **payment_terms** | **str**| This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **platform_name** | **str**| This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 

### Return type

[**Airports**](Airports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **airports_iata_airport_code_get**
> Airport airports_iata_airport_code_get(accept, accept_encoding, authorization, user_agent, language, include, iata_airport_code, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)

Airport

Returns the geographic definition and property mappings for the requested IATA airport code. The response is a single JSON formatted airport object. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.GeographyApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
language = 'language_example' # str | Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: `language=en-US`  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/) 
include = ['include_example'] # list[str] | Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.   * details - Include the metadata, coordinates and associated region of the airport.   * property_ids - Include the list of the property IDs within a 20km radius of the airport.   * associated_region_property_ids - Include the list of property IDs within the polygon of the associated region. The associated region is the city or multi-city most commonly associated with the airport.  Example: `include=details&include=property_ids` 
iata_airport_code = 'iata_airport_code_example' # str | 3-character IATA airport code of the airport to retrieve. The code must be upper case.  Example: `ORD`. 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
billing_terms = 'billing_terms_example' # str | This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  (optional)
partner_point_of_sale = 'partner_point_of_sale_example' # str | This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)
payment_terms = 'payment_terms_example' # str | This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  (optional)
platform_name = 'platform_name_example' # str | This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)

try:
    # Airport
    api_response = api_instance.airports_iata_airport_code_get(accept, accept_encoding, authorization, user_agent, language, include, iata_airport_code, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographyApi->airports_iata_airport_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **language** | **str**| Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: &#x60;language&#x3D;en-US&#x60;  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/)  | 
 **include** | [**list[str]**](str.md)| Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.   * details - Include the metadata, coordinates and associated region of the airport.   * property_ids - Include the list of the property IDs within a 20km radius of the airport.   * associated_region_property_ids - Include the list of property IDs within the polygon of the associated region. The associated region is the city or multi-city most commonly associated with the airport.  Example: &#x60;include&#x3D;details&amp;include&#x3D;property_ids&#x60;  | 
 **iata_airport_code** | **str**| 3-character IATA airport code of the airport to retrieve. The code must be upper case.  Example: &#x60;ORD&#x60;.  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **billing_terms** | **str**| This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **partner_point_of_sale** | **str**| This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **payment_terms** | **str**| This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **platform_name** | **str**| This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 

### Return type

[**Airport**](Airport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_geography_post**
> PropertyGeographyMap properties_geography_post(accept, accept_encoding, authorization, content_type, user_agent, include, properties_geography_request_body, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)

Properties within Polygon

Returns the properties within an custom polygon that represents a multi-city area or smaller. The coordinates of the polygon should be in [GeoJSON format](https://tools.ietf.org/html/rfc7946) and the polygon must conform to the following restrictions:   * Polygon size - diagonal distance of the polygon must be less than 500km   * Polygon type - only single polygons are supported   * Number of coordinates - must be <= 2000 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.GeographyApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
content_type = 'content_type_example' # str | This parameter is to specify which format the partner wants their response to be in. The only supported value is application/json at the moment. Example: `application/json` 
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
include = 'include_example' # str | Options for which content to return in the response. The value must be lower case.   * property_ids - Include the property IDs.  Example: `property_ids` Possible values: `property_ids`. 
properties_geography_request_body = eps_rapid.PropertiesGeoJsonRequest() # PropertiesGeoJsonRequest | 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
billing_terms = 'billing_terms_example' # str | This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  (optional)
partner_point_of_sale = 'partner_point_of_sale_example' # str | This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)
payment_terms = 'payment_terms_example' # str | This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  (optional)
platform_name = 'platform_name_example' # str | This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)

try:
    # Properties within Polygon
    api_response = api_instance.properties_geography_post(accept, accept_encoding, authorization, content_type, user_agent, include, properties_geography_request_body, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographyApi->properties_geography_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **content_type** | **str**| This parameter is to specify which format the partner wants their response to be in. The only supported value is application/json at the moment. Example: &#x60;application/json&#x60;  | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **include** | **str**| Options for which content to return in the response. The value must be lower case.   * property_ids - Include the property IDs.  Example: &#x60;property_ids&#x60; Possible values: &#x60;property_ids&#x60;.  | 
 **properties_geography_request_body** | [**PropertiesGeoJsonRequest**](PropertiesGeoJsonRequest.md)|  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **billing_terms** | **str**| This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **partner_point_of_sale** | **str**| This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **payment_terms** | **str**| This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **platform_name** | **str**| This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 

### Return type

[**PropertyGeographyMap**](PropertyGeographyMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_get**
> Regions regions_get(accept, accept_encoding, authorization, user_agent, language, include, customer_session_id=customer_session_id, ancestor_id=ancestor_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)

Regions

Returns the geographic definition and property mappings of regions matching the specified parameters.<br><br>  To request all regions in the world, omit the `ancestor` query parameter. To request all regions in a specific continent, country or other level, specify the ID of that region as the `ancestor`. Refer to the list of [top level regions](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/).<br><br>  The response is a paginated list of regions. The response will contain a header, `Link`. The `Link` header contains a single URL to get the immediate next page of results, and follows the [IETF standard](https://tools.ietf.org/html/rfc5988). To get the next page of results, simply follow the `next` URL in the `Link` header without modifying it. When no `Link` header is returned with an empty body and a 200 response code, the pagination has completed. If the link expires, there will be an `expires` link-extension that is the UTC date the link will expire, in ISO 8601 format.<br>  * Example: `<https://api.ean.com/2.3/regions?token=DXF1ZXJ5QW5kRmV0Y2gBAAAAAAdcoBgWbUpHYTdsdFVRc2U4c0xfLUhGMzM1QQ>; rel=\"next\"; expires=\"2019-03-05T07:23:14.000Z\"` 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.GeographyApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
language = 'language_example' # str | Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: `language=en-US`  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/) 
include = ['include_example'] # list[str] | Options for which content to return in the response. This parameter can be supplied multiple times with different values. The standard and details options cannot be requested together. The value must be lower case.   * standard - Include the metadata and basic hierarchy of each region.   * details - Include the metadata, coordinates and full hierarchy of each region.   * property_ids - Include the list of property IDs within the bounding polygon of each region.   * property_ids_expanded - Include the list of property IDs within the bounding polygon of each region and property IDs from the surrounding area if minimal properties are within the region.  Example: `include=details&include=property_ids` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
ancestor_id = 'ancestor_id_example' # str | ID of the ancestor of regions to retrieve. Refer to the list of [top level regions](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/).  Example: `602962`.  (optional)
billing_terms = 'billing_terms_example' # str | This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  (optional)
partner_point_of_sale = 'partner_point_of_sale_example' # str | This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)
payment_terms = 'payment_terms_example' # str | This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  (optional)
platform_name = 'platform_name_example' # str | This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)

try:
    # Regions
    api_response = api_instance.regions_get(accept, accept_encoding, authorization, user_agent, language, include, customer_session_id=customer_session_id, ancestor_id=ancestor_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographyApi->regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **language** | **str**| Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: &#x60;language&#x3D;en-US&#x60;  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/)  | 
 **include** | [**list[str]**](str.md)| Options for which content to return in the response. This parameter can be supplied multiple times with different values. The standard and details options cannot be requested together. The value must be lower case.   * standard - Include the metadata and basic hierarchy of each region.   * details - Include the metadata, coordinates and full hierarchy of each region.   * property_ids - Include the list of property IDs within the bounding polygon of each region.   * property_ids_expanded - Include the list of property IDs within the bounding polygon of each region and property IDs from the surrounding area if minimal properties are within the region.  Example: &#x60;include&#x3D;details&amp;include&#x3D;property_ids&#x60;  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **ancestor_id** | **str**| ID of the ancestor of regions to retrieve. Refer to the list of [top level regions](https://developer.expediapartnersolutions.com/reference/geography-reference-lists-2-2/).  Example: &#x60;602962&#x60;.  | [optional] 
 **billing_terms** | **str**| This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **partner_point_of_sale** | **str**| This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **payment_terms** | **str**| This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **platform_name** | **str**| This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 

### Return type

[**Regions**](Regions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regions_region_id_get**
> Region regions_region_id_get(accept, accept_encoding, authorization, user_agent, region_id, language, include, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)

Region

Returns the geographic definition and property mappings for the requested Region ID. The response is a single JSON formatted region object. 

### Example
```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.GeographyApi()
accept = 'accept_example' # str | Must be `application/json`
accept_encoding = 'accept_encoding_example' # str | Must be `gzip`
authorization = 'authorization_example' # str | The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details.
user_agent = 'user_agent_example' # str | The `User-Agent` header string from the customer's request, as captured by your integration. If you are building an application then the `User-Agent` value should be `{app name}/{app version}`.  Example: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36`  Example: `TravelNow/3.30.112` 
region_id = 'region_id_example' # str | ID of the region to retrieve.  Example: `602962`. 
language = 'language_example' # str | Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: `language=en-US`  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/) 
include = ['include_example'] # list[str] | Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.   * details - Include the metadata, coordinates and full hierarchy of the region.   * property_ids - Include the list of property IDs within the bounding polygon of the region.   * property_ids_expanded - Include the list of property IDs within the bounding polygon of the region and property IDs from the surrounding area if minimal properties are within the region.  Example: `include=details&include=property_ids` 
customer_session_id = 'customer_session_id_example' # str | Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br> Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.  (optional)
billing_terms = 'billing_terms_example' # str | This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  (optional)
partner_point_of_sale = 'partner_point_of_sale_example' # str | This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)
payment_terms = 'payment_terms_example' # str | This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  (optional)
platform_name = 'platform_name_example' # str | This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  (optional)

try:
    # Region
    api_response = api_instance.regions_region_id_get(accept, accept_encoding, authorization, user_agent, region_id, language, include, customer_session_id=customer_session_id, billing_terms=billing_terms, partner_point_of_sale=partner_point_of_sale, payment_terms=payment_terms, platform_name=platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeographyApi->regions_region_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Must be &#x60;application/json&#x60; | 
 **accept_encoding** | **str**| Must be &#x60;gzip&#x60; | 
 **authorization** | **str**| The custom generated authentication header. Refer to our [signature authentication](https://developer.expediapartnersolutions.com/reference/signature-authentication) page for full details. | 
 **user_agent** | **str**| The &#x60;User-Agent&#x60; header string from the customer&#39;s request, as captured by your integration. If you are building an application then the &#x60;User-Agent&#x60; value should be &#x60;{app name}/{app version}&#x60;.  Example: &#x60;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36&#x60;  Example: &#x60;TravelNow/3.30.112&#x60;  | 
 **region_id** | **str**| ID of the region to retrieve.  Example: &#x60;602962&#x60;.  | 
 **language** | **str**| Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)  Example: &#x60;language&#x3D;en-US&#x60;  Language Options: [https://developer.expediapartnersolutions.com/reference/language-options/](https://developer.expediapartnersolutions.com/reference/language-options/)  | 
 **include** | [**list[str]**](str.md)| Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.   * details - Include the metadata, coordinates and full hierarchy of the region.   * property_ids - Include the list of property IDs within the bounding polygon of the region.   * property_ids_expanded - Include the list of property IDs within the bounding polygon of the region and property IDs from the surrounding area if minimal properties are within the region.  Example: &#x60;include&#x3D;details&amp;include&#x3D;property_ids&#x60;  | 
 **customer_session_id** | **str**| Insert your own unique value for each user session, beginning with the first API call. Continue to pass the same value for each subsequent API call during the user&#39;s session, using a new value for every new customer session.&lt;br&gt; Including this value greatly eases EPS&#39;s internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user&#39;s session.  | [optional] 
 **billing_terms** | **str**| This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **partner_point_of_sale** | **str**| This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **payment_terms** | **str**| This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.  | [optional] 
 **platform_name** | **str**| This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.  | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

