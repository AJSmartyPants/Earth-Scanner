let classifier;
// Model URL
let imageModelURL = 'https://teachablemachine.withgoogle.com/models/JCF26yjL3/';
//import json;

// Video
//let video;
//let flippedVideo;
// To store the classification
let img
let label = "";

// Load the model first
function preload() {
  classifier = ml5.imageClassifier(imageModelURL + 'model.json');
  //img = loadImage("https://crossorigin.me/C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\object.jpg")
  //img = loadImage("C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\object.jpg")
  img = loadImage('object.jpg')
  //resultfile = loadStrings('C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\results.txt')
  //savefile = loadBytes('C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\results.txt')
}

function setup() {
  createCanvas(500, 500);
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
  text(label, width/3, 30);
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
  createElement('h3', label)
  // Classifiy again!
  //classifyVideo();
}