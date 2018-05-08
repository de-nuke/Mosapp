import * as axios from 'axios';

const BASE_URL = 'http://localhost:8000';

function upload(formData) {
    const url = `${BASE_URL}/api/image/`;
    return axios.post(url, formData)
}

function get_image_url(pk) {
  const url = `${BASE_URL}/api/image/`;
  return axios.get(url, {pk: pk})
}
export { upload }
