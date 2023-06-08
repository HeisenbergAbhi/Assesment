const postToDB = async (data)=>{
  await fetch('http://localhost:5000/addEventToDb', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)));
}
setTimeout(() => {
    pbjs.onEvent('bidRequested', function(data) {
      console.log("bidRequested")
      postToDB(data);
  })

    /* Log when Prebid wins the ad server auction */
  pbjs.onEvent('bidResponse', function(data) {
    console.log("bidResponse")
    postToDB(data);
  console.log(data.bidderCode+ ' won the ad server auction for ad unit ' +data.adUnitCode+ ' at ' +data.cpm+ ' CPM');
  });

  pbjs.onEvent('bidWon', function(data) {
    console.log("bidWon")
    postToDB(data);
    console.log(data.bidderCode+ ' won the ad server auction for ad unit ' +data.adUnitCode+ ' at ' +data.cpm+ ' CPM');
  });
}, 1000);