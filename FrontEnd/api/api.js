// api.js
import axios from 'axios';

// create an axios instance with default options
const http = axios.create({ baseURL: 'http://34.129.239.78:20482/api/v1/diagram/' });

export function getTotalUtilisation() {
  // then return the promise of the axios instance
  return http.get('utilisation/total')
    .catch((e) => {
    // catch errors here
      console.log(e);
    });
}

export function getTreatmentSite() {
  return http.get('utilisation/treatmentsite')
    .catch((e) => {
      console.log(e);
    });
}

export function getReasons() {
  return http.get('/implementing/reasons');
}
