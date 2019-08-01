# eps_rapid
EPS Rapid V2.3

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.3
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import eps_rapid 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import eps_rapid
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import eps_rapid
from eps_rapid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = eps_rapid.BookingApi(eps_rapid.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://api.ean.com/2.3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BookingApi* | [**itineraries_itinerary_id_payment_sessions_put**](docs/BookingApi.md#itineraries_itinerary_id_payment_sessions_put) | **PUT** /itineraries/{itinerary_id}/payment-sessions | Complete Payment Session
*BookingApi* | [**itineraries_itinerary_id_put**](docs/BookingApi.md#itineraries_itinerary_id_put) | **PUT** /itineraries/{itinerary_id} | Resume Booking
*BookingApi* | [**itineraries_post**](docs/BookingApi.md#itineraries_post) | **POST** /itineraries | Create Booking
*BookingApi* | [**payment_sessions_post**](docs/BookingApi.md#payment_sessions_post) | **POST** /payment-sessions | Register Payments
*ContentApi* | [**chains_get**](docs/ContentApi.md#chains_get) | **GET** /chains | Chain Reference
*ContentApi* | [**files_properties_catalog_get**](docs/ContentApi.md#files_properties_catalog_get) | **GET** /files/properties/catalog | Property Catalog File
*ContentApi* | [**files_properties_content_get**](docs/ContentApi.md#files_properties_content_get) | **GET** /files/properties/content | Property Content File
*ContentApi* | [**properties_content_get**](docs/ContentApi.md#properties_content_get) | **GET** /properties/content | Property Content
*ContentApi* | [**properties_property_id_guest_reviews_get**](docs/ContentApi.md#properties_property_id_guest_reviews_get) | **GET** /properties/{property_id}/guest-reviews | Property Guest Reviews
*ContentApi* | [**properties_tripadvisor_get**](docs/ContentApi.md#properties_tripadvisor_get) | **GET** /properties/tripadvisor | Property TripAdvisor Information
*GeographyApi* | [**airports_get**](docs/GeographyApi.md#airports_get) | **GET** /airports | Airports
*GeographyApi* | [**airports_iata_airport_code_get**](docs/GeographyApi.md#airports_iata_airport_code_get) | **GET** /airports/{iata_airport_code} | Airport
*GeographyApi* | [**properties_geography_post**](docs/GeographyApi.md#properties_geography_post) | **POST** /properties/geography | Properties within Polygon
*GeographyApi* | [**regions_get**](docs/GeographyApi.md#regions_get) | **GET** /regions | Regions
*GeographyApi* | [**regions_region_id_get**](docs/GeographyApi.md#regions_region_id_get) | **GET** /regions/{region_id} | Region
*ManageBookingsApi* | [**itineraries_get**](docs/ManageBookingsApi.md#itineraries_get) | **GET** /itineraries | Retrieve Booking with Affiliate Reference Id
*ManageBookingsApi* | [**itineraries_itinerary_id_delete**](docs/ManageBookingsApi.md#itineraries_itinerary_id_delete) | **DELETE** /itineraries/{itinerary_id} | Cancel Held Booking
*ManageBookingsApi* | [**itineraries_itinerary_id_get**](docs/ManageBookingsApi.md#itineraries_itinerary_id_get) | **GET** /itineraries/{itinerary_id} | Retrieve Booking
*ManageBookingsApi* | [**itineraries_itinerary_id_rooms_room_id_delete**](docs/ManageBookingsApi.md#itineraries_itinerary_id_rooms_room_id_delete) | **DELETE** /itineraries/{itinerary_id}/rooms/{room_id} | Cancel a room.
*ManageBookingsApi* | [**itineraries_itinerary_id_rooms_room_id_put**](docs/ManageBookingsApi.md#itineraries_itinerary_id_rooms_room_id_put) | **PUT** /itineraries/{itinerary_id}/rooms/{room_id} | Change details of a room.
*ShoppingApi* | [**properties_availability_get**](docs/ShoppingApi.md#properties_availability_get) | **GET** /properties/availability | Get property room rates and availability
*ShoppingApi* | [**properties_property_id_deposit_policies_get**](docs/ShoppingApi.md#properties_property_id_deposit_policies_get) | **GET** /properties/{property_id}/deposit-policies | Get Deposit Policy
*ShoppingApi* | [**properties_property_id_payment_options_get**](docs/ShoppingApi.md#properties_property_id_payment_options_get) | **GET** /properties/{property_id}/payment-options | Get Accepted Payment Types - EPS MOR Only
*ShoppingApi* | [**properties_property_id_rooms_room_id_rates_rate_id_price_check_get**](docs/ShoppingApi.md#properties_property_id_rooms_room_id_rates_rate_id_price_check_get) | **GET** /properties/{property_id}/rooms/{room_id}/rates/{rate_id}/price-check | Get Current Price for Pre-Booking


## Documentation For Models

 - [AgeCategory](docs/AgeCategory.md)
 - [Airport](docs/Airport.md)
 - [AirportAssociatedRegion](docs/AirportAssociatedRegion.md)
 - [AirportCoordinates](docs/AirportCoordinates.md)
 - [Airports](docs/Airports.md)
 - [Amenity](docs/Amenity.md)
 - [Attribute](docs/Attribute.md)
 - [BedGroup](docs/BedGroup.md)
 - [BedGroupAvailability](docs/BedGroupAvailability.md)
 - [BedGroupAvailabilityConfiguration](docs/BedGroupAvailabilityConfiguration.md)
 - [BedGroupConfiguration](docs/BedGroupConfiguration.md)
 - [BillingContact](docs/BillingContact.md)
 - [BillingContactAddress](docs/BillingContactAddress.md)
 - [Brand](docs/Brand.md)
 - [Chain](docs/Chain.md)
 - [ChainMap](docs/ChainMap.md)
 - [ChangeRoomDetailsRequest](docs/ChangeRoomDetailsRequest.md)
 - [CompletePaymentSession](docs/CompletePaymentSession.md)
 - [Conversations](docs/Conversations.md)
 - [CreateItinerary](docs/CreateItinerary.md)
 - [CreateItineraryLinks](docs/CreateItineraryLinks.md)
 - [CreateItineraryLinksCompletePaymentSession](docs/CreateItineraryLinksCompletePaymentSession.md)
 - [CreateItineraryLinksResume](docs/CreateItineraryLinksResume.md)
 - [CreateItineraryLinksRetrieve](docs/CreateItineraryLinksRetrieve.md)
 - [CreateItineraryRequest](docs/CreateItineraryRequest.md)
 - [CreateItineraryRequestRooms](docs/CreateItineraryRequestRooms.md)
 - [DepositPolicies](docs/DepositPolicies.md)
 - [DepositPolicy](docs/DepositPolicy.md)
 - [Error](docs/Error.md)
 - [ErrorErrors](docs/ErrorErrors.md)
 - [ErrorFields](docs/ErrorFields.md)
 - [GuestReviews](docs/GuestReviews.md)
 - [GuestReviewsVerified](docs/GuestReviewsVerified.md)
 - [Link](docs/Link.md)
 - [PaymentOption](docs/PaymentOption.md)
 - [PaymentOptionAffiliateCollect](docs/PaymentOptionAffiliateCollect.md)
 - [PaymentOptionCreditCard](docs/PaymentOptionCreditCard.md)
 - [PaymentOptionCreditCardCardOptions](docs/PaymentOptionCreditCardCardOptions.md)
 - [PaymentSessions](docs/PaymentSessions.md)
 - [PaymentSessionsRequest](docs/PaymentSessionsRequest.md)
 - [PaymentSessionsRequestCustomerAccountDetails](docs/PaymentSessionsRequestCustomerAccountDetails.md)
 - [PaymentType](docs/PaymentType.md)
 - [Payments](docs/Payments.md)
 - [PaymentsInner](docs/PaymentsInner.md)
 - [Phone](docs/Phone.md)
 - [PropertiesGeoJsonRequest](docs/PropertiesGeoJsonRequest.md)
 - [PropertyAvailabilities](docs/PropertyAvailabilities.md)
 - [PropertyAvailabilityWithoutScore](docs/PropertyAvailabilityWithoutScore.md)
 - [PropertyAvailabilityWithoutScoreCancelPenalties](docs/PropertyAvailabilityWithoutScoreCancelPenalties.md)
 - [PropertyAvailabilityWithoutScorePromotions](docs/PropertyAvailabilityWithoutScorePromotions.md)
 - [PropertyAvailabilityWithoutScorePromotionsDeal](docs/PropertyAvailabilityWithoutScorePromotionsDeal.md)
 - [PropertyAvailabilityWithoutScoreRates](docs/PropertyAvailabilityWithoutScoreRates.md)
 - [PropertyAvailabilityWithoutScoreRooms](docs/PropertyAvailabilityWithoutScoreRooms.md)
 - [PropertyContent](docs/PropertyContent.md)
 - [PropertyContentAddress](docs/PropertyContentAddress.md)
 - [PropertyContentAddressLocalized](docs/PropertyContentAddressLocalized.md)
 - [PropertyContentAirports](docs/PropertyContentAirports.md)
 - [PropertyContentAirportsPreferred](docs/PropertyContentAirportsPreferred.md)
 - [PropertyContentAllInclusive](docs/PropertyContentAllInclusive.md)
 - [PropertyContentAttributes](docs/PropertyContentAttributes.md)
 - [PropertyContentBusinessModel](docs/PropertyContentBusinessModel.md)
 - [PropertyContentCategory](docs/PropertyContentCategory.md)
 - [PropertyContentCheckin](docs/PropertyContentCheckin.md)
 - [PropertyContentCheckout](docs/PropertyContentCheckout.md)
 - [PropertyContentDates](docs/PropertyContentDates.md)
 - [PropertyContentDescriptions](docs/PropertyContentDescriptions.md)
 - [PropertyContentFees](docs/PropertyContentFees.md)
 - [PropertyContentImages](docs/PropertyContentImages.md)
 - [PropertyContentLocation](docs/PropertyContentLocation.md)
 - [PropertyContentLocationCoordinates](docs/PropertyContentLocationCoordinates.md)
 - [PropertyContentMap](docs/PropertyContentMap.md)
 - [PropertyContentOnsitePayments](docs/PropertyContentOnsitePayments.md)
 - [PropertyContentPolicies](docs/PropertyContentPolicies.md)
 - [PropertyContentRatings](docs/PropertyContentRatings.md)
 - [PropertyContentRatingsGuest](docs/PropertyContentRatingsGuest.md)
 - [PropertyContentRatingsProperty](docs/PropertyContentRatingsProperty.md)
 - [PropertyGeography](docs/PropertyGeography.md)
 - [PropertyGeographyMap](docs/PropertyGeographyMap.md)
 - [RateContent](docs/RateContent.md)
 - [Region](docs/Region.md)
 - [RegionAncestors](docs/RegionAncestors.md)
 - [RegionCoordinates](docs/RegionCoordinates.md)
 - [RegionCoordinatesBoundingPolygon](docs/RegionCoordinatesBoundingPolygon.md)
 - [Regions](docs/Regions.md)
 - [Retrieve](docs/Retrieve.md)
 - [RetrieveAdjustment](docs/RetrieveAdjustment.md)
 - [RetrieveConfirmationId](docs/RetrieveConfirmationId.md)
 - [RetrieveLinks](docs/RetrieveLinks.md)
 - [RetrieveLinks1](docs/RetrieveLinks1.md)
 - [RetrieveLinks1Cancel](docs/RetrieveLinks1Cancel.md)
 - [RetrieveLinks1Change](docs/RetrieveLinks1Change.md)
 - [RetrieveLinksCancel](docs/RetrieveLinksCancel.md)
 - [RetrieveRate](docs/RetrieveRate.md)
 - [RetrieveRateCancelPenalties](docs/RetrieveRateCancelPenalties.md)
 - [RetrieveRateCancelRefund](docs/RetrieveRateCancelRefund.md)
 - [RetrieveRateDepositPolicies](docs/RetrieveRateDepositPolicies.md)
 - [RetrieveRateFees](docs/RetrieveRateFees.md)
 - [RetrieveRatePromotions](docs/RetrieveRatePromotions.md)
 - [RetrieveRateStay](docs/RetrieveRateStay.md)
 - [RetrieveRooms](docs/RetrieveRooms.md)
 - [Review](docs/Review.md)
 - [RoomContent](docs/RoomContent.md)
 - [RoomContentArea](docs/RoomContentArea.md)
 - [RoomContentDescriptions](docs/RoomContentDescriptions.md)
 - [RoomContentImages](docs/RoomContentImages.md)
 - [RoomContentOccupancy](docs/RoomContentOccupancy.md)
 - [RoomContentOccupancyMaxAllowed](docs/RoomContentOccupancyMaxAllowed.md)
 - [RoomPriceCheck](docs/RoomPriceCheck.md)
 - [RoomRate](docs/RoomRate.md)
 - [RoomRateFees](docs/RoomRateFees.md)
 - [RoomRateFeesMandatoryFee](docs/RoomRateFeesMandatoryFee.md)
 - [RoomRateFeesMandatoryTax](docs/RoomRateFeesMandatoryTax.md)
 - [RoomRateFeesResortFee](docs/RoomRateFeesResortFee.md)
 - [RoomRateStay](docs/RoomRateStay.md)
 - [RoomRateTotals](docs/RoomRateTotals.md)
 - [RoomRateTotalsExclusive](docs/RoomRateTotalsExclusive.md)
 - [RoomRateTotalsGrossProfit](docs/RoomRateTotalsGrossProfit.md)
 - [RoomRateTotalsInclusive](docs/RoomRateTotalsInclusive.md)
 - [RoomRateTotalsInclusiveBillableCurrency](docs/RoomRateTotalsInclusiveBillableCurrency.md)
 - [RoomRateTotalsInclusiveRequestCurrency](docs/RoomRateTotalsInclusiveRequestCurrency.md)
 - [RoomRateTotalsMarketingFee](docs/RoomRateTotalsMarketingFee.md)
 - [RoomRateTotalsMinimumSellingPrice](docs/RoomRateTotalsMinimumSellingPrice.md)
 - [RoomRateTotalsStrikethrough](docs/RoomRateTotalsStrikethrough.md)
 - [RoomRates](docs/RoomRates.md)
 - [SpokenLanguage](docs/SpokenLanguage.md)
 - [Statistic](docs/Statistic.md)
 - [Theme](docs/Theme.md)
 - [TripAdvisor](docs/TripAdvisor.md)
 - [TripAdvisorMap](docs/TripAdvisorMap.md)
 - [ValueAdd](docs/ValueAdd.md)
 - [ValueAdds](docs/ValueAdds.md)
 - [View](docs/View.md)
 - [PropertyAvailability](docs/PropertyAvailability.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



