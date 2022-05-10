// api.js
import axios from 'axios';

// create an axios instance with default options
const http = axios.create({ baseURL: 'http://127.0.0.1:5000' });

export function GetInfo() {
  // then return the promise of the axios instance
  return http.get('/')
    .catch((e) => {
    // catch errors here
      console.log(e);
    });
}
