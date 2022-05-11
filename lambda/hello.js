const { DynamoDB, Lambda } = require('aws-sdk');
const axios = require('axios').default;
const JSDOM = require('jsdom').JSDOM;
var { Readability } = require('@mozilla/readability');


exports.handler = async function(event) {
  if (event["path"] !== "/") {
    try {
      // Try getting a response from a url and parse if successful
      const path = event["path"].substring(1);
      const response = await axios.get(path);
      const dom = new JSDOM(response.data, {url: path});
      let reader = new Readability(dom.window.document);
      let article = reader.parse();

      return {
        statusCode: 200,
        headers: { "Content-Type": "text/html" },
        body: article["content"]
      };
    } catch (e) {
      // Something went wrong and we return a goofy error message
      return {
        statusCode: 200,
        headers: { "Content-Type": "text/html" },
        body: `
        <h1>Ohhhh nooo, your url didn't work!</h1>
        <img src="https://media.giphy.com/media/l0HlUikdzgYu8paIU/giphy.gif">`
      };
    }
  }

  // No url was given and we return a default message
  return {
    statusCode: 200,
    headers: { "Content-Type": "text/html" },
    body: `
    <h1>Alright, I'm gonna need you to enter a url</h1>
    <img src="https://media.giphy.com/media/l41lM8A5pBAH7UWWY/giphy.gif">`
  };
};
