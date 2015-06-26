<!--
{
"name" : "alpha",
"version" : "0.1",
"title" : "alpha - Yext Codebase",
"description": "Yext Codebase Orientation.",
"freshnessDate" : 2015-06-01,
"homepage" : "https://sites.google.com/a/yext.com/engineering/orientation/alpha",
"license" : "All Rights Reserved"
}
-->

<!-- @section -->

# alpha

This is an overview of the alpha repository.  [view Go code overview](https://sites.google.com/a/yext.com/engineering/orientation/gocode)

Most of it falls into one of these categories:

* Library code - for example, AclCheck.java provides a simple interface for querying user access permissions
* RPC Servers - for example, ProfileServer provides central coordination, validation, and caching of profile data
* Play! web applications - for example, admin2 provides an interface for employees to administer the system
* Message handlers - for example, the Smart Labeler processes profile updates for changes to saved search eligibility

```
admin               Very old admin. Keep out
khan                Job management system
production          Production configuration
spark               Spark - Direct Marketing System (Python/Django)
taskprocessing      Outsourced tasks, e.g. "Is this listing already on this publisher?"
tools               Development tools
yext-selenium       Selenium scripts for testing Storm

test/com/yext/...   Tests are in a parallel directory structure

src/com/yext/...
  admin2            The main Admin application at yext.  http://www.yext.com/admin2/
  analytics         Analytics in Storm
  aws               Helpers for working with Amazon services
  billing           The accounting / billing system. Charge credit cards and create invoices.
  cache             Helpers for constructing cache keys, to avoid conflicts
  categorymanager   The Category Server stores location categories and maps them to publisher categories.
  clientscrapers
  cms/photos        Client for storing photos
  common
  config
  crm
  dam               Digital Asset Management - the Assets/Approvals section in Storm
  emails2           Render transactional emails like "welcome to Yext" and the monthly account summary.
  enhancedlists     Enhanced Content Lists, a wildly popular feature.  (Products, Staff Bios, Calendars, Menus)
  internal          Yext office tasks
  linkedaccounts
  listingextensions Web server for listingextensions.com, where we serve ECLs for Yahoo!
  listings
  listingservice
  livecache         Consumer-facing API for location search
  logging           Sentry integration for log4j
  mailing           Helper for sending mailings
  maintenance       Web app that shows a "Down for maintenance" screen
  matchservice      Get set up with hot singles in NYC!
  memcached         Helper for memcached requests
  messaging         RabbitMQ - MessageHandler, MessagePublisher
  mobileapi         API backend for the Yext mobile apps (iPhone, Android)
  models            Core entities (Account, Location, Social Posts, ...)
  monitoring        Statsd monitoring integration
  olap
  pageload
  partnerpages      Web app that serves mocks of PowerListings on non-web publishers
  pitt              PowerListings testing tool
  play              Play! common libraries, tags, templates
  plc               PowerListings Verifier - Scrape publishers to ensure our data is up.
  powerlistings     PowerListings lifecycle
  profile
  profileservice    ProfileServer manages the saving and fetching of Location Profiles
  profiling
  recruiting
  redshiftadmin
  reports
  reseller-common
  resellers         Reseller Portal - Web interface for partners to sign up customers and manage their accounts
  resellersapi      Resellers API - Public API for signing up customers and administering their PowerListings
  reviews           Review monitoring
  rsa               Really Simple Analytics - Email analytics for our mailings
  sales
  sales2
  scraper
  searchterms
  servicelocator    "Service Locator" is a zookeeper-based system for locating RPC servers
  sms               SMS - Scanning Management Services - Scan listings and generate reports
  social
  socialadmin
  spark
  statusboards
  storm             Storm - Customer facing web interface to Yext
  storm-common      A Play! module for sharing common Storm elements across projects
  subscriptions     Subscriptions processes signups, managing who gets what service and for how much money.
  tags
  testpartner       A fake PowerListings publisher for testing
  textassets
  updates
  ups               UPS delivers PowerListings updates to publishers.
  users             Users serves the login page
  util
  warehouse
```
