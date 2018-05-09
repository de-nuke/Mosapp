import * as axios from 'axios';

const BASE_URL = 'http://localhost:8000';

function upload(formData) {
    const url = `${BASE_URL}/api/image/`;
    return axios.post(url, formData)
}

function get_image_url(pk) {
  const url = `${BASE_URL}/api/image/${pk}`;
  return axios.get(url);
}

function get_download_link(pk){
  return `${BASE_URL}/api/download/${pk}`
}
export { upload, get_image_url, get_download_link, }
