This Django project is similar to an online store or a subscription management system. Products are organized into categories.
Users can purchase subscription packages, and payments are processed through different gateways. All data is stored and managed in a database.

For example, when a user named Ali visits the site, he first registers through the frontend, creating a new user record in the database.
He then selects a one-month subscription package and proceeds to the payment page, choosing a payment gateway to complete the transaction.
If the payment is successful, a payment record is created and a subscription record is added for Ali, storing the package details and expiration date.
The admin can then view in the Django Admin panel which package Ali purchased, which gateway was used, and when his subscription will expire.

The Django Admin panel provides full backend control for this project:
Admins can create and organize products into categories, define and manage payment gateways, and keep track of all payment transactions.
They can also create subscription packages, link them to allowed gateways, and monitor which users have purchased which packages and when their subscriptions expire.
User accounts can be viewed, edited, activated or deactivated, and provinces or regions can be managed for user data consistency.
This clear structure makes it easy to handle an online store and subscription system from a single secure interface

![1431e437-cc64-4c0a-b492-ebccfbb79fd5](https://github.com/user-attachments/assets/aad16c7e-404e-4653-b41c-282c39012512)
