---
title: "Adding terms to your glossary"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/BusinessGlossary/Tutorial/creating-terms.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with business glossaries", "Tutorial - Creating a business glossary"]
---

# Adding terms to your glossary

First, you will create terms for the glossary. Once all your terms have been created, you can then link the terms that are related to each other.

## Creating terms

Do the following:

1. Select the Terms tab.
2. Create the term Annual Contract Value:

   1. Select Create >Term.
   2. After Name, enter Annual Contract Value.
   3. After Abbreviation, enter ACV.
   4. After Status, select Verified
   5. Under Definition, enter A software subscription service metric that breaks down the total value of a customer’s contract into an average value per year. This metric standardizes the total value of the contract over its lifespan to show average revenue from an annual subscription agreement.
   6. Under Related information, enter:

      ##Example formula and calculation: ACV=Total contract value/Total years in contract

      https://www.acme.com/RecurringRevenueEquation

      ##Required information: contracts signed on file

      ##Standard terms and agreement: www.acme.com/contracts/terms

      ##Notes: ACV can be calculated differently in different organizations.
   7. Under Linked resources, click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select the app ContractValues, and click Add link to.
   8. Under Term Stewards, select a user from your Qlik Cloud environment.
   9. Under Categories, select Customer Contracts and Partner Contracts.
   10. Under Tags, enter revenue and Q4 reports.
3. Create the term Annual Recurring Revenue:

   1. Select Create >Term.
   2. After Name, enter Annual Recurring Revenue.
   3. After Abbreviation, enter ARR.
   4. After Status, select Verified
   5. Under Definition, enter Revenue, normalized on an annual basis, that the organization expects to receive from all of its customers for providing them with products or services.
   6. Under Related information, enter:

      ##Example formula and calculation: ARR = (Overall Subscription Cost Per Year + Recurring Revenue From Add-ons or Upgrades) - Revenue Lost from Cancellations.

      https://www.acme.com/RecurringRevenueEquation

      ##Required information: contracts signed on file

      ##Standard terms and agreement: www.acme.com/contracts/terms

      ##Notes: ACV measures a single account; ARR measures all accounts at the same time.
   7. Under Term Stewards, select a user from your Qlik Cloud environment.
   8. Under Categories, select Customer Contracts and Partner Contracts.
   9. Under Tags, enter revenue and Q4 reports.
4. Create the term Total Contract Value:

   1. Select Create >Term.
   2. After Name, enter Total Contract Value.
   3. After Abbreviation, enter TCV.
   4. After Status, select Verified
   5. Under Definition, enter The total amount of revenue you receive from a given customer.
   6. Under Related information, enter:

      ##Example formula and calculation: TCV = Monthly recurring revenue x Duration of contract [in months] + one-time fees

      https://www.acme.com/RecurringRevenueEquation

      ##Required information: contracts signed on file

      ##Standard terms and agreement: www.acme.com/contracts/terms

      ##Notes: Includes all recurring subscription revenue as well as one-time fees that may be associated with the contract, such as implementation fees.
   7. Under Term Stewards, select a user from your Qlik Cloud environment.
   8. Under Categories, select Customer Contracts and Partner Contracts.
   9. Under Tags, enter revenue and financial reports.
5. Create the term Gross Margin:

   1. Select Create >Term.
   2. After Name, enter Gross Margin.
   3. After Abbreviation, enter GM.
   4. After Status, select Draft
   5. Under Definition, enter The amount of money a company retains minus the direct costs associated with producing the goods it provides; net sales less the cost of goods sold (COGS).
   6. Under Related information, enter:

      ##Example formula and calculation: Net sales - COGS

      ##Required information: Revenue numbers, manufacturing costs, ancillary expenses

      ##Standard terms and agreement: www.acme.com/contracts/terms

      ##Notes: Also referred to as gross profit.
   7. Under Term Stewards, select a user from your Qlik Cloud environment.
   8. Under Categories, select Customer Contracts.
   9. Under Tags, enter revenue.
6. Create the term Gross Profit:

   1. Select Create >Term.
   2. After Name, enter Gross Profit.
   3. After Abbreviation, enter GP.
   4. After Status, select Draft
   5. Under Definition, enter The profit a company makes after deducting costs associated with manufacture and sales of product and services.
   6. Under Related information, enter:

      ##Example formula and calculation: Net sales - COGS

      ##Required information: Revenue numbers, manufacturing costs, ancillary expenses

      ##Standard terms and agreement: www.acme.com/contracts/terms

      ##Notes: Also referred to as gross margin.
   7. Under Term Stewards, select a user from your Qlik Cloud environment.
   8. Under Categories, select Customer Contracts.
   9. Under Tags, enter revenue.
