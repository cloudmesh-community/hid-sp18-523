
# Cloud Domo

| Ritesh Tandon
| ritandon@iu.edu
| Indiana University, Bloomington
| hid : hid-sp18-523
| github: [:cloud:](https://github.com/cloudmesh-community/hid-sp18-523/tree/master/paper/paper.md)

---

Keywords: Domo, API, token

---

Domo is cloud based data integration platform that enables employees to
engage with globally distributed data in real time. It provides
flexibility to outside partners and third party vendors to integrate and
collaborate with data. Domo has more than 400 data connectors. Data can
be accessed directly from public or private cloud regardless if it is
available on-premise or proprietary systems.
Data is heart of information for any business. it is very trivial to find 
relevant data that is requiredby different people working in different 
departments of large organization. More so, the bigger challenge is to 
derive insights from the data after it is located. Domo transforms the way 
orgaizations employee access, use, analyze and share data. Domo gives power to
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

## Domo Inbuilt Solutions

Domo has custom inbuilt dashboard and visualization solution for
different roles (such as BI, CEO, Finance, IT, Marketing, Operations,
Sales and Services etc) within organization and for different
industries (such as Education, Healthcare, Manufacturing, Hospitality,
Retail and Transportation etc)

## Data Connectors

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

## Connector Dev Studio ( Creating custom connector )

Connector Dev Studio enables developers to create their own data connectors
if they do not find any existing connector in Domo library. They may chose 
to use that connector exclusively for their own organization or can make it 
publicly available for contributing to community. Developers need to have 
JavaScript knowledge in order to build their own custom connector. 
Certain conditions are required to be met in order to build custom connector; 
APIs must use https, it should be REST API , it should either require No 
Authentication or should be able to get authenticated using OAuth 2.0 or API 
key or through user name and password.Build Now menu command lets the developer 
navigate to Connector Dev Studio Integrated development Environment ( IDE ). 
Developers have to upload their custom connector icon image, configure 
authentication , define reports and  define data processing steps. 
After completing these steps developers may submit their custom connector for 
publishing. Domo developers will review, validate and notify developers when 
their connector will be ready for use [@hid-sp18-523-Domo-Connector].

#### Custom Connector - User Authentication

Developers have to write code block for validating API credentials and 
authenticating using username and password. They need to pass encoded 
user name and password to request header for authorization. After reading 
the response Developer needs to make use of  authenticationSuccess() 
and authenticationFailed() method to let the user 
navigate [@hid-sp18-523-Domo-Connector].

#### Custom Connector - Configure Selectable Reports

Domo Custom connector also has ability to let the developers define reports 
that their custom connectors can contain. These Reports provides extensibility 
to developers of calling  different API endpoints to acheive different function. 
This lets user of the custom connector chose reports they wish to use. 
These reports appears in Report dropdown menu once connector 
is published [@hid-sp18-523-Domo-Connector].


#### Custom Connector - Data processing steps

This step let the developer define data processing and transformation steps of 
the data that is retrieved from API endpoint call. This is performed for every 
report that developer has defined for their custom connector. Developers need to 
write script for parsing , manipulating and storing data in Domo. Data structure 
needs to be defined in code using datagrid.addcolumn() method and then data is 
added one row at a time [@hid-sp18-523-Domo-Connector].


#### Custom Connector - Sending data to Domo

Developers have to ensure that their data is correctly uploaded and represented 
in Domo. In order to do so, developers have to make use of Domo Create/Update 
dataset and Run Script command. Success message will confirm that data is 
successfully published in Domo [@hid-sp18-523-Domo-Connector].


#### Custom Connector - Submission of custom connector


After completing above steps, developers have to submit their custom connector 
for publishing using Domo Submit For Publishing 
command [@hid-sp18-523-Domo-Connector]. 



## Data Flows and Transforms

Cleaning data is herculean task when dealing with dirty data 
that needs to be cleaned before reporting. Domo has Magic ETL tool that
makes data cleaning job looks easy. It helps join, transform and tidy up
data with drag and drop ease of use @hid-sp18-523-Dev.

Domo also has SQL data flow that let the developer select data set,
perform transformation operation through SQL query and generate tidy and
processed output dataset. Domo also give option to run  data flow
whenever dataset is updated; thus making sure that final visualization
and report is always based on latest clean data in almost real time.

## Visualization

Domo has many inbuilt visualization template that helps user present
their user story in refined visual format. These predefined template are
called Cards in Domo. Horizontal bar, Vertical bar, Line, Area, Data
Science, Pie and Funnel are few popular visualization categories. These
individual categories contain many use full templates for e.g Data
Science category has visualization template for scatter plot, box plot,
predictive modeling, outliers etc to visually represent relevant data.
Donut, Pie, Treemap, Funnel, Folded funnel are few of the popular
visualization template under this category.

## Create Domo Visualization Cards

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

## Dev Studio

Integrated development environment that provides developers with web
development experience to create custom apps that can be deployed in 
Domo instance easily. Development environment consists of following 
three main components

Domo App CLI is Used to create, edit and publish custom app on Domo
environment

App Design is Custom built template that can be connected to different
datasets and visualize data (This can be used when there is need of
custom visualization requirement for which standard template is not
available)

App Manifest is Configuration file that defines properties of custom app

## Installation

First Install node.js from https://nodejs.org/en/ website. Make sure 
that itis installed by executing node --version command. Next step
is to install CLI using below command on unix/linux 
platform [@hid-sp18-523-Dev].

      npm install -g ryuu command 

Make sure that firewall is not blocking npm registry by pining
www.npmjs.com through terminal [@hid-sp18-523-Dev].

## Creating simple Domo App

Command domo init on CLI terminal create basic design template.

Enter design name and starter type App. Enter myfirstdomoapp as 
design name and HelloWorld as starter type. This will
create directory and all the necessary files that are needed
for building simple app. Directory structure shown below
is created [@hid-sp18-523-Dev].

      Following project structure is created -
          app.cs
          app.js
          domo.js
          index.html
          manifest.json


Choose the data source to which app needs to connect to. 
This is optional and based on app functionality.
simple custom app that does not connect to data source can 
be deployed on Domo instance.

From the CLI run domo dev command. This will open browser and will
render myfirstdomoapp

Make styling changes in app.css and code logic changes in app.js to
build UI and app functionality respectively.

## Building Responsive App in Domo

Domo lets developer build app that can be displayed on device of any 
size, without losing quality. Domo supports principles of responsive 
design. Developers can build their app using this design that renders 
perfectly on desktop, tablet and mobile devices. Domo use container to 
render content of app. These container supports any of below four sizes

* Full: This is customizable and can be defined in developers app manifest 
file
* Large: This is defined for displaying rendering content on devices 
with 460x540px size
* Medium:This is defined for displaying rendering content on devices 
with 225x250px size
* Small: This is defined for displaying rendering content on devices 
with 225x105px size

By default Domo development environment renders app content inside iframe. 
Developers have to open source code of iframe into new tab which can then 
be changed in order to test responsiveness of app content. Developers have 
to first create directory structure using manifest only option and then later 
on add responsive stylesheet, either of third party vendor or custom created 
css. Developer have to add javascript in order to dynamically create layout 
for placing app content. For e.g Row of tiles and grid can be created using 
java script file.
Developers have to chose and decide number of tiles depending on the size of 
the screen content will be rendered when creating custom responsive css. 
Ideally for larger screen 8 tiles are used to fill in a row. For Normal 
desktop 6 and for tablet 4 tiles in a row are 
ideal [@hid-sp18-523-Domo-Responsive].



## API Authentication

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
secret [@hid-sp18-523-Authticate].

    $curl -v -u {CLIENT_ID}:{CLIENT_SECRET} 
    https://api.domo.com/oauth/token?
        grant_type=client_credentials&scope={SCOPE}


Above command provides result in JSON format.
Body of JSON response contains multiple key value pairs.
The most important among those are access token and expires in key.
These obtained access token must be passed in header of any future request.

For e.g Below command is used for calling Domo API that gives the list
of created datasets after replacing obtained access 
token [@hid-sp18-523-Authticate].

    $curl -v -H Authorization:'bearer {access-token} 
    https://api.domo.com/v1/datasets


Custom app using Domo API can be built as explained above.

## Data API

Base url (end point) of the data API can be accessed through following
command [@hid-sp18-523-DataApi].

    GET /data/v1/:alias?:queryOperators


Alias is the name of the dataset that is defined in manifest file. 
Custom query can be run using queryOperators. Aggregate functions such 
as count, sum, min, max, avg, filter, group by and order by etc can be used
with custom query.

Format of returned data of API can be set using request accept header
of XMLHttpRequest object to following formats [@hid-sp18-523-DataApi].

    array-of-objects
      csv
      excel
      json


Return format can also be specified in domo.get method.

## Multi User API

Domo offer following end point for accessing information to all Domo
instance users [@hid-sp18-523-User]

    GET /domo/users/v1?includeDetails={true|false}
        &limit={int}&offset={int}

 
User details returned by API can be controlled by calling API.
Such as , number of records. Developers also has 
control over retreiving custom user list by passing offset 
to API [@hid-sp18-523-User].


## Single User API

Domo offer following end point for accessing information of 
single user [@hid-sp18-523-User].

    GET /domo/users/v1/:userId?
        includeDetails={true|false}
 

user id of user whose details are required can be passed.It is very
easy to get details of current logged in user by accessing through 
environment variable [@hid-sp18-523-User].


## Sharing custom app using Domo

Custom app, visualization card, report can be easily shared with 
users by logging in to Domo CLI through domo login command and then
publishing the custom built app on domo instance using domo publish
command.

## Conclusion

Domo is used as cloud based tool for real time data visualization and
reporting. Through Dev Studio and public API, Domo lets the developer
extends the capability of customizing visualization and build reporting
template that may be used for building custom app. Domo business cloud
platform offers high availability, performance and scalability for the
applications that are deployed on Domo instance.

## Acknowledgement

The author would like to thank Dr Gregor Von Laszewski for his suggestions
and guidance on the content that is presented in paper.
