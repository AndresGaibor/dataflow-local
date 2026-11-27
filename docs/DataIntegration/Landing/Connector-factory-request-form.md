---
title: "Requesting new connectors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/Connector-factory-request-form.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources"]
---

# Requesting new connectors

With the never-ending demand from business users to access data from more and more sources, the market has not been able to supply new connectors fast enough. This leaves many companies with no choice but to lean on internal teams to build and maintain their own custom connectors – adding more time, cost & complexity to their data infrastructure.

The Connector Factory Request Program streamlines the process and time line to develop a new Qlik connector, thus enabling Qlik to rapidly respond to customer requests for access to new sources. The program enables customers to closely collaborate with the Qlik product development team to ensure that an urgently needed connector will meet all defined requirements when initially released.

The benefits of this program include:

- Increases agility of data teams to rapidly respond to new customer requests for emerging sources.
- Enables data engineering teams to focus on high value activities and not custom one-off integration development and maintenance projects that tend to accumulate technical debt.
- Ensure that the new connector will initially meet the customer’s specific requirements by working with the Qlik R&D group during development and testing of the new connector.

## Further information

- The Connector Factory Request Program will initially be focused on Qlik Talend Cloud connectors to SaaS application sources that have HTTP or REST APIs.
- Once a connector has been developed and previewed by the requesting customer, it will be released and fully supported using the existing designation of a Lite connector. Lite connectors follow the same Service Level Agreements (SLA) for major data integrity, security, and reliability issues as any other connector.
- When Qlik is able to gather sufficient feedback from multiple customers about this new connector and can validate additional use cases, a Lite connector will be upgraded to a Standard connector.

## Process

1. Submission

   You submit a request to build a connector for a specific source. We aim to provide our initial response within 14 business days.

   [Connector Request Form](https://pages.qlik.com/ConnectorFactory_OnDemand.html)
2. Evaluation

   Qlik will review the suitability of the requested connector to determine if it is viable or not. We expect this process to take around 2 weeks.
3. Start

   If your request is approved for build, we will contact you to ensure everyone understands the specific requirements and use cases. You will be requested to grant Qlik developer access to source systems and test data according to program’s full terms and conditions.
4. Development and validation

   Qlik builds and tests the connector. You will receive access to this new connector as a Preview connector for testing and validation in your tenant. It will be your responsibility to confirm that the connector meets your requirements.
5. Release

   Once the new connector passes the relevant tests it will be released as a Lite Connector and made available to all Qlik Talend customers.

## Security

The on-demand building process creates a starter connector in a completely isolated environment meaning that all credential information is stored in Qlik dedicated secure systems. Throughout the connector build process, Qlik uses state-of-the-art security measures to keep your data safe:

- Our single sign-on provider controls data access by enforcing permission validation, deny by default, separation of duties and Defense-in-Depth.
- We mandate multi-factor authentication to access development networks for securing consumer identities and preventing authentication bypass.
- We securely log and monitor all access to correlate and investigate relevant security events like unhandled exceptions, authentication or authorization failures, brute force attempts, etc.
- The environment is ephemeral, development servers are destroyed every seven days.

  Any data downloaded during the process of development is destroyed with the system, and employees are unable to copy data out of this environment.
- We follow the principle of least access control. Only engineers working on building this connector have access to your application.
- We only use this access to validate API calls supported by the application.
