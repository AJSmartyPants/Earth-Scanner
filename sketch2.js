let classifier;
// Model URL
let imageModelURL = 'https://teachablemachine.withgoogle.com/models/5cSgLacCB/';
//import json;
let text_widget;

// Video
//let video;
//let flippedVideo;
// To store the classification
let img
let label = "Loading...";

// Load the model first
function preload() {
  classifier = ml5.imageClassifier(imageModelURL + 'model.json');
  //img = loadImage("https://crossorigin.me/C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\object.jpg")
  //img = loadImage("C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\object.jpg")
  //img = loadImage('Earth-Scanner/object.jpg')
  img = select('img', 'body')
  //resultfile = loadStrings('C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\results.txt')
  //savefile = loadBytes('C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\results.txt')
}

function setup() {
  createCanvas(500, 10);
  // Create the video
  //video = createCapture(VIDEO);
  //video.size(320, 240);
  //video.hide();

  //flippedVideo = ml5.flipImage(video)
  // Start classifying
  //image(img, 0, 0, 200, 200);
  //resulfile = []
  classifyVideo();
}

function draw() {
  //background(0);
  // Draw the video
  // Draw the label
  fill(0);
  textSize(25);
  textAlign(CENTER);
  //text(label, width/3, 30);
}

// Get a prediction for the current video frame
function classifyVideo() {
  //flippedVideo = ml5.flipImage(video)
  classifier.classify(img, gotResult);
}

// When we get a result
function gotResult(error, results) {
  // If there is an error
  if (error) {
    console.error(error);
    return;
  }
  // The results are in an array ordered by confidence.
  //console.log(results[0]);
  label = results[0].label;
  //saveJSON(label, 'result.json')
  //resultfile.splice(0,2);
  //resultfile.push(label)
  //saveStrings(resultfile, 'results.txt')
  //console.log(resultfile)
  
  //writer = 'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\results.txt'
  //writer.write(label)
  //writer.close()
  //htmllabel = index.html.createElement('h3', label);
  //createElement('h3', label)
  passVariableToHTML(label)
  text_widget = createP('');
  let api_url = 'https://api.api-ninjas.com/v1/dictionary?word=' + label;
  var headers = {
    'X-Api-Key': 'wCrBnEMU6ayQP7U+43e7/A==wd7RvCoQVu5k3C2x'
  };
  /*httpGet(api_url, headers={'X-Api-Key': 'wCrBnEMU6ayQP7U+43e7/A==wd7RvCoQVu5k3C2x'}, 'json', false, function(data) {
    for (let i = 0; i < data.length; i++) {
      let item = data[i];
      text_widget.html("Name: " + item["name"] + "<br>");
      text_widget.html("Taxonomy:<br>");
      let taxonomy = item["taxonomy"];
      for (let key in taxonomy) {
        text_widget.html("  " + key.capitalize() + ": " + taxonomy[key] + "<br>");
      }
      text_widget.html("Locations:<br>");
      let locations = item["locations"];
      text_widget.html(str(locations) + "<br>");
      text_widget.html("Characteristics:<br>");
      let characteristics = item["characteristics"];
      for (let key in characteristics) {
        text_widget.html("  " + key.capitalize() + ": " + characteristics[key] + "<br>");
      }
    }
  });*/

  /*httpDo(api_url, {
    method: 'GET',
    headers: headers
  }, function(result) {
    var data = JSON.parse(result);
    for (var i = 0; i < data.length; i++) {
      var item = data[i];
      console.log("Name: " + item["name"]);
      console.log("Taxonomy:");
      var taxonomy = item["taxonomy"];
      for (var key in taxonomy) {
        console.log("  " + key.capitalize() + ": " + taxonomy[key]);
      }
      console.log("Locations:");
      var locations = item["locations"];
      console.log(locations);
      console.log("Characteristics:");
      var characteristics = item["characteristics"];
      for (var key in characteristics) {
        console.log("  " + key.capitalize() + ": " + characteristics[key]);
      }
    }
  });*/

  httpDo(api_url, {
    method: 'GET',
    headers: headers
  }, function(result) {
    var data = JSON.parse(result);
    //var item = data[i]
    var plantdef = data["definition"]
    console.log(plantdef)
    createP(plantdef)
    /*for (var i = 0; i < data.length; i++) {
      var item = data[i];
      console.log("Name: " + item["name"]);
      console.log("Taxonomy:");
      createP("Name: " + item["name"]);
      createP("Taxonomy:")
      var taxonomy = item["taxonomy"];
      for (var key in taxonomy) {
        console.log(key+": " + taxonomy[key]);
        createP(key+": " + taxonomy[key]);
      }
      console.log("Locations:");
      var locations = item["locations"];
      console.log(locations);
      console.log("Characteristics:");
      createP("Locations:");
      createP(locations);
      createP("Characteristics:");
      var characteristics = item["characteristics"];
      for (var key in characteristics) {
        console.log(key+": " + characteristics[key]);
        createP(key+": " + characteristics[key]);
      }
    }
  });*/

  // Classifiy again!
  //classifyVideo();
})

function passVariableToHTML(variable) {
  let variableContainer = document.getElementById("variableContainer");
  variableContainer.innerHTML = variable;
}
}