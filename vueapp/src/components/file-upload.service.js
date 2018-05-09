import * as axios from 'axios';

const BASE_URL = 'http://localhost:8000';

function upload(formData) {
    const url = `${BASE_URL}/api/image/`;
    return axios.post(url, formData)
}

function get_image_url(pk) {
  const url = `${BASE_URL}/api/image/${pk}`;
  return axios.get(url);
  //   .then(x =>  {
  //   return {
  //     ...x.data,
  //     base_url: BASE_URL
  //   }
  // }).catch(e => {
  //   console.log(e);
  // });
}
export { upload, get_image_url }
