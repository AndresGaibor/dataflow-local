---
title: "Club Speed"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Clubspeed.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Club Speed

Club Speed is an activity and venue management software.

Club Speed integration replicates data using the [Club Speed API](https://clubspeed.com/clubspeed/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your private key, contact the [Club Speed support team](mailto:support@clubspeed.com).

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Private Key | Private key. |
| Subdomain | You can find your subdomain in the URL of your account homepage. If the URL is myclubspeed.clubspeedtiming.com, the subdomain is myclubspeed. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### booking

The `booking` table contains info about bookings. A booking record exposes a `heat` to the online booking interface in Club Speed.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | onlineBookingsId |

booking table foreign keys

| Join booking with | on |
| --- | --- |
| [booking\_availability](#booking-availability) | ``` booking.onlineBookingsId = booking_availability.products.onlineBookingsId ```  ``` booking.heatId = booking_availability.heatId ```  ``` booking.heatId = booking_availability.heatSpotsAvailableCombined ```  ``` booking.productsId = booking_availability.products.productsId ``` |
| [reservations](#reservations) | ``` booking.onlineBookingsId = reservations.onlineBookingsId ``` |
| [heat\_main](#heat-main) | ``` booking.heatId = heat_main.heatId ``` |
| [heat\_main\_details](#heat-main-details) | ``` booking.heatId = heat_main_details.heatId ``` |
| [check\_details](#check-details) | ``` booking.productsId = check_details.productId ``` |
| [event\_types](#event-types) | ``` booking.productsId = event_types.onlineProductId ``` |
| [products](#products) | ``` booking.productsId = products.productId ``` |

booking table schema

|  |
| --- |
| **heatId**  INTEGER |
| **isPublic**  BOOLEAN |
| **onlineBookingsId**  INTEGER |
| **productsId**  INTEGER |
| **quantityTotal**  INTEGER |

### booking\_availability

The `booking_availability` table contains info about the current availability for online bookings. These take into account both online and local booking reservations.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | heatId |

booking\_availability table foreign keys

| Join booking\_availability with | on |
| --- | --- |
| [booking](#booking) | ``` booking_availability.products.onlineBookingsId = booking.onlineBookingsId ```  ``` booking_availability.heatId = booking.heatId ```  ``` booking_availability.heatSpotsAvailableCombined = booking.heatId ```  ``` booking_availability.products.productsId = booking.productsId ``` |
| [reservations](#reservations) | ``` booking_availability.products.onlineBookingsId = reservations.onlineBookingsId ``` |
| [heat\_main](#heat-main) | ``` booking_availability.heatId = heat_main.heatId ```  ``` booking_availability.heatSpotsAvailableCombined = heat_main.heatId ```  ``` booking_availability.heatTypeId = heat_main.type ``` |
| [heat\_main\_details](#heat-main-details) | ``` booking_availability.heatId = heat_main_details.heatId ```  ``` booking_availability.heatSpotsAvailableCombined = heat_main_details.heatId ``` |
| [event\_heat\_types](#event-heat-types) | ``` booking_availability.heatTypeId = event_heat_types.heatTypeId ``` |
| [event\_rounds](#event-rounds) | ``` booking_availability.heatTypeId = event_rounds.heatTypeId ``` |
| [heat\_types](#heat-types) | ``` booking_availability.heatTypeId = heat_types.heatTypesId ``` |
| [check\_details](#check-details) | ``` booking_availability.products.productsId = check_details.productId ``` |
| [event\_types](#event-types) | ``` booking_availability.products.productsId = event_types.onlineProductId ``` |
| [products](#products) | ``` booking_availability.products.productsId = products.productId ``` |

booking\_availability table schema

|  |
| --- |
| **heatDescription**  STRING |
| **heatId**  INTEGER |
| **heatSpotsAvailableCombined**  INTEGER |
| **heatSpotsAvailableOnline**  INTEGER |
| **heatSpotsTotalActual**  INTEGER |
| **heatStartsAt**  DATE-TIME |
| **heatTypeId**  INTEGER |
| **isPublic**  BOOLEAN |
| **products**  ARRAY This is a nested data structure:   - onlineBookingsId: INTEGER - price1: NUMBER - productDescription: STRING - productSpotsAvailableOnline: INTEGER - productSpotsTotal: INTEGER - productType: STRING - productsId: INTEGER |

### check\_details

The `check_details` table contains info about line items and quantity info attached to [`checks`](#checks).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | checkDetailId |
| **Replication Key** | createdDate |

check\_details table foreign keys

| Join check\_details with | on |
| --- | --- |
| [gift\_card\_history](#gift-card-history) | ``` check_details.checkDetailId = gift_card_history.checkDetailId ```  ``` check_details.checkId = gift_card_history.checkId ```  ``` check_details.g_CustId = gift_card_history.customerId ```  ``` check_details.p_CustId = gift_card_history.customerId ```  ``` check_details.s_CustId = gift_card_history.customerId ```  ``` check_details.discountUserId = gift_card_history.userId ``` |
| [checks](#checks) | ``` check_details.checkId = checks.checkId ```  ``` check_details.g_CustId = checks.customerId ```  ``` check_details.p_CustId = checks.customerId ```  ``` check_details.s_CustId = checks.customerId ```  ``` check_details.discountId = checks.discountId ```  ``` check_details.discountUserId = checks.discountUserId ```  ``` check_details.discountUserId = checks.userId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` check_details.checkId = event_reservation_links.checkId ``` |
| [payments](#payments) | ``` check_details.checkId = payments.checkId ```  ``` check_details.g_CustId = payments.customerId ```  ``` check_details.p_CustId = payments.customerId ```  ``` check_details.s_CustId = payments.customerId ```  ``` check_details.discountUserId = payments.userId ```  ``` check_details.discountUserId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` check_details.checkId = payments_voided.checkId ```  ``` check_details.g_CustId = payments_voided.customerId ```  ``` check_details.p_CustId = payments_voided.customerId ```  ``` check_details.s_CustId = payments_voided.customerId ```  ``` check_details.discountUserId = payments_voided.userId ```  ``` check_details.discountUserId = payments_voided.voidUser ``` |
| [reservations](#reservations) | ``` check_details.checkId = reservations.checkId ```  ``` check_details.g_CustId = reservations.customersId ```  ``` check_details.p_CustId = reservations.customersId ```  ``` check_details.s_CustId = reservations.customersId ``` |
| [event\_heat\_details](#event-heat-details) | ``` check_details.g_CustId = event_heat_details.customerId ```  ``` check_details.p_CustId = event_heat_details.customerId ```  ``` check_details.s_CustId = event_heat_details.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` check_details.g_CustId = heat_main_details.customerId ```  ``` check_details.p_CustId = heat_main_details.customerId ```  ``` check_details.s_CustId = heat_main_details.customerId ```  ``` check_details.discountUserId = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` check_details.g_CustId = memberships.customerId ```  ``` check_details.p_CustId = memberships.customerId ```  ``` check_details.s_CustId = memberships.customerId ```  ``` check_details.discountUserId = memberships.byUserId ``` |
| [discount\_types](#discount-types) | ``` check_details.discountId = discount_types.discountId ``` |
| [booking](#booking) | ``` check_details.productId = booking.productsId ``` |
| [booking\_availability](#booking-availability) | ``` check_details.productId = booking_availability.products.productsId ``` |
| [event\_types](#event-types) | ``` check_details.productId = event_types.onlineProductId ``` |
| [products](#products) | ``` check_details.productId = products.productId ```  ``` check_details.taxId = products.taxId ``` |
| [taxes](#taxes) | ``` check_details.taxId = taxes.taxId ``` |
| [event\_tasks](#event-tasks) | ``` check_details.discountUserId = event_tasks.completedBy ``` |
| [users](#users) | ``` check_details.discountUserId = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` check_details.discountUserId = event_reservations.userId ``` |

check\_details table schema

|  |
| --- |
| **calculateType**  INTEGER |
| **checkDetailId**  INTEGER |
| **checkId**  INTEGER |
| **createdDate**  DATE-TIME |
| **discountApplied**  NUMBER |
| **discountDesc**  STRING |
| **discountId**  INTEGER |
| **discountNotes**  STRING |
| **discountUserId**  INTEGER |
| **g\_CustId**  INTEGER |
| **g\_Points**  NUMBER |
| **gst**  NUMBER |
| **m\_DaysAdded**  INTEGER |
| **p\_CustId**  INTEGER |
| **p\_Points**  INTEGER |
| **productId**  INTEGER |
| **productName**  STRING |
| **qty**  INTEGER |
| **r\_Points**  INTEGER |
| **s\_CustId**  INTEGER |
| **s\_NoOfLapsOrSeconds**  INTEGER |
| **s\_SaleBy**  INTEGER |
| **s\_Vol**  INTEGER |
| **status**  INTEGER |
| **taxId**  INTEGER |
| **taxPercent**  NUMBER |
| **type**  INTEGER |
| **unitPrice**  NUMBER |
| **unitPrice2**  NUMBER |
| **voidNotes**  STRING |

### checks

The `checks` table contains info about checks, or financial invoices, that have been closed.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | checkId |
| **Replication Key** | closedDate |

checks table foreign keys

| Join checks with | on |
| --- | --- |
| [check\_details](#check-details) | ``` checks.checkId = check_details.checkId ```  ``` checks.customerId = check_details.g_CustId ```  ``` checks.customerId = check_details.p_CustId ```  ``` checks.customerId = check_details.s_CustId ```  ``` checks.discountId = check_details.discountId ```  ``` checks.discountUserId = check_details.discountUserId ```  ``` checks.userId = check_details.discountUserId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` checks.checkId = event_reservation_links.checkId ``` |
| [gift\_card\_history](#gift-card-history) | ``` checks.checkId = gift_card_history.checkId ```  ``` checks.customerId = gift_card_history.customerId ```  ``` checks.discountUserId = gift_card_history.userId ```  ``` checks.userId = gift_card_history.userId ``` |
| [payments](#payments) | ``` checks.checkId = payments.checkId ```  ``` checks.customerId = payments.customerId ```  ``` checks.discountUserId = payments.userId ```  ``` checks.userId = payments.userId ```  ``` checks.discountUserId = payments.voidUser ```  ``` checks.userId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` checks.checkId = payments_voided.checkId ```  ``` checks.customerId = payments_voided.customerId ```  ``` checks.discountUserId = payments_voided.userId ```  ``` checks.userId = payments_voided.userId ```  ``` checks.discountUserId = payments_voided.voidUser ```  ``` checks.userId = payments_voided.voidUser ``` |
| [reservations](#reservations) | ``` checks.checkId = reservations.checkId ```  ``` checks.customerId = reservations.customersId ``` |
| [event\_heat\_details](#event-heat-details) | ``` checks.customerId = event_heat_details.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` checks.customerId = heat_main_details.customerId ```  ``` checks.discountUserId = heat_main_details.userId ```  ``` checks.userId = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` checks.customerId = memberships.customerId ```  ``` checks.discountUserId = memberships.byUserId ```  ``` checks.userId = memberships.byUserId ``` |
| [discount\_types](#discount-types) | ``` checks.discountId = discount_types.discountId ``` |
| [event\_tasks](#event-tasks) | ``` checks.discountUserId = event_tasks.completedBy ```  ``` checks.userId = event_tasks.completedBy ``` |
| [users](#users) | ``` checks.discountUserId = users.userId ```  ``` checks.userId = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` checks.discountUserId = event_reservations.userId ```  ``` checks.userId = event_reservations.userId ``` |

checks table schema

|  |
| --- |
| **broker**  STRING |
| **checkId**  INTEGER |
| **closedDate**  DATE-TIME |
| **customerId**  INTEGER |
| **discount**  NUMBER |
| **discountId**  INTEGER |
| **discountNotes**  STRING |
| **discountUserId**  INTEGER |
| **fee**  NUMBER |
| **gratuity**  NUMBER |
| **invoiceDate**  DATE-TIME |
| **isTaxExempt**  BOOLEAN |
| **name**  STRING |
| **notes**  STRING |
| **openedDate**  DATE-TIME |
| **status**  INTEGER |
| **total**  NUMBER |
| **type**  INTEGER |
| **userId**  INTEGER |

### customers

The `customers` table contains info about the customers for a location.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | customerId |
| **Replication Key** | lastVisited |

customers table schema

|  |
| --- |
| **Address**  STRING |
| **Address2**  STRING |
| **City**  STRING |
| **Country**  STRING |
| **Custom1**  STRING |
| **Custom2**  STRING |
| **Custom3**  STRING |
| **Custom4**  STRING |
| **LicenseNumber**  STRING |
| **State**  STRING |
| **Zip**  STRING |
| **accountCreated**  DATE-TIME |
| **birthdate**  DATE-TIME |
| **cardId**  INTEGER |
| **company**  STRING |
| **creditLimit**  NUMBER |
| **creditOnHold**  BOOLEAN |
| **customerId**  INTEGER |
| **deleted**  BOOLEAN |
| **donotemail**  BOOLEAN |
| **email**  STRING |
| **fax**  STRING |
| **firstname**  STRING |
| **gender**  INTEGER |
| **generalNotes**  STRING |
| **howdidyouhearaboutus**  INTEGER |
| **ignoreDOB**  BOOLEAN |
| **isEmployee**  BOOLEAN |
| **isGiftCard**  BOOLEAN |
| **lastVisited**  DATE-TIME |
| **lastname**  STRING |
| **memberShipTextLong**  STRING |
| **membershipStatus**  INTEGER |
| **membershipText**  STRING |
| **mobilephone**  STRING |
| **originalId**  INTEGER |
| **phoneNumber**  STRING |
| **phoneNumber2**  STRING |
| **priceLevel**  INTEGER |
| **privacy1**  BOOLEAN |
| **proskill**  INTEGER |
| **racername**  STRING |
| **status1**  INTEGER |
| **status2**  INTEGER |
| **status3**  INTEGER |
| **status4**  INTEGER |
| **totalRaces**  INTEGER |
| **totalVisits**  INTEGER |
| **waiver**  INTEGER |
| **waiver2**  INTEGER |
| **webUserName**  STRING |

### discount\_types

The `discount_types` table contains info about discount types.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | discountId |

discount\_types table foreign keys

| Join discount\_types with | on |
| --- | --- |
| [check\_details](#check-details) | ``` discount_types.discountId = check_details.discountId ``` |
| [checks](#checks) | ``` discount_types.discountId = checks.discountId ``` |
| [product\_classes](#product-classes) | ``` discount_types.productClassId = product_classes.productClassId ``` |
| [products](#products) | ``` discount_types.productClassId = products.productClassId ``` |

discount\_types table schema

|  |
| --- |
| **amount**  NUMBER |
| **calculateType**  INTEGER |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **discountId**  INTEGER |
| **enabled**  BOOLEAN |
| **needApproved**  BOOLEAN |
| **productClassId**  INTEGER |

### event\_heat\_details

The `event_heat_details` table contains info about [`customers`](#customers) who have been placed in a queue for a specific [`event`](#events).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | customerId  eventId |
| **Replication Key** | added |

event\_heat\_details table foreign keys

| Join event\_heat\_details with | on |
| --- | --- |
| [check\_details](#check-details) | ``` event_heat_details.customerId = check_details.g_CustId ```  ``` event_heat_details.customerId = check_details.p_CustId ```  ``` event_heat_details.customerId = check_details.s_CustId ``` |
| [checks](#checks) | ``` event_heat_details.customerId = checks.customerId ``` |
| [gift\_card\_history](#gift-card-history) | ``` event_heat_details.customerId = gift_card_history.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` event_heat_details.customerId = heat_main_details.customerId ``` |
| [memberships](#memberships) | ``` event_heat_details.customerId = memberships.customerId ``` |
| [payments](#payments) | ``` event_heat_details.customerId = payments.customerId ``` |
| [payments\_voided](#payments-voided) | ``` event_heat_details.customerId = payments_voided.customerId ``` |
| [reservations](#reservations) | ``` event_heat_details.customerId = reservations.customersId ``` |
| [event\_rounds](#event-rounds) | ``` event_heat_details.eventId = event_rounds.eventId ``` |
| [events](#events) | ``` event_heat_details.eventId = events.eventId ``` |

event\_heat\_details table schema

|  |
| --- |
| **added**  DATE-TIME |
| **customerId**  INTEGER |
| **eventId**  INTEGER |
| **proskill**  INTEGER |
| **roundLoseNum**  INTEGER |
| **totalRaces**  INTEGER |

### event\_heat\_types

The `event_heat_types` table contains info about event type classifications, which are used to look up [`event_rounds`](#event_rounds) when creating [`events`](#events).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventHeatTypeId |

event\_heat\_types table foreign keys

| Join event\_heat\_types with | on |
| --- | --- |
| [booking\_availability](#booking-availability) | ``` event_heat_types.heatTypeId = booking_availability.heatTypeId ``` |
| [event\_rounds](#event-rounds) | ``` event_heat_types.heatTypeId = event_rounds.heatTypeId ``` |
| [heat\_main](#heat-main) | ``` event_heat_types.heatTypeId = heat_main.type ``` |
| [heat\_types](#heat-types) | ``` event_heat_types.heatTypeId = heat_types.heatTypesId ``` |

event\_heat\_types table schema

|  |
| --- |
| **cadetsPerHeat**  INTEGER |
| **description**  STRING |
| **eventHeatTypeId**  INTEGER |
| **eventTypeId**  INTEGER |
| **heatTypeId**  INTEGER |
| **heatsPerRacer**  INTEGER |
| **racersPerHeat**  INTEGER |
| **roundNumber**  INTEGER |

### event\_reservation\_links

The `event_reservation_links` table contains lists of [`check`](#checks) and [`reservation`](#reservations) IDs, or checks that are linked to event reservations.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventReservationLinkId |

event\_reservation\_links table foreign keys

| Join event\_reservation\_links with | on |
| --- | --- |
| [check\_details](#check-details) | ``` event_reservation_links.checkId = check_details.checkId ``` |
| [checks](#checks) | ``` event_reservation_links.checkId = checks.checkId ``` |
| [gift\_card\_history](#gift-card-history) | ``` event_reservation_links.checkId = gift_card_history.checkId ``` |
| [payments](#payments) | ``` event_reservation_links.checkId = payments.checkId ``` |
| [payments\_voided](#payments-voided) | ``` event_reservation_links.checkId = payments_voided.checkId ``` |
| [reservations](#reservations) | ``` event_reservation_links.checkId = reservations.checkId ```  ``` event_reservation_links.reservationId = reservations.onlineBookingReservationsId ``` |
| [events](#events) | ``` event_reservation_links.reservationId = events.reservationId ``` |

event\_reservation\_links table schema

|  |
| --- |
| **checkId**  INTEGER |
| **eventReservationLinkId**  INTEGER |
| **reservationId**  INTEGER |

### event\_reservation\_types

The `event_reservation_types` table contains info about the descriptions for event reservation types.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventReservationTypeId |

event\_reservation\_types table foreign keys

| Join event\_reservation\_types with | on |
| --- | --- |
| [event\_reservations](#event-reservations) | ``` event_reservation_types.eventReservationTypeId = event_reservations.typeId ``` |

event\_reservation\_types table schema

|  |
| --- |
| **description**  STRING |
| **eventReservationTypeId**  INTEGER |

### event\_reservations

The `event_reservations` table contains info about event reservations, which are linked to [`events`](#events).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | eventReservationId |
| **Replication Key** | startTime |

event\_reservations table foreign keys

| Join event\_reservations with | on |
| --- | --- |
| [event\_reservation\_types](#event-reservation-types) | ``` event_reservations.typeId = event_reservation_types.eventReservationTypeId ``` |
| [event\_tasks](#event-tasks) | ``` event_reservations.eventReservationId = event_tasks.eventReservationId ```  ``` event_reservations.mainId = event_tasks.eventReservationId ```  ``` event_reservations.userId = event_tasks.completedBy ``` |
| [event\_types](#event-types) | ``` event_reservations.eventTypeId = event_types.eventTypeId ``` |
| [events](#events) | ``` event_reservations.eventTypeId = events.eventTypeId ``` |
| [check\_details](#check-details) | ``` event_reservations.userId = check_details.discountUserId ``` |
| [checks](#checks) | ``` event_reservations.userId = checks.discountUserId ```  ``` event_reservations.userId = checks.userId ``` |
| [gift\_card\_history](#gift-card-history) | ``` event_reservations.userId = gift_card_history.userId ``` |
| [users](#users) | ``` event_reservations.userId = users.userId ``` |
| [heat\_main\_details](#heat-main-details) | ``` event_reservations.userId = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` event_reservations.userId = memberships.byUserId ``` |
| [payments](#payments) | ``` event_reservations.userId = payments.userId ```  ``` event_reservations.userId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` event_reservations.userId = payments_voided.userId ```  ``` event_reservations.userId = payments_voided.voidUser ``` |

event\_reservations table schema

|  |
| --- |
| **allowOnlineReservation**  BOOLEAN |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **endTime**  DATE-TIME |
| **eventReservationId**  INTEGER |
| **eventTypeId**  INTEGER |
| **externalSystemId**  INTEGER |
| **isEventClosure**  BOOLEAN |
| **mainId**  INTEGER |
| **minNoOfAdultsPerBooking**  INTEGER |
| **noOfRacers**  INTEGER |
| **notes**  STRING |
| **ptsPerReservation**  INTEGER |
| **repId**  INTEGER |
| **startTime**  DATE-TIME |
| **status**  INTEGER |
| **subject**  STRING |
| **typeId**  INTEGER |
| **userId**  INTEGER |

### event\_rounds

The `event_rounds` table contains info about event rounds. This table acts as a link between [`events`](#events) and their corresponding rounds in the [`heat_main`](#heat_main).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventRoundId |

event\_rounds table foreign keys

| Join event\_rounds with | on |
| --- | --- |
| [heat\_main](#heat-main) | ``` event_rounds.eventRoundId = heat_main.eventRound ```  ``` event_rounds.heatTypeId = heat_main.type ``` |
| [event\_heat\_details](#event-heat-details) | ``` event_rounds.eventId = event_heat_details.eventId ``` |
| [events](#events) | ``` event_rounds.eventId = events.eventId ``` |
| [booking\_availability](#booking-availability) | ``` event_rounds.heatTypeId = booking_availability.heatTypeId ``` |
| [event\_heat\_types](#event-heat-types) | ``` event_rounds.heatTypeId = event_heat_types.heatTypeId ``` |
| [heat\_types](#heat-types) | ``` event_rounds.heatTypeId = heat_types.heatTypesId ``` |

event\_rounds table schema

|  |
| --- |
| **cadetsPerHeat**  INTEGER |
| **eventId**  INTEGER |
| **eventRoundId**  INTEGER |
| **heatDescription**  STRING |
| **heatTypeId**  INTEGER |
| **heatsPerRacer**  INTEGER |
| **racersPerHeat**  INTEGER |
| **roundNumber**  INTEGER |

### event\_statuses

The `event_statuses` table contains info about event statuses, which are statuses assigned to [`event_reservations`](#event_reservations).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventStatusId |
| **Useful links** |  |

event\_statuses table schema

|  |
| --- |
| **colorId**  INTEGER |
| **eventStatusId**  INTEGER |
| **seq**  INTEGER |
| **status**  STRING |

### event\_task\_types

The `event_task_types` table contains info about event task types, which are [`event_tasks`](#event_tasks) to be tracked for completion.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventTaskId |
| **Useful links** |  |

event\_task\_types table schema

|  |
| --- |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **eventTaskId**  INTEGER |
| **name**  STRING |
| **seq**  INTEGER |

### event\_tasks

The `event_tasks` table contains info about the tasks to be completed for a given [`event_reservation`](#event_reservations).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | eventTaskId |
| **Replication Key** | completedAt |

event\_tasks table foreign keys

| Join event\_tasks with | on |
| --- | --- |
| [event\_reservations](#event-reservations) | ``` event_tasks.eventReservationId = event_reservations.eventReservationId ```  ``` event_tasks.eventReservationId = event_reservations.mainId ```  ``` event_tasks.completedBy = event_reservations.userId ``` |
| [check\_details](#check-details) | ``` event_tasks.completedBy = check_details.discountUserId ``` |
| [checks](#checks) | ``` event_tasks.completedBy = checks.discountUserId ```  ``` event_tasks.completedBy = checks.userId ``` |
| [gift\_card\_history](#gift-card-history) | ``` event_tasks.completedBy = gift_card_history.userId ``` |
| [users](#users) | ``` event_tasks.completedBy = users.userId ``` |
| [heat\_main\_details](#heat-main-details) | ``` event_tasks.completedBy = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` event_tasks.completedBy = memberships.byUserId ``` |
| [payments](#payments) | ``` event_tasks.completedBy = payments.userId ```  ``` event_tasks.completedBy = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` event_tasks.completedBy = payments_voided.userId ```  ``` event_tasks.completedBy = payments_voided.voidUser ``` |

event\_tasks table schema

|  |
| --- |
| **completedAt**  DATE-TIME |
| **completedBy**  INTEGER |
| **eventReservationId**  INTEGER |
| **eventTaskId**  INTEGER |
| **eventTaskTypeId**  INTEGER |

### event\_types

The `event_types` table contains info about event types.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eventTypeId |

event\_types table foreign keys

| Join event\_types with | on |
| --- | --- |
| [event\_reservations](#event-reservations) | ``` event_types.eventTypeId = event_reservations.eventTypeId ``` |
| [events](#events) | ``` event_types.eventTypeId = events.eventTypeId ``` |
| [booking](#booking) | ``` event_types.onlineProductId = booking.productsId ``` |
| [booking\_availability](#booking-availability) | ``` event_types.onlineProductId = booking_availability.products.productsId ``` |
| [check\_details](#check-details) | ``` event_types.onlineProductId = check_details.productId ``` |
| [products](#products) | ``` event_types.onlineProductId = products.productId ``` |
| [heat\_types](#heat-types) | ``` event_types.trackId = heat_types.trackId ``` |

event\_types table schema

|  |
| --- |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **displayAtRegistration**  BOOLEAN |
| **enabled**  BOOLEAN |
| **eventTypeId**  INTEGER |
| **eventTypeName**  STRING |
| **eventTypeTheme**  INTEGER |
| **memberOnly**  BOOLEAN |
| **onlineProductId**  INTEGER |
| **ptsPerReservation**  INTEGER |
| **trackId**  INTEGER |

### events

The `events` table contains info about events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | eventId |
| **Replication Key** | eventScheduledTime |

events table foreign keys

| Join events with | on |
| --- | --- |
| [event\_reservations](#event-reservations) | ``` events.eventTypeId = event_reservations.eventTypeId ``` |
| [event\_types](#event-types) | ``` events.eventTypeId = event_types.eventTypeId ``` |
| [event\_heat\_details](#event-heat-details) | ``` events.eventId = event_heat_details.eventId ``` |
| [event\_rounds](#event-rounds) | ``` events.eventId = event_rounds.eventId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` events.reservationId = event_reservation_links.reservationId ``` |
| [reservations](#reservations) | ``` events.reservationId = reservations.onlineBookingReservationsId ``` |

events table schema

|  |
| --- |
| **createdHeatSpots**  INTEGER |
| **createdHeatTime**  DATE-TIME |
| **eventDesc**  STRING |
| **eventDuration**  INTEGER |
| **eventId**  INTEGER |
| **eventNotes**  STRING |
| **eventScheduledTime**  DATE-TIME |
| **eventTheme**  INTEGER |
| **eventTypeId**  INTEGER |
| **eventTypeName**  STRING |
| **memberOnly**  BOOLEAN |
| **reservationId**  INTEGER |
| **totalRacers**  INTEGER |
| **trackNo**  INTEGER |

### gift\_card\_history

The `gift_card_history` table acts as a transactional log for keeping track of each change that occurs with gift cards.

Information note**Note**: In Club Speed, each gift card is registered as a [`customer`](#customers). This means that each gift card identifier should be considered a `customerId` in this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | giftCardHistoryId |
| **Replication Key** | transactionDate |

gift\_card\_history table foreign keys

| Join gift\_card\_history with | on |
| --- | --- |
| [check\_details](#check-details) | ``` gift_card_history.checkDetailId = check_details.checkDetailId ```  ``` gift_card_history.checkId = check_details.checkId ```  ``` gift_card_history.customerId = check_details.g_CustId ```  ``` gift_card_history.customerId = check_details.p_CustId ```  ``` gift_card_history.customerId = check_details.s_CustId ```  ``` gift_card_history.userId = check_details.discountUserId ``` |
| [checks](#checks) | ``` gift_card_history.checkId = checks.checkId ```  ``` gift_card_history.customerId = checks.customerId ```  ``` gift_card_history.userId = checks.discountUserId ```  ``` gift_card_history.userId = checks.userId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` gift_card_history.checkId = event_reservation_links.checkId ``` |
| [payments](#payments) | ``` gift_card_history.checkId = payments.checkId ```  ``` gift_card_history.customerId = payments.customerId ```  ``` gift_card_history.userId = payments.userId ```  ``` gift_card_history.userId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` gift_card_history.checkId = payments_voided.checkId ```  ``` gift_card_history.customerId = payments_voided.customerId ```  ``` gift_card_history.userId = payments_voided.userId ```  ``` gift_card_history.userId = payments_voided.voidUser ``` |
| [reservations](#reservations) | ``` gift_card_history.checkId = reservations.checkId ```  ``` gift_card_history.customerId = reservations.customersId ``` |
| [event\_heat\_details](#event-heat-details) | ``` gift_card_history.customerId = event_heat_details.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` gift_card_history.customerId = heat_main_details.customerId ```  ``` gift_card_history.userId = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` gift_card_history.customerId = memberships.customerId ```  ``` gift_card_history.userId = memberships.byUserId ``` |
| [event\_tasks](#event-tasks) | ``` gift_card_history.userId = event_tasks.completedBy ``` |
| [users](#users) | ``` gift_card_history.userId = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` gift_card_history.userId = event_reservations.userId ``` |

gift\_card\_history table schema

|  |
| --- |
| **checkDetailId**  INTEGER |
| **checkId**  INTEGER |
| **customerId**  INTEGER |
| **giftCardHistoryId**  INTEGER |
| **ipAddress**  STRING |
| **notes**  STRING |
| **points**  NUMBER |
| **transactionDate**  DATE-TIME |
| **type**  INTEGER |
| **userId**  INTEGER |

### heat\_main

The `heat_main` table contains info about finished heat mains, which are instances of races on the standard venue calendar.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | heatId |
| **Replication Key** | finish |

heat\_main table foreign keys

| Join heat\_main with | on |
| --- | --- |
| [event\_rounds](#event-rounds) | ``` heat_main.eventRound = event_rounds.eventRoundId ```  ``` heat_main.type = event_rounds.heatTypeId ``` |
| [booking](#booking) | ``` heat_main.heatId = booking.heatId ``` |
| [booking\_availability](#booking-availability) | ``` heat_main.heatId = booking_availability.heatId ```  ``` heat_main.heatId = booking_availability.heatSpotsAvailableCombined ```  ``` heat_main.type = booking_availability.heatTypeId ``` |
| [heat\_main\_details](#heat-main-details) | ``` heat_main.heatId = heat_main_details.heatId ``` |
| [event\_heat\_types](#event-heat-types) | ``` heat_main.type = event_heat_types.heatTypeId ``` |
| [heat\_types](#heat-types) | ``` heat_main.type = heat_types.heatTypesId ``` |

heat\_main table schema

|  |
| --- |
| **beginning**  DATE-TIME |
| **eventRound**  INTEGER |
| **finish**  DATE-TIME |
| **heatColor**  INTEGER |
| **heatId**  INTEGER |
| **lapsOrMinutes**  INTEGER |
| **memberOnly**  BOOLEAN |
| **notes**  STRING |
| **numberOfReservation**  INTEGER |
| **pointsNeeded**  INTEGER |
| **raceBy**  INTEGER |
| **racersPerHeat**  INTEGER |
| **scheduleDuration**  INTEGER |
| **scheduledTime**  DATE-TIME |
| **speedLevel**  INTEGER |
| **status**  INTEGER |
| **track**  INTEGER |
| **type**  INTEGER |
| **winBy**  INTEGER |

### heat\_main\_details

The `heat_main_details` table contains info about customers that were entered into finished heats.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | customerId  heatId |

heat\_main\_details table foreign keys

| Join heat\_main\_details with | on |
| --- | --- |
| [check\_details](#check-details) | ``` heat_main_details.customerId = check_details.g_CustId ```  ``` heat_main_details.customerId = check_details.p_CustId ```  ``` heat_main_details.customerId = check_details.s_CustId ```  ``` heat_main_details.userId = check_details.discountUserId ``` |
| [checks](#checks) | ``` heat_main_details.customerId = checks.customerId ```  ``` heat_main_details.userId = checks.discountUserId ```  ``` heat_main_details.userId = checks.userId ``` |
| [event\_heat\_details](#event-heat-details) | ``` heat_main_details.customerId = event_heat_details.customerId ``` |
| [gift\_card\_history](#gift-card-history) | ``` heat_main_details.customerId = gift_card_history.customerId ```  ``` heat_main_details.userId = gift_card_history.userId ``` |
| [memberships](#memberships) | ``` heat_main_details.customerId = memberships.customerId ```  ``` heat_main_details.userId = memberships.byUserId ``` |
| [payments](#payments) | ``` heat_main_details.customerId = payments.customerId ```  ``` heat_main_details.userId = payments.userId ```  ``` heat_main_details.userId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` heat_main_details.customerId = payments_voided.customerId ```  ``` heat_main_details.userId = payments_voided.userId ```  ``` heat_main_details.userId = payments_voided.voidUser ``` |
| [reservations](#reservations) | ``` heat_main_details.customerId = reservations.customersId ``` |
| [booking](#booking) | ``` heat_main_details.heatId = booking.heatId ``` |
| [booking\_availability](#booking-availability) | ``` heat_main_details.heatId = booking_availability.heatId ```  ``` heat_main_details.heatId = booking_availability.heatSpotsAvailableCombined ``` |
| [heat\_main](#heat-main) | ``` heat_main_details.heatId = heat_main.heatId ``` |
| [event\_tasks](#event-tasks) | ``` heat_main_details.userId = event_tasks.completedBy ``` |
| [users](#users) | ``` heat_main_details.userId = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` heat_main_details.userId = event_reservations.userId ``` |

heat\_main\_details table schema

|  |
| --- |
| **autoNo**  INTEGER |
| **customerId**  INTEGER |
| **finishPosition**  INTEGER |
| **firstTime**  BOOLEAN |
| **groupFinishPosition**  INTEGER |
| **groupId**  INTEGER |
| **heatId**  INTEGER |
| **lineUpPosition**  INTEGER |
| **pointHistoryId**  INTEGER |
| **positionEditedDate**  DATE-TIME |
| **proskill**  INTEGER |
| **proskillDiff**  INTEGER |
| **scores**  NUMBER |
| **timeAdded**  DATE-TIME |
| **userId**  INTEGER |

### heat\_types

The `heat_types` table contains info about heat types.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | heatTypesId |

heat\_types table foreign keys

| Join heat\_types with | on |
| --- | --- |
| [booking\_availability](#booking-availability) | ``` heat_types.heatTypesId = booking_availability.heatTypeId ``` |
| [event\_heat\_types](#event-heat-types) | ``` heat_types.heatTypesId = event_heat_types.heatTypeId ``` |
| [event\_rounds](#event-rounds) | ``` heat_types.heatTypesId = event_rounds.heatTypeId ``` |
| [heat\_main](#heat-main) | ``` heat_types.heatTypesId = heat_main.type ``` |
| [event\_types](#event-types) | ``` heat_types.trackId = event_types.trackId ``` |

heat\_types table schema

|  |
| --- |
| **cannotBelow**  INTEGER |
| **cannotExceed**  INTEGER |
| **cost**  INTEGER |
| **deleted**  BOOLEAN |
| **enabled**  BOOLEAN |
| **heatTypesId**  INTEGER |
| **isEventHeatOnly**  BOOLEAN |
| **isPracticeHeat**  BOOLEAN |
| **lapsOrMinutes**  INTEGER |
| **memberOnly**  BOOLEAN |
| **name**  STRING |
| **raceBy**  INTEGER |
| **racersPerHeat**  INTEGER |
| **scheduleDuration**  INTEGER |
| **speedLevel**  INTEGER |
| **trackId**  INTEGER |
| **winBy**  INTEGER |

### membership\_types

The `membership_types` table contains info about memberships.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | membershipTypeId |

membership\_types table foreign keys

| Join membership\_types with | on |
| --- | --- |
| [memberships](#memberships) | ``` membership_types.membershipTypeId = memberships.membershipTypeId ``` |

membership\_types table schema

|  |
| --- |
| **description**  STRING |
| **enabled**  INTEGER |
| **expirationType**  INTEGER |
| **expires**  BOOLEAN |
| **membershipTypeId**  INTEGER |
| **priceLevel**  INTEGER |
| **seq**  INTEGER |

### memberships

The `memberships` table contains info about memberships, which is a pairing of a [`customer`](#customers) and [`membership_type`](#membership_types).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | customerId  membershipTypeId |
| **Replication Key** | changed |

memberships table foreign keys

| Join memberships with | on |
| --- | --- |
| [check\_details](#check-details) | ``` memberships.customerId = check_details.g_CustId ```  ``` memberships.customerId = check_details.p_CustId ```  ``` memberships.customerId = check_details.s_CustId ```  ``` memberships.byUserId = check_details.discountUserId ``` |
| [checks](#checks) | ``` memberships.customerId = checks.customerId ```  ``` memberships.byUserId = checks.discountUserId ```  ``` memberships.byUserId = checks.userId ``` |
| [event\_heat\_details](#event-heat-details) | ``` memberships.customerId = event_heat_details.customerId ``` |
| [gift\_card\_history](#gift-card-history) | ``` memberships.customerId = gift_card_history.customerId ```  ``` memberships.byUserId = gift_card_history.userId ``` |
| [heat\_main\_details](#heat-main-details) | ``` memberships.customerId = heat_main_details.customerId ```  ``` memberships.byUserId = heat_main_details.userId ``` |
| [payments](#payments) | ``` memberships.customerId = payments.customerId ```  ``` memberships.byUserId = payments.userId ```  ``` memberships.byUserId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` memberships.customerId = payments_voided.customerId ```  ``` memberships.byUserId = payments_voided.userId ```  ``` memberships.byUserId = payments_voided.voidUser ``` |
| [reservations](#reservations) | ``` memberships.customerId = reservations.customersId ``` |
| [membership\_types](#membership-types) | ``` memberships.membershipTypeId = membership_types.membershipTypeId ``` |
| [event\_tasks](#event-tasks) | ``` memberships.byUserId = event_tasks.completedBy ``` |
| [users](#users) | ``` memberships.byUserId = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` memberships.byUserId = event_reservations.userId ``` |

memberships table schema

|  |
| --- |
| **byUserId**  INTEGER |
| **changed**  DATE-TIME |
| **customerId**  INTEGER |
| **expiration**  DATE-TIME |
| **membershipTypeId**  INTEGER |
| **notes**  STRING |

### payments

The `payments` table contains info about collected payments.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | paymentId |
| **Replication Key** | payDate |

payments table foreign keys

| Join payments with | on |
| --- | --- |
| [check\_details](#check-details) | ``` payments.checkId = check_details.checkId ```  ``` payments.customerId = check_details.g_CustId ```  ``` payments.customerId = check_details.p_CustId ```  ``` payments.customerId = check_details.s_CustId ```  ``` payments.userId = check_details.discountUserId ```  ``` payments.voidUser = check_details.discountUserId ``` |
| [checks](#checks) | ``` payments.checkId = checks.checkId ```  ``` payments.customerId = checks.customerId ```  ``` payments.userId = checks.discountUserId ```  ``` payments.voidUser = checks.discountUserId ```  ``` payments.userId = checks.userId ```  ``` payments.voidUser = checks.userId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` payments.checkId = event_reservation_links.checkId ``` |
| [gift\_card\_history](#gift-card-history) | ``` payments.checkId = gift_card_history.checkId ```  ``` payments.customerId = gift_card_history.customerId ```  ``` payments.userId = gift_card_history.userId ```  ``` payments.voidUser = gift_card_history.userId ``` |
| [payments\_voided](#payments-voided) | ``` payments.checkId = payments_voided.checkId ```  ``` payments.customerId = payments_voided.customerId ```  ``` payments.paymentId = payments_voided.paymentId ```  ``` payments.userId = payments_voided.userId ```  ``` payments.voidUser = payments_voided.userId ```  ``` payments.userId = payments_voided.voidUser ```  ``` payments.voidUser = payments_voided.voidUser ``` |
| [reservations](#reservations) | ``` payments.checkId = reservations.checkId ```  ``` payments.customerId = reservations.customersId ``` |
| [event\_heat\_details](#event-heat-details) | ``` payments.customerId = event_heat_details.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` payments.customerId = heat_main_details.customerId ```  ``` payments.userId = heat_main_details.userId ```  ``` payments.voidUser = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` payments.customerId = memberships.customerId ```  ``` payments.userId = memberships.byUserId ```  ``` payments.voidUser = memberships.byUserId ``` |
| [event\_tasks](#event-tasks) | ``` payments.userId = event_tasks.completedBy ```  ``` payments.voidUser = event_tasks.completedBy ``` |
| [users](#users) | ``` payments.userId = users.userId ```  ``` payments.voidUser = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` payments.userId = event_reservations.userId ```  ``` payments.voidUser = event_reservations.userId ``` |

payments table schema

|  |
| --- |
| **cardType**  STRING |
| **checkId**  INTEGER |
| **customerId**  INTEGER |
| **extCardType**  STRING |
| **payAmount**  NUMBER |
| **payDate**  DATE-TIME |
| **payStatus**  INTEGER |
| **payTax**  NUMBER |
| **payTerminal**  STRING |
| **payType**  INTEGER |
| **paymentId**  INTEGER |
| **transaction**  STRING |
| **userId**  INTEGER |
| **voidDate**  DATE-TIME |
| **voidNotes**  STRING |
| **voidTerminal**  STRING |
| **voidUser**  INTEGER |

### payments\_voided

The `payments_voided` table contains info about voided [`payments`](#payments).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | paymentId |
| **Replication Key** | voidDate |

payments\_voided table foreign keys

| Join payments\_voided with | on |
| --- | --- |
| [check\_details](#check-details) | ``` payments_voided.checkId = check_details.checkId ```  ``` payments_voided.customerId = check_details.g_CustId ```  ``` payments_voided.customerId = check_details.p_CustId ```  ``` payments_voided.customerId = check_details.s_CustId ```  ``` payments_voided.userId = check_details.discountUserId ```  ``` payments_voided.voidUser = check_details.discountUserId ``` |
| [checks](#checks) | ``` payments_voided.checkId = checks.checkId ```  ``` payments_voided.customerId = checks.customerId ```  ``` payments_voided.userId = checks.discountUserId ```  ``` payments_voided.voidUser = checks.discountUserId ```  ``` payments_voided.userId = checks.userId ```  ``` payments_voided.voidUser = checks.userId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` payments_voided.checkId = event_reservation_links.checkId ``` |
| [gift\_card\_history](#gift-card-history) | ``` payments_voided.checkId = gift_card_history.checkId ```  ``` payments_voided.customerId = gift_card_history.customerId ```  ``` payments_voided.userId = gift_card_history.userId ```  ``` payments_voided.voidUser = gift_card_history.userId ``` |
| [payments](#payments) | ``` payments_voided.checkId = payments.checkId ```  ``` payments_voided.customerId = payments.customerId ```  ``` payments_voided.paymentId = payments.paymentId ```  ``` payments_voided.userId = payments.userId ```  ``` payments_voided.voidUser = payments.userId ```  ``` payments_voided.userId = payments.voidUser ```  ``` payments_voided.voidUser = payments.voidUser ``` |
| [reservations](#reservations) | ``` payments_voided.checkId = reservations.checkId ```  ``` payments_voided.customerId = reservations.customersId ``` |
| [event\_heat\_details](#event-heat-details) | ``` payments_voided.customerId = event_heat_details.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` payments_voided.customerId = heat_main_details.customerId ```  ``` payments_voided.userId = heat_main_details.userId ```  ``` payments_voided.voidUser = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` payments_voided.customerId = memberships.customerId ```  ``` payments_voided.userId = memberships.byUserId ```  ``` payments_voided.voidUser = memberships.byUserId ``` |
| [event\_tasks](#event-tasks) | ``` payments_voided.userId = event_tasks.completedBy ```  ``` payments_voided.voidUser = event_tasks.completedBy ``` |
| [users](#users) | ``` payments_voided.userId = users.userId ```  ``` payments_voided.voidUser = users.userId ``` |
| [event\_reservations](#event-reservations) | ``` payments_voided.userId = event_reservations.userId ```  ``` payments_voided.voidUser = event_reservations.userId ``` |

payments\_voided table schema

|  |
| --- |
| **cardType**  STRING |
| **checkId**  INTEGER |
| **customerId**  INTEGER |
| **extCardType**  STRING |
| **payAmount**  NUMBER |
| **payDate**  DATE-TIME |
| **payStatus**  INTEGER |
| **payTax**  NUMBER |
| **payTerminal**  STRING |
| **payType**  INTEGER |
| **paymentId**  INTEGER |
| **transaction**  STRING |
| **userId**  INTEGER |
| **voidDate**  DATE-TIME |
| **voidNotes**  STRING |
| **voidTerminal**  STRING |
| **voidUser**  INTEGER |

### product\_classes

The `product_classes` table contains info about classes applied to [`products`](#products). Product classes determine how products are aggregated in Club Speed’s reporting system.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | productClassId |

product\_classes table foreign keys

| Join product\_classes with | on |
| --- | --- |
| [discount\_types](#discount-types) | ``` product_classes.productClassId = discount_types.productClassId ``` |
| [products](#products) | ``` product_classes.productClassId = products.productClassId ``` |

product\_classes table schema

|  |
| --- |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **exportName**  STRING |
| **productClassId**  INTEGER |

### products

The `products` table contains info about products.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | productId |

products table foreign keys

| Join products with | on |
| --- | --- |
| [discount\_types](#discount-types) | ``` products.productClassId = discount_types.productClassId ``` |
| [product\_classes](#product-classes) | ``` products.productClassId = product_classes.productClassId ``` |
| [booking](#booking) | ``` products.productId = booking.productsId ``` |
| [booking\_availability](#booking-availability) | ``` products.productId = booking_availability.products.productsId ``` |
| [check\_details](#check-details) | ``` products.productId = check_details.productId ```  ``` products.taxId = check_details.taxId ``` |
| [event\_types](#event-types) | ``` products.productId = event_types.onlineProductId ``` |
| [taxes](#taxes) | ``` products.taxId = taxes.taxId ``` |

products table schema

|  |
| --- |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **enabled**  BOOLEAN |
| **g\_Points**  NUMBER |
| **p\_Points**  NUMBER |
| **price1**  NUMBER |
| **price2**  NUMBER |
| **priceCadet**  NUMBER |
| **productClassId**  INTEGER |
| **productId**  INTEGER |
| **productType**  INTEGER |
| **r\_Points**  NUMBER |
| **taxId**  INTEGER |

### reservations

The `reservations` table contains info about reservations. Reservations are indications that a [`customer`](#customers) is looking to purchase a spot in a [`booking`](#booking_availability) or has already purchased a spot.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | onlineBookingReservationsId |
| **Replication Key** | createdAt |

reservations table foreign keys

| Join reservations with | on |
| --- | --- |
| [booking](#booking) | ``` reservations.onlineBookingsId = booking.onlineBookingsId ``` |
| [booking\_availability](#booking-availability) | ``` reservations.onlineBookingsId = booking_availability.products.onlineBookingsId ``` |
| [check\_details](#check-details) | ``` reservations.checkId = check_details.checkId ```  ``` reservations.customersId = check_details.g_CustId ```  ``` reservations.customersId = check_details.p_CustId ```  ``` reservations.customersId = check_details.s_CustId ``` |
| [checks](#checks) | ``` reservations.checkId = checks.checkId ```  ``` reservations.customersId = checks.customerId ``` |
| [event\_reservation\_links](#event-reservation-links) | ``` reservations.checkId = event_reservation_links.checkId ```  ``` reservations.onlineBookingReservationsId = event_reservation_links.reservationId ``` |
| [gift\_card\_history](#gift-card-history) | ``` reservations.checkId = gift_card_history.checkId ```  ``` reservations.customersId = gift_card_history.customerId ``` |
| [payments](#payments) | ``` reservations.checkId = payments.checkId ```  ``` reservations.customersId = payments.customerId ``` |
| [payments\_voided](#payments-voided) | ``` reservations.checkId = payments_voided.checkId ```  ``` reservations.customersId = payments_voided.customerId ``` |
| [event\_heat\_details](#event-heat-details) | ``` reservations.customersId = event_heat_details.customerId ``` |
| [heat\_main\_details](#heat-main-details) | ``` reservations.customersId = heat_main_details.customerId ``` |
| [memberships](#memberships) | ``` reservations.customersId = memberships.customerId ``` |
| [events](#events) | ``` reservations.onlineBookingReservationsId = events.reservationId ``` |

reservations table schema

|  |
| --- |
| **checkId**  INTEGER |
| **createdAt**  DATE-TIME |
| **customersId**  INTEGER |
| **expiresAt**  DATE-TIME |
| **onlineBookingReservationStatusId**  INTEGER |
| **onlineBookingReservationsId**  INTEGER |
| **onlineBookingsId**  INTEGER |
| **quantity**  INTEGER |
| **sessionId**  STRING |

### sources

The `sources` table contains info about how customers find and register at venues.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sourceId |

sources table schema

|  |
| --- |
| **deleted**  BOOLEAN |
| **enabled**  BOOLEAN |
| **locationId**  INTEGER |
| **name**  STRING |
| **seq**  INTEGER |
| **sourceId**  INTEGER |

### taxes

The `taxes` table contains info about tax calculations, which are typically applied to [`products`](#products).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | taxId |

taxes table foreign keys

| Join taxes with | on |
| --- | --- |
| [check\_details](#check-details) | ``` taxes.taxId = check_details.taxId ``` |
| [products](#products) | ``` taxes.taxId = products.taxId ``` |

taxes table schema

|  |
| --- |
| **amount**  NUMBER |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **gst**  NUMBER |
| **taxId**  INTEGER |

### users

The `users` table contains info about employees and system users. **Note**: While some employees may also be [`customers`](#customers), this table does not contain customer information.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | userId |

users table foreign keys

| Join users with | on |
| --- | --- |
| [check\_details](#check-details) | ``` users.userId = check_details.discountUserId ``` |
| [checks](#checks) | ``` users.userId = checks.discountUserId ```  ``` users.userId = checks.userId ``` |
| [event\_tasks](#event-tasks) | ``` users.userId = event_tasks.completedBy ``` |
| [gift\_card\_history](#gift-card-history) | ``` users.userId = gift_card_history.userId ``` |
| [event\_reservations](#event-reservations) | ``` users.userId = event_reservations.userId ``` |
| [heat\_main\_details](#heat-main-details) | ``` users.userId = heat_main_details.userId ``` |
| [memberships](#memberships) | ``` users.userId = memberships.byUserId ``` |
| [payments](#payments) | ``` users.userId = payments.userId ```  ``` users.userId = payments.voidUser ``` |
| [payments\_voided](#payments-voided) | ``` users.userId = payments_voided.userId ```  ``` users.userId = payments_voided.voidUser ``` |

users table schema

|  |
| --- |
| **cardId**  INTEGER |
| **deleted**  BOOLEAN |
| **email**  STRING |
| **empStartDate**  DATE-TIME |
| **enabled**  BOOLEAN |
| **firstname**  STRING |
| **isSystemUser**  BOOLEAN |
| **lastname**  STRING |
| **phone**  STRING |
| **userId**  INTEGER |
| **username**  STRING |
