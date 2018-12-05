
# Cloud Domo  :hand: hid-sp18-523 

| Ritesh Tandon
| ritandon@iu.edu
| Indiana University, Bloomington
| hid : hid-sp18-523
| github: [:smiley:](https://github.com/cloudmesh-community/hid-sp18-523/tree/master/paper/paper.md)

---

Keywords: Domo

---

Abstract
============

Domo is cloud based data integration platform that enables employees to
engage with globally distributed data in real time. It provides
flexibility to outside partners and third party vendors to integrate and
collaborate with data. Domo has more than 400 data connectors. Data can
be accessed directly from public or private cloud regardless if it is
available on-premise or proprietary systems.


Introduction
============

Data is heart of information for any business. Though it might seems
easy; but, it is very trivial to find relevant data that is required
by different people working in different departments of large
organization. More so, the bigger challenge is to derive insights
from the data after it is located. Domo transforms the way orgaizations
employee access, use, analyze and share data. Domo gives power to
users and helps them make decision in real time. Domo can be thought of 
as cloud based data operating system that has the ability to handle and 
process data regardless of its type and location. Domo brings different data
sources spread across different locations at one central location so
that it can be easily accessible for use. Domo lets user share
and collaborate different data sources. Users can also visualize and 
report data through Domo. It also has reliable data management feature that 
provides high level of security, speed and scalability. 
Domo makes data available on any device of any size thus making it truly 
mobile.

Domo- Inbuilt Solutions
=======================

Domo has custom inbuilt dashboard and visualization solution for
different roles (such as BI, CEO, Finance, IT, Marketing, Operations,
Sales and Services etc) within organization and for different
industries (such as Education, Healthcare, Manufacturing, Hospitality,
Retail and Transportation etc)

Data Connectors
===============

Data Connectors is the heart of Domo. Different types of data 
sources, such as relational , non relational, flat files , csv
Cloud App, cloud File, third party API etc can be easily 
connected through Domo.

Cloud App Connectors; Domo has more than 400 cloud app connectors
including all famous ones such as amazon s3, AWS, Adobe analytics,
Google Analytics, Facebook, Fitbit, instagram and salesforce etc.

File Connectors; Domo can also connect to data that is stored
in files such as excel and/or csv files.

Database; Domo has connectors for connecting relational, non relational,
SQL and NO-SQL databases such as Oracle, MS SQL, MySQL and Hadoop etc.

On Premise; Other than cloud based connectors Domo can also connect to
on premise databases/files etc as long as security protocols are opened
securely for connection.

Api; Domo has Dev Studio tool for creating custom apps. It is best
suited for developers having web development experience (java script,
css, html). Domo App CLI is the main tool that is used to create, edit
and publish app designs to the Domo instance.

Data Flows and Transforms
=========================

Cleaning data is herculean task when dealing with dirty data 
that needs to be cleaned before reporting. Domo has Magic ETL tool that
makes data cleaning job looks easy. It helps join, transform and tidy up
data with drag and drop ease of use @hid-sp18-523-Dev.

Domo also has SQL data flow that let the developer select data set,
perform transformation operation through SQL query and generate tidy and
processed output dataset. Domo also give option to run  data flow
whenever dataset is updated; thus making sure that final visualization
and report is always based on latest clean data in almost real time.

Visualization
=============

Domo has many inbuilt visualization template that helps user present
their user story in refined visual format. These predefined template are
called Cards in Domo. Horizontal bar, Vertical bar, Line, Area, Data
Science, Pie and Funnel are few popular visualization categories. These
individual categories contain many use full templates for e.g Data
Science category has visualization template for scatter plot, box plot,
predictive modeling, outliers etc to visually represent relevant data.
Donut, Pie, Treemap, Funnel, Folded funnel are few of the popular
visualization template under this category.

How It Works
============

Create data connector as needed (file, cloud, on premise, Api etc)

Select the connector and create required data set by selecting 
table, views or by custom sql query.

Select dataset and chose visualization card under respective
category (Bar, Pie, Funnel, Scatter, Predictive modeling etc)

Drag and drop the fields/attributes that are needed in
visualization/report

Apply inbuilt aggregate function on fields as needed

Save card. Move to dashboard if needed.

Give access and share your visualization card with concerned users.

Dev Studio
==========

Integrated development environment that provides developers with web
development experience to create custom apps that can be deployed in Domo
instance easily. Development environment consists of following three
main components

Domo App CLI is Used to create, edit and publish custom app on Domo
environment

App Design is Custom built template that can be connected to different
datasets and visualize data (This can be used when there is need of
custom visualization requirement for which standard template is not
available)

App Manifest is Configuration file that defines properties of custom app

Installation
============

Install node.js through download

Install CLI using below command -

npm install -g ryuu command ( unix/linux based platform ). 

Make sure that firewall is not blocking npm registry by pining
www.npmjs.com through terminal

Creating simple Domo App
========================

Command domo init on CLI terminal create basic design template.

Enter design name and starter type App. Enter myfirstdomoapp as 
design name and HelloWorld as starter type. This will
create directory and all the necessary files that are needed
for building simple app

      Following project structure is created -
          app.cs
          app.js
          domo.js
          index.html
          manifest.json

 @hid-sp18-523-Dev

Choose the data source to which app needs to connect to. 
This is optional and based on app functionality.
simple custom app that does not connect to data source can 
be deployed on Domo instance.

From the CLI run domo dev command. This will open browser and will
render myfirstdomoapp

Make styling changes in app.css and code logic changes in app.js to
build UI and app functionality respectively.

API Authentication
==================

Security of data that is transmitted over wire is of highest importance
to any organization. Any public API is expected to validate and
authenticate only those clients that have access. Domo API uses OAuth2.0
for authenticating and authorizing clients. Security is managed through
access tokens. Only authenticated and authorized users can get tokens.
For accessing Domo API through OAuth security client program must obtain
ClientId and client Secret. Once authenticated; users can access API
functionality through access token. Login to Domo instance and click on
create new client link under user avatar icon to create client. Specify
application name and description. Choose one or more from Audit, Data,
Dashboard and User application scope as applicable. One has to be
careful while choosing application scope; if application scope is only
for accessing data one should only select Data scope else developers will
get access to user, audit related information as well. Once Client Id and
Client Secret is obtained, next step to obtain access token.
Following request can be made to obtain access token using Id and
secret @hid-sp18-523-Authticate

    $curl -v -u {CLIENT_ID}:{CLIENT_SECRET} 
    https://api.domo.com/oauth/token?
        grant_type=client_credentials&scope={SCOPE}

 @hid-sp18-523-Authticate

Above command provides result in JSON format.
Body of JSON response contains multiple key value pairs.
The most important among those are access token and expires in key.
These obtained access token must be passed in header of any future request.

For e.g Below command is used for calling Domo API that gives the list
of created datasets after replacing obtained access token.

    $curl -v -H Authorization:'bearer {access-token} 
    https://api.domo.com/v1/datasets

 @hid-sp18-523-Authticate

Custom app using Domo API can be built as explained above.

Data API
========

Base url (end point) of the data API can be accessed through following
command

    GET /data/v1/:alias?:queryOperators

@hid-sp18-523-DataApi

Alias is the name of the dataset that is defined in manifest file. 
Custom query can be run using queryOperators. Aggregate functions such 
as count, sum, min, max, avg, filter, group by and order by etc can be used
with custom query.

Format of returned data of API can be set using request accept header
of XMLHttpRequest object to following formats @hid-sp18-523-DataApi.

    array-of-objects
      csv
      excel
      json

 @hid-sp18-523-DataApi

Return format can also be specified in domo.get method.

Multi User API
==============

Domo offer following end point for accessing information to all Domo
instance users

    GET /domo/users/v1?includeDetails={true|false}
        &limit={int}&offset={int}

 @hid-sp18-523-User 
 
User details returned by API can be controlled by calling API.
Such as , number of records. Developers also has 
control over retreiving custom user list by passing offset to API.

@hid-sp18-523-User.

Single User API
===============

Domo offer following end point for accessing information of single user

    GET /domo/users/v1/:userId?
        includeDetails={true|false}

@hid-sp18-523-User 

user id of user whose details are required can be passed.It is very
easy to get details of current logged in user by accessing through 
environment variable.

@hid-sp18-523-User.

Sharing custom app using Domo
=============================

Custom app, visualization card, report can be easily shared with 
users by logging in to Domo CLI through domo login command and then
publishing the custom built app on domo instance using domo publish
command.

Conclusion
==========

Domo is used as cloud based tool for real time data visualization and
reporting. Through Dev Studio and public API, Domo lets the developer
extends the capability of customizing visualization and build reporting
template that may be used for building custom app. Domo business cloud
platform offers high availability, performance and scalability for the
applications that are deployed on Domo instance.

Author would like to thank Dr Gregor Von Laszewski for his suggestions
and guidance on the content that is presented in paper.
