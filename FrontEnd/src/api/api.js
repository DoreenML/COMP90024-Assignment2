// api.js
import axios from 'axios';

// create an axios instance with default options
const http = axios.create({ baseURL: 'http://172.26.134.245:5000' });

export function GetHealthRelatedTopicTrend() {
  // then return the promise of the axios instance
  return http.get('/HealthRelatedTopicTrend').catch((e) => {
    // catch errors here
      console.log(e);
  });
}

export function GetHealthMap() {
  // then return the promise of the axios instance
  return http.get('/HealthMap').catch((e) => {
    // catch errors here
      console.log(e);
  });
}

export function GetDepressChart() {
  // then return the promise of the axios instance
  return http.get('/DepressionChart').catch((e) => {
    // catch errors here
      console.log(e);
  });
}

export function GetMentalTimeline() {
  // then return the promise of the axios instance
  return http.get('/MentalTimeLine').catch((e) => {
    // catch errors here
      console.log(e);
  });
}

export function GetSentimentWave() {
  // then return the promise of the axios instance
  return http.get('/SentimentWave').catch((e) => {
    // catch errors here
      console.log(e);
  });
}
