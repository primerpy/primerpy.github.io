---
title: "Advanced Javascript Ajax"
slug: "advanced-javascript-ajax"
date: "2017-11-02"
tags: ["advanced-javascript"]
---

## HTML
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">    
  <title>Title of the document</title>
  <script
     src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

<body>
  <button id="getBtn">GET()</button>
  <button id="postBtn">POST()</button>
  <button id="getJSONBtn">GETJSON()</button>
</body>

</html>
```

## JS
```javascript
$("#getBtn").click(function(){
  $.get("https://api.github.com/users/isaaczhou")
      .done(function(data){
          console.log(data.blog);
      }).fail(function(){
          {
              console.log("Error!")
          }
      })
})

$("#postBtn").click(function(){
  var data = {
      name: "Isaac",
      city: "New York"
  };
  $.post("www.isaaczhou.com", data)
      .done(function(data){
          console.log("Hi Isaac!")
      }).fail(function(error){
          console.log(error);
      })
})

$("#getJSONBtn").click(function(){
  $.getJSON("https://raw.githubusercontent.com/RobertLowe/nvd3/master/examples/nations.json")
      .done(function(data){
          console.log(data[153]);
      }).fail(function(error){
          console.log(error)
      })
})
```
