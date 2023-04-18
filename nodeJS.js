const https = require('https');

const options = {
  hostname: 'api.nytimes.com',
  port: 443,
  path: '/svc/books/v3/lists.json?list-name=hardcover-fiction&api-key=YOUR_API_KEY',
  method: 'GET'
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => {
    data += chunk;
  });
  res.on('end', () => {
    const books = JSON.parse(data).results[0].book_details.slice(0, 10);
    console.log('Top 10 Books:');
    for (let book of books) {
      console.log(`- ${book.title}`);
    }
  });
});

req.on('error', (error) => {
  console.error(error);
});

req.end();
