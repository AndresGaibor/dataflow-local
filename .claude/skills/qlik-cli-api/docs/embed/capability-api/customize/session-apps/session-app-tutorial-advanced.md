---
source: https://qlik.dev/embed/capability-api/customize/session-apps/session-app-tutorial-advanced/
last_updated: 2025-07-08T16:09:30Z
---

# Creating a session app - Advanced tutorial

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

Learn how to create a session app, including a couple of visualizations on the fly
using the Capability APIs.

If you are new to session apps, review [apps and session apps](https://qlik.dev/embed/foundational-knowledge/apps-session-apps) before
continuing.

The session app is created when clicking a button which also loads data from the
prepared test script and displays two visualizations.

![The Session App Tutorial screen. Two
visualizations are displayed, a bar chart and a pie chart.](https://qlik.dev/_astro/session-app-tutorial.BURsseqg.png)

The Session App Tutorial screen. Two visualizations are displayed, a bar chart
and a pie chart.

## Creating the container

Create a folder that will contain your assets. The folder can be created in a
location of your choice.

## Creating the main script file

Then it is time to create the main JavaScript file. This file is placed in the
same folder that you just created. Name the file `session-app-tutorial.js`.

### Configuring your connection to Qlik Cloud

The Qlik Cloud tenant being used must be configured in your mashup. This is needed
for the following reasons:

- To define the actual Qlik associative engine connection, which is used when you
  open an app or get a list of apps. This is covered by the `config` JavaScript
  object, used as a parameter in the `qlik.sessionApp()` call.

- To define where the Qlik Sense client side software and extensions should be
  loaded from. This is achieved by configuring `reguirejs` with the `require.config()`
  call and setting the `baseUrl`.

In most cases, you use the same Qlik CLoud tenant for both purposes, which means
you can create the `baseUrl` from the `config` object.

```javascript
const config = {
  host: '<TENANT_URL>', //for example, 'abc.us.qlikcloud.com'
  prefix: '/',
  port: 443,
  isSecure: true,
  webIntegrationId: '<WEB_INTEGRATION_ID>'
};
require.config( {
  baseUrl: ( config.isSecure ? "https://" : "http://" ) + config.host + 
  (config.port ? ":" + config.port : "") + config.prefix + "resources"});
```

### Setting the global require and alert

The JavaScript file is loaded in the browser when your mashup is used. RequireJS
is used as a module loader.

```javascript
require( ["js/qlik"], ( qlik )=> {
  qlik.on( "error", ( error )=> {
    $( '#popupText' ).append( error.message + "<br>" );
    $( '#popup' ).fadeIn( 1000 );
  } );
  $( "#closePopup" ).click( ()=> {
    $( '#popup' ).hide();
  });
```

### Creating the session app

The session app is created using the `qlik.sessionApp` method.

```javascript
$( ".create-session-app" ).click( ()=> {
  const sessionApp = qlik.sessionApp(config);
} );
```

### Setting and loading the data load script

The script used in this tutorial is a from a shortened version of the prepared
test script that loads a set of inline data fields into the session app.

The script is set with the `app.setScript` method and then loaded into the
session app using the `app.doReload` method.

```javascript
$( ".create-session-app" ).click(()=> {
  const sessionApp = qlik.sessionApp(config);
  const script = 
  "Characters: Load Chr(RecNo()+Ord('A')-1) as Alpha, RecNo() as Num 
  autogenerate 26;   
  ASCII: Load if(RecNo()&gt;=65 and RecNo()&lt;=90,RecNo()-64) as Num,
  Chr(RecNo()) as AsciiAlpha,   RecNo() as AsciiNum autogenerate 255  Where
  (RecNo()&gt;=32 and RecNo()&lt;=126) or RecNo()&gt;=160 ;   Transactions: Load
  TransLineID,   TransID,  mod(TransID,26)+1 as Num,
  Pick(Ceil(3*Rand1),'A','B','C') as Dim1,
  Pick(Ceil(6*Rand1),'a','b','c','d','e','f') as Dim2,
  Pick(Ceil(3*Rand()),'X','Y','Z') as Dim3,  Round(1000*Rand()*Rand()*Rand1) as
  Expression1,  Round(  10*Rand()*Rand()*Rand1) as Expression2,
  Round(Rand()*Rand1,0.00001) as Expression3; Load   Rand() as Rand1,  IterNo()
  as TransLineID,  RecNo() as TransID Autogenerate 1000  While Rand()&lt;=0.5 or
  IterNo()=1;  Comment Field Dim1 With 'This is a field comment';";
  sessionApp.setScript(script).then(()=>{
    const stop = setInterval(()=>{
      sessionApp.global.getProgress(sessionApp.model.handle).then((progress)=>{
       //console.log("DoReload progress", progress);
      });
    }, 100);
    sessionApp.doReload()
  });
});
```

### Creating the visualizations

Use the `app.visualization.create` method to create two visualizations: a bar
chart and a pie chart. Also add a selections bar.

```javascript
sessionApp.doReload().then(function(result){
  sessionApp.visualization.create('barchart',["Dim1", "=Sum([Expression1])"],
  {"title":"Session App - Bar Chart"}).then((vis)=>{
    vis.show("QV01");
  });
  sessionApp.visualization.create('piechart',["Dim1", "=Count([Expression1])"],
  {"title":"Session App - Pie Chart"}).then((vis)=>{
    vis.show("QV02");
  });
  sessionApp.getObject('CurrentSelections','CurrentSelections');
});
```

### Setting actions for selections

Then use the app.clearAll, app.forward, app.back, and app.lockAll methods to add
actions for clearing all selections, stepping back and forward in the selection
history list, and locking all selections. These actions can be assigned to
buttons in the HTML.

These actions can be assigned to buttons in the HTML.

```javascript
sessionApp.doReload().then((result)=>{
  sessionApp.visualization.create('barchart',["Dim1", "=Sum([Expression1])"],
  {"title":"Session App - Bar Chart"}).then((vis)=>{
    vis.show("QV01");
  });
  sessionApp.visualization.create('piechart',["Dim1", "=Count([Expression1])"],
  {"title":"Session App - Pie Chart"}).then((vis)=>{
    vis.show("QV02");
  });
  sessionApp.getObject('CurrentSelections','CurrentSelections');
  $( ".clear-all" ).click( ()=>{
    sessionApp.clearAll();
  } );
  $( ".step-forward" ).click( ()=>{
    sessionApp.forward();
  } );
  $( ".step-back" ).click( ()=>{
    sessionApp.back();
  } );
  $( ".lock-all" ).click( ()=>{
    sessionApp.lockAll();
  } );
});
```

## Creating the main HTML file

Create an HTML file and name it `session-app-tutorial.html`. Save the file in
the same folder as the previously created files.

### Defining the relationships

Relationships between the current document and the linked Qlik Cloud defined
style sheets are specified in `link rel` tags inside the `head` of the HTML file.

```html
<link rel="stylesheet" href="<TENANT_URL>/resources/autogenerated/qlik-styles.css">
<link rel="stylesheet" href="session-app-tutorial.css">
<script src="<TENANT_URL>/resources/assets/external/requirejs/require.js"></script>
<script src="session-app-tutorial.js"></script>
```

### Placing the session objects

The session objects that have been defined in the JavaScript file are placed
inside `div` tags inside the `body` of the HTML file.

```html
<div class="sections section-3">
  Test qlik.sessionApp()
</div>
<div class="content content-3">
  <div class="row">
    <button class="lui-button  lui-button--info create-session-app">Create Session
    App</button>
    <div class="text1">*Creates a session app loaded with data from a prepared
    test script (Ctrl+00). </div>
  </div>
  <div class="row result">
    <div class="bold">RESULT</div>
  </div>
  <div id="CurrentSelections"></div>
  <div class="flex-container">
    <div id="QV01" class="object"></div>
    <div id="QV02" class="object"></div>
  </div>
  <div class="row result buttons-wrapper">
    <button class="lui-button  lui-button--info clear-all">Clear all selections</button>
    <button class="lui-button  lui-button--info step-forward">Step forward</button>
    <button class="lui-button  lui-button--info step-back">Step back</button>
    <button class="lui-button  lui-button--info lock-all">Lock all selections</button>
  </div>
  <div class="row result">
    <div class="bold">NOTE:</div>
    <div>Two visualizations should be displayed: a bar chart and a pie chart.</div>
  </div>
</div>
```

## Styling your mashup

To add some styling to your mashup, create a CSS file and name it
`session-app-tutorial.css`. This file is also saved in the same folder as the
previously created files.

### Extract

```css
.app-title{
  position: absolute;
  font-size: 15px;
  font-weight: bold;
  top: 14px;
  left: 46px;
}

.object{
  flex: 1 1 auto;
  height: 300px;
  min-width: 400px;
  margin: 45px 0 0 45px;
}

.header-row{
  height: 70px;
  background: rgb(70, 139, 176);
  color: rgb(255, 255, 255);
  line-height: 70px;
  font-size: 33px;
  font-family: Arial;
  text-align: center;
  border-bottom: 2px solid white;
}

.sections{
  height: 35px;
  background: #468bb0;
  color: white;
  line-height: 35px;
  font-size: 18px;
  font-family: Arial;
  text-align: center;
  cursor: pointer;
  border-bottom: 2px solid white;
}

.content{
  font-family: Arial;
  display: none;
}
```

## Tutorial source code

Explore the full source code of this tutorial below.

### session-app-tutorial.js

<details>
  <summary>Click to expand this section</summary>

  ```javascript
  const config = {
    host: '<TENANT_URL>', //for example, 'abc.us.qlikcloud.com'
    prefix: '/',
    port: 443,
    isSecure: true,
    webIntegrationId: '<WEB_INTEGRATION_ID>'
  };
  require.config( {
    baseUrl: ( config.isSecure ? "https://" : "http://" ) + config.host + 
    (config.port ? ":" + config.port : "") + config.prefix + "resources"});

  require( ["js/qlik"], ( qlik ) => {
    qlik.setOnError( ( error ) => {
      $( '#popupText' ).append( error.message + "<br>" );
      $( '#popup' ).fadeIn( 1000 );
    } );
    $( "#closePopup" ).click( () => {
      $( '#popup' ).hide();
    } );

    $( ".create-viz" ).addClass( "lui-disabled" );

    $( ".section-3" ).click( () => {
      $( ".content-3" ).toggleClass( "show-section" );
    } );

    $( ".get-script" ).click( () => {
      const appId = $( ".app-id" ).val();
      app1 = qlik.openApp(appId, config);
      app1.getScript().then(( script ) => {
        $( ".get-script-result" ).val( script.qScript );
        //console.log( script );
      });
    });

    $( ".set-script" ).click(  () => {
      $( ".msg-success" ).removeClass( "show" );
      $( ".msg-fail" ).removeClass( "show" );

      const script = $( ".set-script-input" ).val();
      const app2 = qlik.sessionApp(config);
      app2.setScript(script).then(() => {
        const stop = setInterval(() => {
          app2.global.getProgress(app2.model.handle).then((progress) => {
            //console.log("DoReload progress", progress);
          });
        }, 100);
      app2.doReload().then((result) => {
        if( result ){
          $( ".msg-success" ).addClass( "show" );
        } 
        else {
          $( ".msg-fail" ).addClass( "show" );
        }
      }).finally(( => {
        clearInterval(stop);
      }).catch( ( error ) => {
        console.log( error );
      } );

      app2.getScript().then(( script ) => {
        $( ".set-script-result" ).val( script.qScript );
        });
      });
    });

    $( ".create-session-app" ).click( () => {
      const sessionApp = qlik.sessionApp(config);
      const script2 = "Characters: Load Chr(RecNo()+Ord('A')-1) as Alpha, RecNo()
      as Num autogenerate 26;   ASCII: Load   if(RecNo()>=65
      and RecNo()<=90,RecNo()-64) as Num,  Chr(RecNo()) as AsciiAlpha,   RecNo() as
      AsciiNum autogenerate 255  Where (RecNo()>=32 and RecNo()<=126) or
      RecNo()>=160 ;   Transactions: Load  TransLineID,   TransID,
      mod(TransID,26)+1 as Num,  Pick(Ceil(3*Rand1),'A','B','C') as Dim1,
      Pick(Ceil(6*Rand1),'a','b','c','d','e','f') as Dim2,
      Pick(Ceil(3*Rand()),'X','Y','Z') as Dim3,  Round(1000*Rand()*Rand()*Rand1) as
      Expression1,  Round(  10*Rand()*Rand()*Rand1) as Expression2,
      Round(Rand()*Rand1,0.00001) as Expression3; Load   Rand() as Rand1,  IterNo()
      as TransLineID,  RecNo() as TransID Autogenerate 1000  While Rand()<=0.5 or
      IterNo()=1;  Comment Field Dim1 With 'This is a field comment';";

      //createdApp.getScript().then((script)=>{
      sessionApp.setScript(script2).then(() => {
        const stop = setInterval((){
          sessionApp.global.getProgress(sessionApp.model.handle).then((progress)=>{
            //console.log("DoReload progress", progress);
          });
        }, 100);
        sessionApp.doReload().then((result) => {
          sessionApp.visualization.create('barchart',["Dim1",
          "=Sum([Expression1])"],   {"title":"Session App - Bar Chart"}).then((vis)=>{
          vis.show("QV01");
          });
          sessionApp.visualization.create('piechart',["Dim1",
          "=Count([Expression1])"],   {"title":"Session App - Pie Chart"}).then((vis)=>{
          vis.show("QV02");
          } );
          sessionApp.getObject('CurrentSelections','CurrentSelections');
          $( ".clear-all" ).click( () => {
            sessionApp.clearAll();
          } );
          $( ".step-forward" ).click( () => {
            sessionApp.forward();
          } );
          $( ".step-back" ).click( () => {
            sessionApp.back();
          } );
          $( ".lock-all" ).click( () => {
            sessionApp.lockAll();
          } );

        }).finally(function(){
          clearInterval(stop);
        }).catch( function ( error ) {
          console.log( error );
        });
      });
    });
  });
  ```
</details>

### session-app-tutorial.html

<details>
  <summary>Click to expand this section</summary>

  ```html
  <!doctype html>
  <html><head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Qlik Sense Mashup</title>
    <meta charset="utf-8">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="HandheldFriendly" content="True">
    <meta name="MobileOptimized" content="320">
    <meta name="viewport" content="width=device-width, initial-scale=1.0,
     maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta http-equiv="cleartype" content="on">
    <link rel="stylesheet" href="<TENANT_URL>/resources/autogenerated/qlik-styles.css">
    <link rel="stylesheet" href="session-app-tutorial.css">
    <script src="<TENANT_URL>/resources/assets/external/requirejs/require.js"></script>
    <script src="session-app-tutorial.js"></script>
  </head>
  <body style="overflow: auto">
    <div class="header-row">
      Session app tutorial
    </div>
    <div class="sections section-3">
      Test qlik.sessionApp()
    </div>
    <div class="content content-3">
      <div class="row">
        <button class="lui-button  lui-button--info create-session-app">Create
        Session App</button>
        <div class="text1">*Creates a session app loaded with data from a prepared
          test script (Ctrl+00).</div>
      </div>
      <div class="row result">
        <div class="bold">RESULT</div>
      </div>
      <div id="CurrentSelections"></div>
      <div class="flex-container">
        <div id="QV01" class="object"></div>
        <div id="QV02" class="object"></div>
      </div>
      <div class="row result buttons-wrapper">
        <button class="lui-button  lui-button--info clear-all">Clear all selections</button>
        <button class="lui-button  lui-button--info step-forward">Step forward</button>
        <button class="lui-button  lui-button--info step-back">Step back</button>
        <button class="lui-button  lui-button--info lock-all">Lock all selections</button>
      </div>
      <div class="row result">
        <div class="bold">NOTE:</div>
        <div>Two visualizations should be displayed: a bar chart and a pie chart.</div>
      </div>
    </div>

    {/*Error Popup*/}
    <div id="popup">
      <button type="button" class="close" data-dismiss="modal" aria-label="Close"
      id="closePopup"><span aria-hidden="true">�</span></button>
      <p id="popupText"></p>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>

    </body>
  </html>
  ```
</details>

### session-app-tutorial.css

<details>
  <summary>Click to expand this section</summary>

  ```css
  @keyframes example {
    0% { height: 0; }
    25% { height: 25%; }
    50% { height: 50%; }
    100% { height: 100%; }
  }

  .data-1, .data-2, .data-3, .data-4{
    width:150px;
    margin: 0 10px;
  }

  .flex-container {
    display: flex;
    flex-wrap: wrap;
    padding: 0 45px 45px 0;
    background: #e3e4e5;
    position:relative;
  }

  .qvplaceholder, .qvobject {
    flex: 1 1 auto;
    height: 300px;
    min-width: 400px;
    margin: 45px 0 0 45px;
  }

  .big-wrap{
    display: flex;
  }

  .break-line{
    border-right: 3px solid white;
  }

  .app-title{
    position: absolute;
    font-size: 15px;
    font-weight: bold;
    top: 14px;
    left: 46px;
  }

  .object{
    flex: 1 1 auto;
    height: 300px;
    min-width: 400px;
    margin: 45px 0 0 45px;
  }

  .header-row{
    height: 70px;
    background: rgb(70, 139, 176);
    color: rgb(255, 255, 255);
    line-height: 70px;
    font-size: 33px;
    font-family: Arial;
    text-align: center;
    border-bottom: 2px solid white;
  }

  .sections{
    height: 35px;
    background: #468bb0;
    color: white;
    line-height: 35px;
    font-size: 18px;
    font-family: Arial;
    text-align: center;
    cursor: pointer;
    border-bottom: 2px solid white;
  }

  .content{
    font-family: Arial;
    display: none;
  }

  .show-section{
    display: inline;
  }

  .row{
    display: flex;
    line-height:28px;
    padding: 10px 20px;
  }

  .app-id, .created-app, .app-id-session {
    width: 300px;
    margin: 0 30px 0 5px;
  }

  .object-id-1, .object-id-2 {
    width: 150px;
    margin: 0 30px 0 5px;
  }

  .script{
    margin: 0px 30px 0px 11px;
    min-height: 189px;
    width:600px;
  }

  .bold{
    font-weight:bold;
    padding-right: 6px;
  }

  .result{
    background: #e3e4e5;
  }

  .text1{
    padding-left: 15px;
  }

  .msg-success{
    color: green;
    display:none;
  }

  .msg-fail{
    color: red;
    display:none;
  }

  .msg-success-2{
    color: green;
    display:none;
    padding-left:15px;
  }

  .msg-fail-2{
    color: red;
    display:none;
    padding-left:15px;
  }

  .show{
    display: inline;
  }

  .buttons-wrapper{
    display: flex;
    justify-content: center;
  }

  .buttons-wrapper button{
    margin-right: 15px;
  }

  .app-wrapper{
    flex: 1 1 auto;
  }

  #popup {
    background-color: #c3534b;
    color: #FFFFFF;
    position: fixed;
    max-width: 250px;
    padding: 10px;
    margin: 10px;
    bottom: 0;
    right: 0;
    display: none;
    border-radius: 5px;
    z-index: 6;
    font-family: sans-serif;
  }

  .close {
    cursor: pointer;
    background: 0 0;
    border: 0;
    float: right;
    font-size: 21px;
    font-weight: 700;
    line-height: 1;
    color: #000;
    text-shadow: 0 1px 0 #fff;
    opacity: .2;
    position: absolute;
    right: 9px;
    top: 7px;
  }

  .close:hover {
    opacity: .5;
  }

  #popupText {
    margin-right: 23px;
  }
  ```
</details>
