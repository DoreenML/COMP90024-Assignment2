// Qi Li & 1138875 & lql4@student.unimelb.edu.au
// Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
// Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
// Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
// Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au
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
