---
source: https://qlik.dev/embed/capability-api/quickstart/mashups-build-cloud/
last_updated: 2025-07-03T16:05:11+02:00
---

# Building your first mashup with Qlik Cloud

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> To do something similar with qlik-embed, refer
> to [embedding Qlik Analytics using qlik-embed web components](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart).

This topic assumes that you are using an external web server to host your
mashup. To keep things simple, any code related to authentication has been
omitted.

## Creating the container

Create a folder named `helpdesk` to contain your assets.

## Creating the main script file

Create the main JavaScript file `helpdesk.js`. This file is placed in the
`helpdesk` folder.

### Configuring your Qlik Sense host

The Qlik Sense host being used must be configured in your mashup. This is needed
for the following reasons:

- To define the actual Qlik associative engine connection, which is used when you
  open an app or get a list of apps. This is covered by the `config` JavaScript
  object, used as a parameter in the `openApp` call.

- To define where the Qlik Sense client side software and files should be loaded
  from. This is achieved by configuring RequireJS with the require.config call
  and setting the baseUrl.

- To define the web integration ID, which is necessary to enable cross-domain
  resource sharing. For details on how to find the web integration ID, refer to
  Managing web integrations.

```javascript
var config = {
    host: '<TENANT_URL>', //for example, 'abc.us.example.com'
    prefix: '/',
    port: 443,
    isSecure: true,
    webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require.config( {
    baseUrl: ( config.isSecure ? "https://" : "http://" ) + config.host + 
    (config.port ? ":" + config.port : "") + config.prefix + "resources",
    webIntegrationId: config.webIntegrationId
} );
```

### Setting the global require and alert

The JavaScript file is loaded in the browser when your mashup is used. RequireJS
is used as a module loader.

```javascript
require( ["js/qlik"], ( qlik ) => {
  qlik.on( "error", ( error ) => {
    $( '#popupText' ).append( error.message + "<br>" );
    $( '#popup' ).fadeIn( 1000 );
  } );
  $( "#closePopup" ).click( () => {
    $( '#popup' ).hide();
  } );
  //open apps -- inserted here --
  //get objects -- inserted here --
} );
```

> **Note:** Do not use different versions of RequireJS on the same web page.
> You can find out which version of RequireJS is being used by typing `require.version` in the browser console while
> viewing the mashup in the browser.

### Connecting to the Qlik Sense app

You need to connect to the Qlik Sense app containing the objects you want to
display on your web page.

```javascript
//open apps -- inserted here --
var app = qlik.openApp( '<APP_ID>', config ); //Replace 'AppId' with the actual
                                           // helpdesk app ID 
```

> **Note:** Add this code within the scope of the `require()` method.

### Retrieving the Qlik Sense objects to use

You then need to fetch the objects you want to display.

```javascript
//get objects -- inserted here --
app.visualization.get('uETyGUP').then((vis)=>{
    vis.show("QV01");
} );
app.visualization.get('xfvKMP').then((vis)=>{
    vis.show("QV02");
} );
app.visualization.get('rJFbvG').then((vis)=>{
    vis.show("QV03");
} );
app.visualization.get('PAppmU').then((vis)=>{
    vis.show("QV04");
} );
app.visualization.get('ca4463f1-31fc-4eed-98a7-5e770b8387f3').then((vis)=>{
    vis.show("QV05");
} );
app.visualization.get('ff551649-420e-428d-bede-38accf80dce8').then((vis)=>{
    vis.show("QV06");
} );
```

> **Note:** Add this code within the scope of the `require()` method.

### Pre-selecting fields in the app

Making pre-selections in the app before rendering visualizations is a best
practice. It allows the engine to do calculations once, which is quicker and
puts less burden on the engine than making selections after the visualizations
are rendered.

```javascript
//function to pre-select fields
function getCaseOwner(callback) {
    // call some backend functionality and call the “callback” function when ready
    callback("Thomas R. Allman");
}

//call getCaseOwner with callback function
getCaseOwner(function(caseOwner) {
    app.field("Case Owner").selectMatch(caseOwner)
    .then(function() {
        //get objects -- inserted here --
        app.visualization.get('uETyGUP').then((vis)=>{
            vis.show("QV01");
        } );
        app.visualization.get('xfvKMP').then((vis)=>{
            vis.show("QV02");
        } );
        app.visualization.get('rJFbvG').then((vis)=>{
            vis.show("QV03");
        } );
        app.visualization.get('PAppmU').then((vis)=>{
            vis.show("QV04");
        } );
        app.visualization.get('ca4463f1-31fc-4eed-98a7-5e770b8387f3').then((vis)=>{
            vis.show("QV05");
        } );
        app.visualization.get('ff551649-420e-428d-bede-38accf80dce8').then(=>(vis){
            vis.show("QV06");
        } );
    })
})
```

## Creating the main HTML file

Create an HTML file, name it index.html, and save it in the helpdesk folder.

### Defining the relationships

The relationship between the current document and the linked Qlik Sense defined
style sheet is specified in a link rel tag inside the head of the HTML file.

> **Note:** Add host to the link rel tags if the web server hosting the mashup is different from the web server hosting the static
> Qlik Sense content.

```html
<link rel="stylesheet" href="https://<TENANT_URL>/resources/autogenerated/qlik-styles.css">
<script src="https://<TENANT_URL>/resources/assets/external/requirejs/require.js"></script>
<script src="helpdesk.js"></script>
```

### Adding an internal style sheet

Add some internal styling inside the head of the HTML file to organize the
presentation of the charts.

```html
<style>
div.flex-container {
    display: flex;
    flex-wrap: wrap;
    margin: 0 45px 45px 0;
}
div.qvobject {
    flex: 1 1 auto;
    height: 300px;
    min-width: 400px;
    margin: 45px 0 0 45px;
}
</style>
```

### Placing the Qlik Sense objects

The Qlik Sense objects that have been defined in the JavaScript file are placed
inside div tags inside the body of the HTML file.

```html
<div class="flex-container">
  <div id="QV01" class="qvobject"></div>
  <div id="QV02" class="qvobject"></div>
  <div id="QV03" class="qvobject"></div>
  <div id="QV04" class="qvobject"></div>
  <div id="QV05" class="qvobject"></div>
  <div id="QV06" class="qvobject"></div>
</div>
```

## Testing the mashup

Now is a good time to test your mashup.

1. Log into Qlik Cloud.
2. Access the mashup:

   For example:

   `https://your_web_server_URL:port`
