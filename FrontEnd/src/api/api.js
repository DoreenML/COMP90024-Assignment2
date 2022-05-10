// api.js
import axios from 'axios';

// create an axios instance with default options
const http = axios.create({ baseURL: 'http://127.0.0.1:5000' });

export function GetHealthRelatedTopicTrend() {
  // then return the promise of the axios instance
  return http.get('/HealthRelatedTopicTrend').catch((e) => {
    // catch errors here
      console.log(e);
  });
}

// export function getTreatmentSite() {
//   return http.get('utilisation/treatmentsite')
//     .catch((e) => {
//       console.log(e);
//     });
// }

// export function getReasons() {
//   return http.get('/implementing/reasons')
//     .catch((e) => {
//       console.log(e);
//     });
// }