7. Create the term Customer:

   1. Select Create >Term.
   2. After Name, enter Customer.
   3. After Status, select Verified
   4. Under Definition, enter A person, business, or entity that buys goods or services from another business. A customer is or has been in an active contract with the organization.
   5. Under Related information, enter:

      ##Required information: www.acme.com/customercontracts

      ##Standard terms and agreement: Attach signed SLA to customer file

      ##Notes:
   6. Under Term Stewards, select a user from your Qlik Cloud environment.
   7. Under Categories, select Customer.
   8. Under Tags, enter revenue and territory.
8. Create the term Service Level Agreement:

   1. Select Create >Term.
   2. After Name, enter Service Level Agreement.
   3. After Abbreviation, enter SLA.
   4. After Status, select Verified
   5. Under Definition, enter A contractual agreement between a service provider and a customer where particular levels of services (such as up-time) are guaranteed or the customer is entitled to remuneration. As an example, Internet service providers and telcos will commonly include service level agreements within the terms of their contracts with customers to define the level(s) of service being sold in plain language terms.
   6. Under Related information, enter:

      ##Required information:

      ##Standard terms and agreement: www.acme.com/contracts/terms

      ##Notes:
   7. Under Term Stewards, select a user from your Qlik Cloud environment.
   8. Under Categories, select Customer and Partner.
   9. Under Tags, enter contract and service-level.
9. Create the term Accounts Payable:

   1. Select Create >Term.
   2. After Name, enter Accounts Payable.
   3. After Abbreviation, enter AP.
   4. After Status, select Draft
   5. Under Definition, enter Amount of money owed by your company to external suppliers.
   6. Under Related information, enter:

      ##Required information:

      ##Standard terms and agreement:www.acme.com/externalcontractterms

      ##Notes: A/P payments must meet guidelines to be approved.
   7. Under Term Stewards, select a user from your Qlik Cloud environment.
   8. Under Categories, select Partner.
   9. Under Tags, enter COGS and EBITDA.
10. Create the term Accounts Receivable:

    1. Select Create >Term.
    2. After Name, enter Accounts Receivable.
    3. After Abbreviation, enter AR.
    4. After Status, select Verified
    5. Under Definition, enter The balance of money owed to a firm for goods or services delivered or used but not yet paid for by customers.
    6. Under Related information, enter:

       ##Required information:

       ##Standard terms and agreement: www.acme.com/contracts/terms

       ##Notes:
    7. Under Term Stewards, select a user from your Qlik Cloud environment.
    8. Under Categories, select Customer Contracts.
    9. Under Tags, enter revenue and payment terms.
11. Create the term Cost of Goods Sold:

    1. Select Create >Term.
    2. After Name, enter Cost of Goods Sold.
    3. After Abbreviation, enter COGS.
    4. After Status, select Verified
    5. Under Definition, enter All of the costs and expenses directly related to the production of goods. COGS excludes indirect costs such as overhead and sales & marketing.
    6. Under Related information, enter:

       ##Example formula and calculation: COGS = the starting inventory + purchases – ending inventory

       ##Required information: inventory reports

       ##Standard terms and agreement:

       ##Notes: Gross profit=Revenue-Cost of Goods Sold (COGS)
    7. Under Term Stewards, select a user from your Qlik Cloud environment.
    8. Under Categories, select Customer.
    9. Under Tags, enter revenue, Q4, and EBITDA.

## Adding related terms

With all terms added, you can now update your terms with their related terms.

Do the following:

1. Select Annual Contract Value and under Related terms, click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Annual Contract Value and Annual Recurring Revenue, and click Select related terms.
2. Select Annual Recurring Revenue and under Related terms, click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Annual Contract Value and Total Contract Value, and click Select related terms.
3. Select Total Contract Value and under Related terms, click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Annual Contract Value and Annual Recurring Revenue, and click Select related terms.
4. Select Gross Margin and under Related terms, click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Gross Profit, select Synonym, and click Select related terms.
5. Select Gross Profit and under Related terms, click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Gross Margin, select Synonym, and click Select related terms.
6. Select Customer and under Related terms:

   1. Click ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg).
   2. Select Annual Contract Value, Total Contract Value, and Service Level Agreement.
   3. Click Select related terms.
7. Select Service Level Agreement and under Related terms, click ![Add](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Customer, and click Select related terms.
8. Select Accounts Payable and under Related terms, click ![Add](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select COGS, and click Select related terms.
9. Select Accounts Receivable and under Related terms, click ![Add](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Customer, and click Select related terms.
10. Select Cost of Goods Sold and under Related terms, click ![Add](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg), select Gross Profit, and click Select related terms.

If you have added all of the categories and terms above, you will see how the addition of more content and links to various content within the glossary and apps can reinforce business processes and trust in your data.
