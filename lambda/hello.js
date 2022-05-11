const { DynamoDB, Lambda } = require('aws-sdk');
const axios = require('axios').default;


exports.handler = async function(event) {
  console.log("request:", JSON.stringify(event, undefined, 2));

  // const axios = require('axios').default;

  // const response = await axios.get("https://www.lego.com/en-us");

  console.log("RESPONSE: ");//, response);

  return {
    statusCode: 200,
    headers: { "Content-Type": "text/plain" },
    body: `Hello, CDK! You've hit ${event.path}\n`
  };
};
